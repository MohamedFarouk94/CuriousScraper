from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
import pandas as pd


# Initialize Selenium WebDriver (Chrome example)
chrome_options = Options()
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
driver = webdriver.Chrome(chrome_options)  # Make sure ChromeDriver is in your PATH or specify the location
driver.get("https://curiouscat.live/mohfarouk94")  # Replace with the actual URL
# action = ActionChains(driver)

# Let the page load (adjust the sleep time as necessary)
try:
    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-175oi2r')))
except TimeoutException:
    print("Loading took too much time!")
    driver.quit()
    exit()
time.sleep(2.22)
html = driver.find_element(By.TAG_NAME, "body")
# driver.find_element(By.CLASS_NAME, 'css-175oi2r').click()


# Scroll down to load more content if necessary (add a scroll loop if needed)
SCROLL_PAUSE_TIME = 0.1
COUNTER = 0
all_divs = []

while COUNTER < 500:
    COUNTER += 1
    print(f'Scolling ({COUNTER})')
    soup = BeautifulSoup(driver.page_source, "html.parser")
    divs = soup.find_all("div", class_="css-175oi2r")
    all_divs.extend(divs)
    # print(len(html.text))
    # Scroll down to the bottom
    html.click()
    # time.sleep(1.111)
    html.send_keys(Keys.DOWN)
    # action.send_keys_to_element(html, "END").perform()
    # driver.execute_script("window.scrollTo(0, window.scrollY+500);")

    # Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    # new_height = driver.execute_script("return document.body.scrollHeight")
    # print(new_height)


# Get the page source and parse it using BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")


# Find all the main divs with class "css-175oi2r"
# divs = soup.find_all("div", class_="css-175oi2r")

# List to hold the dictionaries
data_list = []

# Iterate through each main div to extract sub divs
for div in all_divs:
    try:
        # Extract the question
        question_div = div.find("div", class_="css-1rynq56 r-1wns2tv r-ubezar r-fdjqy7 r-9cokr0 r-1xnzce8 r-35wr9i r-13uqrnb r-1it3c9n")
        question = question_div.get_text(strip=True) if question_div else "N/A"

        # Extract the asker
        asker_div = div.find("div", class_="css-1rynq56 r-fdjqy7 r-9cokr0 r-1xnzce8 r-9krj61 r-1b43r93 r-5x3879 r-13uqrnb r-1it3c9n")
        asker = asker_div.get_text(strip=True) if asker_div else "N/A"

        # Extract the date
        date_div = div.find("div", class_="css-1rynq56 r-fdjqy7 r-9cokr0 r-1xnzce8 r-1put3z6 r-1b43r93 r-1bymd8e r-5x3879 r-13uqrnb r-1it3c9n")
        date = date_div.get_text(strip=True) if date_div else "N/A"

        # Extract the answer
        answer_div = div.find("div", class_="css-1rynq56 r-1wns2tv r-ubezar r-fdjqy7 r-9cokr0 r-1xnzce8 r-5x3879 r-13uqrnb r-1it3c9n")
        answer = answer_div.get_text(strip=True) if answer_div else "N/A"

        # Create a dictionary for this entry
        data = {
            "question": question,
            "asker": asker,
            "date": date,
            "answer": answer
        }

        # Append to the list
        if 'N/A' not in data.values() and data not in data_list:
            data_list.append(data)

    except Exception as e:
        print(f"Error processing div: {e}")
        continue

# Close the browser after scraping
driver.quit()

print(len(data_list))
print(data_list[-5:])
df = pd.DataFrame(data_list)
df.to_csv('cat.csv', index=False)
