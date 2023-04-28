from .config import *
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader
import io
import requests as req
import validators
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# download file from given url
def read_pdf(url=''):
  if not validators.url(url): return ''
  return ''.join(
    [ 
      page.extract_text() 
      # GET pdf by url --> to bytes --> load by PdfReader
      for _,page in enumerate(PdfReader(io.BytesIO(req.get(url=url,timeout=120).content)).pages) 
      if page.extract_text()
    ]) 

# divide large file into small chunk (text collections)
def beautify_pdf_texts(
  pdf_texts='',separator="\n",chunk_size=1000, chunk_overlap=200):
  if not pdf_texts: return ''
  
  return CharacterTextSplitter(        
      separator       = separator,
      chunk_size      = chunk_size,
      chunk_overlap   = chunk_overlap,
      length_function = len,
    ).split_text(pdf_texts)

# gpt word embedding chat-room for summarizing long paragraphs
def gpt_emb(doc_texts='', user_query=''):
  if not doc_texts: return ''
  # Download embeddings from OpenAI
  embeddings = OpenAIEmbeddings()
  # https://python.langchain.com/en/latest/index.html
  docsearch = FAISS.from_texts(doc_texts, embeddings) 
  chain = load_qa_chain(OpenAI(), chain_type="stuff")
  docs = docsearch.similarity_search(user_query)
  return chain.run(input_documents=docs, question=user_query)

