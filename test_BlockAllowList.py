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


def createNewBAList():
    # Navigate to BA List
    navigateToBAList()
    sleep(0.5)


def countOptionsInBAList():
    options_list = []
    elements = driver.find_elements_by_tag_name('span')
    for i in elements:
        if 'filterName' in i.get_attribute('class'):
            options_list.append(i)
    return len(options_list)


def emptyBAList():
    x = driver.find_elements_by_tag_name('i')
    sleep(0.5)
    for i in x:
        if 'fa fa-fw fa-trash' in i.get_attribute('class'):
            i.click()
            sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div[3]/button').click()
            sleep(1)
            driver.refresh
            sleep(1)


def navigateToBAList():
    try:
        driver.find_element_by_id('bwlistsActive').click()
        print('Move to BA list.')
    except NoSuchElementException:
        print('Element is missing.')


def checkElementListNameField():
    try:
        element = driver.find_element_by_id('newListName')
        print('najdem')
        return element
    except NoSuchElementException:
        print('ne najdem')
        return 'Element is missing'


def checkElementCreateListButton():
    try:
        element = driver.find_element_by_id('newListBtn_v2')
        print('najdem')
        return element
    except NoSuchElementException:
        print('ne najdem')
        return 'Element is missing'


### TEST CASES ####

# def test_FindListNameField(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     navigateToBAList()
#     element = checkElementListNameField()
#     assert 'Element is missing' != element, f'Did not find element List Name Field.'


# def test_FindCreateListButton(test_setup):
#     logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
#     navigateToBAList()
#     element = checkElementCreateListButton()
#     assert 'Element is missing' != element, f'Did not find element List Name Field.'


# def test_createBlockAllowList(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Število list {counter}')
    if counter > 0:
        emptyBAList()
    sleep(1)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    # click on button
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    counter2 = countOptionsInBAList()
    sleep(1)
    x = ''
    if counter2 > 0:
        x = 'OK'  # New list was created
    else:
        x = 'NOK'  # New list was not created

    assert 'OK' == x, f'New list was not created.'


# def test_createBlockAllowListWithoutName(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(1)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    # click on button
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    message = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]').text
    sleep(2)
    assert 'Error! A list with that name already exists.' == message, f'Test failed. Message is not as predicted.'


# def test_createBlockAllowListWitHSpecCharacter(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(1)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    if counter > 0:
        emptyBAList()
    sleep(1)
    driver.find_element_by_id('newListName').send_keys('Blocksi_#$')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    x = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/span[1]').text

    assert 'Blocksi_#$' == x, f'Test failed.'


# def test_createBlockAllowListWithExistingName(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    navigateToBAList()
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Število list {counter}')
    if counter > 0:
        emptyBAList()
    sleep(1)
    for x in range(2):
        driver.find_element_by_id('newListName').send_keys('Blocksi')
        sleep(1)
        # click on button - add filter
        driver.find_element_by_id('newListBtn_v2').click()
        sleep(1)
    sleep(2)
    error_message = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]').text

    assert 'Error! A list with that name already exists.' == error_message, f'Test failed.'


# def test_duplicateBlockAllowList(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(1)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(2)
    print(f'Število list {counter}')
    if counter > 0:
        emptyBAList()
    sleep(2)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    # click on button
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on duplicate
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[1]/i').click()
    sleep(0.5)
    # type duplicate name
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/input').send_keys('Blocksi2')
    # click ok to apply duplicate
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/button[1]').click()
    counter2 = countOptionsInBAList()
    print(counter2)
    sleep(1)
    # two elements are expected that means 0 and 1
    if counter2 == 1:
        x = 'OK'
    else:
        x = 'NOK'
    assert 'OK' == x, f'Test failed.'


# def test_duplicateBlockAllowListWithoutName(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(1)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
   # click on button
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on duplicate
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[1]/i').click()
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/button[1]').click()
    sleep(1)

    try:
        error = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
        print(f'Error name is: {error}')
    except NoSuchElementException:
        print('Exception happened, test will fail.')
        error = 'NoSuchElementException'
    assert 'Error! Filter name can not be empty!' == error, f'Test failed.'


# def test_duplicateBlockAllowListWithSpecChar(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(1)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on duplicate button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[1]/i').click()
    sleep(1)
    # set name of duplicate as original
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/input').send_keys('Blocksi_#$')
    # click ok to apply duplicate
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/button[1]').click()
    sleep(1)
    counter2 = countOptionsInBAList()
    print(counter2)
    # sleep(1)
    # two elements are expected that means 0 and 1
    if counter2 == 2:
        x = 'OK'
    else:
        x = 'NOK'
    assert 'OK' == x, f'Test failed.'


# def test_duplicateBlockAllowListWithExistingName(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Število list {counter}')
    if counter > 0:
        emptyBAList()
    sleep(2)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on duplicate button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[1]/i').click()
    sleep(1)
    # set name of duplicate as original
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/input').send_keys('Blocksi')
    # click ok to apply duplicate
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/button[1]').click()
    sleep(1)
    try:
        error_message = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        error_message = ''
    assert 'Error!' == error_message, f'Test failed.'


# def test_editBlockAllowListAddURL(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('www.partis.si')
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
    sleep(1)
    try:
        url = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[3]/div')
    except NoSuchElementException:
        url = ''
    print(url)
    assert url != '', f'Test failed.'


# def test_editBlockAllowListAddURL(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('www.nba.com/*')
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
    sleep(1)
    try:
        url = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[3]/div')
    except NoSuchElementException:
        url = ''
    print(url)
    assert url != '', f'Test failed.'


# def test_editBlockAllowListAddEmptyURL(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('')
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
    sleep(1)
    try:
        error_message = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        error_message = ''

    assert error_message == 'Error! Url is too short.', f'Test failed.'


# def test_editBlockAllowListAddExistingURL(test_setup):
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL two times
    for x in range(2):
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('www.partis.si')
        sleep(0.5)
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
        sleep(1)
    try:
        error_message = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        error_message = ''

    assert error_message == 'Error! URL already exists.', f'Test failed.'


# def test_editBlockAllowListUpdateURL(test_setup):
    # change url from block to allow
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('www.partis.si')
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
    sleep(1)
    try:
        error_message = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        print('URL was not added.')

    # click on Allow
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[3]/div/div/label[1]').click()
    except NoSuchElementException:
        print('No button Allow.')
    # click on Update
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[3]/div/div/span').click()
    except NoSuchElementException:
        print('No button Update.')
    # find message
    sleep(1)
    try:
        message_success = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        message_success = ''

    assert message_success == 'Success!', f'Test failed.'


def test_editBlockAllowListDeleteURL(test_setup):
    # change url from block to allow
    logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    sleep(2)
    navigateToBAList()
    sleep(1)
    counter = countOptionsInBAList()
    sleep(1)
    print(f'Number of lists is: {counter}')
    if counter > 0:
        emptyBAList()
    sleep(0.5)
    driver.find_element_by_id('newListName').send_keys('Blocksi')
    sleep(1)
    driver.find_element_by_id('newListBtn_v2').click()
    sleep(1)
    # click on edit button
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/a[2]/i').click()
    sleep(1)
    # enter URL
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('www.partis.si')
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/button/a').click()
    sleep(1)
    try:
        error_message = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        print('URL was not added.')
    sleep(1)
    # click delete
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div[3]/div/div/a/i').click()
    try:
        message_success = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]').text
    except NoSuchElementException:
        message_success = ''

    assert message_success == 'Success!', f'Test failed.'
