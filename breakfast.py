import os
import sys
from langchain_openai import ChatOpenAI

# Read the API key from the environment, never hard-coded
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    sys.exit("Error: OPENAI_API_KEY environment variable is not set.")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
prompt = """List exactly 5 healthy breakfast ideas.

"Healthy" means:  Pure south Indian vegetarian breakfasts under 400 kcal.

Format rules:
- Numbered 1 to 5, one idea per line
- Each line is just the dish name with a short description, under 12 words
- No introduction, no closing remarks, no markdown, no blank lines
"""

reply = llm.invoke(prompt)
print(reply.content)  # only the text, not the whole message object