from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/bye/{id_name}")
async def bye(id_name: str):
    return {"message": "ByeBye World - %s" % id_name.capitalize() }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

'''-----'''

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    won = "won"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    if model_name.value == "won":
        return {"model_name": model_name, "message": "RTFM - AFK - BTW - IMHO - IMNSHO"}

    return {"model_name": model_name, "message": "Have some residuals"}


'''-----'''


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


'''-----'''


@app.get("/my-maps/{my_map_id}")
async def my_maps(my_map_id: int):
    return {"my_map_id": my_map_id}


@app.get("/my-pyscripts/{my_pyscript_id}")
async def my_pyscript(my_pyscript_id: int):
    return {"my_pyscript_id": my_pyscript_id}




