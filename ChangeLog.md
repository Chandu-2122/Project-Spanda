# Changelog

All notable changes to **Project Spanda** will be documented in this file.

## [3.0.0] - Upcoming
### 🗣️🎙️User Voice Cloning
#### Added
- 

#### Changed
- 

#### Notes
- 

---

## [2.1.0] - Planned
### 🎯 Intent-Based Command Routing

#### Added
- 🧠 Intent classification for user queries:
  - Command
  - Question
  - Conversation
  - System control
- 🔀 Dynamic routing between:
  - Rule-based command execution
  - LLM-based responses
- ❓ Clarification prompts for ambiguous inputs

#### Changed
- 🧩 Replaced pure `if/elif` fallback with intent-first decision flow
- 🤖 Reduced unnecessary LLM calls for known commands

#### Improved
- 🎯 Accuracy of command execution
- ⚡ Faster and more relevant responses
- 🗣️ More natural interaction flow

#### Notes
- Intent detection initially rule-based, with optional LLM-assisted classification

---

## [2.0.0] - 2025-12-16
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

## [1.1.0] - 2025-10-14
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

## [1.0.0] - 2025-10-12
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

