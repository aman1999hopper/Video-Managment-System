# backend/app/services/stream_manager.py
import cv2
import threading
from .model_pipeline import ModelPipeline
from .dummy_model import DummyModel

stream_handlers = {}

class StreamHandler:
    def __init__(self, source, stream_id):
        self.source = source
        self.stream_id = stream_id
        self.model_pipeline = ModelPipeline(models=[DummyModel()])
        self.running = True
        self.thread = threading.Thread(target=self.run)

    def start(self):
        self.thread.start()

    def run(self):
        cap = cv2.VideoCapture(self.source)
        while self.running:
            ret, frame = cap.read()
            if not ret:
                break
            result = self.model_pipeline.run(frame)
            self.model_pipeline.save_result(self.stream_id, result)

        cap.release()

    def stop(self):
        self.running = False

def start_stream(stream_id, source):
    handler = StreamHandler(source, stream_id)
    handler.start()
    stream_handlers[stream_id] = handler
    return {"message": f"Stream {stream_id} started"}

def stop_stream(stream_id):
    if stream_id in stream_handlers:
        stream_handlers[stream_id].stop()
        return {"message": f"Stream {stream_id} stopped"}
    return {"error": "Invalid stream ID"}

def get_status():
    return {"active_streams": list(stream_handlers.keys())}
