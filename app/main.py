from fastapi import FastAPI
from .routes import posts,users,auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://www.google.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")
def root():
    return {'message': 'Hello world'}



