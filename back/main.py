from pydantic import BaseModel
from model_services import predict_burnout
from database import collection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend working"}

@app.get("/github/{username}")
def github_user(username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    data = response.json()

    if data.get("message") == "Not Found":
        return data

    collection.update_one(
    {"username": data["login"]},
    {
        "$set": {
            "repos": data["public_repos"],
            "followers": data["followers"],
            "following": data["following"],
            "avatar": data["avatar_url"]
        }
    },
    upsert=True
)

    return data



class BurnoutRequest(BaseModel):
    lateNightCommits: int
    weekendCommits: int
    codingStreak: int
    reviewLoad: int


@app.post("/predict-burnout")
def predict(data: BurnoutRequest):

    result = predict_burnout(
        data.lateNightCommits,
        data.weekendCommits,
        data.codingStreak,
        data.reviewLoad
    )

    collection.insert_one({

        "lateNightCommits":
        data.lateNightCommits,

        "weekendCommits":
        data.weekendCommits,

        "codingStreak":
        data.codingStreak,

        "reviewLoad":
        data.reviewLoad,

        "burnoutRisk":
        result

    })

    return {

        "burnoutRisk":
        result

    }

    