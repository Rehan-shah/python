import os
from suppriser import main
import requests
from interpert import comp


list = [ 
    {'Collaborative paired Assessment for Learning (AfL) driven swift school improvement': 'https://library.camtree.org/server/api/core/bitstreams/fc7038b1-8b37-4ae1-b8da-7feb50d4f118/content'}, 
    {'Collaborative paired Assessment for Learning (AfL) driven swift school improvement': 'https://library.camtree.org/server/api/core/bitstreams/785c1bbb-d0b0-449f-a16a-e27ce40bb86f/content'}, 
    {'Collaborative paired Assessment for Learning (AfL) driven swift school improvement': 'https://library.camtree.org/server/api/core/bitstreams/c049dbad-280b-4a07-89fe-0c698766eef9/content'}, 
    {'Collaborative paired Assessment for Learning (AfL) driven swift school improvement': 'https://library.camtree.org/server/api/core/bitstreams/b407de48-b113-45e2-a3ce-3fb2e21a1de6/content'}, 
    {'Collaborative paired Assessment for Learning (AfL) driven swift school improvement': 'https://library.camtree.org/server/api/core/bitstreams/4f6b90e5-b642-496b-9e00-85770171c7ce/content'}]

topics = [
    "Using lesson study as a whole-school approach to improving guided writing",
    "Storytelling: Engaging and supporting early writers through Talk for Writing",
    "IDP for Dyslexia and the creative curriculum at Fellside Community Primary School",
    "A whole school approach to guided writing",
    "Increasing children's engagement in independent reading and writing in the Early Years"
]


if not len(topics) == len(list):
    raise TypeError('the links and topics obj do not have the same length ')



def to_snake_case(string):
    snake_case_string = string.replace(' ', '_').lower()
    return snake_case_string
# URL from which pdfs to be downloaded
for i in range(0,21):
    for (key , value) in list[i].items():
        url = value
        title = to_snake_case(topics[i])
        main(url)
        os.mkdir("./files/" + title)
        response = requests.get(url)


        with open(f"./files/{title}/{title}.pdf" ,"wb") as f:
            f.write(response.content)

        comp("./files/"+title+"/"+title+".txt" , title) 
        print(f"{title} printeed ")


