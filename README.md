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
```
cd backend
```
```
pip install -r .\requirements.txt
```
```
uvicorn main:app --reload     #start server
```
```
visit  127.0.0.1:8000/
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
