from fastapi import FastAPI

app = FastAPI(title="Lesson 02")

@app.get("/method")
def read_method():
    return {"method": "GET", "purpose": "read"}

# Fastapi docs 
# Swagger  UI에서 post 요청을 테스트할수 있도록 status_code를 201로 설정
@app.post("/method", status_code=201)  #클라이언트 요청이 성공적으로 실행이 되었다는 서버코드
def create_method():
    return {"method": "POST", "purpose": "create"}

read_method()
print(read_method)