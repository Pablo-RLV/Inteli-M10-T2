import base64
import io
import json

from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from PIL import Image
from redis import Redis
from rembg import remove

from helpers.decoder import decoder

redis = Redis(host="redis", port=6379, db=0, decode_responses=True)

app = FastAPI()

class ImageRequest(BaseModel):
    base64_image: str

def remove_background_from_base64(base64_image: str) -> str:
    try:
        image_data = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_data))

        result_image = remove(image)

        buffered = io.BytesIO()
        result_image.save(buffered, format="PNG")
        base64_output_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return base64_output_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/remove-bg", tags=["Image"], status_code=200)
async def remove_bg(image_request: ImageRequest, auth_id: str =  Header(...)):
    try:
        auth = json.loads(redis.get(auth_id))
        if not auth.get("access token"):
            return HTTPException(status_code=401, detail="Unauthorized request")
        base64_result = remove_background_from_base64(image_request.base64_image)
        return {"base64_image": base64_result}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
