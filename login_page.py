from base_page import BasePage
from dashboard_page import DashboardPage


class LoginPage(BasePage):

	def username_box(self):
		return self.by_id("user_login")

	def password_box(self):
		return self.by_id("user_pass")

	def login_button(self):
		return self.by_id("wp-submit")

	def login(self,username,password):
		self.username_box().send_keys(username)
		self.password_box().send_keys(password)
		self.login_button().click()

		return DashboardPage(self.dr)
