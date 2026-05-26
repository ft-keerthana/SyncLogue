print("Loading model...")

import joblib
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml-engine",
    "burnout_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "ml-engine",
    "label_encoder.pkl"
)

print(MODEL_PATH)

model = joblib.load(MODEL_PATH)

print("Model loaded")

encoder = joblib.load(
    ENCODER_PATH
)

print("Encoder loaded")


def predict_burnout(
    lateNightCommits,
    weekendCommits,
    codingStreak,
    reviewLoad
):

    sample = [[
        lateNightCommits,
        weekendCommits,
        codingStreak,
        reviewLoad
    ]]

    prediction = model.predict(sample)

    return encoder.inverse_transform(
        prediction
    )[0]