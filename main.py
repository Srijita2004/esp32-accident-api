from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Accident API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read image bytes
    img_bytes = await file.read()

    # Basic validation (image open test)
    try:
        Image.open(io.BytesIO(img_bytes)).convert("RGB")
    except:
        return JSONResponse({"ok": False, "error": "Invalid image"}, status_code=400)

    # ✅ For now: demo response (later we'll load your model here)
    return {"ok": True, "prediction": "no_accident", "confidence": 0.50}
