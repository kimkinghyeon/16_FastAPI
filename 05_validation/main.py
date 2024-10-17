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