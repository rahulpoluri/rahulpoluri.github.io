def opening_usms(driver,time,pyautogui):
    result = 0
    while result is 0:
        try:
           #driver.get(r'https://usms.upc.biz')
            driver.execute_script("window.open ('https://usms.upc.biz','usms')")
            driver.switch_to.window('usms')
            print(1)
            #time.sleep(1)
            result=1
        except:
            pass


    driver.maximize_window()

    result = 0
    while result is 0:
        try:
            driver.find_element_by_xpath("//*[text()='Liberty Global']").click()
            time.sleep(1)
            result=1
        except:
            pass



    result = 0
    while result is 0:
        try:
            button=driver.find_element_by_name('select');button.click()
            time.sleep(1)
            result=1
        except:
            pass


    time.sleep(2)
    pyautogui.click(925, 496)
    time.sleep(2)
    pyautogui.click(514, 150)
    time.sleep(1)
    pyautogui.typewrite('XXXXXXXXXXXXX')
    pyautogui.press('tab')
    pyautogui.typewrite('XXXXXXXXXXXXX')
    time.sleep(2)
    pyautogui.press('enter')

    result = 0
    while result is 0:
        try:
            applications=driver.find_element_by_id(r'reg_img_304316340');applications.click()
            time.sleep(1)
            result=1
        except:
            pass
    result = 0
    while result is 0:
        try:
            incident_management=driver.find_element_by_link_text('Incident Management');incident_management.click()
            time.sleep(1)
            result=1
        except:
            pass
    result = 0
    while result is 0:
        try:
            search_incident=driver.find_element_by_link_text('Search Incident');search_incident.click()
            time.sleep(1)
            result=1
        except:
            pass

