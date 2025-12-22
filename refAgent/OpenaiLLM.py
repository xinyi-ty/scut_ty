import openai

class OpenAILLM:
    def __init__(self, api_key, prompt=None):
        """Initialize the OpenAI LLM wrapper.

        Args:
            api_key (str): OpenAI API key.
            prompt (str|None): Optional system prompt to set once at initialization.
        """
        openai.api_key = api_key
        self.message_history = []
        self.prompt = None
        # If a prompt is provided at creation, set it once at the start of history
        if prompt is not None:
            self.prompt = prompt
            self.message_history.append({"role": "system", "content": prompt})
    
    def query_llm(self, prompt, query, model="gpt-4", max_tokens=4096):
        """Query the LLM.

        Args:
            prompt (str): System prompt / context.
            query (str | list[str]): Either a single user query string or a list of user query strings.
            model (str): Model name to use.
            max_tokens (int): Maximum tokens for the response.
            temperature (float): Sampling temperature.

        Returns:
            str: Assistant reply or an error message.
        """
        try:
            # Accept either a single string or a list of strings for queries
            queries = query
            if isinstance(queries, str):
                queries = [queries]
            elif queries is None:
                queries = []
            elif not isinstance(queries, list):
                raise TypeError("`query` must be a string or list of strings")

            # Build messages: append system prompt only if not already set in history
            if prompt is not None and not any(m.get("role") == "system" for m in self.message_history):
                # set prompt once and append as the first message
                self.prompt = prompt
                # ensure system message is first
                self.message_history.insert(0, {"role": "system", "content": prompt})

            for q in queries:
                self.message_history.append({"role": "user", "content": q})

            # Fallback: if no user messages provided, keep at least the system prompt
            if not self.message_history:
                raise ValueError("No prompt or queries provided to send to the LLM")

            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model=model,
                messages=self.message_history,
                max_tokens=max_tokens,
                temperature=0.7,
            )

            # Extract response text
            reply = response['choices'][0]['message']['content'].strip()
            self.message_history.append({"role": "assistant", "content": reply})
            return reply

        except Exception as e:
            return f"An error occurred: {str(e)}"