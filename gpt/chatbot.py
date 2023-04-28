from .config import *

# classical gpt chat room for recommendations or illustrations
def gpt_chat(
  model="gpt-3.5-turbo", # default model as gpt-3.5-turbo, but gpt-4 is also available to selective users 
  max_tokens=4000,
  temperature=1.2, 
  messages=[{"role":"user","content":"What recommendations can you provide in general regarding a cooperative financial report"}],
  old_messages=[],
  ):
  """_summary_
  model: string, openai model versions https://platform.openai.com/docs/models, default "gpt-3.5-turbo"
  max_tokens: integer, default to 4000
  temperature: integer, default to 1.2
  messages: list[dict], {"role": "user" | "assistant", content: string }, default message applied
  old_messages: list[dict|empty], would be added to new messages as memory, default as empty []
  
  Returns:
    see chat gpt returns https://platform.openai.com/docs/guides/chat/chat-vs-completions
  """
  return openai.ChatCompletion.create(
      model=model,
      max_tokens=max_tokens,
      temperature=temperature,
      messages= messages + old_messages[-1] if old_messages else messages 
    )