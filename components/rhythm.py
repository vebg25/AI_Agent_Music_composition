# components/rhythm.py

from langchain.prompts import ChatPromptTemplate
from config.llm import llm
from core.state import MusicState
from typing import Dict

def rhythm_analyzer(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Analyze and suggest a rhythm for this melody and harmony: {melody}, {harmony}. Represent it as a string of durations in music21 format."
    )
    chain = prompt | llm
    rhythm = chain.invoke({"melody": state["melody"], "harmony": state["harmony"]})
    return {"rhythm": rhythm.content}
