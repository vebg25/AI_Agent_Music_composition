# components/style.py

from langchain.prompts import ChatPromptTemplate
from config.llm import llm
from core.state import MusicState
from typing import Dict

def style_adapter(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Adapt this composition to the {style} style: Melody: {melody}, Harmony: {harmony}, Rhythm: {rhythm}. Provide the result in music21 format."
    )
    chain = prompt | llm
    adapted = chain.invoke({
        "style": state["style"],
        "melody": state["melody"],
        "harmony": state["harmony"],
        "rhythm": state["rhythm"]
    })
    return {"composition": adapted.content}
