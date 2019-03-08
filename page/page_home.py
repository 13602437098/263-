# 书写所有此页面相关的动作出来
import time

from selenium.webdriver.common.by import By

from base.baseaction import BaseAction

class HomePageAction(BaseAction):

    into_btn_feature = By.XPATH,"//*[@text='立即体验']"
    # home_btn_feature = By.XPATH,"//*[@text='登录']"
    home_btn_feature = By.ID,"com.em.mobile:id/logintext"
    # home_btn_feature = By.XPATH,("text,登录","resource-id,com.em.mobile:id/logintext")

    # 定义可以实现自动进入首页的动作
    def auto_enter_home(self):
        # 强制等待让加载页面小时
        time.sleep(3)

        try:
            # 寻找首页元素做判断有没有启动的3个画面
            self.find_element(self.home_btn_feature)
        except Exception:
            #  执行两次滑屏操作，【通用性-封装】
            self.swipe_left(2)

            time.sleep(0.6)
            #  By.XPATH,"//*[@text='立即体验']"
            # 点击进入登陆页面按钮
            self.click(self.into_btn_feature)
        else:
            print("欢迎使用263邮箱")




