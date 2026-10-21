from fastapi import FastAPI

app = FastAPI(
    title="Sea-Info Agent",
    description="해양생물과 물때 정보를 알아보는 바다 정보 비서",
    version="0.1.0",
)

# 기본 안내
@app.get("/")
def root():
    return {
        "service": "Sea-Info Agent",
        "message": "궁금한 바다 생물과 우리 지역의 바다 정보를 만나보세요.",
        "status": "현재는 서비스 소개와 메뉴를 제공합니다.",
    }


# 제공할 정보 분야
@app.get("/sea_info")
def get_sea_info():
    return {
        "categories": [
            "해양생물 도감",
            "물때 정보",
            "바다 날씨",
            "바다 수온",
        ]
    }


# 서비스 메뉴
@app.get("/menus")
def get_menus():
    return {
        "menus": [
            "홈",
            "생물 알아보기",
            "물때·날씨",
            "나의 바다 기록",
            "서비스 소개",
        ]
    }



