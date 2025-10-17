# 🤖 AI Voice Agent (First Iteration)

This project was my **first experiment** building an **AI-powered voice agent** using **LiveKit** and **Google Realtime AI**.  
The goal was to understand how **AI agents work**, how they **connect to rooms**, and how to build a **voice-activated assistant** from scratch.

---

## Learning Goals
- Understand how an **AI agent session** is created and managed.
- Use **LiveKit Agents SDK** for real-time audio interaction.
- Connect an agent to a **LiveKit room** and process audio input/output.
- Use **Google Realtime Model** for speech generation and responses.
- Learn the workflow of `Agent`, `AgentSession`, and `RoomInputOptions`.

---

## Overview

The agent performs the following steps:
1. Connects to a **LiveKit room** using API credentials.
2. Initializes a **Realtime AI model** (`google.beta.realtime.RealtimeModel`).
3. Starts an **agent session** with noise cancellation and voice settings.
4. Waits for a participant to connect, listens for input, and **generates spoken replies**.

This served as the foundation for later projects (e.g., **SAGE 1.0 Research Agent**).

---

## ⚙️ Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.10+** | Core programming language |
| **LiveKit Agents SDK** | Handles real-time communication and room management |
| **Google Realtime Model** | Provides speech synthesis and AI response generation |
| **dotenv** | Loads environment variables (API keys) |
| **asyncio** | Manages asynchronous tasks |

---

## ▶️ Getting Started

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
2️⃣ Set Environment Variables
Create a .env file in the project root:
```

```
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
GOOGLE_API_KEY=your_google_api_key
3️⃣ Run the Agent
Run the worker in development or console mode:
```

```
python agent.py dev
or
```

```
python agent.py console
The agent will connect to your LiveKit room, initialize the AI voice, and begin listening for input.
```

🎯 Accomplishments
- Built a functioning voice-activated AI agent.
- Learned the structure and workflow of agent sessions.
- Established a foundation for future AI agent development (SAGE series).
