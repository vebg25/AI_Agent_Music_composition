# components/harmony.py

from langchain.prompts import ChatPromptTemplate
from config.llm import llm
from core.state import MusicState
from typing import Dict

def harmony_creator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Create harmony for this melody: {melody}. Represent it as a string of chords in music21 format."
    )
    chain = prompt | llm
    harmony = chain.invoke({"melody": state["melody"]})
    return {"harmony": harmony.content}
