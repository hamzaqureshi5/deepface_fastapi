# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Poetry!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/img")
async def process_image(image: UploadFile = File(...)):
    # Check if the uploaded file is an image
    # if image.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
    #     return JSONResponse(
    #         status_code=400,
    #         content={"error": "Invalid file type. Only JPEG and PNG are supported."},
    #     )

    # Example: Read the image content
    image_content = await image.read()

    # Add your processing logic here (e.g., save the image, analyze it, etc.)
    # For now, we'll just return the filename and content type
    response = {
        "filename": image.filename,
        "content_type": image.content_type,
        "message": "Image processed successfully",
    }

    return response


# Define a model for the input JSON
class TestRequest(BaseModel):
    id: str
    img: str


# Define the test endpoint
@app.post("/testjson")
async def test_json(request: TestRequest):
    # Access input data
    id = request.id
    img = request.img

    # processing function

    #    process_image()

    # Example processing logic
    response_data = {
        "id": id,
        "img": img,
        "age": "1",
        "gender": "male",
        "emotion": "neutral",
        "detected": "true"
    }

    # Return JSON response
    return response_data


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
