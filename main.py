from fastapi import FastAPI, Query
from pydantic import BaseModel


class Users(BaseModel):
    name: str
    surname: str
    age: int

class Posts(BaseModel):
    post_id: str
    details: str


app = FastAPI()


@app.get("/")
async def test():
    return "Hello"


@app.post("/users")
async def users(user: Users):
    return {"Users": user.name}

@app.get("/posts/{post_id}")
async def posts(post_id: str, query: str):
    return {"Post ID": query}


@app.post("/posts")
async def post(post: Posts):
    return {"Post": post}


@app.get("/tests/{post_id}")
async def posts(post_id: str, query: str | None = Query(min_length=6)):
    return {"Post ID": query}




