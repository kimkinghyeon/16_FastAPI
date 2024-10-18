from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
import models
from database import engine, session_local
from sqlalchemy.orm import Session

# fastapi에서 진자2 템플릿 엔진을 사용하도록 설정
templates = Jinja2Templates(directory="template")  # 템플릿 디렉토리 설정

app = FastAPI()

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)


# 데이터베이스 세션
def get_db():
    db = session_local()  # 호출될 때마다 새로운 세션 객체 생성
    try:
        yield db  # 데이터베이스 세션 객체 반환
    finally:
        db.close()


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    # 데이터베이스에서 todo 모델을 가져온다. (id를 기준으로 내림차순 정렬)
    todos = (
        db.query(models.Todo).order_by(models.Todo.id.desc()).all()
    )  # 데이터베이스에서 모든 할 일 조회
    return templates.TemplateResponse(
        "index.html", {"request": request, "todos": todos}
    )  # 템플릿에 데이터를 전달
