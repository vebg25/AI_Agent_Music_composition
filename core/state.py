# core/state.py

from typing import TypedDict

class MusicState(TypedDict):
    musician_input: str
    melody: str
    harmony: str
    rhythm: str
    style: str
    composition: str
    midi_file: str
