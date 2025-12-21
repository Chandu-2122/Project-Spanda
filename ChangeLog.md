# Changelog

All notable changes to **Project Spanda** will be documented in this file.


## Version[2.1.0] - 2025-12-21
### 🧘 Voice-First Reflection Engine & Architecture Stabilization
#### Added
- 🧘 Structured voice-led reflection session workflow:
  - Check-in → Reflection → Tuning → Planning → Closure
- 🧠 Session state tracking using a non-interpretive `state` dictionary
- 📝 Neutral session summary generation using the user’s own words
- 💾 Optional long-term reflection memory with explicit user consent
- 🗂️ Persistent ReflectionMemory to optionally save session summaries to a JSON file.
- ⚡ Exit reflection session gracefully after max retries to continue with normal LLM fallback.
- 🎛️ Profile-driven reflection preferences (tone, structure, pace, prompt style)
- 🧩 Safe, bounded profile updates based only on explicit user feedback
- 🛑 Consent-first design for saving and reading back reflections

#### Changed
- 📦 Modularized speech, workflow, memory, and personalization layers

#### Fixed
- 🐛 Potential crashes from unavailable audio devices
- 🐛 Inconsistent function signatures across internal modules

#### Notes
- This release establishes a **stable, voice-first reflection foundation**
- LLM-guided reflection modules remain present but **inactive**
- No behavioral inference or advice is generated in reflection mode

---

## Version[*.*.*] - Roadmap / Planning Marker
### 🧩 Advanced Memory, Personality & Tool Integration (WIP)
#### Added / In Progress
- 💾 Retrieval-Augmented Generation (RAG) for long-term knowledge:
Spanda will be able to reference personal notes and files to provide context-aware answers. 
- 🤖 Fine-tuning / personality alignment:
Efforts underway to adjust Spanda’s responses to reflect a distinct character and better understanding of the user [Note: to be done only if no fine-tuning method doesn't work good]. 
- 📝 Note-taking capabilities / tool usage:
Spanda will be able to create, read, and update notes using local files or applications like Notepad. 
- 🔄 Dynamic personality switching:
Experimental system prompts allow Spanda’s tone and behavior to change on demand. 
- 🛠️ LangChain / LangGraph pipelines:
Frameworks being integrated to orchestrate memory, RAG retrieval, and tool-based actions.

#### Notes
- No production code was released under this version
- Features listed here may ship across multiple future versions

---

## Version[2.0.0] - 2025-12-16
### 🧠 Local LLM Integration (Ollama)
#### Added
- 🤖 Integrated local LLM using **Ollama (llama3.2:latest)**
- 🧠 Intelligent fallback response system when no voice command matches
- 🗣️ Natural language question answering via LLM
- 🔄 Automatic switch between command-based logic and AI reasoning
- ⚙️ Configurable system prompt to define Project Spanda’s personality
- 💾 Short-term conversational memory via ChatMemory to retain last N user–assistant interactions, allowing context-aware responses and recall

#### Changed
- 🧩 Assistant now attempts reasoning before responding with default errors
- 🔄 LLM fallback now uses memory context to provide more coherent answers

#### Notes
- LLM runs **fully locally** via Ollama (no cloud dependency)
- Voice output continues to use `pyttsx3`
- Memory is currently RAM-only; resets on assistant restart

---

## Version[1.1.0] - 2025-10-13
### App & Window Control + Media Actions
#### Added
- 🗣️📄 Voice-controlled closing of Browser
- 😂 Tells jokes on command
- 📴 System shutdown and 🔄 restart via voice
- Tab navigation in browsers:
  - ➡️⬅️ Switch to next/previous tab with window title feedback
  - ❌🗂️ Close current tab and announce its title
- Basic YouTube controls via voice:
  - ▶️⏸️ Play/pause video
  - 🔇🔊 Mute/unmute video
  - ⛶ Fullscreen and 🔙 exit fullscreen
- 📰 Reads latest news
`- 📷 Takes screenshot
- 😴 Sleeps and wakes up🫡 on command
`
#### Fixed
- 🕰️ Mentioning time while greeting

---

## Version[1.0.0] - 2025-10-12
### 🎉 Initial Release
#### Added:
- 🗣️ Greeting system based on time (Good Morning, Afternoon, Evening)
- 🎧 Speech recognition via microphone input
- 🧠 Command parsing and handling
- 🎶 YouTube integration:
  - Search and play the first result via voice
- ❌ Exit the assistant via voice (e.g., "bye", "quit", "leave")

#### Notes:
- Speech synthesis engine is optimized using fresh pyttsx3 instance per call (for Windows stability).
- Implemented fallback and exception handling for YouTube and Wikipedia errors.

---

