import sys
sys.path.append('../')

from prog.files_manager import DataStorage, DATA_STORAGE_PATH
from pathlib import Path

def test_blank():
    assert True

def test_create_file():
    proj1 = DataStorage()
    assert proj1.create_Project() == Path(DATA_STORAGE_PATH, "Data/proj_2024-01-10_1")
    proj2 = DataStorage()
    assert proj2.create_Project() == Path(DATA_STORAGE_PATH, "Data/proj_2024-01-10_2")
    proj3 = DataStorage()
    assert proj3.create_Project() == Path(DATA_STORAGE_PATH, "Data/proj_2024-01-10_3")