
# importing web drivers from selenium
from selenium import webdriver

# assigning the Chrome driver to a variable
driver = webdriver.Chrome()

#Passing the url to the variable
driver.get('https://youtube.com')

#Getting the search Button through xpath
searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys('Imran Khan')

#Getting the search Button through xpath
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()