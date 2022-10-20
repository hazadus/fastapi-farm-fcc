# FastAPI-MongoDB-React backend for ToDos
Part of FreeCodeCamp FARM tutorial: to-do list API.

**How it works:**
Sign up, log in, get 'access token' in response. Then use it in headers to access 'protected' APIs.
Example:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/user/info/hazadus7%40gmail.com' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiaGF6YWR1czdAZ21haWwuY29tIiwiZXhwaXJlcyI6MTY2NjI3NjEyMS40MDcyNzF9.ZHApsPHULvAQxJkM1p6BIy4ih8xs7VfFHDnCrFHNBmc'
```

**Further development:**
- Read token to see which user requests the API in user_info, [read docs here](https://fastapi.tiangolo.com/tutorial/header-params/#declare-header-parameters).
- Add 'due date', 'is_done' fields to `ToDo` model.
- Try user authorisation with React front end.
- Store users in MongoDB.
- Add password hashing.

## References
- [FreeCodeCamp Tutorial: FARM Stack Course - FastAPI, React, MongoDB](https://www.youtube.com/watch?v=OzUzrs8uJl8)
- [FastAPI Authentication with JWT (JSON Web Tokens)](https://www.youtube.com/watch?v=0_seNFCtglk)
- [Auth - tutorial author's code](https://github.com/BekBrace/FASTAPI-and-JWT-Authentication/tree/cdcf569584aa64613dee8eb53bedad4975dfc7f5)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Install MongoDB on Mac OS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
- [Install MongoDB on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
- [Motor: Asynchronous Python driver for MongoDB](https://motor.readthedocs.io/en/stable/)
- [Pydantic Docs](https://pydantic-docs.helpmanual.io)
- [FastAPI CORS Docs](https://fastapi.tiangolo.com/tutorial/cors/)
- [JSON Web Tokens](https://jwt.io)

## Running
Create and `.env` file in project directory with following variables:
```bash
secret = secret_string_see_below_how_to_create
algorithm = HS256
```
Run the server:
```bash
# Dev:
$ uvicorn main:app --reload --port=8000
# Server:
$ uvicorn main:app --port=8001
```

## Notes
- How to create a 'secret' fast:
```python
import secrets
secrets.token_hex(16)
```