from fastapi import FastAPI
from models import ToDo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#get todos by id
@app.get("/todos/{todo_id}")
async def get_todos_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todos": todos}
    return {"message": "No item found"}

#create todos
@app.post("/todos")
async def create_todo(todo: ToDo):
    todos.append(todo)
    return {"message": "Todo has been added"}

#update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: ToDo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todos": todos}
    return {"message": "No todos found to update"}

#delete a todo
@app.delete("/todos/{todo_id}")
async def get_todos_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"Message": f"todo id: {todo_id} has been deleted"}
    return {"message": "No item found"}