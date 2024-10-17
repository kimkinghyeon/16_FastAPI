'''
Fast API

pip install fastapi[all]

fastapi 관련 패키지들, uvicorn

- 부분적으로 설치
pip install fastapi
pip install uviconr
'''

# main.py : 프로젝트 전체적인 환경을 설정하는 파일

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'messgae' : 'hello'}

# uvicorn main:app --reload

# main => main.py 파일의 이름을 의미
# app => main.py 파일에서 fastapi() 객체를 가지고 있는 app 객체를 의미

# --reload : 파일에 변화가 생기면 재시작 하겠다는 옵션