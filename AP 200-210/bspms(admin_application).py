import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import messagebox

service = Service(executable_path="C:/Users/Teacher/Desktop/Report/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://10.10.99.18:8004/login")

title = driver.title
expected_title = "BSPMS - Balik Scientist Program Management System"

if expected_title != title:
    messagebox.showerror("Login Failed", "Page title doesn't match.")
    raise AssertionError("Login Test Failed")
else:
    print("Logged in Successfully")

email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input.send_keys("sjjinahon@gmail.com")
password.send_keys("Dost@123")
try:
    assert email_input.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button.click()
time.sleep(3)

print("Successfully entered the page.")

try:
    expected_text = "REPUBLIC OF THE PHILIPPINES"
    header = driver.find_element(By.XPATH, "//p[text()='Republic of the Philippines']")
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Balik Scientist Program"
    header = driver.find_element(By.XPATH, '//p[normalize-space(text())="Balik Scientist Program"]')
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "DEPARTMENT OF SCIENCE AND TECHNOLOGY"
    header = driver.find_element(By.XPATH, '//p[normalize-space(text())="Department of Science and Technology"]')
    actual_text = header.text.strip()

    if actual_text == expected_text:
        print(f"Header text sverification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: Expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the 'Applications' sidebar menu label
try:
    expected_text = "Applications"
    App_label = driver.find_element(By.XPATH, '//*[@id="drawer-navigation"]/div[1]/ul/li/a/span[2]')
    actual_text = App_label.text.strip()

    if actual_text == expected_text:
        print(f"Sidebar menu label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Sidebar menu label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Sidebar menu label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

# Verify the 'Applications' header label
try:
    expected_text = "Applications"
    App_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/header/div/h2/div/span')
    actual_text = App_label.text.strip()

    if actual_text == expected_text:
        print(f"Header text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Header text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Header text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Filter by"
    filter_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/main/div[1]/div[1]/div[1]/span')
    actual_text = filter_label.text.strip()

    if actual_text == expected_text:
        print(f"Filter label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Filter label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Filter label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
    assert Profile.is_displayed(), "Profile button is not visible."
    driver.execute_script("arguments[0].click();", Profile)
    time.sleep(3)
    print("Navigated to profile page.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Profile: {e}")

print("Navigated to profile page.")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

try:
    expected_text = "SYSTEM ADMIN"
    SysAd_label = driver.find_element(By.XPATH, '//*[@id="user-dropdown"]/div/span[1]')
    actual_text = SysAd_label.text.strip()

    if actual_text == expected_text:
        print(f"System Admin label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"System Admin label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "System Admin label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "DOST-CO"
    DOSTCO_label = driver.find_element(By.XPATH, '//*[@id="user-dropdown"]/div/span[2]')
    actual_text = DOSTCO_label.text.strip()

    if actual_text == expected_text:
        print(f"DOST-CO sub-label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"DOST-CO sub-label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "DOST-CO label mismatch"
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Change password"
    Change_Ac = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    actual_text = Change_Ac.text.strip()

    if actual_text == expected_text:
        print(f"Change password Action link verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change password Acation link verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Log Out"
    Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
    actual_text = Log_Out.text.strip()

    if actual_text == expected_text:
        print(f"Log Out Action link verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Log Out Action link verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Log Out label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    assert Change_pass.is_displayed(), "Change Password button is not visible."
    driver.execute_script("arguments[0].click();", Change_pass)
    time.sleep(2)
    print("The Change Password button was clicked.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Change Password: {e}")

try:
    expected_text = "Change Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_modal"]/div/div/div[1]/h3')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Confirm New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[3]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


try:
    expected_text = "Current Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[1]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Current password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Current password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[2]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Confirm New Password"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="change_password_form"]/div/div[3]/label')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Change New password Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Change New password label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Change New password label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Save"
    ChangePass = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')
    actual_text = ChangePass.text.strip()

    if actual_text == expected_text:
        print(f"Button Text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Button Text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Button Text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    Close_but = driver.find_element(By.ID, "change_password_modal_close")
    assert Close_but.is_displayed(), "Close button is not visible."
    driver.execute_script("arguments[0].click();", Close_but)
    time.sleep(2)
    print("It closed the close button of the change password modal.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking the close button: {e}")

try:
    Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
    assert Profile.is_displayed(), "Profile button is not visible."
    driver.execute_script("arguments[0].click();", Profile)
    time.sleep(3)
    print("Navigated to profile page.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Profile: {e}")

print("Navigated to profile page.")


try:
    Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    assert Change_pass.is_displayed(), "Change Password button is not visible."
    driver.execute_script("arguments[0].click();", Change_pass)
    time.sleep(2)
    print("The Change Password button was clicked.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Change Password: {e}")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Save = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("")
New_pass.send_keys("")
Confirm_pass.send_keys("")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")


try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="current_password_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "This field is required."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


Change_pas = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pas)
time.sleep(2)
print("The Change Password button was clicked.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Save = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')

Current_pass.send_keys("Dost@12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@12345")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(3)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

try:
    expected_text = "Passwords do not match."
    Error_Message = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation_error"]')
    actual_text = Error_Message.text.strip()

    if actual_text == expected_text:
        print(f"Error Message verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Error Message verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Error Message"

except AssertionError as e:
    print(f"Assertion failed: {e}")


Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Confirm_pass.send_keys("Dost@12")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("Dost@1")
Confirm_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
    print("Change password Successfully")
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")
Save.click()
time.sleep(2)



# Verify the 'Filter by' label
try:
    expected_text = "Password changed successfully."
    Modal_label = driver.find_element(By.XPATH, '//*[@id="swal2-title"]')
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Modal label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Modal label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Modal label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Please login again."
    Modal_label = driver.find_element(By.XPATH, '//*[@id="swal2-html-container"]')
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Sub-label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Sub-label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Sub-label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "OK"
    Modal_label = driver.find_element(By.XPATH, "//button[text()='OK']")
    actual_text = Modal_label.text.strip()

    if actual_text == expected_text:
        print(f"Button Text verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Button Text verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Button Text mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

ok_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
ok_button.click()
time.sleep(2)

email_input6 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password6 = driver.find_element(By.ID, "password")
login_button6 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input6.send_keys("sjjinahon@gmail.com")
password6.send_keys("Dost@123")
try:
    assert email_input6.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password6.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button6.click()
time.sleep(3)

print("Successfully entered the page.")


# Verify the 'Filter by' label
try:
    expected_text = "Filter by"
    filter_label = driver.find_element(By.XPATH, '//*[@id="bsp-content"]/main/div[1]/div[1]/div[1]/span')
    actual_text = filter_label.text.strip()

    if actual_text == expected_text:
        print(f"Filter label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Filter label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Filter label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")
time.sleep(2)

No = driver.find_element(By.XPATH, '//span[contains(@class, "ascending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No)
time.sleep(2)
No1 = driver.find_element(By.XPATH, '//span[contains(@class, "descending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No1)
time.sleep(2)

try:
    expected_text = "No."
    No = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[1]/button/div/span[4]')
    actual_text = No.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

Name = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name)
time.sleep(2)
Name1 = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name1)
time.sleep(2)

try:
    expected_text = "Name"
    Name = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[2]/button/div/span[4]')
    actual_text = Name.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")


Engagement = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement)
time.sleep(2)
Engagement1 = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement1)
time.sleep(2)

try:
    expected_text = "Engagement"
    Engage = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[3]/button/div/span[4]')
    actual_text = Engage.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

HostI = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI)
time.sleep(2)
HostI1 = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI1)
time.sleep(2)

try:
    expected_text = "Host Institution"
    Host_I = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[4]/button/div/span[4]')
    actual_text = Host_I.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

Status = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status)
time.sleep(2)
Status1 = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status1)
time.sleep(2)

try:
    expected_text = "Status"
    Status = driver.find_element(By.XPATH, '//*[@id="applications_table"]/thead/tr/th[5]/button/div/span[4]')
    actual_text = Name.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

dropdown_element = driver.find_element(By.ID, "council_filter")
dropdown_element.click()
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("DOST-CO")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCAARRD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCIEERD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCHRD")
time.sleep(1)

try:
    expected_text = "All"
    label = driver.find_element(By.XPATH, '//*[@id="council_filter"]/option[1]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "DOST-CO"
    label = driver.find_element(By.XPATH, '///*[@id="council_filter"]/option[2]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCAARRD"
    label = driver.find_element(By.XPATH, '///*[@id="council_filter"]/option[3]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCHRD"
    label = driver.find_element(By.XPATH, '///*[@id="council_filter"]/option[4]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "PCIEERD"
    label = driver.find_element(By.XPATH, '///*[@id="council_filter"]/option[5]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"Label verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

dropdown1 = driver.find_element(By.ID, 'status_filter')
dropdown1.click()
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approval')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Legal Clearance')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Evaluation')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Request')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Others')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Disapproved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Revision')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Status')
time.sleep(1)

try:
    expected_text = "Status"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[1]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Approval"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[2]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Legal Clearance"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[3]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Evaluation"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[4]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Request"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[5]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)

try:
    expected_text = "Others"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[6]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Approved"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[7]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Disapproved"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[8]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Revision"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[9]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Revision"
    label = driver.find_element(By.XPATH, '//*[@id="status_filter"]/option[9]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"List verification PASSED: '{actual_text}' matches expected.")
    else:
        print(f"List verification FAILED: expected '{expected_text}', but found '{actual_text}'")
        assert False, "List mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    expected_text = "Search..."
    label = driver.find_element(By.XPATH, '//*[@id="applications_search"]')
    actual_text = label.text.strip()

    if actual_text == expected_text:
        print(f"Label verification passed: '{actual_text}' matches expected.")
    else:
        print(f"Label verification failed: expected '{expected_text}', but found '{actual_text}'")
        assert False, "Label mismatch"

except AssertionError as e:
    print(f"Assertion failed: {e}")

search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ñew")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ÑEW")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("M@%ks*")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("Christian")
time.sleep(2)

Select_data = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr/td[2]')
driver.execute_script("arguments[0].click();", Select_data)
time.sleep(5)
print("Data had been selected")

original_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    if "BSPMS - Balik Scientist Program Management System" in driver.title:
        print("Currently at Selected Profile window.")
        break

driver.get("http://10.10.99.18:8004/applications")

print("Navigated to BSPMS")
time.sleep(3)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(3)
print("Navigated to profile page.")

Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
driver.execute_script("arguments[0].click();", Log_Out)
time.sleep(2)
print("Logout completed.")

input("Press Enter to exit and close the browser...")
driver.quit()