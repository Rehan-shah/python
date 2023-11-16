
import json
from langchain.chains.mapreduce import MapReduceChain
from langchain.llms.base import LLM
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.document_loaders import OnlinePDFLoader, UnstructuredPDFLoader, YoutubeLoader
from langchain.prompts import PromptTemplate
from typing import Optional , Mapping, List , Any
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import RetrievalQA

def main(url):
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    id = requests.get("http://127.0.0.1:5000/start").json()["id"]

    print(id)

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

## load the doc and creat vector stor ##

    loader = OnlinePDFLoader(url)
     

    docs = loader.load() 


    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(docs)


    vectorstore = Chroma.from_documents(documents=all_splits, embedding=hf)



    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())



### Get Problme repsonse ###


    response_schemas = [
        ResponseSchema(name="Title 1", description="Here is the title for the para described"),
        ResponseSchema(name="Para 1", description="Discribes the problem here , minium 100 words"),
        ResponseSchema(name="Title 2", description="Here is the title for the 2nd para described"),
        ResponseSchema(name="Para 2", description="Discribes the 2nd problem here , minium 100 words"),
        ResponseSchema(name="Title 3", description="Here is the title for the 3rd para described"),
        ResponseSchema(name="Para 3", description="Discribes the 3rd problem here , minium 100 words"),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)


    ans = qa_chain({"query": "\nFrom above text : Identify there issues from the passage above. Provide a corresponding title for each issue. Please present only three issues. Describe the issues in approx 100 words"})["result"]


    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template="{format_instructions}\n{answer}",
        input_variables=["answer"],
        partial_variables={"format_instructions": format_instructions})

    _input = prompt.format_prompt(answer=ans)
    output = llm(_input.to_string())
    output = output_parser.parse(output)
    with open("data.json" , "w") as f:
        f.write(json.dumps({"problems" : output}))

### Get teachers repsonse ###




    def get_solution(res):
        ans = qa_chain({"query": f"Problem :{res} Using the text in 100 words give me instrcution a teacher can follow to slove the problem.\n KEEP TO 100 WORDS ONLY AND VERY SHORT"})["result"]
        
        return ans

    sol_1 = get_solution(f"Title : {output['Title 1']} , explanation of the problem : {output['Para 1']}") 


    sol_2 = get_solution(f"Title : {output['Title 2']} , explanation of the problem : {output['Para 2']}")
    sol_3 = get_solution(f"Title : {output['Title 3']} , explanation of the problem : {output['Para 3']}")

    with open("data.json" , "r") as f:
        dic = json.load(f)

    with open("data.json" , "w") as f:
        dic["solution"] = {}
        dic["solution"]["para1"] = sol_1
        dic["solution"]["para2"] = sol_2
        dic["solution"]["para3"] = sol_3

        f.write(json.dumps(dic))



    with open("data.json" , "r") as f:
        dic = json.load(f)

    prompt = PromptTemplate(
        input_variables=["instruc"],
        template="Teacher's answer : {instruc} ,\n Using teachers answe, give as a students reaction to the response witch may be in the class room. Explain how the child felt after giving soltuion. Givee more contexual context",
    )

    chain = LLMChain(llm=llm , prompt=prompt)

    hello =  chain.run(instruc = dic["solution"]["para1"])
    bye =  chain.run(instruc = dic["solution"]["para2"])
    hi =  chain.run(f"This is teacher's answer : {dic['solution']['para3']} \n now using answer judge how will the student in a class recat if teacher imeplented the solution")


    with open("data.json" , "w") as f:
        dic.update({"child reposnes" : {"one" : hello , "two" : bye , "three" : hi}})
        f.write(json.dumps(dic))


    requests.post("http://127.0.0.1:5000/stop" , json={"id" : id})


