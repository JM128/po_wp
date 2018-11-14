from selenium import webdriver

class BasePage():

 	def __init__(self,driver,url=None):
 		self.dr = driver
 		self.url = url
 		if self.url != None:
 			self.open_browser()
 		self.dr.maximize_window()
 		self.dr.implicitly_wait(5)


 	def by_id(self,id_):
 		return self.dr.find_element_by_id(id_)

 	def by_css(self,css):
 		return self.dr.find_element_by_css_selector(css)

 	def open_browser(self):
 		return self.dr.get(self.url)