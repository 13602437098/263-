#首页模型,一个模型对应一个page页面
from base import initDriver
from page.page import Page

class TestDemo:
    # 每个函数都需要用到的初始化操作

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_auto_intohome(self):
        #滑动
        self.page.inithomepage().auto_enter_home()
        #点击立即体验


    def test_login(self):
        pass

