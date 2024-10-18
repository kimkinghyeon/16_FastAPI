import models , schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_teacher(db : Session, teacher = schemas.TeacherCreate):
    db_teacher = models.Teacher(
        name=teacher.name,
        is_active=teacher.is_active,
        nickname=teacher.nickname,
        description=teacher.description
    )
    db.add(db_teacher)
    db.commit()
    
    return db_teacher

# id로 teacher 찾기
def get_teacher_by_id(db : Session,teacher_id : int):
    found_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    return found_teacher

# 모든 teachers 찾기
def get_all_teachers(db: Session):
    # 모든 teacher 모델 가져오기
    all_teachers = db.query(models.Teacher).all()
    return all_teachers

# teachers 수정
def update_teacher(db : Session ,teacher_id : int ,teacher : schemas.TeacherUpdate):
    
    found_teacher = get_teacher_by_id(db, teacher_id)
    
    if found_teacher is None:
        raise HTTPException(status_code=404,detail='teacher not found')
    
    if teacher.name is not None:
        found_teacher.name = teacher.name
    if teacher.name is not None:
        found_teacher.is_active = teacher.is_active
    if teacher.name is not None:
        found_teacher.nickname = teacher.nickname
    if teacher.name is not None:
        found_teacher.description = teacher.description
        
    db.commit()
    
    return found_teacher

# teachers 삭제
def delete_teacher(db : Session,teacher_id : int):

    found_teacher = get_teacher_by_id(db, teacher_id)
    
    if found_teacher is None:
        raise HTTPException(status_code=404,detail='teacher not found')

    db.delete(found_teacher)
    
    db.commit()
    
    return found_teacher


