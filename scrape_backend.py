from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm


MAIN_CLASS_NAME = 'css-175oi2r'
QUESTION_CLASS_NAME = 'css-1rynq56 r-1wns2tv r-ubezar r-fdjqy7 r-9cokr0 r-1xnzce8 r-35wr9i r-13uqrnb r-1it3c9n'
ASKER_CLASS_NAME = 'css-1rynq56 r-fdjqy7 r-9cokr0 r-1xnzce8 r-9krj61 r-1b43r93 r-5x3879 r-13uqrnb r-1it3c9n'
DATE_CLASS_NAME = 'css-1rynq56 r-fdjqy7 r-9cokr0 r-1xnzce8 r-1put3z6 r-1b43r93 r-1bymd8e r-5x3879 r-13uqrnb r-1it3c9n'
ANSWER_CLASS_NAME = 'css-1rynq56 r-1wns2tv r-ubezar r-fdjqy7 r-9cokr0 r-1xnzce8 r-5x3879 r-13uqrnb r-1it3c9n'


def start_driver(url, waiting_time=2.22):
    chrome_options = Options()
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    # chrome_options.add_argument('--headless')
    # chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(chrome_options)
    driver.get(url)

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, MAIN_CLASS_NAME)))
    except TimeoutException:
        print("Loading took too much time!")
        driver.quit()
        exit()
    time.sleep(waiting_time)
    html = driver.find_element(By.TAG_NAME, "body")
    return driver, html


def scrape(driver, html, scroll_pause_time=3, n_scrolls=25):
    all_divs = []
    prev_height = len(html.text)
    html.click()
    print('Scraping CuriousCat profile...')
    iterator = tqdm(range(n_scrolls))

    for _ in iterator:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        divs = soup.find_all("div", class_=MAIN_CLASS_NAME)
        all_divs.extend(divs)
        # html.click()
        html.send_keys(Keys.END)
        time.sleep(scroll_pause_time)

        try:
            new_height = len(html.text)
            if new_height == prev_height:
                iterator.close()
                print('Early Stop! I touched the bottom!')
                break
            prev_height = new_height
        except Exception:
            pass

    return all_divs


def end_driver(driver):
    driver.quit()


def extract_data(all_divs):
    data_list = []
    print('Extracting data...')

    for div in tqdm(all_divs):
        try:
            question_div = div.find("div", class_=QUESTION_CLASS_NAME)
            question = question_div.get_text(strip=True) if question_div else "N/A"

            asker_div = div.find("div", class_=ASKER_CLASS_NAME)
            asker = asker_div.get_text(strip=True) if asker_div else "N/A"

            date_div = div.find("div", class_=DATE_CLASS_NAME)
            date = date_div.get_text(strip=True) if date_div else "N/A"

            answer_div = div.find("div", class_=ANSWER_CLASS_NAME)
            answer = answer_div.get_text(strip=True) if answer_div else "N/A"

            data = {
                "question": question,
                "asker": asker,
                "date": date,
                "answer": answer
            }

            if 'N/A' not in data.values() and data not in data_list:
                data_list.append(data)

        except Exception as e:
            print(f"Error processing div: {e}")
            continue

    print(f'I succesfully extracted {len(data_list)} questions.')
    return data_list
