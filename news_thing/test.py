import json
import markdown2
import pdfkit



file = open('news_data.json',"r")
data = json.load(file)
file.close()


with open("input.md",'w') as doc:
    doc.write("""# Current affaris 
______\n""")
    for n in data:
        print(n)
        print(data[n]["technology"])
        try:
            worldeco = f"\n### World economci forum" \
                       f"\n- {data[n]['worldeconomic1']}" \
                       f"\n- {data[n]['worldeconomic2']}"
        except :
            worldeco = ""

        doc.write(f"## {n}"
                   f"\n### InShorts"
                   f"\n- {data[n]['national']}"
                   f"\n- {data[n]['world']}"
                   f"\n- {data[n]['business']}"
                   f"\n- {data[n]['technology']}"+worldeco+"\n\n")

filename = "input.md"
# mode = "r"

# with open(filename, mode) as file:
#     markdown_text = file.read()
#     html_text = markdown2.markdown(markdown_text)
#     config = pdfkit.configuration(wkhtmltopdf="/path/to/wkhtmltopdf.exe")
#     pdfkit.from_string(html_text, "output.pdf", configuration=config)
