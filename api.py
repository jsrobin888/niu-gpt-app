from flask import Flask, jsonify, redirect, request
import os
from gpt.chatbot import gpt_chat
from gpt.docs_emb import beautify_pdf_texts, gpt_emb, read_pdf


gptapp = Flask(__name__)
gptapp.config['SECRET_KEY'] = os.urandom(24)

@gptapp.get("/health")
def health():return "healthy"

@gptapp.post("/chat")
def chatapp():
  print("chat")
  model        = request.json['model']        if 'model'         in request.json else "gpt-3.5-turbo"
  max_tokens   = request.json['max_tokens']   if 'max_tokens'    in request.json else 200
  temperature  = request.json['temperature']  if 'temperature'   in request.json else 1.2
  messages     = request.json['messages']     if 'messages'      in request.json else [{ "role": "user","content": "What recommendations could you provide?" }]
  old_messages = request.json['old_messages'] if 'old_messages'  in request.json else []  
  return jsonify(
    gpt_chat(model=model,max_tokens=max_tokens,temperature=temperature,messages=messages,old_messages=old_messages)
  )
@gptapp.post('/file')
def embfile():
  url              = request.json['url']           if 'url'           in request.json else '' 
  separator        = request.json['separator']     if 'separator'     in request.json else '\n' 
  chunk_size       = request.json['chunk_size']    if 'chunk_size'    in request.json else 1000
  chunk_overlap    = request.json['chunk_overlap'] if 'chunk_overlap' in request.json else 200
  user_query       = request.json['user_query']    if 'user_query'    in request.json else ''
  
  return jsonify(
    gpt_emb(
          doc_texts=beautify_pdf_texts(
                      pdf_texts=read_pdf(url),
                      separator=separator,
                      chunk_size=chunk_size,
                      chunk_overlap=chunk_overlap,
                    ),
          user_query=user_query)
  )
if __name__ == "__main__":
  gptapp.run("0.0.0.0",5000)