from PyDictionary import PyDictionary
import fitz
import json
import re
def search_word_meaning(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)

    if meaning:
        result = ""
        for key, value in meaning.items():
            result += f"{key.capitalize()} meaning(s):\n"
            for index, m in enumerate(value, start=1):
                result += f"{index}. {m}\n"
        return result
    else:
        return "No meaning found for the word."

# Example usage


# def extract_text_from_ans_pdf(pdf_path):
#     filename = pdf_path
#     with open("data.json" ,'r') as doc:
#         pre_json = json.load(doc) 
#
#     doc = fitz.open(filename)
#     state_q = False
#     for pages in doc:
#         last_chapter = "Chapter 1"
#         words = pages.get_text()
#         list = words.split("\n")
#         qes = None
#         for word in list:
#             print(word)
#             if word.startswith("Answers"):
#                 state_q = True
#             elif re.match(r'^\d{1,3}\.', word) and state_q:
#                 qes = word[:len(word)-1]
#             elif state_q :
#                 try :
#                     pre_json[last_chapter][qes]["Answer"] += word
#                 except KeyError :
#                     pre_json[last_chapter][qes]["Answer"] = word
#             elif re.match(r'^d{1,3}]\.' , word) and state_q:
#                 state_q = False
#
#     doc.close()
#
#     with open("n.json","w") as doc:
#         doc.write(json.dumps([pre_json]))
#

