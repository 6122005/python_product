# python_product

# WhatsPilot AI

Day 36

Backend only.

## Features

- Uses Gemini API
- Generates WhatsApp replies
- Backend separated into modules
- No UI

## Run

Install packages

```bash
pip install -r backend/requirements.txt
```

Create `.env`

```env
GOOGLE_API_KEY=YOUR_KEY
```

Run

```bash
cd backend
python test.py
```








# WhatsPilot AI

## Day 37 Progress

### Features

- Gemini API integration
- Backend separated into modules
- Streamlit web interface
- Text input
- Generate Reply button
- AI-generated WhatsApp reply

## Project Structure

```
whatspilot-ai/
│
├── backend/
│   ├── core.py
│   ├── llm.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
├── README.md
└── .gitignore
```

## Install

```bash
pip install -r backend/requirements.txt
```

## Run

```bash
streamlit run frontend/app.py
```





## Day 38 Progress

### New Features

- Empty input validation
- Whitespace validation
- Maximum 500-character input limit
- Loading spinner while AI generates a reply
- Success notification
- Error handling with try/except
- Improved user experience




## Day 39 Progress

### New Features

- Reply history using Streamlit Session State
- Stores the latest 5 generated replies
- Expandable history section
- Built-in copy button for each reply using `st.code()`
- Clear History button