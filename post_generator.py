import httpx

async def get_generated_post(prompt: str) -> str:
    url = "https://Tafclassick-Lilly-Social-Post-Generator.hf.space/run/predict"
    payload = {
        "data": [prompt]
    }
    headers = {
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response_data = response.json()
        return response_data["data"][0]
