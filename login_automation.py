from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("user-data-dir=/path/to/your/profile") 
chrome_options.add_argument("profile-directory=Default")  
chrome_options.binary_location = "/usr/bin/chromium-browser"  
service = Service('/usr/bin/chromedriver')  
driver = webdriver.Chrome(service=service, options=chrome_options)

def login_to_linkedin():
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("xyz@domain.com")  #Replace with your Linkedin ID
    password_input.send_keys("mysecretpassword1234")  # Replace with your LinkedIn password

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//img[@class='global-nav__me-photo']"))
        )
        print("Login successful!")
    except Exception as e:
        print(f"Login failed! {e}")

def main():
    login_to_linkedin()
    time.sleep(15) 

    driver.quit()

if __name__ == "__main__":
    main()
