from selenium import webdriver
import time
import unittest
from login_page import LoginPage
from dashboard_page import DashboardPage
from post_list_page import PostlistPage
from post_new_page import PostnewPage

class PostCase(unittest.TestCase):

		def test_create_post(self):

			username = 'ZJM128'
			password = 'pass2word'

			login_page = LoginPage(self.dr,self.domain + "wp-login.php")
			dashboard_page = login_page.login(username,password)
			
			title = "title12333333333"
			content = "content12333333333333"
			post_list_url = self.domain + "edit.php"
			post_list_page = PostlistPage(self.dr,post_list_url)
			time.sleep(2)
			post_list_page.write_post_button()
			time.sleep(1)
			PostnewPage.create_post(title,content)
			#返回所有文章页面，断言
			post_list_page = PostlistPage(self.dr,post_list_url)
			post_list_title = post_list_page.get_post_list_title()
			assertTrue(post_list_title == title)

if __name__ == '__main__':
	unittest.main()