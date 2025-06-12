# ✅ `README.md`

# Gemini Multi-Turn Chat

This project is a console-based chatbot using the **Google Gemini 1.5 API** with multi-turn memory and temperature control.

## 🧠 Features

- Uses `gemini-1.5-flash` via `google-genai`
- Preserves context across multiple messages
- Allows the user to control the temperature parameter (creativity of output)
- Runs entirely in the terminal

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Set up API key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Run the chatbot

```bash
python gemini_chat.py
```

You'll be prompted to enter the temperature and then engage in a multi-turn chat. Responses will reflect the full conversation context.

## ✅ Example

```
Set temperature (e.g., 0.7 for balanced creativity): 0.7

User [1]: What is the future of AI?
Gemini [1]: The future of AI holds vast potential, with advances in fields like healthcare, education, and climate modeling...

User [2]: Can it replace human jobs?
Gemini [2]: AI may automate some jobs but is more likely to augment human capabilities...

User [3]: So should we be worried?
Gemini [3]: A healthy balance of optimism and caution is wise...
```

✅ **Final Output:** The final Gemini response is printed at the end of the conversation.

