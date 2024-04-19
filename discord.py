def discord():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from datetime import datetime
    import pytz
    from helper import check, login, show_notification
    from time import sleep
    
    local_timezone = pytz.timezone("America/Los_Angeles") #to change the time zone to use the tz_identifier https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    date_time = datetime.now(local_timezone)  
    log_datetime = date_time.strftime("%m%d%Y-%H%M-%S")
    current_time = date_time.strftime("%H")
    task_time_format = date_time.strftime("%H%M")
    try:
        op = webdriver.ChromeOptions()
        op.add_argument('--log-level=3')
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=op)
        driver.maximize_window()
        driver.get('https://discord.com/login')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label = "Email or Phone Number"]')))
        present_element=driver.find_element(By.XPATH, '//input[@aria-label = "Email or Phone Number"]')
        login(driver, present_element)
        driver.implicitly_wait(5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-dnd-name ="Coding Dojo"]')))
        driver.find_element(By.XPATH, '//div[@data-dnd-name ="Coding Dojo"]').click()
        if int(current_time) <= 14:
            
            msg = "Hello Ninjas! I'll be here until 8pm PST. ```If you are struggling, remember the 20 min rule then post your question/issue in either your stack general channel or cohort channel with as much information as well as screenshots of your error and code. This way TAs/Instructors will have an easier time finding your issue.```"
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "ta-availability"]').click()
            check(driver, msg)
            # ====================================================================================
            # driver.find_element(By.XPATH, '//li[@data-dnd-name= "cohort-caden-december"]').click()
            # check(driver, msg)
            show_notification("Discord","Success", task_time_format)
            driver.quit()
            
        elif int(current_time) == 15:
            msg = "Lunch"
            driver.find_element(By.XPATH, "//div[contains(text(),'🔒pt-ta-chat')]").click()
            sleep(1)
            check(driver, msg)
            show_notification("Discord","Success", task_time_format)
            driver.quit()
        elif int(current_time) == 16:
            msg = "Back"
            driver.find_element(By.XPATH, "//div[contains(text(),'🔒pt-ta-chat')]").click()
            sleep(1)
            check(driver, msg)
            show_notification("Discord","Success", task_time_format)
            driver.quit()
        else:
            msg = "Goodnight ninjas! If I helped you today, please leave some feedback for me! Feedback is anonymous and helps us as TAs improve your experiences in Coding Dojo. https://form.typeform.com/to/rX5h1pbL#ta_name=Samuel%20Reid"
        # ==============================================================================================================
            # driver.find_element(By.XPATH, '//li[@data-dnd-name= "cohort-caden-december"]').click()
            # check(driver, msg)
            # ====================================================================================
            driver.find_element(By.XPATH, '//li[@data-dnd-name= "ta-availability"]').click()
            check(driver, msg)
            show_notification("Discord","Success", task_time_format)
            driver.quit()
            
    except Exception as error_code:
        import os
        show_notification("Discord","Failed", task_time_format)
        log_directory= os.path.join(os.path.dirname(__file__), 'logs', f'discord-{log_datetime}.txt')
        driver.save_screenshot(f'logs/screenshots/discord-{log_datetime}.png')
        with open(log_directory, 'w') as file:
                file.write(str(error_code))
        driver.quit()


