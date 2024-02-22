from pathlib import Path
from moviepy.editor import VideoClip, ImageClip, CompositeVideoClip, concatenate_videoclips


AUDIO_EXT = ["aud"]
VIDEO_EXT = ["vid"]
IMAGE_EXT = ["im"]

def Which_content(Type: str):
    if Type == "audio": 
        return AUDIO_EXT
    elif Type == "video": 
        return VIDEO_EXT
    elif Type == "image":
        return IMAGE_EXT
    else:
        raise ValueError("Type not supported")

def get_content(type: str, path: Path):
    exts = Which_content(type)
    files = []
    for i in exts:
        found = list(path.glob(f"**/*.{i}"))
        print(found)
        for f in found:
            files.append(f)
    return files

class VideoAssembler:
    def __init__(self, projectPath: Path) -> None:
        self.projectPath = projectPath
        self.content = {
            "intro" : {},
            "segments" : [],
            "outro" : {},
            "background": {}
        }

    def get_videoParts(self):
        ContentTypes = ["audio", "video", "image"]
        for k in self.content.keys():
            dirPath = self.projectPath / k
            if dirPath.is_dir():
                if k != "segments":
                    for c in ContentTypes:
                        cont = get_content(c, dirPath)
                        if len(cont) > 0:
                            self.content[k][c] = cont
                else:
                    for s in [x for x in dirPath.iterdir() if x.is_dir()]:
                        self.content[k].append({})
                        for c in ContentTypes:
                            cont = get_content(c, s)
                            if len(cont) > 0:
                                self.content[k][-1][c] = cont
            else:
                raise NameError("Directory not found")

    
class VideoEditer:
    def __init__(self, videoName: str, videoContent: VideoAssembler) -> None:
        self.videoName = videoName
        self.videoContent = videoContent
        self.videoParts = []

    def generate_videoParts(self):
        # Make intro

        pass