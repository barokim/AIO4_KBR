from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Response
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

class TaskInput(BaseModel):  #데이터 클래스 => 변수들만 가지고 객체를 만들려고 하는것
    #BaseModel을 상속 -validation을 측정가능
    # =>클래스 상속기능이 있고
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")  # 클래스가 객체 생성
    title: str = Field(min_length=1, max_length=80) #필드: 유효범위를 나타낼때
    done: bool = Field(default=False, strict=True) # true, false로만

class TaskOut(TaskInput):
    id: int

app = FastAPI(title="Lesson 05") #FastAPI 라고 되어있으며 서버
tasks = {1: {"id": 1, "title": "FastAPI basics", "done": False}}
next_id = 2

def require_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.get("/tasks", response_model=list[TaskOut])  #@app.get => 서버/tasks로 해야 실행
def list_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: Annotated[int, Path(ge=1)]):
    return require_task(task_id)

@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(payload: TaskInput):
    global next_id      
    task = {"id": next_id, **payload.model_dump()}
    tasks[next_id] = task
    next_id += 1
    return task
