# backend/app/services/model_pipeline.py
import json
import os

class ModelPipeline:
    def __init__(self, models):
        self.models = models

    def run(self, frame):
        results = {}
        for model in self.models:
            results[model.name] = model.predict(frame)
        return results

    def save_result(self, stream_id, result):
        os.makedirs("data/results", exist_ok=True)
        with open(f"data/results/{stream_id}.json", "a") as f:
            f.write(json.dumps(result) + "\n")
