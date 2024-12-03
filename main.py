# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
# import cv2
import uvicorn
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from PIL import Image
from api.utlity import process_wrapper

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
        print('len: ', len(image_array), 'shape: ', image_array.shape)
        result = process_wrapper(image_array)

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

os.environ["TF_ENABLE_ONEDNN_OPTS"] = '0'
os.environ['DEEPFACE_HOME'] = "C:/Users/hamza.qureshi/PycharmProjects/deepface_repr"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
