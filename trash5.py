# Imports
import time

# Start Timer
start = time.time()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random

# Local Imports
from var.names import fname
from var.surname import lname
from var.others import *

# Chrome Start
driver = webdriver.Chrome('./chromedriver')

for x in range(10000):
    # First Name Randomizer
    first_name = random.choice(fname)
    second_name = random.choice(lname)

    # Full Screen
    # driver.maximize_window()

    driver.get("https://ffcii.com")
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="access"]').send_keys("FFCI-7CN140", Keys.ENTER)

    except Exception:
        print("Splash Error")
        continue

    # First and Last Name
    try:
        driver.find_element_by_name('firstname').send_keys(first_name)
    except Exception:
        print("Name Error")
        continue

    driver.find_element_by_name('lastname').send_keys(second_name)

    # Age, Gender, Status and Address
    driver.find_element_by_name("birthdate").send_keys(
        (f"{random.randint(1, 9)}/{random.randint(1, 28)}/19{random.randint(60, 89)}"))

    driver.find_element_by_name("age").send_keys(random.randint(21, 98))
    driver.find_element_by_name("gender").send_keys(random.choice(gender))
    driver.find_element_by_name("status").send_keys(random.choice(status))
    driver.find_element_by_name("address").send_keys(random.choice(address))

    # Location
    time.sleep(1)
    test = driver.find_element_by_name("country").send_keys("United States")
    time.sleep(4)
    driver.find_element_by_name("state").send_keys("California")
    time.sleep(1)
    driver.find_element_by_name("city").send_keys(random.choice(cities))

    driver.find_element_by_name("facebookname").send_keys(f"{first_name.lower()}{second_name.lower()}")
    driver.find_element_by_name("emailaddress").send_keys(
        f"{first_name.lower()}{second_name.lower()}@{random.choice(email)}")

    driver.find_element_by_name("chapterlocation_id").send_keys("Abroad")
    time.sleep(1)
    driver.find_element_by_name("chapter_id").send_keys(random.choice(countries))
    driver.find_element_by_name("position_id").send_keys(random.choice(position))

    # Upload File
    driver.find_element_by_id("actual-btn").send_keys(
        f"/home/ubuntu/PycharmProjects/FillUpAI/pictures/download{random.randint(1, 46)}.jpg")

    # break
    # Submit Form
    driver.find_element_by_xpath('//*[@id="form_members"]/div[7]/button').click()
    users_created += 1
    print(f"Total Dummies Created: {users_created}")
    time.sleep(5)

# End Timer
end = time.time()
result = round(end - start, 2)
print(f"Runtime of the program is {result}")