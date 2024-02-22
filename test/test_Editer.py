import sys
sys.path.append('../')

from pathlib import Path
from prog.Video_Editer import *

def test_blank():
    assert True

def test_getters():
    dir = Path("./testDir")
    assert get_content("audio", dir) == [Path("./testDir/file.aud")]
    assert get_content("video", dir) == [Path("./testDir/file.vid")]
    assert get_content("image", dir) == [Path("./testDir/file.im")]
