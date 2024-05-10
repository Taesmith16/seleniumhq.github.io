from saucedemo import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

Swag Labs = driver.title
assert title == "Swag Labs"

url = driver.current_url
assert url == "https://www.selenium.dev/"
Log in details == "usernames, password, login_header, product_title"
Product name = "Sauce Labs Backpac, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie"
driver.quit()
