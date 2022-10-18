from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import ToDo
import database

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all for debug purposes ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def root():
    return {
        'message': 'Hello API world! fastapi-farm-fcc serving.'
    }


@app.get('/todo/{todo_id}', response_model=ToDo)
async def get_todo(todo_id):
    response = await database.get_todo(todo_id)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo_id}')


@app.get('/all-todos/')
async def get_all_todos():
    response = await database.get_all_todos()
    return response


@app.post('/add-todo/', response_model=ToDo)  # NB: There should be NO {}s in URL when you pass class!!!
# @app.post('/add-to do/{To Do}', response_model=To Do)  # This is WRONG, caused bugs with frontend!
async def add_todo(todo: ToDo):
    response = await database.add_todo(todo)
    if response:
        return response
    raise HTTPException(status_code=400,
                        detail='Something went wrong - Cant add todo - Bad request.')


@app.put('/edit-todo/{ToDo}', response_model=ToDo)  # nb: PUT verb for update
async def edit_todo(todo: ToDo):  # we assume that we get *edited* to-do
    response = await database.edit_todo(todo_id=todo.id,
                                        new_title=todo.title,
                                        new_description=todo.description)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo.id}')


@app.delete('/delete-todo/{todo_id}')
async def delete_todo(todo_id):
    response = await database.delete_todo(todo_id=todo_id)
    if response:
        return {
            'status': 'success',
            'id': todo_id
        }
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo_id}')
