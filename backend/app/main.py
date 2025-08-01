# backend/app/main.py
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.services.stream_manager import start_stream, stop_stream, get_status

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start-stream")
def api_start_stream(stream_id: str = Form(...), source: str = Form(...)):
    return start_stream(stream_id, source)

@app.post("/stop-stream")
def api_stop_stream(stream_id: str = Form(...)):
    return stop_stream(stream_id)

@app.get("/status")
def api_status():
    return get_status()
