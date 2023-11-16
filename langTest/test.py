from os import close
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
list = []
driver = webdriver.Edge()

urls = [
    "https://library.camtree.org/items/17e12fe1-fc71-47ea-919b-6e746f3a71b3",
    "https://library.camtree.org/items/a2cd1eac-42d2-4ded-8752-fcd9d943a5a7",
    "https://library.camtree.org/items/96fadfb7-b3b2-4c5e-93bd-1a7a444a7c14",
    "https://library.camtree.org/items/48962a3a-028b-4982-9bc2-e3ae44b907aa",
    "https://library.camtree.org/items/da4db1f1-3826-447a-bdd3-87d4fd171b86",
    "https://library.camtree.org/items/5bc552be-94f7-45c5-9175-395f16658533",
    "https://library.camtree.org/items/fa881ed2-eab4-4c59-b7e9-34850ce87dad",
    "https://library.camtree.org/items/0bedaafc-bffb-467f-82a4-b3b96be42d8b",
    "https://library.camtree.org/items/e45e4150-a00a-4a0f-a807-ca4e0d22cfe4",
    "https://library.camtree.org/items/54da5194-57a3-47a2-a420-82e2d32f24ff",
    "https://library.camtree.org/items/9f4f1973-9f39-49ad-8fa4-a7486f738153",
    "https://library.camtree.org/items/22801d48-a32e-43d9-8ec9-92631863a9d8",
    "https://library.camtree.org/items/a3603a79-d37d-4547-913e-b06c1a03b57c",
    "https://library.camtree.org/items/aed63c34-460a-4268-93f3-85cb1038f2ed",
    "https://library.camtree.org/items/f9872cd8-5155-41b6-938b-d6e921950007",
    "https://library.camtree.org/items/fbd767f9-1272-45bb-adaa-cad40cab48f3",
    "https://library.camtree.org/items/8e105643-a41e-40e9-9b1b-077e45ce81c3",
    "https://library.camtree.org/items/ff243bb2-8ec3-4b7c-b317-22f7bb0bb4cd",
    "https://library.camtree.org/items/19c00d04-9a76-45cb-8094-3a3242dc3608",
    "https://library.camtree.org/items/745f4332-027b-417a-98e2-af79f9c96b6a",
    "https://library.camtree.org/items/69a9f608-6403-4aa7-b1ed-47eef1152e52",
    "https://library.camtree.org/items/abe095df-35e8-47c9-b712-769126b22a06",
    "https://library.camtree.org/items/3d0544c5-bea5-4b6a-a88f-8c9371d580f6"
]

topics = [
    "Collaborative paired Assessment for Learning (AfL) driven swift school improvement",
    "Storytelling through the Arts - Developing opportunities for literacy across the curriculum",
    "Improving the achievement and progress of children with SEND",
    "Behaviour and its impact upon educational attainment; a whole school approach",
    "Using transfer to empower pupils to take responsibility for their learning",
    "Boiler suits and buns: Using modelling in science to develop independent learning",
    "The impact of talk and role play on writing",
    "Raising attainment by establishing whole-school Assessment for Learning (AfL)",
    "STAR: Supporting through the arts – An initiative linking the arts to the development of writing",
    "Raising standards in writing through storytelling",
    "Power of Reading - Raising achievement in literacy through enjoyment and creativity",
    "Behaviour and attendance: The role of the senior leadership team (SLT) in leading and managing improvement",
    "The poetry of podcasting",
    "Creative maths to engage pupils and raise standards",
    "SEAL: Communication and conflict",
    "IDP: Using the Inclusion Development Programme (Autism Spectrum) to support the school community",
    "Every Child a Reader: The wider impact",
    "Reluctant writers project",
    "Using lesson study as a whole-school approach to improving guided writing",
    "Storytelling: Engaging and supporting early writers through Talk for Writing",
    "IDP for Dyslexia and the creative curriculum at Fellside Community Primary School",
    "A whole school approach to guided writing",
    "Increasing children's engagement in independent reading and writing in the Early Years"
]
for n in urls:
    i = 0
    te = topics[i]
    driver.get(n)
    time.sleep(5)

    link = driver.find_element(By.XPATH , '/html/body/ds-app/ds-themed-root/ds-root/div/div/main/div/ds-themed-item-page/ds-item-page/div/div/div/ds-listable-object-component-loader/ds-untyped-item/div[2]/div[1]/ds-themed-item-page-file-section/ds-item-page-file-section/ds-metadata-field-wrapper/div/div/div/ds-themed-file-download-link[1]/ds-file-download-link/a/span[1]')
    link.click()
    time.sleep(10)
    list.append({te : driver.current_url})
    i += 1


print(list)


