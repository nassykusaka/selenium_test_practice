# -*- coding: utf-8 -*-
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')
browser.quit()
