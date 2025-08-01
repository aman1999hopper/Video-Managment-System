# backend/app/services/dummy_model.py
class DummyModel:
    name = "DummyModel"

    def predict(self, frame):
        return {"message": "Mock inference: green pixels found"}

