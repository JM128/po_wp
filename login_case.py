from selenium import webdriver
import time
import unittest
from login_page import LoginPage
from dashboard_page import DashboardPage
from post_list_page import PostlistPage
from post_new_page import PostnewPage
from selenium.common.exceptions import NoSuchElementException


class LoginWordpress(unittest.TestCase):

	def setUp(self):
		print("test starting")
		self.dr = webdriver.Chrome()
		self.domain = "http://47.107.76.72:8000/"
		self.username = 'ZJM128'
		self.password = 'pass2word'
		self.title = "title12333333333"
		self.text = "text1233333333333"
	
	def tearDown(self):
		print("test end")
		self.dr.quit()

	@unittest.skip('跳过')
	def test_01_login_success(self):
		'''登录测试用例'''
		login_page = LoginPage(self.dr,self.domain + "wp-login.php")
		dashboard_page = login_page.login(self.username,self.password)
		time.sleep(2)

		self.assertTrue('wp-admin' in self.dr.current_url)

	@unittest.skip('跳过')
	def test_02_create_post(self):
		'''创建文章测试用例'''
		# 登录
		self.login_wp()
		#进入写文章页面
		post_new_page = PostnewPage(self.dr,self.domain + "wp-admin/post-new.php")
		post_new_page.create_post(self.title,self.text)
		#返回所有文章页面，断言
		post_list_page = PostlistPage(self.dr,self.domain + "wp-admin/edit.php")
		post_list_title = post_list_page.get_post_list_title()
		self.assertTrue(post_list_title == title)


	def test_03_delete_post(self):
		'''删除文章测试用例'''

		self.login_wp()

		post_new_page = PostnewPage(self.dr,self.domain + "wp-admin/post-new.php")
		post_id =post_new_page.create_post(self.title,self.text)

		post_list_page = PostlistPage(self.dr,self.domain + "wp-admin/edit.php")
		row_id = post_list_page.move_to_trashcan(post_id)

		with self.assertRaises(NoSuchElementException):
			self.dr.find_element_by_css_selector(row_id)

	def login_wp(self):
		login_page = LoginPage(self.dr,self.domain + "wp-login.php")
		dashboard_page = login_page.login(self.username,self.password)


if __name__ == "__main__":
	unittest.main()

