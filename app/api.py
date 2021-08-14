from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_403_FORBIDDEN
from fastapi.middleware.cors import CORSMiddleware

USERNAME = "foo"
PASSWORD = "bar"

app = FastAPI()
security = HTTPBasic()


todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/", tags=["root"])
async def read_root(username: str = Depends(get_current_username)) -> dict:
    return {"message": f"Welcome to your todo list {username}"}


@app.get("/todo", tags=["todos"])
async def get_todos(_: str = Depends(get_current_username)) -> dict:
    return {"data": todos}


@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict, _: str = Depends(get_current_username)) -> dict:
    todos.append(todo)
    return {
        "data": {"Todo added."}
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(
        id: int, body: dict, username: str = Depends(get_current_username)
    ) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated for: {username}."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(
        id: int, username: str = Depends(get_current_username)
    ) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} fo user: {username} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
