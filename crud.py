from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
    {"id": 4, "name": "David", "age": 28},
]

@app.get("/users")
async def get_users() -> list[User]:
    return [User(**user) for user in users]

@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    for user in users:
        if user["id"] == user_id:
            return User(**user)
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    users.append(user.model_dump())
    return Response(status_code=status.HTTP_201_CREATED, content=user.model_dump_json())

@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index] = updated_user.model_dump()
            return Response(status_code=status.HTTP_201_CREATED, content=updated_user.model_dump_json())
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            del users[index]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/")
async def root() -> HTMLResponse:
    user_form = """
    <html>
        <head>
            <title>User API</title>
        </head>
        <body>
            <h1>Welcome to the User API</h1>
            <form id="userForm">
                <label for="id">ID:</label><br>
                <input type="number" id="id" name="id"><br>
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="age">Age:</label><br>
                <input type="number" id="age" name="age"><br><br>
                <input type="submit" value="Create User">
            </form>
            <script>
                document.getElementById('userForm').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const userData = {
                        id: parseInt(document.getElementById('id').value),
                        name: document.getElementById('name').value,
                        age: parseInt(document.getElementById('age').value)
                    };
                    try {
                        const response = await fetch('/users', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify(userData)
                        });
                        if (response.ok) {
                            alert('User created successfully!');
                            document.getElementById('userForm').reset();
                        } else {
                            alert('Failed to create user');
                        }
                    } catch (error) {
                        alert('Error: ' + error.message);
                    }
                });
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=user_form, status_code=200)