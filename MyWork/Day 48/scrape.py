from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"


def launchBrowser():
    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    s = webdriver.Chrome(service=ser, options=op)

    s.get("https://www.python.org/")

    event_times = s.find_elements(By.CSS_SELECTOR, ".event-widget time")
    for time in event_times:
        print(time.text)

    event_names = s.find_elements(By.CSS_SELECTOR, ".event-widget li a")
    for name in event_names:
        print(name.text)
    events = {}
    for n in range(len(event_times)):
        events[n] = {
            "time": event_times[n].text,
            "name": event_names[n].text
        }

    print(events)




launchBrowser()
