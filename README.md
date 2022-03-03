# info-loker
basic crud, jwt auth using FastAPI


## Technology Stack
* FastAPI
* Uvicorn (server)
* Pytest
* Sqlalchemy
* Postgres


## How to start the app ?
```
git clone https://github.com/alif-arrizqy/info-loker.git
```
```
cd info-loker
```
- create a virtual environment
```
python -m venv env   
```
- activate your virtual environment
```
env\Scripts\activate
```
- enter to directory backend/
```
cd backend
```
- install all requirements
```
pip install -r .\requirements.txt
```

## PostgreSQL Config
- create database in postgreSQL
- create .env using command
```
cp .env-example .env
```
- edit .env file 

![image](https://user-images.githubusercontent.com/45624651/156493462-021f5a33-d922-4563-b6e2-b0f87f21a19b.png)

- running the website
```
uvicorn main:app --reload     #start server
```
- open in browser
```
127.0.0.1:8000/
```
- API Schemas
```
http://127.0.0.1:8000/docs
```

## Post a job
```
http://127.0.0.1:8000/post-a-job
```
## Delete a post
```
http://127.0.0.1:8000/delete-job
```

Features:
 - ✔️ Serving Template
 - ✔️ Static Files in Development
 - ✔️ Connecting to Database
 - ✔️ Schemas
 - ✔️ Dependency Injection
 - ✔️ Password Hashing
 - ✔️ Unit Testing (What makes an app stable)
 - ✔️ Authentication login/create user/get token
 - ✔️ Authorization/Permissions 
 - ✔️ Webapp (Monolithic)
