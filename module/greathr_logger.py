from selenium.webdriver.common.by import By
import time

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
    #enter username
    driver.set_window_size(3840, 2160)  # set window size
    time.sleep(2)
    username_input = driver.find_element(By.ID,"username")
    username_input.send_keys(user_name)
    time.sleep(1)
    #enter password
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(password)
    time.sleep(1)
    #click login button
    login_button = driver.find_element(By.XPATH, '//button[text()=" Login "]')
    login_button.click()
    time.sleep(5)
    #click signIn/signOut button
    driver.set_window_size(1920, 1080)          # set window size
    driver.execute_script("window.scrollBy(0, 200);") # scroll a little down
    time.sleep(2)
    shadow_host = driver.find_element(By.CSS_SELECTOR, "gt-button")
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    sign_in_button = shadow_root.find_element(By.CSS_SELECTOR, 'button[name="primary"]')
    sign_in_button.click()
