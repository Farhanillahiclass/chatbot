# Frequently Asked Questions

## General

### What model does this chatbot use?
The chatbot uses OpenAI's **GPT-3.5-turbo** model by default. You can change this in the `streamlit_app.py` file. See the [Configuration](Configuration) page for details.

### Is this chatbot free to use?
The chatbot application itself is free and open-source under the Apache 2.0 license. However, you need an OpenAI API key, which requires an OpenAI account with billing set up. OpenAI charges based on usage (tokens processed).

### Where can I get an OpenAI API key?
Visit [OpenAI's API Keys page](https://platform.openai.com/account/api-keys) to create an API key. You will need to create an OpenAI account and set up billing.

## Troubleshooting

### The app shows "Please add your OpenAI API key to continue"
You need to enter a valid OpenAI API key in the text input field. Make sure your key starts with `sk-` and that your OpenAI account has billing enabled.

### I get an "AuthenticationError"
This means your API key is invalid or expired. Generate a new key from the [OpenAI Platform](https://platform.openai.com/account/api-keys).

### I get a "RateLimitError"
You have exceeded your OpenAI API rate limit or quota. Check your [usage dashboard](https://platform.openai.com/usage) and ensure you have sufficient credits.

### The app is slow to respond
- GPT-3.5-turbo is generally fast, but response time depends on the length of the conversation and the response
- Check your internet connection
- The OpenAI API may experience high traffic at times

### Chat history disappears when I refresh the page
This is expected behavior. Chat history is stored in Streamlit's session state, which resets on page refresh. To persist chat history, you would need to add a database or file-based storage mechanism.

### How do I change the chatbot's personality?
Add a system message to the initial session state. See the [Configuration](Configuration) page for instructions on adding a system prompt.

## Development

### Can I use a different LLM provider?
Yes. You would need to modify `streamlit_app.py` to use a different API client. Many providers offer OpenAI-compatible APIs, making the switch straightforward.

### How do I add more features?
Common enhancements include:
- Adding a system prompt for custom behavior
- Implementing chat history persistence with a database
- Adding file upload capabilities
- Integrating with other APIs or tools
- Adding user authentication

### Can I deploy this for production use?
Yes. See the [Deployment](Deployment) page for various deployment options. For production use, consider adding authentication, rate limiting, and proper secrets management.
