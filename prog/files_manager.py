from pathlib import Path
from datetime import datetime
import os

DATA_STORAGE_PATH = os.path.dirname(os.path.abspath(__file__))

class DataStorage:
    def __init__(self) -> None:
        self.storagePath = Path(DATA_STORAGE_PATH, "Data")
        self.projectNumber = len([x for x in self.storagePath.iterdir() if x.is_dir() and str(datetime.today().strftime('%Y-%m-%d')) in str(x)]) + 1
        self.projectName = f"proj_{datetime.today().strftime('%Y-%m-%d')}_{self.projectNumber}"
        self.projectPath = Path(self.storagePath, self.projectName)

    def create_Project(self) -> Path:
        self.projectPath.mkdir()
        return self.projectPath

    def delete_Project(self) -> None:
        empty = not any(self.projectPath.iterdir())
        if empty:
            self.projectPath.rmdir()
        else:
            for i in self.projectPath.iterdir():
                if os.path.isfile(i):
                    i.unlink()
                else:
                    self.delete_Project(i)
        
    def save_file_to_Project(self):
        pass

    def update_projects_names():
        pass


proj = DataStorage()
proj.create_Project()

for i in range(1000000):
    print(i)

proj.delete_Project()
