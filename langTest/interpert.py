import json


def comp(url:str,name:str):
    with open("./data.json" , "r") as f:
        dict = json.load(f)


    with open(url , "w") as f:
        f.write(f'''
card {name}-one
    title "the educational challenge : {dict["problems"]["Title 1"]}"
    text "{dict["problems"]["Para 1"]}"
    choice "solution" -> {name}-one

card {name}-one-solution
    title "the educational challenge : {dict["problems"]["Title 1"]}"
    text "{dict["solution"]["para1"]}"
    choice "child reaction" -> {name}-one-reaction


card {name}-one-reaction
    title "{dict["problems"]["Title 1"]} : childern reaction"
    text "{dict["child reposnes"]["one"]}"
    choice "child reaction" -> {name}-two

card {name}-two
    title "the educational challenge : {dict["problems"]["Title 2"]}"
    text "{dict["problems"]["Para 2"]}"
    choice "solution" -> {name}-two

card {name}-two-solution
    title "the educational challenge : {dict["problems"]["Title 2"]}"
    text "{dict["solution"]["para2"]}"
    choice "child reaction" -> {name}-two-reaction


card {name}-two-reaction
    title "{dict["problems"]["Title 2"]} : childern reaction"
    text "{dict["child reposnes"]["two"]}"
    choice "child reaction" -> {name}-three

card {name}-three
    title "the educational challenge : {dict["problems"]["Title 3"]}"
    text "{dict["problems"]["Para 3"]}"
    choice "solution" -> {name}-three

card {name}-three-solution
    title "the educational challenge : {dict["problems"]["Title 3"]}"
    text "{dict["solution"]["para3"]}"
    choice "child reaction" -> {name}-three-reaction

card {name}-three-reaction
    title "{dict["problems"]["Title 3"]} : childern reaction"
    text "{dict["child reposnes"]["three"]}"
    choice "child reaction" -> {name}-end

card {name}-end
    title "practice finshied"
    text "thank you for your time" 
''')

