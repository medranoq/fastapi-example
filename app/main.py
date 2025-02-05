from fastapi import FastAPI,HTTPException
from models import Todo
from fastapi.responses import JSONResponse

app = FastAPI(
    title="FastAPI Example",
    summary="This is a simple FastAPI example for beginners",
    version="0.0.1"
)

todos = []

def api_response(status: bool = True,message="OK",data: any = None) -> dict:

    return {
        "status":status,
        "message":message,
        "data":data
    }

@app.get("/")
async def root():
    return JSONResponse(
        content=api_response(),
    )

#Index todo list

@app.get("/todo")
async def read_todos():

    return api_response(
        data=todos
    )

#Show todo list
@app.get("/todo/{todo_id}")
async def show_todo(todo_id:int):

    for todo in todos:
        if todo.id == todo_id:
            return JSONResponse(
                content=api_response(
                message="Resources found",
                data=todo.model_dump())
            )
        
    raise HTTPException(
        status_code=404,
        detail=api_response(status=False, message="Resource not found")
    )

#Create todo list

@app.post("/todo")
async def create_todo(todo : Todo):
    id = len(todos) + 1
    todo.id = id
    todos.append(todo)

    return JSONResponse(
        content=api_response(
        message="Todo created succesfully",
        data=todo.model_dump()),
        status_code=201
    )

#Update todo list

@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int,todo:Todo):

    for todo_item in todos:

        if todo_item.id == todo_id:
            todo_item.title = todo.title
            todo_item.status = todo.status

            return api_response(
                message="Todo update succesfully",
                data=todos.model_dump()
            )
        
    raise HTTPException(status_code=404, detail="Resource not found")


#Delete todo list:

@app.delete("/todo/{todo_id}",status_code=204)
async def distroy_todo(todo_id:int):

    for todo in todos:
        if todo.id == todo_id:

            todos.pop(todo_id-1)
            return api_response(
                message="Resources deleted"
            )
    
    return api_response(
        status=False,
        message="Resources not found"
    )