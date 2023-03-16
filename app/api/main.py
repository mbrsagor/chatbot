from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies)

"""
Example-1:
https://github.com/flavien-hugs/fastapi-book-microservice
Example-2:
https://github.com/scalablescripts/fastapi-microservices
Example-3:
https://github.com/marttp/fastapi-microservice
Example-4:
https://github.com/paurakhsharma/python-microservice-fastapi
"""
