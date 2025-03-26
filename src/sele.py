from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import shutil
import os
# import chromedriver_autoinstaller
import datetime
import traceback
import logging

# Configure logging
logging.basicConfig(
    filename='selenium_crawl.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def perform_action(actions, btn):
    actions.key_down(btn).key_up(btn).perform()
    time.sleep(5)


def crawl_ibm_extension(website, adblock=False):
    # Path to your IBM Equal Access extension
    extension_path = 'IBM-Equal-Access-Accessibility-Checker.zip'  # or .crx

    # Set preferences to download files to a specific folder
    if adblock:

        prefs = {
            "download.default_directory": f'Web-Ads-Accessibility/src/output/{website}/adblock',
        }
    else:
        prefs = {
            "download.default_directory": f'Web-Ads-Accessibility/src/output/{website}/normal',
        }
    
    # Initialize Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")
    chrome_options.add_extension(extension_path)
    if adblock:
        chrome_options.add_extension('uBlock-Origin.zip')
    chrome_options.add_argument("--remote-debugging-port=9222")

    chrome_options.add_argument("--start-maximized")
    # important for linux
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--virtual-time-budget=30000")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_driver_path = ChromeDriverManager().install()

    # Aggressive network and download configuration
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--disable-gpu")
    

    # Specific network-related flags
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")

    chrome_options.add_argument("--ignore-ssl-errors")
    
    # Increase network timeouts
    chrome_options.add_experimental_option('prefs', {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "network.http_max_connections": 1000,
        "network.http_max_persistent_connections_per_server": 100,
        "network.http_max_connections_per_server": 100
    })

    try:
        # Initialize the WebDriver
        service = Service(chrome_driver_path)
        
        # Detailed logging before driver creation
        logging.info(f"Attempting to create WebDriver for {website}")
        logging.info(f"ChromeDriver path: {chrome_driver_path}")
        
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(60)
        
        # Open the webpage you want to test
        webpage_url = f'https://{website}'
        
        try:
            logging.info(f"Navigating to {webpage_url}")
            driver.get(webpage_url)
        except WebDriverException as nav_error:
            logging.error(f"WebDriver navigation error for {website}: {nav_error}")
            logging.error(f"Full error details: {traceback.format_exc()}")
            raise

        # Wait for the DevTools to open and extension to be ready
        time.sleep(10)  # Adjust based on your system speed

        if adblock:
            # Save the HTML content to a file
            with open(f'Web-Ads-Accessibility/src/output/{website}/adblock/complete_website.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)
        else:
            # Save the HTML content to a file
            with open(f'Web-Ads-Accessibility/src/output/{website}/normal/complete_website.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)

        # Interact with the extension within DevTools
        try:
            # Switch to the DevTools window
            devtools_window = driver.window_handles[-1]
            driver.switch_to.window(devtools_window)
            
            # Create an instance of ActionChains
            actions = ActionChains(driver)

            actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

            # Perform Cmd + ] to navigate tabs in DevTools on macOS
            for _ in range(10):
                actions.key_down(Keys.CONTROL).send_keys(']').key_up(Keys.CONTROL).perform()
                time.sleep(3) 

            time.sleep(5)
            perform_action(actions, Keys.ENTER)
            time.sleep(90)
            [perform_action(actions, Keys.TAB) for _ in range(11)]
            perform_action(actions, Keys.ENTER)

        except WebDriverException as devtools_error:
            logging.error(f"DevTools interaction error for {website}: {devtools_error}")
            logging.error(f"Full error details: {traceback.format_exc()}")
            raise

    except WebDriverException as e:
        # Comprehensive logging for WebDriver exceptions
        logging.error(f"WebDriver Exception for {website}: {e}")
        logging.error(f"Exception Type: {type(e)}")
        logging.error(f"Exception Args: {e.args}")
        logging.error(f"Detailed Traceback:\n{traceback.format_exc()}")

        
        # Optional: capture more system information
        try:
            import platform
            import sys
            logging.info(f"Python Version: {sys.version}")
            logging.info(f"Platform: {platform.platform()}")
        except Exception as info_error:
            logging.error(f"Error capturing system info: {info_error}")
        
        # Re-raise to maintain original error handling
        raise


    finally:
        # Ensure driver is always closed and Chrome processes are killed
        try:
            driver.quit()
        except Exception as quit_error:
            logging.error(f"Error during driver quit: {quit_error}")
        
        os.system('pkill chrome')
        logging.info(f"Completed crawl for {website}")

# Function to extract the domain from a URL
def extract_domain(url):
    return url.split('//')[-1].split('/')[0]

# Path to the text file containing the URLs
file_path = 'Web-Ads-Accessibility/src/websites.txt'

# Read the file line by line
with open(file_path, 'r') as file:
    urls = file.readlines()

# Process each URL
for url in urls:
    # url = url.strip()
    if url:  # Check if the line is not empty
        try:
            # using now() to get current time
            start_time = datetime.datetime.now()
            # website = extract_domain(url)
            website = url
            print(f'Crawling {website} with ads')
            if not os.path.isdir(f'Web-Ads-Accessibility/src/output/{website}'):
                os.mkdir(f'Web-Ads-Accessibility/src/output/{website}')
                os.mkdir(f'Web-Ads-Accessibility/src/output/{website}/normal')
                os.mkdir(f'Web-Ads-Accessibility/src/output/{website}/adblock')
            if len(os.listdir(f'Web-Ads-Accessibility/src/output/{website}/normal')) == 0:
                crawl_ibm_extension(website, adblock=False) 
            # if len(os.listdir(f'output/{website}/adblock')) == 0:
            #     crawl_ibm_extension(website, adblock=True)
            # using now() to get current time
            end_time = datetime.datetime.now()
            print(start_time, end_time, end_time-start_time)
            print(f'{website} completed') 
            os.system('pkill chrome')
        except:
            os.system('pkill chrome')
            print(f'{website} crashed')
            print("Error details:")
            traceback.print_exc()
