from typing import Any
import numpy as np
from deepface import DeepFace
#from deepface.commons import package_utils
#from deepface.commons import functions
import cv2
from typing import Union
#from tensorflow.keras.models import load_model

#a = load_model('SASSa')

# Load custom models from your codebase
# age_model = load_model("path/to/age.h5")
# gender_model = load_model("path/to/gender.h5")
# emotion_model = load_model("path/to/emotion.h5")

# Define models in a dictionary as DeepFace expects
# custom_models = {
#     "age": age_model,
#     "gender": gender_model,
#     "emotion": emotion_model
# }


def process_image_prediction(input_image: np.ndarray) -> Union[dict, None]:
    try:
        #        input_image: cv2.Mat = cv2.imread("example_1.jpg")

        # Get results
        result: list[dict[str, Any]]=DeepFace.analyze(
            input_image,
            actions=["age", "gender", "emotion"],
            #            models = custom_models,  # Pass the custom models
            detector_backend="opencv",
            anti_spoofing=False,
            enforce_detection=False,
            expand_percentage=100,

        )
        age = result[0]["age"]
        gender = result[0]["dominant_gender"]
        emotion = result[0]["dominant_emotion"]
        print("......................................................")
        print("......................................................")
        print("Age: ", age, "Gender: ", gender, "Emotion: ", emotion)
        print("......................................................")
        print("......................................................")
        resp: dict = {'age': age, 'gender': gender, 'emotion': emotion}
        return resp
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None
