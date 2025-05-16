# components/midi.py

import music21, random, tempfile
from core.state import MusicState
from typing import Dict

def midi_converter(state: MusicState) -> Dict:
    piece = music21.stream.Score()
    piece.append(music21.expressions.TextExpression(state["composition"]))

    scales = {
        'C major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C minor': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
    }
    chords = {
        'C major': ['C4', 'E4', 'G4'],
        'C minor': ['C4', 'Eb4', 'G4'],
    }

    def create_melody(scale, duration):
        melody = music21.stream.Part()
        for _ in range(duration):
            note = music21.note.Note(random.choice(scale) + '4')
            note.quarterLength = 1
            melody.append(note)
        return melody

    def create_chords(chord_set, duration):
        harmony = music21.stream.Part()
        for _ in range(duration):
            chord = music21.chord.Chord(random.choice(list(chord_set.values())))
            chord.quarterLength = 1
            harmony.append(chord)
        return harmony

    scale_name = 'C minor' if 'minor' in state['musician_input'].lower() else 'C major'
    melody = create_melody(scales[scale_name], 7)
    harmony = create_chords(chords, 7)

    melody.append(music21.note.Note(scales[scale_name][0] + '4'))
    harmony.append(music21.chord.Chord(chords[scale_name]))

    piece.append(melody)
    piece.append(harmony)
    piece.insert(0, music21.tempo.MetronomeMark(number=60))

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as temp_midi:
        piece.write('midi', temp_midi.name)

    return {"midi_file": temp_midi.name}
