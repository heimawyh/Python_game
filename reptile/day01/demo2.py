import  selenium.webdriver

url = "https://www.bilibili.com/"

driver = selenium.webdriver.Chrome()
driver.get(url)
data = driver.page_source

file_path = "D:/Code/bilibili/b_google.html"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(data)

driver.close()