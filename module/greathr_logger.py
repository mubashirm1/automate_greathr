from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def scroll_until_found(driver, max_scrolls=5):
    for i in range(max_scrolls):
        try:
            shadow_host = WebDriverWait(driver,4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "gt-button")))
            shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
            sign_button = WebDriverWait(shadow_root,4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[name="primary"]')))
            return sign_button
        except Exception as e:
            print(e)
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 100);")  # scroll down a bit
    raise TimeoutException(f"Element not found after {max_scrolls} scrolls")


def greathr_logger(driver,user_name:str, password:str) -> None:
    """
    loggs in and out of greatHR(https://vcreatek.greythr.com/uas/portal/auth)
    inputs - driver: selenium driver instance
             username: str
             password:str
    output - None
    """

    #go to the site
    driver.get("https://vcreatek.greythr.com/uas/portal/auth")
    time.sleep(5)
    driver.set_window_size(3840, 2160)  # set window size

    #enter username
    username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.send_keys(user_name)
    #enter password
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"password")))
    password_input.send_keys(password)
    #click login button
    login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[text()=" Login "]')))
    login_button.click()
    time.sleep(5)
    driver.set_window_size(1920, 1080)          # set window size 

    #click signIn/signOut button
    sign_button = scroll_until_found(driver)
    sign_button.click()
    time.sleep(2)
    current_button = scroll_until_found(driver)
    return current_button.text
