import uuid

import motor.motor_asyncio

from model import ToDo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
# These lines create stuff in MongoDB if not exists already:
database = client.todo_list
collection = database.todo  # it's like a table in SQL DBs


async def add_todo(todo: ToDo):
    document = todo
    todo_with_uuid = {
        'id': str(uuid.uuid1()),
        'title': todo.dict()['title'],
        'description': todo.dict()['description']
    }
    result = await collection.insert_one(todo_with_uuid)
    return todo_with_uuid  # nb: document, not anything else...


async def get_todo(todo_id: str):
    document = await collection.find_one({'id': todo_id})
    return document


async def get_all_todos() -> list:
    todos = []
    cursor = collection.find({})

    async for document in cursor:
        todos.append(ToDo(**document))

    return todos


async def edit_todo(todo_id: str, new_title: str, new_description: str):
    await collection.update_one({'id': todo_id},
                                {
                                    '$set': {
                                        'title': new_title,
                                        'description': new_description
                                    }
                                })
    document = await collection.find_one({'id': todo_id})
    return document


async def delete_todo(todo_id: str):
    await collection.delete_one({'id': todo_id})
    return True
