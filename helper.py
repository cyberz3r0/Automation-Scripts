from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from decouple import config
from time import sleep

def show_notification(title = "Task", message = None):
    from notifypy import Notify
    import platform
    import os
    notification = Notify()
    notification.title = title
    notification.message = message
    if platform.system() == "Windows":
        notification.audio = os.path.join(os.path.dirname(__file__), 'assets', 'Windows_Foreground.wav')
    elif platform.system() == "Darwin":
        notification.audio = os.path.join(os.path.dirname(__file__), 'assets', 'burn_complete.wav')
    
    notification.send()
        
def check(driver, msg):
    action = ActionChains(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
    element = driver.find_element(By.XPATH, '//div[@role="textbox"]')
    action.move_to_element(element).click(element)
    element = driver.switch_to.active_element
    element.send_keys(msg)
    first_check = len(driver.find_elements(By.XPATH, '//span[text()="dojo_Samuel_Reid"]')) #If this Line goes above the previous line first_check says 0 
    element.send_keys(Keys.ENTER)
    second_check = len(driver.find_elements(By.XPATH, '//span[text()="dojo_Samuel_Reid"]'))
    driver.implicitly_wait(2)
    if first_check == second_check:
        element.clear()
        check()
        
def login(driver, element):
    if element.is_displayed():
        driver.find_element(By.XPATH, '//input[@aria-label = "Email or Phone Number"]').send_keys(config('discord_user'))
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(config('discord_pw'))
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    else:
        driver.get('https://discord.com/login')
        login(driver, element)