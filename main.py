from fastapi import FastAPI, Query, Path, Body, Response
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated, Literal, Any
from enum import Enum
from pydantic import BaseModel, EmailStr
from datetime import datetime, time, timedelta
from uuid import UUID


class Users(BaseModel):
    name: str
    surname: str
    age: int
    password: str
    email: EmailStr

class UserResponse(BaseModel):
    name: str
    surname: str
    age: int

class Posts(BaseModel):
    post_id: str
    details: str

class DataQuery(BaseModel):
    model_config = {"extra": "allow"}
    my_data: Literal["data1", "data2"]
    details1: list[str] = ["Rushabh"]
    posts: list[Posts]

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []




app = FastAPI()


@app.get("/")
async def test():
    return "Hello"


@app.post("/users", response_model=UserResponse)
async def users(user: Users):
    return user

@app.get("/post_get/")
async def postsss() -> Any:
    return {
            "post1": Posts(post_id="Rushabh", details="asd"),
            "post2": Posts(post_id="Shah", details="asdf")
    }

@app.get("/posts/{post_id}")
async def posts(post_id: str, query: str):
    return {"Post ID": query}


@app.post("/posts")
async def post(post: Posts):
    return {"Post": post}


@app.get("/tests/{post_id}")
async def posts(post_id: str, query: str | None = Query(min_length=6)):
    return {"Post ID": query}

@app.get("/query/{query_id}")
async def posts(query_id: str, query: Annotated[DataQuery, Query()]):
    return {"Post ID": query}

@app.get("/query1/{query_id}")
async def posts(query_id: str, query: Annotated[DataQuery, Query()]):
    return {"Post ID": query}

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/shreya/{user_id}")
async def shreya(user_id: str) -> Response:
    if user_id == "eat":
        return RedirectResponse(url="https://www.cricbuzz.com/")
    else:
        return JSONResponse(content={"Status Details": "Rushabh Shah"})

@app.get("/teleport")
async def get_teleport() -> JSONResponse:
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items_details/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# response_model_exclude_defaults=True
# response_model_exclude_none=True


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]



