"""07장: 간결한 FastAPI + Pydantic CRUD 학습 예제 (메모리 저장)."""
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field, ValidationError

app = FastAPI(title='Chapter 07 - Pydantic CRUD', version='1.0')


class TaskIn(BaseModel):
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True) 
    # 여백 안되고forbid는 죽이고에러발생, ignore는 무시, allow는 허용 공백을 제거한다
    title: str = Field(min_length=1, max_length=80)
    done: bool = Field(default=False, strict=True)


class TaskPatch(BaseModel):
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True)
    title: str | None = Field(default=None, min_length=1, max_length=80)
    done: bool | None = Field(default=None, strict=True)


class TaskOut(TaskIn):
    id: int


_db: dict[int, TaskOut] = {1: TaskOut(id=1, title='Pydantic 학습')}
_next_id = 2


def reset_demo_data() -> None:
    """테스트에서 상태 초기화: 실제 운영용 코드가 아니다."""
    global _next_id
    _db.clear()
    _db[1] = TaskOut(id=1, title='Pydantic 학습')
    _next_id = 2


def get_existing(task_id: int) -> TaskOut:
    if task_id not in _db:
        raise HTTPException(status_code=404, detail='작업을 찾을 수 없습니다')
    return _db[task_id]


@app.get('/')
def index() -> dict[str, str]:
    return {'message': '실습 문서: /docs'}


@app.get('/tasks', response_model=list[TaskOut])
def list_tasks() -> list[TaskOut]:
    return list(_db.values())


@app.get('/tasks/{task_id}', response_model=TaskOut)
def read_task(task_id: int) -> TaskOut:
    return get_existing(task_id)

#브라우저에서 호출방식은 get방식, 프로그램적으로는 포스트 방식
#입력을 띄울때는 get방식으로 띄우고 post방식으로 등록
@app.post('/tasks', response_model=TaskOut, status_code=status.HTTP_201_CREATED) 
#호출 성공 => 201(상수표현) --> 매직넘버
def create_task(payload: TaskIn) -> TaskOut:
    global _next_id #global => 함수영역 밖에서 변수를 선언하지 않고 함수내에서 변수를 호출하여 사용하기 위해서
    task = TaskOut(id=_next_id, **payload.model_dump())
    _db[task.id] = task
    _next_id += 1
    return task

#put 전체데이터 교체
@app.put('/tasks/{task_id}', response_model=TaskOut)
def replace_task(task_id: int, payload: TaskIn) -> TaskOut:
    get_existing(task_id)
    task = TaskOut(id=task_id, **payload.model_dump())
    _db[task_id] = task
    return task

#patch 필요한 부분만 교체
@app.patch('/tasks/{task_id}', response_model=TaskOut)
def update_task(task_id: int, payload: TaskPatch) -> TaskOut:
    stored = get_existing(task_id)
    change = payload.model_dump(exclude_unset=True)
    # PATCH는 실제 전송된 값만 병합한다. null이 들어오면 재검증에서 422가 발생한다.
    try:
        updated = TaskOut.model_validate({**stored.model_dump(), **change})
    except ValidationError as error:  #에러를 발생
        raise HTTPException(
            status_code=422,
            detail=[{'loc': list(e['loc']), 'msg': e['msg'], 'type': e['type']}
                    for e in error.errors()],
        ) from error
    _db[task_id] = updated
    return updated


@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    get_existing(task_id)
    del _db[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)