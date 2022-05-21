## Python FAST-API Demo
[![CircleCI](https://circleci.com/gh/senolatac/fastapi-demo/tree/master.svg?style=svg)](https://circleci.com/gh/senolatac/fastapi-demo/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/5385a550ab924eb3959aa1340c368875)](https://www.codacy.com/gh/senolatac/fastapi-demo/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=senolatac/fastapi-demo&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/5385a550ab924eb3959aa1340c368875)](https://www.codacy.com/gh/senolatac/fastapi-demo/dashboard?utm_source=github.com&utm_medium=referral&utm_content=senolatac/fastapi-demo&utm_campaign=Badge_Coverage)
### Install dependencies
```
pip install -r requirements.txt
```

### Run project
```
uvicorn --port 5000 --host 127.0.0.1 app.main:app --reload
```

### Create dependencies
```
pip freeze > requirements.txt  
```

### Run tests
```
pytest  
```
