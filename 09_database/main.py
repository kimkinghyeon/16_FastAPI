from fastapi import FastAPI , Depends
from database import session_local , engine
import models , schemas
from sqlalchemy.orm import Session
import teacher_crud
import student_crud

models.Base.metadata.drop_all(bind=engine)
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
        
# teacher add
@app.post('/teachers',response_model=schemas.TeacherResponse)
# Depends 세션 객체를 먼저 생성하기 위해
async def create_teacher(teacher : schemas.TeacherCreate,db : Session = Depends(get_db)):
    response = teacher_crud.create_teacher(db,teacher)
    return response

# teacher get by - id 
@app.get('/teacher/{teacher_id}',response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int,db:Session =Depends(get_db)):
    db_teacher = teacher_crud.get_teacher_by_id(db,teacher_id)
    return db_teacher

# teacher get - all
@app.get('/teachers',response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session = Depends(get_db)):
    all_teachers = teacher_crud.get_all_teachers(db)
    return all_teachers

# teacher by - id put
@app.put('/teacher/{teacher_id}',response_model=schemas.TeacherResponse)
async def update_teacher(teacher_id:int,teacher:schemas.TeacherUpdate,db:Session = Depends(get_db)):
    update_teacher = teacher_crud.update_teacher(db,teacher_id,teacher)
    return update_teacher

# teacher by - id delete
@app.delete('/teacher/{teacher_id}',status_code=204)
async def felete_teacher(teacher_id:int , db:Session = Depends(get_db)):
    teacher_crud.delete_teacher(db,teacher_id)
    return None

# ----------------------------------------------------------------

# student add
@app.post('/students',response_model=schemas.StudentResponse)
# Depends 세션 객체를 먼저 생성하기 위해
async def create_student(student : schemas.StudentCreate,db : Session = Depends(get_db)):
    response = student_crud.create_student(db,student)
    return response

# student get by - id 
@app.get('/student/{student_id}',response_model=schemas.StudentResponse)
async def find_student_by_id(student_id:int,db:Session =Depends(get_db)):
    db_student = student_crud.get_student_by_id(db,student_id)
    return db_student

# student get - all
@app.get('/students',response_model=list[schemas.StudentResponse])
async def find_all_students(db: Session = Depends(get_db)):
    all_students = student_crud.get_all_students(db)
    return all_students

# student by - id put
@app.put('/student/{student_id}',response_model=schemas.StudentResponse)
async def update_student(student_id:int,student:schemas.StudentUpdate,db:Session = Depends(get_db)):
    update_student = student_crud.update_student(db,student_id,student)
    return update_student

# student by - id delete
@app.delete('/student/{student_id}',status_code=204)
async def felete_student(student_id:int , db:Session = Depends(get_db)):
    student_crud.delete_student(db,student_id)
    return None