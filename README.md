## Python FAST-API Demo
[![CircleCI](https://circleci.com/gh/senolatac/fastapi-demo/tree/master.svg?style=svg)](https://circleci.com/gh/senolatac/fastapi-demo/tree/master)

### Install dependencies
```
pip install -r requirements.txt
```

### Run project
```
uvicorn --port 5000 --host 127.0.0.1 main:app --reload
```

### Create dependencies
```
pip freeze > requirements.txt  
```

### Run tests
```
pytest  
```
