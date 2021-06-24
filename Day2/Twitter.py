from selenium import webdriver


handle = input('input your handle here:')
driver = webdriver.Chrome()
driver.implicitly_wait(600)
driver.get('http://twitter.com/'+handle)
try:
  html = driver.find_element_by_xpath('//a[@href="/'+handle+'/followers"]')
  print (html.text)
except:
  print('Acount not found')
