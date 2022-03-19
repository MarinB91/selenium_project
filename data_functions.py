from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def get_data():
    """Navigating index.hr and scraping top article data"""
    s = Service('C:/ChromeDriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get("https://index.hr")

    try:  # Catching exception in case of pop-up ad.
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()
    except TimeoutException:
        driver.quit()

    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.TAG_NAME, 'h2'))).click()

    scrape_title = driver.find_element(By.XPATH, '/html/body/article/div[2]/div[1]/h1').text
    scrape_author = driver.find_element(By.XPATH, '/html/body/article/div[2]/div[1]/div/div[1]/span[1]').text
    scrape_text = driver.find_element(By.XPATH, '/html/body/article/div[2]/div[2]/div/div/div[2]/div[1]/p[1]').text

    driver.quit()

    return [scrape_title, scrape_author, scrape_text]


def short_intro(data):
    """Takes the first passage of the scraped article and shortens it to 20 characters."""
    split = data[2].split()
    shortened = split[0:20]
    short_summary = ' '.join(shortened) + '...'
    return short_summary
