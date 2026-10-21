from typing import Annotated    ##Annotated라는 클래스만 가져옴
from fastapi import FastAPI, HTTPException, Path

app = FastAPI(title="Lesson 03")   # 이거만 해도 서버구동 
tasks = {1: {"id": 1, "title": "FastAPI basics", "done": False}}

# Fixed paths must be declared before the variable route.
@app.get("/tasks/stats")   
def task_stats(): # 경로에 매핑되는 메서드를 호출
    return {"total": len(tasks)}  ## 콜백 함수 , Len() 숫자 개수 확인

@app.get("/tasks/{task_id}")  #task_id => type 검사 => int
def read_task(task_id: Annotated[int, Path(ge=1)]):  
    # - ge=1: 값이 1 이상이어야 합니다. ge는 “greater than or equal”을 뜻합니다.
    # 검증을 통과하면 데이터 존재 여부를 확인합니다. 
    # 해당 ID가 없으면 404 오류를 보내고, 있으면 할 일 정보를 반환합니다

    if task_id not in tasks: ## task_id가 tasks안에 키값들로 비교하여 있지 않으면 오류를 발생시킨다
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]