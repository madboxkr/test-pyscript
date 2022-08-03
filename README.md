# test-pyscript
test-pyscript


# Root Cause
https://pyscript.net/
https://fastapi.tiangolo.com/ko/

https://pydantic-docs.helpmanual.io/

Templates - Jinja2 
GraphQL - GraphQL, Strawberry is the recommended library as it has the design closest to FastAPI's design, it's all based on type annotations.

https://flask.palletsprojects.com/


# Goal
Build My MAP for riding.


# Env 
```
pyenv virtualenv 3.9.4 test-pyscript
pyenv shell test-pyscript
noglob pip install fastapi[all]
pip install uvicorn
pip install flask
```

# pypi - pip requirements.pip

```
❯ pip freeze
anyio==3.6.1
asgiref==3.5.2
certifi==2022.6.15
charset-normalizer==2.1.0
click==8.1.3
dnspython==2.2.1
email-validator==1.2.1
fastapi==0.79.0
Flask==2.2.0
h11==0.13.0
httptools==0.4.0
idna==3.3
importlib-metadata==4.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
orjson==3.7.11
pydantic==1.9.1
python-dotenv==0.20.0
python-multipart==0.0.5
PyYAML==6.0
requests==2.28.1
six==1.16.0
sniffio==1.2.0
starlette==0.19.1
typing_extensions==4.3.0
ujson==5.4.0
urllib3==1.26.11
uvicorn==0.17.6
uvloop==0.16.0
watchgod==0.8.2
websockets==10.3
Werkzeug==2.2.1
zipp==3.8.1
```

# main.py = Hello World
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```


# RUN
```
uvicorn main:app --reload
```

# Connect
```
Main page - http://127.0.0.1:8000 - Hello World
Swagger UI - http://127.0.0.1:8000/docs - https://github.com/swagger-api/swagger-ui
ReDoc - http://127.0.0.1:8000/redoc - https://github.com/Redocly/redoc
OpenAPI - http://127.0.0.1:8000/openapi.json - https://github.com/OAI/OpenAPI-Specification
```


