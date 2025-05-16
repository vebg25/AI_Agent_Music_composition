from langchain.prompts import ChatPromptTemplate
from config.llm import llm
from core.state import MusicState
from typing import Dict

def melody_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Generate a melody based on this input: {input}. Represent it as a string of notes in music21 format."
    )
    chain = prompt | llm
    melody = chain.invoke({"input": state["musician_input"]})
    return {"melody": melody.content}
