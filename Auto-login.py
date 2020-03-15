#!/usr/bin/env python
# coding: utf-8




import selenium.webdriver 
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
driver = selenium.webdriver.Chrome()

source = [('201710412216','511902'),('201710412226','510623')]
for id in source:
    url = 'https://xsswzx.cdu.edu.cn:81/isp/index.html'
    driver.get(url)
    source = driver.find_element_by_xpath('//p[@class="mb-md-5 mb-3 welcome-para"]/a')
    # source.get_attribute('href').click()
    ur2 = source.get_attribute('href')
    driver.get(ur2)  # 来到登录界面
    time.sleep(10)
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    s = bs.findAll(name='div')[14].text[3:7]  # 获得验证码
    time.sleep(5)
    # 输入用户名，密码，验证码
    driver.find_element_by_name("username").send_keys(id[0])
    driver.find_element_by_name("userpwd").send_keys(id[1])
    driver.find_element_by_name("code").send_keys(s)
    driver.find_element_by_name("login").click()
    time.sleep(5)
    # 这里是解决页面跳转问题，用了笨办法
    url3 = 'https://xsswzx.cdu.edu.cn:81/isp/com_user/webindex.asp'
    driver.get(url3)
    time.sleep(10)
    driver.switch_to.frame('leftFrame')
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    url4 = 'https://xsswzx.cdu.edu.cn:81/isp/com_user/'
    url5 = bs.findAll('a')[43].get('href')
    url6 = url4 + url5
    driver.get(url6)
    time.sleep(5)
    driver.find_element_by_xpath('//input[@value="【一键登记：无变化】"]').click()
    dig_alert = driver.switch_to.alert
    dig_alert.accept()
    time.sleep(5)
    try:
        dig_alert = driver.switch_to.alert
        dig_alert.accept()
    except:
        pass
    time.sleep(10)
    try:
        driver.find_element_by_xpath('//input[@value="退出系统"]').click()
    except:
        pass
    print("登记成功")
driver.close()




