# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import json
import uvicorn
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from io import BytesIO
from PIL import Image
from detection.detection import process_image_pred
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Poetry!"}

@app.post("/img")
async def process_image(image: UploadFile = File(...)):
    # Check if the uploaded file is an image
    try:
        # Check if the uploaded file is a valid image type
        if image.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid file type. Only JPEG and PNG are supported."},
            )

        # Example: Read the image content
        image_content = await image.read()

        # Load the image from binary content
        image_pil = Image.open(BytesIO(image_content))

        # Convert the image to a NumPy array
        image_array = np.array(image_pil)

#        print(image_array)
        input_image: np.ndarray = cv2.imread("example_1.jpg")
        result = process_image_pred(input_image)

        if result is None:
            return JSONResponse(
                status_code=500,
                content={"error": "Failed to analyze the image. Please try again."},
            )

        return JSONResponse(
            status_code=200,
            content={
                "filename": image.filename,
                "content_type": image.content_type,
                "analysis": result,
            },
        )
    except Exception as e:
        return JSONResponse(
        status_code=500,
        content={"error": f"An unexpected error occurred: {str(e)}"},
    )

    # Add your processing logic here (e.g., save the image, analyze it, etc.)
    # For now, we'll just return the filename and content type
    # response = {
    #     "filename": image.filename,
    #     "content_type": image.content_type,
    #     "message": "Image processed successfully",
    #     "age": "1212",
    #     "gender": "MMFF",
    #     "emotion": "HHSS",
    # }
    #
    # return response


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


import  os
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
