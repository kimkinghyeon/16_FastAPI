from pydantic import BaseModel
from typing_extensions import Optional


# request 반거나. response를 받을때
# 기본 형식을 만들어 놓을 수 있다.
class TeacherBase(BaseModel):
    name: str
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] = None

# sqlalchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조정의
# pydantic 모델 : api 요청과 응답을 위한 데이터 구조정의

# request 요청 모델
class TeacherCreate(TeacherBase):
    pass


# response 응답 모델
class TeacherResponse(TeacherBase):
    id: int
    
# 업데이트할때 사용되는 모델
