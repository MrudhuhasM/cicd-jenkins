from pathlib import Path

current_dir = Path(__file__).resolve().parent.parent

DATA_PATH = current_dir / "data"
MODEL_PATH = current_dir / "model"