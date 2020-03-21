from flask import Flask, Response, render_template, request
from bs4 import BeautifulSoup
import pandas as pd
import os

app = Flask(__name__)

def collect_documents(filter = None):
  '''
  Collect and filter documents in the annotated corpus
  '''
  if filter == None:
    filter = ''
  else:
    filter = filter.lower()
  xml = open('final_annotated_corpus.xml').read()
  soup = BeautifulSoup(xml, 'lxml')
  documents = ''
  for document in soup.find_all('document'):
    if filter in document.text.lower():
      documents += '<tr><td>' + str(document) + '</tr></td>'
  return documents

@app.route("/")
def home():
  return render_template('index.html', documents = documents)

@app.route("/search", methods = ['GET'])
def search():
  keyword = request.args.get('keyword')
  documents = collect_documents(filter = keyword)
  return render_template('index.html', documents = documents)
  

if __name__ == "__main__":
  documents = collect_documents(filter = None)
  app.run(host = "0.0.0.0", port = 80)
  
