from selenium import webdriver
from PIL import Image


# 登录4399

driver = webdriver.Chrome(executable_path='D:\App\chrome\Chrome\chromedriver.exe')
driver.get('http://www.4399.com')
driver.find_element_by_xpath('//*[@id="login_tologin"]').click()

driver.switch_to.frame('popup_login_frame')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('2201815280')
driver.find_element_by_xpath('//*[@id="j-password"]').send_keys('123456a')

'''
# 识别验证码，3种方法
# 1.先截取全屏---在切割出登录框---再截验证码
# 2.直接截取登录框---再截验证码
# 3.直接截取验证码
'''
# 第二种方法
element = driver.find_element_by_id('popup_login_frame')
element.screenshot('b.png')
driver.switch_to.frame('popup_login_frame')
y_element = driver.find_by_xpath('//*[@id="captcha"]')
'''
# 打印出验证码坐标点及宽、高
print(y_element.location)
print(y_size)
'''
x = y_element.location['x']
y = y_element.location['y']
width = y_element.size['width']
height = y_element.size['height']
im = Image.open('b.png')
im = im.crop(x, y, weight, height)
im.save('c.png')
code = input('请输入正确验证码：')
driver.find_element_by_xpath('').send_keys(code)    # 找到验证码框的xpath并输入
driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[5]/input').click()








