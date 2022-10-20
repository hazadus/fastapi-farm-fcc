# FastAPI-MongoDB-React backend for ToDos
Part of FreeCodeCamp FARM tutorial: to-do list API.

**How it works:**
Nothing special here yet. Just run server and use the API.

**Further development:**
- Add 'due date', 'is_done' fields to `ToDo` model.
- Add user authorisation.

## References
- [FreeCodeCamp Tutorial: FARM Stack Course - FastAPI, React, MongoDB](https://www.youtube.com/watch?v=OzUzrs8uJl8)
- [FastAPI Authentication with JWT (JSON Web Tokens)](https://www.youtube.com/watch?v=0_seNFCtglk)
- [Install MongoDB on Mac OS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
- [Install MongoDB on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
- [Motor: Asynchronous Python driver for MongoDB](https://motor.readthedocs.io/en/stable/)
- [FastAPI CORS Docs](https://fastapi.tiangolo.com/tutorial/cors/)

## Running
```bash
# Dev:
$ uvicorn main:app --reload --port=8000
# Server:
$ uvicorn main:app --port=8001
```