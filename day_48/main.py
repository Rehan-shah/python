from selenium import webdriver
from selenium.webdriver.common.by import By

edge_driver_path = "/Users/Rehan/msedgedriver"
driver = webdriver.Edge(executable_path=edge_driver_path)


wd =driver.get("https://www.python.org/")

menu= driver.find_elements(By.CSS_SELECTOR , ".event-widget .shrubbery .menu li")

main_dic = {}

for i ,item in enumerate(menu):
    elements = item.text.split("\n")

    main_dic[i] = {elements[0] : elements[1]}
print(main_dic)

driver.quit()
