#=================
# To be completed
#=================
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
# ======= Setting =============
first_name = ""
last_name = ""
phone_number = ""
email = ""
party_size = 2
available_dates = {}
available_times = {}
# =============================
# Open the Website
browser.get('https://www.exploretock.com/tfl/')
content = browser.find_element(By.CLASS_NAME, 'MuiTypography-root css-veqgne')
guests = content[0]
if content[0] < 2:
  ++guest
  browser.find_element_by_class_name('tock-icon icon_plus').click()
else if content[0] > 2:
  --guest
  browser.find_element_by_class_name('tock-icon icon_minus').click()
# =============================
# Filling in the credentials

