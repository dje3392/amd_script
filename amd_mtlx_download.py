from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Prompt the user to choose the download resolution
choice = input("Choose the download resolution: highest (1) or lowest (0)? ")
while choice not in ("0", "1"):
    print("Invalid choice, please choose again.")
    choice = input("Choose the download resolution: highest (1) or lowest (0)? ")

# prompt the user to choose the download directory
download_dir = input("Choose the download directory: ")
a = os.path.exists(download_dir)
while os.path.exists(download_dir) is False:
    print("Invalid choice, please choose again.")
    download_dir = input("Choose the download directory: ")

# define options for selenium
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_dir}
options.add_experimental_option('prefs', prefs)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the main site
driver.get("https://matlib.gpuopen.com/main/materials/all")
time.sleep(3)


# Find the first material element
material_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pa-4 no-focus d-flex flex-column v-card v-card--link v-sheet theme--dark cardBg']")))
material_element.click()

while True:
    # Wait for the download button to be clickable
    wait = WebDriverWait(driver, 10)
    download_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-icon.notranslate.mx-auto.mdi.mdi-download.theme--dark")))

    if choice == "1":
        # Click on the highest resolution download button to download the material
        download_buttons[-1].click()
        time.sleep(1)
    else:
        # Click on the lowest resolution download button to download the material
        download_buttons[0].click()
        time.sleep(1)
    
    # Check if the next material button exists
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".v-icon.notranslate.mdi.mdi-chevron-double-right.theme--dark")
    except:
        break
    
    # Click on the next material button
    next_button.click()
    time.sleep(1)

# Close the browser
driver.quit()

