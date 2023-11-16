import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

repo_id = 'timdettmers/guanaco-33b-merged'

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

template = """Imagine you are amazing prompter whihc generates image prompts out of description. Descriptions is {description}. Rember that it take place in indian school. The theme of the image should be upbright . 

Prompt:
It’s the end of the year- there is an annual performance and the girls in the . 4th are super active and enthusiastic. Rember that it take place in indian.school. The theme of the image should be upbright .""" 


prompt = PromptTemplate(template=template, input_variables=["description"])


llm_chain = LLMChain(prompt=prompt, 
                     llm=HuggingFaceHub(repo_id="timdettmers/guanaco-33b-merged", 
                                        model_kwargs={"temperature":0.001, 
                                                      "max_length":2000}))

question = "It’s the end of the year- there is an annual performance and the girls in the 4th are super active and enthusiastic"

print(llm_chain.run(question))
