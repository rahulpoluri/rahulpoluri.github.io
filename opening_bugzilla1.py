def opening_bugzilla(driver):
    driver.execute_script("window.open ('http://coraltreesystems.com/bugzilla/','bugzilla')")
    driver.switch_to.window('bugzilla')
    driver.find_element_by_id('account').click()
    driver.find_element_by_id('Bugzilla_login').send_keys("XXXXXXXXXXXXXXXXX")
    driver.find_element_by_id('Bugzilla_password').send_keys("XXXXXX")
    driver.find_element_by_id('log_in').click()
