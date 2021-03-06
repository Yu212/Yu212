from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get("https://atcoder.jp/users/Yu_212")
    driver.set_window_size(1920, 1080)
    png = driver.find_element("id", "ratingGraph").screenshot_as_png
    with open("./rating-graph.png", "wb") as f:
        f.write(png)
    driver.close

if __name__ == "__main__":
    main()