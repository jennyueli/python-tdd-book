#book club tdd with python
#functional test scripts
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")
#browser.get("http://www.google.com")
assert 'Django' in browser.title
