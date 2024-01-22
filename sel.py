from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Initialize the Chrome WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
# Navigate to YouTube
driver.get("https://www.youtube.com")
driver.maximize_window()
# Locate the search bar and enter the search query
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("never gonna give you up")
search_box.send_keys(Keys.RETURN)
# Wait for search results to load
wait = WebDriverWait(driver, 10)
first_video_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#video-title')))
first_video_link.click()
# Close the browser after a brief delay (you can remove this if not needed)
# import time
# time.sleep(5)  # Wait for 5 seconds
# driver.quit()

