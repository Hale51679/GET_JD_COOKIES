from splinter import Browser
from selenium import webdriver
import time
import json


def main():
    chrome_path = 'D:/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # 替换为你的Chromedriver的实际路径
    service = webdriver.chrome.service.Service(chrome_path)
    executable_path = 'C:/Users/Haolen/AppData/Local/Google/Chrome/Application/chrome.exe'  # 替换为你的Chrome的实际路径
    browser = Browser('chrome', service=service ,executable_path=executable_path)

    browser.visit('https://plogin.m.jd.com/login/login')
    input('登陆后按Enter键继续...')

    browser.visit('https://home.m.jd.com/myJd/newhome.action')
    time.sleep(2)
    cookies = browser.cookies.all()
    jd_cookie = 'pt_key=' + cookies['pt_key'] + ';pt_pin=' + cookies['pt_pin'] + ';'

    print(jd_cookie)
    browser.quit()


if __name__ == '__main__':
    main()