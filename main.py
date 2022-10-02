from fastapi import FastAPI
from db.user import user


app = FastAPI()


@app.get('/')
def root():
    return {"message": "HELLO!"}


@app.get('/get_user')
def get_user():
    return {"message": "get user!"}


@app.get('/create_user')
def create_user():
    return {"message": "create user!"}


@app.get('/update_user')
def update_user():
    return {"message": "update user!"}
