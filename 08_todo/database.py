# SQLAlchemy
# 파이썬에서 사용하는 ORM(object-relational-mapping) 라이브러리
# orm
# => d 객체와 관계형 데이터베이스를 연결하는 라이브러리이다.

# 엔진 생성을 위한 함수
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqllite
# 파이썬에 내장되어있는 db 라이브러리

DB_URL = "sqlite:///todo.sqlite3"

# 데이터베이스 엔진 생성
engine = create_engine(DB_URL)

# 연결 세션을 생성하기 위한 객체
# autocommit=False : 자동 커밋을 비활성화
# autoflush=False : 자동 플러시를 비활성화 (플러시: 세션의 변경사항을 데이터베이스에 동기화)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델 클래스가 상속받을 기본 모델 클래스를 지정
Base = declarative_base()
