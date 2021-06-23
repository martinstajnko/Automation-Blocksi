from copy import Error
from typing import Text
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def logInWithGoogle(email, password):
    url = 'https://parent.blocksi.net/'
    driver.get(url)
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/form[2]/input[2]').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    sleep(5)


def checkSideNavBarElements(x):
    if (x == 0):
        dashboard = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/ul/li[2]/a').text
        return dashboard
    elif(x == 1):
        block_allow_list = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/ul/li[3]/a').text
        return block_allow_list
    elif(x == 2):
        access_time_control = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/ul/li[4]/a').text
        return access_time_control
    else:
        insights = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/ul/li[5]/a').text
        return insights


def checkUserTableElements(element):
    if (element == 'status'):
        try:
            status = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]')
            return status
        except NoSuchElementException:
            return ('Element STATUS is missing')

    elif (element == 'email'):
        try:
            email = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[2]')
            return email
        except NoSuchElementException:
            return ('Element EMAIL is missing')

    elif (element == 'atc'):
        try:
            atc = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[3]/select')
            return atc
        except NoSuchElementException:
            return ('Element ACCESS TIME CONTROL is missing')

    elif (element == 'bl'):
        try:
            bl = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[4]/select')
            return bl
        except NoSuchElementException:
            return ('Element BLOCK LIST is missing')

    elif (element == 'pause_internet'):
        try:
            pause_internet = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[5]/label')
            return pause_internet
        except NoSuchElementException:
            return ('Element PAUSE INTERNET is missing')

    # delete button
    else:
        try:
            delete = driver.find_elements_by_xpath(
                '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[6]/a/i')
            return delete
        except NoSuchElementException:
            return ('Element DELETE is missing')


def checkAccessTimeControl():
    pass


def setOptionInDropDownMenu(filter):
    if filter == 'AccessTimeControl':
        options = Select(driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[3]/select'))
        num_options = countOptionsInList(options)
        print(num_options)
    # filter == 'BlockList'
    else:
        options = Select(driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[4]/select'))
        num_options = countOptionsInList(options)
        print(num_options)

    """ ČE IMAMO DVE MOŽNOSTI - DVA FILTRA  """
    if num_options > 1:
        # options.select_by_index(1)
        before_option = options.first_selected_option.text
        if before_option == 'None':
            options.select_by_index(1)
        else:
            options.select_by_index(0)

        after_option = options.first_selected_option.text
        return after_option

    # ČE IMAMO SAMO ENO MOŽNOST, NAJPREJ NAREDIMO ŠE EN FILTER
    else:
        createNewAccessTimeControl()
        before_option = options.first_selected_option.text
        if before_option == 'None':
            options.select_by_index(1)
        else:
            options.select_by_index(0)

        after_option = options.first_selected_option.text
        return after_option


def readOptionInDropDownMenu(filter):
    # if 0 then Access Time Control else Block List
    if filter == 'form-control selectATP':
        options = Select(driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[3]/select'))
        selected_option = options.first_selected_option.text
        return selected_option
    else:
        options = Select(driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[4]/select'))
        selected_option = options.first_selected_option.text
        return selected_option


def countOptionsInList(s):
    options_list = []

    options = s.options
    for i in options:
        print(i)
        options_list.append(i)

    # print(len(options_list))

    return len(options_list)


def createNewAccessTimeControl():
    x = driver.find_element_by_id('timecontrol').click()
    sleep(0.5)
    before = driver.find_elements_by_class_name('b_filter')
    x = len(before)
    find_field = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('martin123')
    click_CreateATC = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[2]/button/a').click()
    sleep(2)
    # dobimo elemente v od elementov v accsess time controlu
    after = driver.find_elements_by_class_name('b_filter')
    y = len(after)
    if x < y:
        print('OK')
    else:
        print('NOK')


def createNewBlockAllowList():
    pass


def modifyAccessTimeControl():
    pass


def modifyBlockAllowList():
    pass


def insights():
    pass


def addStudent(student):
    driver.find_element_by_id(
        'newStudentEmail').send_keys(student)
    sleep(1)
    driver.find_element_by_id('requestStudentBtn').click()


def getUsersInUserTable():

    ### TEST CASES ###

    # Main navigation bar
    # def test_dashboard(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     element = checkSideNAvBarElements(0)
    #     assert element == 'Dashboard', f'Test failed. {element} is not as predicted "Dashboard".'

    # def test_BlockAllowList(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     element = checkSideNAvBarElements(1)
    #     assert element == 'Block/Allow List', f'Test failed. {element} is not as predicted "Block/Allow List".'

    # def test_AccessTimeControl(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     element = checkSideNAvBarElements(2)
    #     assert element == 'Access Time Control', f'Test failed. {element} is not as predicted "Access Time Control".'

    # def test_Insights(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     element = checkSideNAvBarElements(3)
    #     assert element == 'Insights', f'Test failed. {element} is not as predicted "Insights".'

    # def test_ExpandWindow(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')

    #     # id_wrapper -> empty class name when window toggles to full screen it changes to toggled
    #     # now is empty " "
    #     class_name = driver.find_element_by_xpath(
    #         '/html/body/div[3]').get_attribute('class')

    #     # extend window
    #     driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[1]/a/i').click()
    #     sleep(1)

    #     # now is "toggled"
    #     class_name2 = driver.find_element_by_xpath(
    #         '/html/body/div[3]').get_attribute('class')

    #     # compare
    #     if class_name != class_name2:
    #         print('OK, window is extended. {class_name} != {class_name2}.')
    #     else:
    #         print('NOK, window is not extended.')

    #     assert class_name != class_name2, f'Test failed.'  # DOKONČAJ KOMENTAR

    #     sleep(1)

    #     # reduce window
    #     driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[1]/a/i').click()
    #     sleep(1)

    #     class_name3 = driver.find_element_by_xpath(
    #         '/html/body/div[3]').get_attribute("class")

    #     if class_name2 != class_name3:
    #         print('OK, window is not extended. {class_name2} != {class_name3}.')
    #     else:
    #         print('NOK, window is extended.')

    #     assert class_name2 != class_name3, f'Test failed.'  # DOKONČAJ KOMENTAR

    # def test_recentStatsTable(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     recent_stats = driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[2]/div[3]/div/div')
    #     print(recent_stats.text)
    #     assert recent_stats != '', f'Test failed.'

    # def test_userTable(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     users_table = driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]').get_attribute('class')
    #     assert "usersTable" in users_table, f'Test failed.'

    # def test_emailAccountField(test_setup):
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     email_field = driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[2]/div[4]/div[1]/input').get_attribute('placeholder')
    #     print(email_field)
    #     assert 'Enter an email account' in email_field, f'Test failed.'

    # def test_requestValidationButton(test_setup):
    #     print('Start with test request validation button')
    #     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    #     button_name = driver.find_element_by_xpath(
    #         '/html/body/div[3]/div[2]/div/div[2]/div[4]/div[2]/button/a').text
    #     assert button_name == 'REQUEST VALIDATION', f'Test failed. Button name is not as predicted.'

    # def test_changeTimezone(test_setup):
    print('Start with test change timezone')
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    # Click on timezone dropdown menu
    zones = Select(driver.find_element_by_id('timezoneList'))
    # Change time zone
    zones.select_by_value('Asia/Dhaka')
    sleep(2)
    # Check for message "Updated!"
    message = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]').text
    print(message)
    # Close pop up window
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div[3]/button').click()
    sleep(0.5)
    # Change timezone to Europe/Paris
    zones.select_by_value('Europe/Paris')
    print('Change zone back to Euro/Paris.')
    assert message == 'Updated!', f'Test failed. Message is not as predicted.'


# def test_logOut(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    element = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[2]/div/div[1]/ul/li[3]/a')
    element[0].click()
    sleep(5)
    title = driver.title
    assert title == 'BM Education Everywhere sign up', f'Somethong went wrong.'
    # WORKS


# def test_userTable(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    h4_tag = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]').get_attribute('h4')
    expected_result = 'USERS TABLE'
    assert h4_tag == expected_result, f'Something went wrong.'
    # WORKS


# def test_userTableStatus(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('status')
#     assert actual_result != 'Element STATUS is missing', f'Element is missing.'
#     # WORKS


# def test_userTableEmail(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('email')
#     assert actual_result != 'Element EMAIL is missing', f'Element is missing.'
#     # WORKS


# def test_userTableATC(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('atc')
#     assert actual_result != 'Element ACCESS TIME CONTROL is missing', f'Element is missing.'
#     # WORKS


# def test_userTableBL(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('bl')
#     assert actual_result != 'Element BLOCK LIST is missing', f'Element is missing.'
#     # WORKS


# def test_userTablePauseInternet(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('bl')
#     assert actual_result != 'Element PAUSE INTERNET is missing', f'Element is missing.'
#     # WORKS


# def test_userTableDelete(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(2)
#     actual_result = checkUserTableElements('delete')
#     assert actual_result != 'Element DELETE is missing', f'Element is missing.'
#     # WORKSP

# def test_setATCFilter(test_setup):
#     print('Start with test: Set Access Time Control filter')
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(1)
#     before_option = readOptionInDropDownMenu('form-control selectATP')
#     sleep(1)
#     setOptionInDropDownMenu('AccessTimeControl')
#     sleep(1)
#     after_option = readOptionInDropDownMenu('form-control selectATP')
#     assert before_option != after_option, f'Not ok option did not change. Before: {before_option}, after: {after_option}'


# def test_setBlockList(test_setup):
#     print('Start with test: Set Block List filter')
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(1)
#     before_option = readOptionInDropDownMenu('form-control selectBW')
#     setOptionInDropDownMenu('BlockList')
#     sleep(1)
#     after_option = readOptionInDropDownMenu('form-control selectBW')
#     assert before_option != after_option, f'Not ok option did not change. Before: {before_option}, after: {after_option}'


# def test_setPauseInternet(test_setup):
#     print('Start with test: Set Pause Internet')
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     sleep(1)


def test_deleteUser(test_setup):
    print('Start with test: Delete user.')
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')


def test_addStudent(test_setup):
    print('Start with test: Add student.')
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    addStudent('demo_test@blocksicloud.net')
    sleep(1)
