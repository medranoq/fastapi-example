from fastapi import FastAPI
from models import Todo

app = FastAPI(
    title="FastAPI Example",
    summary="This is a simple FastAPI example for beginners",
    version="0.0.1"
)

todos = []

@app.get("/")
async def root():
    return {"message":"Hello World!"}

#Index todo list

@app.get("/todo")
async def read_todos():

    return  {
        "status":True,
        "message":"OK",
        "data":todos
    }

#Show todo list
@app.get("/todo/{todo_id}")
async def show_todo(todo_id:int):

    for todo in todos:
        if todo.id == todo_id:
            return {
                "status":"OK",
                "message":"Resources found",
                "data": todos[todo_id-1]
            }
    
    return {
            "status":"Error",
            "message":"Resources not found",
            "data": None
    }

#Create todo list

@app.post("/todo")
async def create_todo(todo : Todo):

    todos.append(todo)

    return {
        "status":True,
        "message":"Todo created succesfully",
        "data":todos[todo.id-1]
    }

#Update todo list

@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int,todo:Todo):

    for todo_item in todos:

        if todo_item.id == todo_id:
            todo_item.title = todo.title
            todo_item.status = todo.status

            return {
                "status":True,
                "message":"Todo update succesfully",
                "data":todos[todo_id-1]
            }
    
    return {
            "status":"Error",
            "message":"Resources not found",
            "data": None
    }


#Delete todo list:

@app.delete("/todo/{todo_id}")
async def distroy_todo(todo_id:int):

    for todo in todos:
        if todo.id == todo_id:

            todos.pop(todo_id-1)
            return {
                "status":"OK",
                "message":"Resources deleted",
                "data": None
            }
    
    return {
            "status":"Error",
            "message":"Resources not found",
            "data": None
    }
