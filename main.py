import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Step 1: Extract command line arguments
user_prompt = sys.argv[1]  # Get the prompt
verbose = False  # Default to not verbose

# Check if verbose flag is present
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    verbose = True
    print(f"User prompt: {user_prompt}")  # This can go here since user_prompt exists
    
# Step 2: Build messages using the extracted prompt
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Step 3: Make the API call
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages)

# Step 4: Handle verbose output
if verbose:
    # Now response exists, so you can print the token counts here
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Step 5: Print the response
print(response.text)