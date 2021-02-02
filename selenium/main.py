from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.bilibili.com/v/digital/pc/#/")
driver.maximize_window()
driver.implicitly_wait(10)
page = driver.page_source

#打印源码，防止乱码加上编码格式；
print(page.encode("utf8"))

#保存网页源码名称为：testclass_cn.html，存储路径为工程根目录；
f=open('./testclass_cn.html',mode="w",encoding="utf-8")
f.write(page)
