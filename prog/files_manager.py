from pathlib import Path
from datetime import datetime
import os

DATA_STORAGE_PATH = os.path.dirname(os.path.abspath(__file__))

class DataStorage:
    def __init__(self) -> None:
        self.storagePath = Path(DATA_STORAGE_PATH, "Data")
        self.projectNumber = len([x for x in self.storagePath.iterdir() if x.is_dir() and str(datetime.today().strftime('%Y-%m-%d')) in str(x)]) + 1
        self.projectName = f"proj_{datetime.today().strftime('%Y-%m-%d')}_{self.projectNumber}"

    def create_Project(self) -> Path:
        projectPath = Path(self.storagePath, self.projectName)
        projectPath.mkdir()
        return projectPath

    def delete_Project(self) -> None:
        pass
        
    def save_file_to_Project(self):
        pass

    def update_project_names():
        pass