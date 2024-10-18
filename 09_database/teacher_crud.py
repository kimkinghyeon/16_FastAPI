import models , schemas
from sqlalchemy.orm import Session

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