from .config import *

# classical gpt chat room for recommendations or illustrations
def gpt_chat(
  model="gpt-3.5-turbo", # default model as gpt-3.5-turbo, but gpt-4 is also available to selective users 
  max_tokens=4000,
  temperature=1.2, 
  messages=[{"role":"user","content":"What recommendations can you provide in general regarding a cooperative financial report"}],
  old_messages=[],
  ):
  return openai.ChatCompletion.create(
      model=model,
      max_tokens=max_tokens,
      temperature=temperature,
      messages= messages + old_messages[-1] if old_messages else messages 
    )