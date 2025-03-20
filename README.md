# OpenAI-Compatible Gemini Chatbot

A chatbot built to be compatible with OpenAI’s API while leveraging Gemini’s capabilities.

## 🚀 Live Deployment

You can access the live deployment here:  
[**Gemini Chatbot on Vercel**](https://gemini-chiefkarim-chiefkarims-projects.vercel.app/docs)

---

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Introduction

This chatbot integrates OpenAI-compatible API endpoints to support interactions with Gemini’s models. It is built using Python and deployed on **Vercel**.

## ✨ Features

- OpenAI API-compatible interface.
- Supports chatbot conversations.
- Easily deployable via Vercel.
- Structured routes for handling API requests.
- Configurable via environment variables.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone git@github.com:chiefkarim/gemini.git
cd gemini
```

### 2️⃣ Set Up a Virtual Environment Using `uv`

```bash
uv venv  # Create a virtual environment
```

### 3️⃣ Activate the Virtual Environment

```bash
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 4️⃣ Install Dependencies Using `uv`

```bash
uv install
```

### 5️⃣ Set Up Environment Variables

Create a `.env` file and configure it based on your API keys and settings.

---

## 🚀 Usage

### Running Locally

```bash
uvicorn routes.app:app --reload
```

This will start the API server locally.

### API Endpoints

You can test API endpoints via:

- [Swagger UI](http://localhost:8000/docs) (if enabled)
- Postman or similar API testing tools

---

## 🔧 Configuration

Environment variables are stored in `.env`. Here are some expected values:

```
API_KEY=<your-api-key>
```

---

## 🗂️ Project Structure

```
gemini/
│── models/           # Data models and schemas
│── routes/           # API route handlers
│── services/         # Core logic for chatbot interactions
│── scripts/          # Utility scripts
│── .env              # Environment variables (ignored in Git)
│── requirements.txt  # Dependencies
│── pyproject.toml    # Project configuration
│── vercel.json       # Deployment settings
│── README.md         # Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a PR.

---

## 📜 License

[MIT License](LICENSE) – Feel free to modify and use this project.

```

---

Now it correctly uses `uv install` instead of `uv pip install`. Let me know if you need any more refinements! 🚀🔥
```
