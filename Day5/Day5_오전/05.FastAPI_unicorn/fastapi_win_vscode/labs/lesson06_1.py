tasks = [{"id": 1, "title": "FastAPI basics", "done": False}]

'''
1. 데이터 조회 get(/tasks)
return tasks
2. 데이터 추가 post(/tasks)
tasks.append
3. 특정번호의 데이터 조회 get (/tasks/task_id)
return tasks[task_id]
4. 특정번호의 데이터를 전부 교체 put (/tasks/{task_id})
tasks[task_id] = {"id": task_id, "title": "FastAPI"}
5. 특정번호의 데이터 일부수정 patch(/tasks/task_id)
'''