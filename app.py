from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def browser_function(username, password, option):
    
    # To open Chrome Browser
    driver = webdriver.Chrome()
    
    # In the place of example.com replace with your greythr URL
    driver.get("https://healtech.greythr.com/")
    
    #To maximize browser window
    driver.maximize_window()
    
    # To capture the username, password and Log in button
    username_input=WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("id", "username")))
    password_input=WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("id", "password")))
    submit_button=WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[type='submit']")))
    
    # To pass the Username, Password and click on Log in button
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button = submit_button[0]
    submit_button.click()
    
    # To capture and click on Sign In button, once it opens
    wait = WebDriverWait(driver, 10)
    sign_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app/ng-component/div/div/div[2]/div/ghr-home/div[2]/div/gt-home-dashboard/div/div[2]/gt-component-loader/gt-attendance-info/div/div/div[3]/gt-button")))
    sign_button.click()
    
    # To click on the dropdown option box
    select_drop = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app/ng-component/div/div/div[2]/div/ghr-home/div[2]/div/gt-home-dashboard/gt-popup-modal/div/div/div[1]/div[1]/gt-dropdown")))
    select_drop.click()
    
    
    # To click on the dropdown option based on the option passed during the execution
    shadowHost = driver.find_element(By.TAG_NAME, "gt-dropdown")
    shadowRoot = shadowHost.shadow_root
    selector = 'div > div.dropdown > div > div:nth-child({}) > div'.format(option)
    selectElement = shadowRoot.find_element(By.CSS_SELECTOR, selector)
    selectElement.click()
    
    # To capture and click on Sign In button, once it visible
    shadow = driver.find_element(By.CSS_SELECTOR, ".flex.justify-end.hydrated").shadow_root
    time.sleep(1)
    shadow.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-medium").click()
    
    driver.quit()
    

# Inputs required for the script    
username=int(input("Enter Employee iD:- "))
password=input("Enter your password:- ")
print("Sign-in location --> Client Location = 1, Field = 2, Office = 3, Work From Home = 4")
option=int(input("Enter Sign-In Location number:- "))    

# Function to the execute the logic
browser_function(username, password, option)
