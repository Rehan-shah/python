import os
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = "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"


loader = DirectoryLoader("./folder_lllm", glob="**/*.txt")

documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)

texts = text_splitter.split_documents(documents)
print(texts)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

docsearch = Chroma.from_documents(texts, embeddings)

qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)

query = "which was the 1st class that the author attend ?"

hi = qa.run(query)
print("bye")
print(hi)

