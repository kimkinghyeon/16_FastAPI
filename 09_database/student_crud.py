import models , schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_student(db : Session, student = schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        nickname=student.nickname,
        launch_menu=student.launch_menu,
        description=student.description
    )
    db.add(db_student)
    db.commit()
    
    return db_student

# id로 student 찾기
def get_student_by_id(db : Session,student_id : int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    return found_student

# 모든 student 찾기
def get_all_student(db: Session):
    # 모든 teacher 모델 가져오기
    all_student = db.query(models.Student).all()
    return all_student

# student 수정
def update_student(db : Session ,student_id : int ,student : schemas.StudentUpdate):
    
    found_student = get_student_by_id(db, student_id)
    
    if found_student is None:
        raise HTTPException(status_code=404,detail='student not found')
    
    if student.name is not None:
        found_student.name = student.name
    if student.name is not None:
        found_student.launch_menu = student.launch_menu
    if student.name is not None:
        found_student.nickname = student.nickname
    if student.name is not None:
        found_student.description = student.description
        
    db.commit()
    
    return found_student

# student 삭제
def delete_student(db : Session,student_id : int):

    found_student = get_student_by_id(db, student_id)
    
    if found_student is None:
        raise HTTPException(status_code=404,detail='student not found')

    db.delete(found_student)
    
    db.commit()
    
    return found_student   
    