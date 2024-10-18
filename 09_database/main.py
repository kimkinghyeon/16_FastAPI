from fastapi import FastAPI , Depends
from database import session_local , engine
import models , schemas
from sqlalchemy.orm import Session
import teacher_crud

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# 제너레이터 함수
# 함수가 제너레이팅한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
@app.post('/teachers',response_model=schemas.TeacherResponse)
async def create_teacher(teacher : schemas.TeacherCreate,db : Session = Depends(get_db)):
    response = teacher_crud.create_teacher(db,teacher)
    return response

@app.get('/teacher/{teacher_id}',response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int,db:Session =Depends(get_db)):
    db_teacher = teacher_crud.get_teacher_by_id(db,teacher_id)
    return db_teacher