'''短信第一个页面元素'''
from selenium.webdriver.common.by import By
# 第一个页面的元素信息
new_mas_id = (By.ID,"com.android.mms:id/action_compose_new")
# 第二个页面的元素
new_user_xpath = (By.ID,"com.android.mms:id/recipients_editor")
send_mas_xpath = (By.ID,"com.android.mms:id/embedded_text_editor")
click_mas_xpath = (By.ID,"com.android.mms:id/send_button_sms")
assert_mss_id =(By.ID,"com.android.mms:id/text_view")
# 返回
black_mms = (By.ID,"android:id/up")