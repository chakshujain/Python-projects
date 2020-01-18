from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
nameslist = list(map(str,input("Enter names of users you wanna send message: ").split()))

msg = input("Enter message: ")
count = int(input("How many times you wanna send: "))
input("Enter any key after scanning code")

for name in nameslist:
    
    user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()
driver.minimize_window()
