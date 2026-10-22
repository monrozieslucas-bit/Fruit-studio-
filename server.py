import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from huggingface_hub import InferenceClient

app = FastAPI(title="FruitStudio")
class VideoRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=2000)
    format: str = "9:16"
    duration: int = 10

@app.post("/api/generate")
def generate_video(request: VideoRequest):
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise HTTPException(status_code=503, detail="La clé HF_TOKEN n’est pas configurée côté serveur.")
    # Hugging Face routes the request to an inference provider. Free usage is limited;
    # video generation may require paid credits depending on account/model availability.
    try:
        client = InferenceClient(provider="fal-ai", api_key=token)
        prompt = (
            f"{request.prompt}. Animated cinematic video, format {request.format}. "
            "Colorful expressive characters, smooth motion."
        )
        video_bytes = client.text_to_video(
            prompt,
            model="Wan-AI/Wan2.2-TI2V-5B"
        )
        return Response(content=video_bytes, media_type="video/mp4",
                        headers={"Cache-Control": "no-store"})
    except Exception as exc:
        # Avoid returning secrets or full internal tracebacks to the browser.
        raise HTTPException(
            status_code=502,
            detail="Le fournisseur vidéo a refusé la demande ou le quota est insuffisant. "
                   "Vérifie l’accès au modèle et le quota de ton compte."
        )

app.mount("/", StaticFiles(directory=".", html=True), name="static")
