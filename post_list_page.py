from base_page import BasePage
from post_new_page import PostnewPage
from selenium.webdriver.common.action_chains import ActionChains

class PostlistPage(BasePage):

	def write_post_button(self):
		self.by_css(".page-title-action").click()
		return PostnewPage(self.dr)

	def get_post_list_title(self):
		return self.by_css(".row-title").text

	def get_post_id(self,post_id):
		row_id = 'post-' + post_id
		return self.by_id(row_id)

	def move_to_trashcan(self,post_id):
		delete_title = self.get_post_id(post_id)
		row_id = delete_title.get_attribute("id")
		ActionChains(self.dr).move_to_element(delete_title).perform()
		delete_title.find_element_by_css_selector('a.submitdelete').click()

		return row_id
