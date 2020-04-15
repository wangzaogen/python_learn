from fastapi import FastAPI
my_app = FastAPI()


@my_app.get("/")
def read_index():
    return {"Hello":"World"}