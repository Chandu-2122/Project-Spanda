# Changelog

All notable changes to **Project Spanda** will be documented in this file.

---
## [1.1.0] - 2025-10-12
### Added
- Wikipedia integration
- YouTube search and playback
- Application opening commands (Notepad, CMD)
### Fixed
- YouTube playback using `youtube-search-python`


---

## [1.0.0] - 2025-10-12
### 🎉 Initial Release

#### Added:
- 🗣️ Greeting system based on time (Good Morning, Afternoon, Evening)
- 🎧 Speech recognition via microphone input
- 🧠 Command parsing and handling
- 📄 Open Notepad via voice command
- 💻 Open Command Prompt via voice
- 📷 Open camera using OpenCV
- 🌐 Open popular websites:
  - Google
  - LinkedIn
  - GitHub
- 🎶 YouTube integration:
  - Search and play the first result via voice
- 🌐 Wikipedia search (voice-triggered + article preview + full-page open)
- 🌍 Fetch and speak the public IP address
- ❌ Exit the assistant via voice (e.g., "bye", "quit", "leave")

#### Notes:
- Speech synthesis engine is optimized using fresh pyttsx3 instance per call (for Windows stability).
- Implemented fallback and exception handling for YouTube and Wikipedia errors.

---

