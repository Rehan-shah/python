import fitz
import requests
import io
YEAR = 2022
VERSION = 2
SESSION = "m"

## https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2019/9702_m19_qp_12.pdf


pdf_url = "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2019/9702_m19_qp_12.pdf"
response = requests.get(pdf_url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"fetcch failed {e}")
    exit()


doc = fitz.open(stream=io.BytesIO(response.content) , filetype="pdf")
doc.delete_pages(0 ,2)

print(doc.page_count)

doc.save("hello.pdf")

