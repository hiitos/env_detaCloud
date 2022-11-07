from fastapi.responses import JSONResponse
import json
from fastapi import APIRouter, Depends, HTTPException
from setting import deta,users
from schemas import user as user_schema

router = APIRouter()

@router.get("/")
def index():
  return {"message": "hello world update"}

@router.get("/users")
def read_user():
  return next(users.fetch())

@router.post("/users", status_code=200)
def create_user(user: user_schema.User):
  user = users.put(user.dict())
  return json.dumps(user)

@router.get("/users/{uid}")
def read_user(uid: str):
  user = users.get(uid)
  if user:
    return user
  res = JSONResponse({"message": "user not found"}, status_code=404)
  return res

@router.patch("/users/{uid}")
def update_user(uid: str, uu:user_schema.UserUpdate):
  update = {k:v for k,v in uu.dict().items() if v is not None}
  try:
    users.update(update, uid)
    return users.get(uid)
  except Exception:
    return JSONResponse({"message": "user not found"}, status_code=404)

@router.delete("/users/{uid}")
def delete_user(uid: str):
  users.delete(uid)
  return JSONResponse({"message": "user is deleted"}, status_code=200)