from base_page import BasePage
import json

class PostnewPage(BasePage):

	def post_title(self):
		return self.by_id("title")

	def publish_button(self):
		return self.by_id("publish")

	def set_content(self,text):
		js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' %(text)
		self.dr.execute_script(js)

	def create_post(self,title,text):
		self.post_title().send_keys(title)
		self.set_content(text)
		self.publish_button().click()
		
		return self.dr.current_url.split('=')[1].split('&')[0]


