
🌐 ARIA — Omnitrix AI

ARIA (Artificial Real-time Intelligent Assistant) is a voice-based conversational AI system designed for seamless human-AI interaction. Built with Python, ARIA integrates speech recognition, text-to-speech, natural language processing, and real-time web search to deliver a truly intelligent assistant experience.

“Think Jarvis, but open-source.”

🚀 Features

- 🎤 Voice Recognition  
  Understands and responds to real-time voice input using SpeechRecognition and PyAudio.

- 🧠 Conversational AI  
  Generates smart, context-aware responses using integrated LLMs (OpenAI/Gemini API support).

- 🌍 Web Search Integration  
  Performs real-time internet searches for current information and answers.

- 🗣️ Text-to-Speech (TTS)  
  Responds audibly with expressive and natural-sounding speech using pyttsx3 or gTTS.

- 🧩 Modular Architecture  
  Designed for flexibility — plug in APIs, animations, or GUI modules easily.

- 🧑‍💻 GUI Interface (Optional)  
  Supports an interactive user interface with neon effects for enhanced visual appeal.

🧰 Tech Stack

- Backend: Python 3.10+
- Speech Recognition: speech_recognition, pyaudio
- Text to Speech: pyttsx3 / gTTS
- AI Integration: OpenAI / Gemini API (optional)
- Web Automation: requests, BeautifulSoup4 / Selenium
- GUI (optional): Tkinter / PyQt5 / custom animation with pygame or manim

⚙️ Installation

# Clone the repo
git clone https://github.com/your-username/Aria-Omnitrix-AI.git
cd Aria-Omnitrix-AI

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

🧪 Usage

# Run the main assistant
python main.py

Or use the GUI version (if available):

python gui_launcher.py

📁 Project Structure

Aria-Omnitrix-AI/
|
├── main.py                # Core logic and voice interaction
├── modules/
│   ├── speech_engine.py   # Handles TTS
│   ├── recognizer.py      # Handles voice input
│   ├── ai_core.py         # AI logic / LLM API integration
│   └── web_search.py      # Real-time search module
├── gui/                   # Optional GUI files
├── assets/                # Neon visuals, sounds, etc.
├── README.md
└── requirements.txt

✨ Future Enhancements

- Voice threading for memory-based context handling  
- Animation modules (neon fairy assistant on start)  
- Real-time system control (open apps, manage files)  
- Integration with IoT devices  
- ChatGPT/Gemini hybrid API support

🤖 Credits

Developed by Nikhil Kumar Singh  
MCA | AI & Cybersecurity Enthusiast | Developer of ARIA  

📜 License

This project is licensed under the MIT License.










# env format

CohereAPIKey = 
Username = Nikhil Singh
Assistantname = Nikhil
GroqAPIKey = 
InputLanguage = en
AssistantVoice = en-CA-ClaraNeural
HuggingFaceAPIKey = 
