from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from creds.log import username,pw
from datetime import datetime
from winotify import Notification, audio


def show_notification(message):
    win_notify = Notification(app_id="Login/Logout",
                        title="Message",
                        msg=message,
                        duration="long")
    win_notify.set_audio(audio.Default, loop=False)
    if message == "Failed":
        win_notify.add_actions(label="Click", launch="https://hcm92.careered.com/psc/HRPRD/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL")
    win_notify.show()


date_time = datetime.now()
log_datetime = date_time.strftime("%m%d%Y-%H%M-%S")
current_time = date_time.strftime("%H%M")

try:
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--log-level=3')
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=op)
    # driver = webdriver.Remote(command_executor="http://192.168.1.150:4444/wd/hub", options=op)
    driver.get('https://hcm92.careered.com/psc/HRPRD/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
    driver.find_element(By.ID, 'i0116').send_keys(username)
    driver.find_element(By.ID, 'idSIButton9').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'userNameInput')))
    driver.find_element(By.ID, 'passwordInput').send_keys(pw)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
    driver.find_element(By.ID, 'idSIButton9').click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, 'win0divPTNUI_LAND_REC_GROUPLET$0')))
    driver.find_element(By.ID, 'win0divPTNUI_LAND_REC_GROUPLET$0').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ps-dropdown')))
    if int(current_time) <= 1100 or int(current_time) == 1600:
        Select(driver.find_element(By.ID, 'TL_RPTD_TIME_PUNCH_TYPE$0')).select_by_value("1")
        driver.find_element(By.ID, 'TL_WEB_CLOCK_WK_TL_SAVE_PB').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'TL_WEB_CLOCK_WK_TL_SAVE_PB')))
        show_notification("Success")
        driver.quit()
    else:
        Select(driver.find_element(By.ID, 'TL_RPTD_TIME_PUNCH_TYPE$0')).select_by_value("2") # change to 1 for login
        driver.find_element(By.ID, 'TL_WEB_CLOCK_WK_TL_SAVE_PB').click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'CE_DERIVED_ETEO_YES')))
        driver.find_element(By.ID, 'CE_DERIVED_ETEO_YES').click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ps-dropdown')))
        show_notification("Success")
        driver.quit()
except Exception as error_code:
    show_notification("Failed")
    with open(f'C:/Users/reids/Documents/automation/automate/Logs/timesheet-{log_datetime}.txt', 'w') as file:
            file.write(str(error_code))
    driver.quit()


