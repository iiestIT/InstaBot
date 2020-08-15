from insta_bot.api.api import api
import uvicorn


def run():
    uvicorn.run(api, host="0.0.0.0", port=8000)
