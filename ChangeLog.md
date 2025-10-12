# Changelog

All notable changes to **Project Spanda** will be documented in this file.

---

## [1.1.0] - 2025-10-12
### App & Window Control + Media Actions
#### Added
- Voice-controlled closing of Notepad, Command Prompt, and Browser
- Tells jokes on command
- System shutdown and restart via voice
- Locking the screen using voice command
- Minimize all windows (go to desktop)
- Switch between windows using "alt + tab"
- Open Task View and navigate between open windows (with voice-based "next", "back", "enter", "cancel")
- Tab navigation in browsers:
  - Switch to next/previous tab with window title feedback
  - Close current tab and announce its title
- Basic YouTube controls via voice:
  - Play/pause video
  - Mute/unmute video
  - Fullscreen and exit fullscreen
#### Fixed
- Mentioning time while greeting

#### Need To Fix/Add
- Avoid closing apps that aren’t actually open
- Alarm setting functionality
- Read latest news
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

