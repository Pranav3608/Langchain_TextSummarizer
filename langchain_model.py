# -*- coding: utf-8 -*-
"""langchain_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gH5xlm274y87e0Sp3mQ2D79nP65eol4L
"""

!pip install openai
openai_api_key = "YOUR_OPENAI_API_KEY"
openai_api_type = "AZURE"
openai_api_version = 'YOUR_API_VERSION'
openai_api_base = "YOUR_AZURE_ACCOUNT_OPENAI_ENDPOINT"
model_name="YOUR_MODEL_NAME"

!pip install langchain
from langchain.llms import AzureOpenAI
llm = AzureOpenAI(engine="YOUR_ENGINE_NAME", model_name=model_name, temperature=0, openai_api_key=openai_api_key, openai_api_version=openai_api_version, openai_api_base=openai_api_base, openai_api_type=openai_api_type)

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

input_text = "./apple.txt"

with open(input_text, 'r') as file:
  text = file.read()

!pip install tiktoken

llm.get_num_tokens(text)

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=2000, chunk_overlap = 0)
docs = text_splitter.create_documents([text])

nums_docs = len(docs)
nums_tokens_first_doc = llm.get_num_tokens(docs[0].page_content)
print(f"Now we have {nums_docs} documents and the first one has {nums_tokens_first_doc} tokens")

summary_chain = load_summarize_chain(llm = llm, chain_type='refine', verbose=True)

output = summary_chain.run(docs)

output
