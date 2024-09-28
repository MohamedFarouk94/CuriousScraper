# CuriousCat Data Scraper 🐱‍💻

CuriousCat is officially sunsetting on **October 7, 2024**. Yep, that's right, our beloved Q&A platform is waving its final goodbye. According to *CuriousCat* themselves, the service is closing due to "prolonged deficits." and they declared that we the users should back up or move our 'valuable' data. SO I made this script to save our data before moving to their final fate in the digital abyss.

## What is this?

I've created a quick-and-not-so-dirty Python script that scrapes and saves your **CuriousCat** user data. You can pull down your profile, questions, and answers, then export them in several formats: **HTML**, **CSV**, and **JSON**.

⚠️ **Disclaimer**:\
    1. This script was thrown together to quickly achieve a single purpose—get your data. It might not be the fastest, prettiest, or bug-free solution, but hey, it works (most of the time)! If you hit a snag, remember this was built with love, tea doses, and minimal testing.\
    2. I don't scrape images. Too much effort and they're not that common anyway.\
    3. The scraping is not headless. So you will monitor the browser while doing it.

## User Guide 🚀

Let’s get you up and running. Here's how to use this Python-based scraper:

### 1. Install Python 🐍

You’ll need **Python 3** installed. If you don’t already have it:

- **Windows**: [Download it here](https://www.python.org/downloads/).
- **Mac/Linux**: It’s probably already installed! Run `python3 --version` to check.

### 2. Download Repository ⬇️

From the green button `code` in the top of this page, choose the tab `local` and then `Download ZIP`.

Extract the file in a directory on your system. This will be the project directory.

### 3. Set Up a Virtual Environment 🌐

- Open your terminal/command prompt.
- Navigate to the project directory.
- Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

- Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 4. Install the Requirements 📦

Run the following to install the necessary packages:

```bash
pip install -r requirements.txt
```

### 5. Run the Scraper 🏃‍♂️

Open a Python shell:

```bash
python3
```

Now, let’s scrape some data!

```python
from curiousscraper import get_profile

url = 'https://curiouscat.live/username'  # replace 'username' with your actual CuriousCat username

profile = get_profile(
    url,
    waiting_time=2.22,       # Time to wait before scraping begins (in seconds)
    scroll_pause_time=3,     # Time between scrolls (in seconds)
    n_scrolls=25             # Number of scrolls to simulate (acts like pressing END key)
)

# Save your data!
profile.to_html('file_name.html')  # Exports data to HTML file
profile.to_csv('file_name.csv')   # Exports data to CSV file
profile.to_json('file_name.json')  # Exports data to JSON file
```

### 5. Customization 🛠️

You can modify the **waiting_time**, **scroll_pause_time**, and **n_scrolls** arguments to suit your needs. If you don’t provide any, the defaults will be:

- **waiting_time** = 2.22 seconds
- **scroll_pause_time** = 3 seconds
- **n_scrolls** = 25 scrolls

These values help control how long the script waits before starting to scrape, how long it pauses between scrolls (to load more content), and how many times it simulates pressing the "END" key to scroll down.

Keep in mind that 25 scrolls will scrape ~750 CuriousCat questions approximately, so this might help you decide **n_scrolls**.

Also if you decreased **scroll_pause_time**, the script might skip some questions for it won't wait a proper time for them to load. So adjust at your own responsibility. It's not guaranteed that no questions will be skipped anyway, but the odds are in your favor!

Also, if you don't determine the file name in the functions `to_html`, `to_csv` and `to_json`, the file will be named `cat<SEQUENCE_OF_NUMBERS>.<THE_RIGHT_EXTENSION>`.

## Enjoy Your Data Backup! 🧳

So, that’s it! Save your CuriousCat data before the site goes down forever. Make sure to keep your files safe, as they’re all you’ll have left of your CuriousCat experience.

Feel free to fork this project, improve it, or reuse it in any future similar situations. It got the job done for me, and I hope it helps you too!

Happy Scraping! 🐱✨