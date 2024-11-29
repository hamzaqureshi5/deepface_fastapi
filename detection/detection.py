from typing import Any

import numpy as np
from deepface import DeepFace
import cv2
from typing import Union


def process_image(input_image: np.ndarray) -> Union[dict, None]:
    try:
        #        input_image: cv2.Mat = cv2.imread("example_1.jpg")

        # Get results
        result: list[dict[str, Any]] = DeepFace.analyze(
            input_image,
            actions=["age", "gender", "emotion"],
            detector_backend="opencv",
            anti_spoofing=False,
            enforce_detection=True,
            expand_percentage=100,
        )
        age = result[0]["age"]
        gender = result[0]["dominant_gender"]
        emotion = result[0]["dominant_emotion"]
        print(".............................................")
        print("Age: ", age, "Gender: ", gender, "Emotion: ", emotion)
        resp: dict = {'age': age, 'gender': gender, 'emotion': emotion}
        return resp
    except Exception as e:
        print(e)

#        return dict('error': str(e))
