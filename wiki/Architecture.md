# Architecture

## Project Structure

```
chatbot/
├── .devcontainer/
│   └── devcontainer.json    # Dev Container / Codespaces configuration
├── .github/
│   └── CODEOWNERS           # Code ownership for reviews
├── .gitignore               # Git ignore rules
├── LICENSE                  # Apache License 2.0
├── README.md                # Project README
├── requirements.txt         # Python dependencies
└── streamlit_app.py         # Main application file
```

## Application Flow

```
User Input → Streamlit UI → OpenAI API → Streamed Response → Display
                ↕
         Session State (chat history)
```

### Detailed Flow

1. **Initialization**: Streamlit renders the page with the title, description, and API key input
2. **API Key Validation**: The app checks if an API key has been entered before proceeding
3. **Session State Setup**: On first run, an empty message list is initialized in `st.session_state`
4. **Message Display**: Existing messages from session state are rendered using `st.chat_message`
5. **User Input**: When the user submits a message via `st.chat_input`:
   - The message is appended to session state
   - The message is displayed in the chat UI
6. **API Call**: The full conversation history is sent to the OpenAI API with `stream=True`
7. **Response Streaming**: The response is rendered incrementally using `st.write_stream`
8. **State Update**: The assistant's complete response is appended to session state

## Key Components

### Streamlit Session State
- Stores chat messages as a list of dictionaries with `role` and `content` keys
- Persists across Streamlit script reruns (triggered by user interaction)
- Resets when the page is refreshed or the app is restarted

### OpenAI Client
- Uses the `openai` Python package to communicate with the GPT-3.5-turbo model
- Streaming is enabled for real-time response display
- The full conversation history is sent with each request to maintain context

### Chat Message Format
Each message in session state follows this structure:
```python
{
    "role": "user" | "assistant",
    "content": "message text"
}
```

## Dependencies

| Package    | Purpose                              |
|------------|--------------------------------------|
| streamlit  | Web UI framework with chat components|
| openai     | OpenAI API client library            |
