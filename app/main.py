from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

#command that tells sqlalchemy to run create 
#statement to generate all of the tables since
# we have alembic its no longer needed
##models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##stored memory json
##array, contain whole bunch of post objects,
##each post is essentially a dictionary
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
# {"title": "favorite shoes", "content": "I like adidas", "id": 2}]
 
# def find_post(id):
#    for p in my_posts:
#        if p["id"] == id:
#            return p
 
# # gives the index of dictionary with the specific id
# def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
   return {"message": "Hello World"}
