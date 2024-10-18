from fastapi import FastAPI, Request, Depends , Form , status
from fastapi.templating import Jinja2Templates
import models
from database import engine, session_local
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

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
        db.query(models.Todo).order_by(models.Todo.id.desc())
    )  # 데이터베이스에서 모든 할 일 조회
    return templates.TemplateResponse(
        "index.html", {"request": request, "todos": todos}
    )  # 템플릿에 데이터를 전달

@app.post('/add')
async def add(request:Request, task:str=Form(...) , db:Session = Depends(get_db)):
    # Todo 클래스의 객체를 생성하고, tesk 값을 전달하여 Todo 에 전달
    todo = models.Todo(task=task)
    
    # 데이터베이스에 추가
    db.add(todo)
    
    # 변경사항 커밋
    db.commit()
    
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)

# 수정 페이지로 이동
@app.get('/edit/{todo_id}')
async def add(request:Request, todo_id:int,db:Session = Depends(get_db)):
    
    # Todo 단건 조회()
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return templates.TemplateResponse('edit.html',{"request": request, "todo": todo})

# 변경 요청 처리
@app.post('/edit/{todo_id}')
async def edit(request:Request, todo_id:int, task: str = Form(...),completed:bool = Form(False),db:Session = Depends(get_db)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    # todo task 속성을 입력받은 값으로 수정
    todo.task = task
    todo.completed = completed
    
    db.commit()
    
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/delete/{todo_id}')
async def felete(request:Request,todo_id:int,db:Session=Depends(get_db)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    db.delete(todo)
    
    db.commit()
    
    return RedirectResponse(url=app.url_path_for('home'),status_code=status.HTTP_303_SEE_OTHER)
    