from scrape_backend import start_driver, scrape, end_driver, extract_data
from profile import Profile


def get_profile(url, waiting_time=2.22, scroll_pause_time=3, n_scrolls=25):
    driver, html = start_driver(url, waiting_time=waiting_time)
    all_divs = scrape(driver, html, scroll_pause_time=scroll_pause_time, n_scrolls=n_scrolls)
    end_driver(driver)
    data_list = extract_data(all_divs)

    return Profile(data_list)
