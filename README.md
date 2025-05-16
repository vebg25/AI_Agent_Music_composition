## 🎼 AI Music Agent Generator 🎶
#### A Modular AI-Powered Music Agent Composition Pipeline Using LangGraph, LLMs, and music21

### Overview
#### AI Music Agent Collaborator is an interactive AI-powered music generation system that turns a simple musical idea (like “a happy piano tune in C major”) into a complete MIDI composition.

#### This is achieved through a modular, multi-step LangGraph pipeline that simulates a collaborative music creation process:

### -🧠 Melody generation
         
### -🎹 Harmony creation

### -🥁 Rhythm analysis

### -🎼 Style adaptation

### -🎧 MIDI synthesis and playback

### 🛠 Features
### -✅ LLM-powered composition using Groq's Llama models via LangChain

### -🧩 Modular graph-based pipeline via LangGraph

### -🎵 Music theory encoded with the help of music21

### -🔊 Playable MIDI output using pygame

### -🌱 Built for experimentation and musical creativity

### 📦 Directory Structure
```bash

├── config/               # LLM setup
├── core/                 # Graph and state logic
├── components/           # Individual LangGraph nodes
├── utils/                # Playback utility
├── .env                  # Groq API key
├── main.py               # Entry point
├── requirements.txt      # Dependencies
└── README.md             # Project doc
```
### ⚙️ Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/vebg25/AI_Agent_Music_composition.git
```

2. Install dependencies
```bash

pip install -r requirements.txt

```
3. Set your API key

Create a .env file in the root directory:

```ini
GROQ_API_KEY=your_groq_key_here
```
### 🚀 Run the Project
```bash
python main.py
```

### 📚 Technologies Used
#### -LangGraph – graph-based multi-agent execution engine

#### -LangChain – LLM orchestration framework

#### -Groq llama 3.1-8b model – natural language generation

#### -music21 – music representation and MIDI creation

#### -pygame – audio playback

#### -python-dotenv – environment management

### 🔄 Pipeline Breakdown

| Stage       | Component     | Description                                   |
| ----------- | ------------- | --------------------------------------------- |
| 🎼 Melody   | `melody.py`   | Generates main melodic line from prompt       |
| 🎹 Harmony  | `harmony.py`  | Adds chord progressions to match melody       |
| 🥁 Rhythm   | `rhythm.py`   | Applies rhythm patterns to melody and harmony |
| 🎻 Style    | `style.py`    | Transforms music into desired genre/style     |
| 🧾 MIDI     | `midi.py`     | Converts composition to playable `.mid`       |
| 🔊 Playback | `playback.py` | Plays back the final output using pygame      |
