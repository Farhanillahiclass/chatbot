# Usage Guide

## Starting a Conversation

1. **Launch the app** by running `streamlit run streamlit_app.py`
2. **Enter your OpenAI API key** in the password field at the top of the page
3. **Type a message** in the chat input at the bottom of the page
4. **Press Enter** to send your message

## Chat Interface

The chat interface consists of:

- **API Key Input**: A password-masked text field where you enter your OpenAI API key
- **Chat History**: Displays all messages in the current session, with user messages and assistant responses clearly distinguished
- **Chat Input**: A text field at the bottom of the page for typing new messages

## How It Works

1. When you type a message, it is added to the session state and displayed in the chat
2. The message history is sent to the OpenAI GPT-3.5 API
3. The response is streamed back in real-time, appearing character by character
4. Both your message and the assistant's response are stored in session state for the duration of the session

## Tips

- **Context window**: The chatbot sends the full conversation history with each request. For very long conversations, consider refreshing the page to start fresh.
- **API key security**: Your API key is entered locally and sent directly to OpenAI. It is not stored or logged by the application.
- **Streaming**: Responses appear in real-time as they are generated. You can see the text being typed out character by character.

## Managing Your API Key

You have two options for providing your OpenAI API key:

### Option 1: Manual Entry (Default)
Enter the key in the text input field each time you use the app.

### Option 2: Streamlit Secrets
Create a file at `.streamlit/secrets.toml` in the project root:

```toml
OPENAI_API_KEY = "sk-your-api-key-here"
```

Then modify the app to read from `st.secrets["OPENAI_API_KEY"]` instead of the text input.
