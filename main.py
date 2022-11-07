from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from deta import Deta
import json

# "project key" is necessary in local, but it's not on Deta base
deta = Deta()
# userテーブル(名前:fastapi-crud)を作成
users = deta.Base("fastapi-crud")

app = FastAPI()

# CRUD用のmethod
class User(BaseModel):
  name: str
  age: int
  hometown: str

class UserUpdate(BaseModel):
  name: str = None
  age: int = None
  hometown: str = None

@app.get("/")
def index():
  return {"message": "hello world"}

@app.get("/users")
def read_user():
  return next(users.fetch())

@app.post("/users", status_code=200)
def create_user(user: User):
  user = users.put(user.dict())
  return json.dumps(user)

@app.get("/users/{uid}")
def read_user(uid: str):
  user = users.get(uid)
  if user:
    return user
  res = JSONResponse({"message": "user not found"}, status_code=404)
  return res

@app.patch("/users/{uid}")
def update_user(uid: str, uu:UserUpdate):
  update = {k:v for k,v in uu.dict().items() if v is not None}
  try:
    users.update(update, uid)
    return users.get(uid)
  except Exception:
    return JSONResponse({"message": "user not found"}, status_code=404)

@app.delete("/users/{uid}")
def delete_user(uid: str):
  users.delete(uid)
  return JSONResponse({"message": "user is deleted"}, status_code=200)