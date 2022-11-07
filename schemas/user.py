import datetime
from typing import Optional
from pydantic import BaseModel, Field

# CRUD用のmethod
class User(BaseModel):
  name: str
  age: int
  hometown: str

class UserUpdate(BaseModel):
  name: str = None
  age: int = None
  hometown: str = None