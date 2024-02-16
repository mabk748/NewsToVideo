from pathlib import Path
import glob

AUDIO_EXT = ["aud"]
VIDEO_EXT = ["vid"]
IMAGE_EXT = ["im"]

def get_audio(path: Path):
    files = []
    for i in AUDIO_EXT:
        found = list(path.glob(f"**/*.{i}"))
        print(found)
        for f in found:
            files.append(f)
    print(files)
    return files

def get_video(path: Path):
    files = []
    for i in VIDEO_EXT:
        found = list(path.glob(f"**/*.{i}"))
        for f in found:
            files.append(f)
    return files

def get_images(path: Path):
    files = []
    for i in IMAGE_EXT:
        found = list(path.glob(f"**/*.{i}"))
        for f in found:
            files.append(f)
    return files

class VideoAssembler:
    def __init__(self, projectName: str) -> None:
        self.name = projectName
        self.content = {
            "intro" : {},
            "segments" : [],
            "outro" : {},
            "background": {}
        }

    def get_intro(self, path: Path):
        self.content["intro"]["video"] = get_video(path)
        self.content["intro"]["audio"] = get_audio(path)

    def get_segments(self, path: Path):
        segments = [x for x in path.iterdir() if x.is_dir()]
        for s in segments:
            self.content["segments"].append({})
            self.content["segments"][-1]["video"] = get_video(path)
            self.content["segments"][-1]["audio"] = get_audio(path)
            self.content["segments"][-1]["images"] = get_images(path)

    def get_outro(self, path: Path):
        self.content["outro"]["video"] = get_video(path)
        self.content["outro"]["audio"] = get_audio(path)

    def get_background(self, path: Path):
        self.content["background"]["images"] = get_video(path)
        self.content["background"]["audio"] = get_audio(path)
    
class VideoEditer:
    def __init__(self) -> None:
        pass