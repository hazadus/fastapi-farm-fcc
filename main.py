from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.middleware.cors import CORSMiddleware

from model import ToDo, User, Login
import database
from auth.jwt_handler import sign_jwt
from auth.jwt_bearer import JwtBearer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all for debug purposes ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# 'Demo' user 'DB' to test signup/login functions
users = []


@app.get('/', tags=['Test'])  # 'tags' is used to group APIs in '/docs/' web interface.
async def root():
    return {
        'message': 'Hello API world! fastapi-farm-fcc serving: simple ToDos API.'
    }


@app.get('/all-todos/', tags=['ToDos'])
async def get_all_todos():
    response = await database.get_all_todos()
    return response


@app.get('/todo/{todo_id}', response_model=ToDo, tags=['ToDos'])
async def get_todo(todo_id):
    response = await database.get_todo(todo_id)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo_id}')


@app.post('/add-todo/', response_model=ToDo,   # NB: There should be NO {}s in URL when you pass class!!!
          tags=['ToDos'])
# @app.post('/add-to do/{To Do}', response_model=To Do)  # This is WRONG, caused bugs with frontend!
async def add_todo(todo: ToDo):
    response = await database.add_todo(todo)
    if response:
        return response
    raise HTTPException(status_code=400,
                        detail='Something went wrong - Cant add todo - Bad request.')


@app.put('/edit-todo/{ToDo}', response_model=ToDo, tags=['ToDos'])  # nb: PUT verb for update
async def edit_todo(todo: ToDo):  # we assume that we get *edited* to-do
    response = await database.edit_todo(todo_id=todo.id,
                                        new_title=todo.title,
                                        new_description=todo.description)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo.id}')


@app.delete('/delete-todo/{todo_id}', tags=['ToDos'])
async def delete_todo(todo_id):
    response = await database.delete_todo(todo_id=todo_id)
    if response:
        return {
            'status': 'success',
            'id': todo_id
        }
    raise HTTPException(status_code=404,
                        detail=f'No todos with id={todo_id}')


@app.post('/user/signup/', tags=['User Management'])
async def user_sign_up(new_user: User = Body(default=None)):
    """
    Add a new user. Contents of passed info checked by pydantic, as always.
    """
    users.append(new_user)
    return sign_jwt(new_user.email)


def check_user(user: Login):
    """
    Check if user 'registered' in our API.
    """
    for i_user in users:
        if i_user.email == user.email and i_user.password == user.password:
            return True
    return False


@app.post('/user/login/', tags=['User Management'])
async def user_login(login: Login = Body(default=None)):
    if check_user(login):
        return sign_jwt(login.email)
    else:
        return {
            'error': 'Invalid user credentials.'
        }


@app.get('/user/info/{user_email}',
         dependencies=[Depends(JwtBearer())],   # nb!
         tags=['User Management'])
async def user_info(user_email: str):
    """
    This is to test login/logout functions are working properly.
    """
    for user in users:
        if user.email == user_email:
            return user.json()
    return {
        'error': 'No user with such email registered.'
    }
