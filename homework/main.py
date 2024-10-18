from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class calculating_machine(BaseModel):
    sign : str 
    num1 : int
    num2 : int

def calculate(sign: str, num1: int, num2: int):
    if  sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '%':
        return num1 % num2
    else:
        raise HTTPException(status_code=400,detail='입력 읒 같이하지마셈!!!!!')

@app.post('/')
async def post_T(request:calculating_machine):
    
    sum = calculate(request.sign,request.num1,request.num2)
    
    return sum


