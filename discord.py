def discord():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from decouple import config
    from time import sleep
    from datetime import datetime
    import pytz
    from notifypy import Notify
    import platform
    import os
    # =======================Helper===========================
    def check():
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
        element = driver.find_element(By.XPATH, '//div[@role="textbox"]')
        action.move_to_element(element).click(element)
        element = driver.switch_to.active_element
        element.send_keys(msg)
        first_check = len(driver.find_elements(By.XPATH, '//span[text()="dojo_Samuel_Reid"]')) #If this Line goes above the previous line first_check says 0 
        element.send_keys(Keys.ENTER)
        second_check = len(driver.find_elements(By.XPATH, '//span[text()="dojo_Samuel_Reid"]'))
        sleep(2)
        if first_check == second_check:
            element.clear()
            check()
        show_notification("Success")
        
    def login(element):
        if element.is_displayed():
            driver.find_element(By.XPATH, '//input[@aria-label = "Email or Phone Number"]').send_keys(config('tauser'))
            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(config('discordpw'))
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            
        else:
            driver.get('https://discord.com/login')
            login(element)
            
    def show_notification(message):
            notification = Notify()
            notification.title = "Discord"
            notification.message = message
            if platform.system() == "Windows":
                notification.audio = os.path.join(os.path.dirname(__file__), 'assets', 'Windows_Foreground.wav')
            elif platform.system() == "Darwin":
                notification.audio = os.path.join(os.path.dirname(__file__), 'assets', 'burn_complete.wav')
                
            notification.send()
    # ================================MAIN========================================
    PST = pytz.timezone("America/Los_Angeles")
    date_time = datetime.now(PST)
    log_datetime = date_time.strftime("%m%d%Y-%H%M-%S")
    current_time = date_time.strftime("%H")

    try:
        op = webdriver.ChromeOptions()
        op.add_argument('--log-level=3')
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=op)
        action = ActionChains(driver)
        driver.get('https://discord.com/login')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label = "Email or Phone Number"]')))
        print("On site")
        present_element=driver.find_element(By.XPATH, '//input[@aria-label = "Email or Phone Number"]')
        login(present_element)
        print("Logged in")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-dnd-name ="Coding Dojo"]')))
        driver.find_element(By.XPATH, '//div[@data-dnd-name ="Coding Dojo"]').click()
        print("clicked on Coding Dojo")
        if int(current_time) <= 14:
            
            msg = "Hello Ninjas! I'll be here until 8pm PST. ```If you are struggling, remember the 20 min rule then post your question/issue in either your stack general channel or cohort channel with as much information as well as screenshots of your error and code. This way TAs/Instructors will have an easier time finding your issue.```"
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "ta-availability"]').click()
            check()
            # ====================================================================================
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "cohort-caden-december"]').click()
            check()
            driver.quit()
            
        elif int(current_time) == 15:
            msg = "Lunch"
            driver.find_element(By.XPATH, '//li[@data-dnd-name ="🔒pt-ta-chat"]').click()
            check()
            
        elif int(current_time) == 16:
            msg = "Back"
            driver.find_element(By.XPATH, '//li[@data-dnd-name ="🔒pt-ta-chat"]').click()
            check()
        else:
            msg = "Goodnight ninjas! If I helped you today, please leave some feedback for me! Feedback is anonymous and helps us as TAs improve your experiences in Coding Dojo. https://form.typeform.com/to/rX5h1pbL#ta_name=Samuel%20Reid"
        # ==============================================================================================================
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "cohort-caden-december"]').click()
            check()
            # ====================================================================================
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "ta-availability"]').click()
            check()
            driver.quit()
    except Exception as error_code:
        show_notification("Failed")
        log_directory= os.path.join(os.path.dirname(__file__), 'logs', f'discord-{log_datetime}.txt')
        with open(log_directory, 'w') as file:
                file.write(str(error_code))
        driver.quit()


