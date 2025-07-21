import os, sys
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)  # Line-buffered output

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import sys
import codecs
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_popup(driver):
    try:
        # Wait for the iframe to load (the popup lives inside it)
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.hs-widget-frame"))
        )
        # Switch into the iframe
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.hs-widget-frame")
        driver.switch_to.frame(iframe)

        # Click the close button inside the iframe
        close_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Close'], .close, .widget-close-button"))
        )
        close_button.click()

        # Return to the main page context
        driver.switch_to.default_content()

    except (NoSuchElementException, TimeoutException):
        driver.switch_to.default_content()  # Just in case we were still inside
        pass  # No popup = no problem
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

try:
# Set up Firefox options directly
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")


    options.set_preference("browser.download.folderList", 2)  # Custom folder
    options.set_preference("browser.download.dir", "C:\\Users\\-----\\Downloads")  # Adjust path as needed
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    options.set_preference("pdfjs.disabled", True)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.panel.shown", False)
    options.set_preference("browser.download.animateNotifications", False)
    options.set_preference("browser.download.improvements_to_download_panel", False)

    # Launch the browser
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    # Credentials
    USERNAME = '-----'
    PASSWORD = '----------'

    # Navigate to login
    print("Logging in...", flush=True)
    driver.get('https://mo.-------.com/log-in')

    # Login procedure
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD + Keys.RETURN)

    # After login: Wait until navbar appears
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'navbar-fixed-top'))
    )
    
    close_popup(driver)

    # Navigate to Packages directly
    driver.get('https://mo.-----.com/industry/---------/packages')

    # Click the "Active" tab
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-controls='packages_tabstrip-1']"))
    ).click()

    # Wait explicitly for grid content to appear
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'packages_tabstrip-1'))
    )
    
    # Wait for loading spinner to disappear
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image"))
    )

    # Click the "Export" dropdown button
    export_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Export data to file']"))
    )
    export_dropdown.click()

    # Wait for the Excel link to appear and click it
    excel_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Excel"))
    )
    excel_link.click()
    time.sleep(10) 
    
    print("Export clicked for -------156", flush=True)

    # Step: Click the dropdown first
    fac_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".facilities-dropdown .dropdown-toggle"))
    )
    fac_dropdown.click()

    # Wait for options to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".facilities-dropdown a"))
    )

    time.sleep(10)

    # Load specific facility packages page
    driver.get('https://mo.-----.com/industry/---------/packages')

    # Wait for tab to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "packages_tabstrip-1"))
    )
   
    close_popup(driver)

    # Click the Active tab
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-controls='packages_tabstrip-1']"))
            ).click()

    # Click Export button
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Export data to file']"))
    ).click()

    # Click Excel link
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Excel"))
            ).click()
    time.sleep(10) 
    print("Export clicked for -------175", flush=True)

except Exception as e:
    print(f"Script failed: {str(e)}", flush=True)
    time.sleep(10)
    
finally:
    try:
        driver.quit()
    except:
        pass  