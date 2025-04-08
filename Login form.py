import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox

service = Service(executable_path="C:/Users/Teacher/Desktop/Report/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://10.10.99.23/login")

title = driver.title
expected_title = "Log in - DOST-ISSP"
if expected_title != title:
    messagebox.showerror("Login Failed", "Page title doesn't match.")
    raise AssertionError("Login Test Failed")
else:
    print("Login Successfully")

email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")

email_input.send_keys("jioclyde21@gmail.com")
password.send_keys("Dost@1234")
login_button.click()
time.sleep(5)

input("Press Enter to exit and close the browser...")
driver.quit()
