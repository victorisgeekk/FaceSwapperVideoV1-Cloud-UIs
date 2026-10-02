import os
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse

app = FastAPI(title="FaceSwapperVideoV1 SageMaker")
REPO_DIR = Path("/opt/program/FaceSwapperVideoV1")
OUTPUT_DIR = Path("/tmp/faceswap-output")


@app.get("/")
def root():
    return {"status": "ok", "message": "FaceSwapperVideoV1 SageMaker service is running."}


@app.post("/swap")
async def swap_video(
    video: UploadFile = File(...),
    source_face: UploadFile = File(...),
    quality: str = Form("high"),
    provider: str = Form("cuda"),
):
    if not REPO_DIR.exists():
        raise RuntimeError("Repo not found. Make sure the upstream FaceSwapperVideoV1 project is mounted or cloned.")

    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    input_video = OUTPUT_DIR / video.filename
    input_face = OUTPUT_DIR / source_face.filename

    input_video.write_bytes(await video.read())
    input_face.write_bytes(await source_face.read())

    output_path = OUTPUT_DIR / "result.mp4"
    import subprocess

    cmd = [
        "python",
        str(REPO_DIR / "cli.py"),
        "swap",
        "--input",
        str(input_video),
        "--source-face",
        str(input_face),
        "--output",
        str(output_path),
        "--quality",
        quality,
        "--provider",
        provider,
        "--keep-audio",
        "true",
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_DIR))
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout or "Face swap failed")

    if not output_path.exists():
        raise FileNotFoundError("Output video was not generated")

    return FileResponse(output_path, media_type="video/mp4", filename="result.mp4")
