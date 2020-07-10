from selenium import webdriver

b = webdriver.Chrome(executable_path="C://Users//Real fadil//AppData//Local//Temp//Rar$EXa7632.37358//chromedriver.exe")
mobile_emulation = { "deviceName": "Nexus 5" }
b.add_experimental_option("mobileEmulation", mobile_emulation)
