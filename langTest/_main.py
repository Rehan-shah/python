from langchain.chains.mapreduce import MapReduceChain
from langchain.llms.base import LLM
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.document_loaders import YoutubeLoader
from langchain.prompts import PromptTemplate
from typing import Optional , Mapping, List , Any
import requests
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import RetrievalQA


model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

id = requests.get("http://127.0.0.1:5000/start").json()["id"]


class CustomLLM(LLM):

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return requests.post(url='http://127.0.0.1:5000/chat',json={"prompt":prompt , "id" : id}).json()["message"] 
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model" : "falcon-40b"}

llm = CustomLLM()

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=h6FYs_AUCsQ" , add_video_info =True)

docs = loader.load() 
# Map
# map_template = """The following is a set of documents
# {docs}
# Based on this list of docs, please identify the main themes.ONLY INCULED ANSWER IN LISTS. 
# Helpful Answer:"""
# map_prompt = PromptTemplate.from_template(map_template)
# map_chain = LLMChain(llm=llm, prompt=map_prompt , verbose=True)


# para = map_chain.run({"docs": docs})
#
# print(para)
#
# def extract_words_before_colon(text):
#     pattern = r'(\w+)\s*:'
#     matches = re.findall(pattern, text)
#     return matches
#
# list_topic = extract_words_before_colon(para)


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(docs)


vectorstore = Chroma.from_documents(documents=all_splits, embedding=hf)



qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())

response_schemas = [
    ResponseSchema(name="Question", description="Make a MCQ question form this topic"),
    ResponseSchema(name="option 1", description="from a MCQ question give a option 1 for this topic"),
    ResponseSchema(name="option 2", description="from a MCQ question give a option 2 for this topic"),
    ResponseSchema(name="option 3", description="from a MCQ question give a option 3 for this topic"),
    ResponseSchema(name="option 4", description="from a MCQ question give a option 4 for this topic"),
    ResponseSchema(name="answer", description="from a MCQ question give the correct answer for this topic"),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# ans = qa_chain({"query": "Give me a mcq question for Superconductive , The answer should have 4 options , One question and also answer to mcq"})["result"]
#
# print(ans)
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="{format_instructions}\n{answer}",
    input_variables=["answer"],
    partial_variables={"format_instructions": format_instructions})

# _input = prompt.format_prompt(answer=ans)
# output = llm(_input.to_string())
# print(output)
# print(output_parser.parse(output))

ans2 =  qa_chain({"query": "What is meisser effect ? if the answer is not give the text reply with i do not know . USE THE DOCUMENT ONLY FOR ANSWER"})
ans2 =  qa_chain({"query": "What is meisser effect ?"})
print(ans2)

requests.post("http://127.0.0.1:5000/stop" , json={"id" : id})
