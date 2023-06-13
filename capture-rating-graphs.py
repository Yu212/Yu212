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
    with webdriver.Chrome(options=options) as driver:
        driver.set_window_size(1920, 1080)
        driver.get("https://atcoder.jp/users/Yu_212")
        png = driver.find_element("id", "ratingGraph").screenshot_as_png
        with open("./rating-graph-algorithm.png", "wb") as f:
            f.write(png)
        driver.get("https://atcoder.jp/users/Yu_212?contestType=heuristic")
        png = driver.find_element("id", "ratingGraph").screenshot_as_png
        with open("./rating-graph-heuristic.png", "wb") as f:
            f.write(png)

if __name__ == "__main__":
    main()