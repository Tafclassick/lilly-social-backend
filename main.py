from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from post_generator import get_generated_post

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-post")
async def generate_post(request: PromptRequest):
    try:
        generated_text = await get_generated_post(request.prompt)
        return {"generated_post": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
