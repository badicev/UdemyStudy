# ------------------------Selenium Webdriver-------------------------------------#
# Get the browser to do things automatically depending on a script or a piece of code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\ChromeDriver\chromedriver.exe"


def launchBrowser():
    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    s = webdriver.Chrome(service=ser, options=op)

    s.get("https://www.amazon.com.tr/Tuopuda-Kap%C3%BC%C5%9Fonlu-Svet%C5%9F%C3%B6rt-Sweatshirt-Einheitsgr%C3%B6%C3"
          "%9Fe/dp/B09CTBDCSD/ref=is_sr_s_dp_2?keywords=giyilebilir%2Bbattaniye&qid=1672346821&refinements=p_85"
          "%3A21345931031&rnid=21345902031&rps=1&s=apparel&sprefix=giyiklebilir%2Cfashion%2C118&sr=1-18&th=1")

    price_list = s.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/div[1]/span/span[2]/span[1]")
    for price in price_list:
        print(price.text)


launchBrowser()
