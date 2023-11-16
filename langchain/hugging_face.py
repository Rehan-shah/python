from transformers import HfAgent
from transformers import OpenAiAgent
from PIL import Image
import matplotlib.pyplot as plt
import requests


# Starcoder agent
agent = OpenAiAgent(model="text-davinci-003", api_key="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")
# StarcoderBase
# agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoderbase")
# OpenAssistant
# agent = HfAgent(url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

# Load an image from a URL or a local file
url = "https://cdn.discordapp.com/attachments/1070967585279049741/1108679719278346240/image.png"
image = Image.open(requests.get(url, stream=True).raw)
image = image.convert("RGB")
image = image.resize((224, 224))



prompt = "draw a box around a  element with a label around it of what time .Element can a shape , image or a text. " \
         "The image should be the last thing you should label if the image can not fit image or text"
# Run the agent with a natural language query and the image
mask = agent.run(prompt, image=image)
im = Image.open(mask)
plt.imshow(im)
plt.show()
