from database import Base
from sqlalchemy import Column , Integer , String , Text , Boolean

# string = 고정된길이 ( 길이 제한 )
# text = 길이제한이 없다.

class Teacher(Base):
    __tablename__ = 'teachers'
    
    # 컬럼설정
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    is_active = Column(Boolean,default=True)
    description = Column(Text)