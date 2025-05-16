# core/workflow.py

from langgraph.graph import StateGraph, END
from core.state import MusicState
from components.melody import melody_generator
from components.harmony import harmony_creator
from components.rhythm import rhythm_analyzer
from components.style import style_adapter
from components.midi import midi_converter

def build_workflow():
    workflow = StateGraph(MusicState)
    workflow.add_node("melody_generator", melody_generator)
    workflow.add_node("harmony_creator", harmony_creator)
    workflow.add_node("rhythm_analyzer", rhythm_analyzer)
    workflow.add_node("style_adapter", style_adapter)
    workflow.add_node("midi_converter", midi_converter)

    workflow.set_entry_point("melody_generator")
    workflow.add_edge("melody_generator", "harmony_creator")
    workflow.add_edge("harmony_creator", "rhythm_analyzer")
    workflow.add_edge("rhythm_analyzer", "style_adapter")
    workflow.add_edge("style_adapter", "midi_converter")
    workflow.add_edge("midi_converter", END)

    return workflow.compile()
