# main.py

from core.workflow import build_workflow
from utils.playback import play_midi

if __name__ == "__main__":
    app = build_workflow()
    inputs = {
        "musician_input": "Create a happy piano piece in C major",
        "style": "Romantic era"
    }
    result = app.invoke(inputs)

    print("Composition created.")
    print(f"MIDI file saved at: {result['midi_file']}")
    play_midi(result["midi_file"])
