#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 15:24
# @Author  : Chris.Ma
# 一、作业一：操作百度页面
# 1、作业要求：①打开百度页面，②设置→搜索设置，③将【搜索结果显示条数】按下拉框逐个选中展示
# 2、作业格式：homework1_姓名_0804.py
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

#打开谷歌driver
driver = webdriver.Chrome()
#打开百度页面
driver.get("https://www.baidu.com/")
sleep(1)
#以文本形式定位【设置】
element = driver.find_element_by_link_text("设置")
#悬停
ActionChains(driver).move_to_element(element).perform()
sleep(1)
#以文本形式定位【搜索设置】，并点击
element1 = driver.find_element_by_link_text("搜索设置").click()
sleep(1)
#查询下拉框元素，并声明已变量
select1 = driver.find_element_by_id("nr")
#将下拉框元素，转换为select
select = Select(select1)
#索引:以下标形式
select.select_by_index(1)
sleep(2)
#索引：以value值形式
select.select_by_value("20")
sleep(2)
#索引：以文本形式
select.select_by_visible_text("每页显示50条")
sleep(2)

#关闭
driver.quit()