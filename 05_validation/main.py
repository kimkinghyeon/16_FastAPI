from fastapi import FastAPI
from typing import Union

app = FastAPI()

# 각 파라미터 (사용자가 전달할 데이터) 에 대해 검증과
# 추가정보 입력을 위한 기능을 제공해준다.

# query parameter validation
from fastapi import Query

@app.get('/teachers')
async def print_teacher_name(
    name : Union[str,None] = Query( default= None , max_length=20 , min_length=2)
):
    return f'teacher_name : {name}'

# 정규 표현식을 이용한 검증
@app.get('/teachres/lectures')
async def print_teacher_lecture(
    # 과목_로 시작하는 문자열만 허용
    lecture : str = Query( 
                        default= 'lecture_java' ,
                        # ^: 문자열의 시작 ("^lecture_"이 문자로 시작을 해야한다는 것을 의미) 
                        # *: 임의의 문자가 0개 이상 올 수 있다.
                        # $: 문자열의 끝을 의미
                        pattern='^lecture_.*$')
):
    return f"lecture : {lecture}"

# path parameter validation
from fastapi import Path

# gt : greater than          초과
# ge : greater than or equal 이상
# lt : less than             미만
# le : less than or equal    이하

@app.get('/lectures/{lecture_id}')
async def print_lecture_info(
    lecture_id : int = Path(
        # lecture_id 는 0 보다 크고 10보다 작아야한다. ( 라는 조건문 작성해보기 )
        gt = 0,
        lt = 10
    )
    
):
    return f'lecture : {lecture_id}'


# request body validation

from pydantic import BaseModel , Field
class Teacher(BaseModel):
    
    # ... : 필수 필드를 의미한다.
    is_working : str = Field(...,min_length=2,max_length=20)
    
    name : str
    
    # 필수 필드 , 최소 2자 최대 30자
    nickname : str = Field(...,min_length=2,max_length=30)
    
    # 필수 필드 , 18 이상 100 이하
    age : int = Field(...,gt =18 , lt=100)
    
    # 필수 필드 , 이메일 형식을 검사
    email: str = Field(...,pattern='^[\w\.-]+@[\w\.-]+\.\w+$')
    # ^[\w\.-]+ : 하나이상의 문자,숫자,밑줄,점으로 시작
    # @ : 반드시 @ 가 포함
    # \. : 반드시 . 이 포함
    # \w+ : 하나 이상의 문자나 숫자가 와야함
    
@app.post('/teacher/info')
async def teacher_info(teacher:Teacher):
    return {
        'is_working': teacher.is_working,
        'name': teacher.name,
        'nickname': teacher.nickname,
        'age' : teacher.age,
        'email' : teacher.email
            } 