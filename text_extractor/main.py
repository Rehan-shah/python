import re
import json
import fitz
from test import search_word_meaning

pre_json = {}


def extract_text_from_pdf(pdf_path):
    filename = pdf_path
    doc = fitz.open(filename)
    last_chapter = None
    question_mode = True
    state_q = False
    last_chapter = "Chapter 1"
    qes = None
    for page in doc:
        print(last_chapter)
        string = page.get_text()
        list = string.split("\n")
        state = True
        last_question = None
        if list[len(list) - 2].startswith("Chapter"):
            last_chapter = list[len(list) - 2]
            pre_json[last_chapter] = {}
            question_mode = True
            state_q = False

        if "Answers" in string:
            print("yes")
            question_mode = False
        for string in list:
            if question_mode:
                if "Sentence Completion Questions" in string:
                    state = False

                if list[len(list) - 2].startswith("Chapter"):
                    pass
                if state and re.match(r'^\d{1,3}\.', string):
                    split_string = string.split(".")
                    number = split_string[0].strip()
                    pre_json[last_chapter][f"{number}"] = {"Question": string[2:]}
                    last_question = f"{number}"
                find_n = False 
                for letter in ["a", "b", "c", "d", "e"]:
                    if state and string.startswith(letter):
                        # pre_json[last_chapter][f"{last_question}"][letter] = {"option": string[3:],
                        #                                                       "meaning": search_word_meaning(
                        #                                                           string[3:])}

                        pre_json[last_chapter][f"{last_question}"][letter] = {"option": string[3:],
                                                                              "meaning":"hii"}
                        find_n = True

                if re.match(r"^\d{4,}\.", string) and state and not find_n:
                    split_string = string.split(".")
                    number = split_string[0].strip()
                    pre_json[last_chapter][f"{number[:3]}"] = {"Question": string}
                    last_question = f"{number[:2]}"
                elif state and not find_n:
                    try:
                        pre_json[last_chapter][last_question]["Question"] += string
                    except:
                        pass
            else:
                print(qes)
                if string.startswith("Answers"):
                    print("also yes")
                    state_q = True
                elif re.match(r'^\d{1,4}\.', string) and state_q:
                    qes = string.split(".")[0]
                elif state_q:
                    try:
                        pre_json[last_chapter][qes]["Answer"] += string
                    except KeyError:
                        pre_json[last_chapter][qes]["Answer"] = string

    doc.close()


extract_text_from_pdf('main.pdf')

with open("test.json", "w") as f:
    json.dump(pre_json, f)
