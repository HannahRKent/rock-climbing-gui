import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.mountainproject.com/")

data_list = []
states_list = []
num_routes_list = []

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "route-guide"))
    )

    mb_half_elements = element.find_elements_by_class_name("mb-half")
    for mb_half_element in mb_half_elements:
        for element in mb_half_element.find_elements_by_xpath("strong/div/div[1]/*"):
            element_text = element.text
            if element_text != "":
                data_list.append(element.text)

finally:
    driver.quit()

for x, val in enumerate(data_list):
    if x % 2 == 0:
        num_routes_list.append(int(val.replace(",", "")))
    else:
        states_list.append(val)

with open('../data/number_of_routes_by_state.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['state_name', 'number_of_routes'])
    for row in zip(states_list, num_routes_list):
        print(row)
        csv_out.writerow(row)
