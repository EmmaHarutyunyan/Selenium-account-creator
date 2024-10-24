import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

driver = webdriver.Chrome()

try:
    driver.get("https://www.facebook.com/")
    
    time.sleep(2)  
    create_account_btn = driver.find_element(By.LINK_TEXT, "Create new account")
    create_account_btn.click()

    time.sleep(2) 
    

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    password = generate_random_password()

    time.sleep(2) 
    first_name_input = driver.find_element(By.NAME, "firstname")
    last_name_input = driver.find_element(By.NAME, "lastname")
    email_input = driver.find_element(By.NAME, "reg_email__")
    password_input = driver.find_element(By.NAME, "reg_passwd__")
    birthday_day = driver.find_element(By.NAME, "birthday_day")
    birthday_month = driver.find_element(By.NAME, "birthday_month")
    birthday_year = driver.find_element(By.NAME, "birthday_year")
    gender = driver.find_element(By.XPATH, "//input[@value='2']")

    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)
    email_input.send_keys(email)
    password_input.send_keys(password)
    birthday_day.send_keys("1")  
    birthday_month.send_keys("Jan")
    birthday_year.send_keys("2002") 
    gender.click() 

    sign_up_btn = driver.find_element(By.NAME, "websubmit")
    sign_up_btn.click()

    time.sleep(5) 

    with open("text.txt", "w") as f:
        f.write(f"First Name: {first_name}\n")
        f.write(f"Last Name: {last_name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")

finally:
    driver.quit() 
