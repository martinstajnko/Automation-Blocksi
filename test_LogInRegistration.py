import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# Class TestLogIn()
# put self in the methods

# test_setup runs everytime when we have test
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    #print('Test run finished.')


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

    title = driver.title

    return title


def logInWithBlocksi(email, password):
    url = 'https://parent.blocksi.net/'
    driver.get(url)
    # Fill email
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/form[1]/span[1]/input').send_keys(email)
    sleep(0.5)
    # Fill password
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/form[1]/span[2]/input').send_keys(password)
    sleep(0.5)
    # Submit Log in
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/form[1]/button').click()
    sleep(5)

    title = driver.title

    return title


def registerWithGoogleOrBlocksi(x, email, password, student_email):
    url = 'https://parent.blocksi.net/'
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div/div[1]/section/a').click()
    sleep(3)

    # GOOGLE
    if (x == 1):
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

        # Sign up form
        # First name field
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/div/span[1]/input').send_keys('Ime')
        # Last name field
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/div/span[2]/input').send_keys('Priimek')
        # Valid student E-main field
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/span[1]/input').send_keys('student355@blocksicloud.net')
        # School field
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/span[2]/input').send_keys('OSSTICNA')
        # Phone number field
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/span[3]/input').send_keys('+38645781141')
        # Click button Create account
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/form/button').click()

        sleep(5)

        status = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]/b').text

    # BLOCKSI
    else:
        # E-mail field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[1]/input').send_keys(email)
        # Password field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[2]/input').send_keys(password)
        # Repeat password field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[3]/input').send_keys(password)
        # First name field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[4]/input').send_keys('Ime')
        # Last name field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[5]/input').send_keys('Priimek')
        # Phone number field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[6]/input').send_keys('+38645781141')
        # Valid student E-main field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[7]/input').send_keys(student_email)
        # Click button Create account
        sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/button').click()

        sleep(5)

        status = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]/b').text

    return status


def registerWithGoogleOrBlocksiWrongAccreditation(x, email, password, student_email):
    url = 'https://parent.blocksi.net/'
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div/div[1]/section/a').click()
    sleep(1)

    if (x == 1):
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
        sleep(1)

        title = driver.title

    else:
        # E-mail field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[1]/input').send_keys(email)
        # Password field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[2]/input').send_keys(password)
        # Repeat password field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[3]/input').send_keys(password)
        # First name field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[4]/input').send_keys('Ime')
        # Last name field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[5]/input').send_keys('Priimek')
        # Phone number field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[6]/input').send_keys('+38645781141')
        # Valid student E-main field
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/span[7]/input').send_keys(student_email)
        # Click button Create account
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/form[1]/button').click()

        sleep(1)
        title = driver.title

    return title


def delete_parentFromParentList(email):

    driver = webdriver.Chrome('./chromedriver')
    url = 'https://bm.blocksi.net/'
    driver.get(url)
    sleep(1)
    user = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    sleep(0.5)
    user.send_keys('admin@blocksicloud.net')
    navigate = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    navigate.click()
    sleep(2)
    passw = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    sleep(0.5)
    passw.send_keys('SiBlock2021@')
    sleep(2)
    navigate = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    navigate.click()
    sleep(5)
    allow_btn = driver.find_elements_by_xpath(
        '/html/body/div[2]/form/div[2]/div/div[1]/input[1]')

    if len(allow_btn) > 0:
        allow_btn[0].click()
    else:
        pass

    sleep(3)

    # Click on Dashboard Settings
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[1]/ul/li/div[8]/a').click()

    sleep(2)

    # Clik on Parent Dashboard
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[1]/ul/li/div[8]/article/p[3]/a').click()
    sleep(0.5)
    # Search for field "Search parents..." and input parent name
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[2]/div/div[2]/div[1]/div[12]/section/input').send_keys(email)
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[2]/div/div[2]/div[1]/div[12]/section/a').click()
    sleep(2)

    # Check if table contains of parent by <tbody>
    table = driver.find_element_by_xpath(
        '/html/body/div[11]/div[2]/div/div[2]/div[1]/div[12]/table/tbody')

    if not table.text:
        # List is empty
        pass
    else:
        driver.find_element_by_xpath(
            '/html/body/div[11]/div[2]/div/div[2]/div[1]/div[12]/table/tbody/tr/td[4]/a/b').click()
    sleep(1)

    # Log out - create new method
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[2]/div/div[1]/ul/div/li/div/button/div/span').click()
    driver.find_element_by_xpath(
        '/html/body/div[11]/div[2]/div/div[1]/ul/div/li/div/div/a[5]').click()

    driver.close()
    driver.quit()


##########################################
############## TEST CASES ################
##########################################

# Log in
def test_logInWithGoogle(test_setup):
    title = logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa1')
    assert title == 'Blocksi Parent Dashboard', f'Title is not same as predicted {title}'
    print('First test is done.')


def test_logInWithGoogleWrongAccreditation(test_setup):
    title = logInWithGoogle('mstajnko@blocksi.net', 'PesniKusa123')
    assert title == 'Prijava – Google Računi', f'Title is not same as predicted {title}'
    print('Second test is done.')


def test_logInWithBlocksi(test_setup):
    title = logInWithBlocksi(
        'parent_jernej@gedu.demo.blocksi.net', 'august2011')
    print(title)
    assert title == 'Blocksi Parent Dashboard', f'Title is not same as predicted {title}'


def test_loginWithBlocksiWrongAccreditation(test_setup):
    title = logInWithBlocksi(
        'parent_jernej@gedu.demo.blocksi.net', 'august201123')
    assert title == 'BM Education Everywhere sign up', f'Title is not same as predicted {title}'


# Register
def test_registerWithGoogle(test_setup):
    delete_parentFromParentList('rok.teacher')
    status = registerWithGoogleOrBlocksi(
        1, 'rok.teacher@blocksicloud.net', 'august2011', 'student355@blocksicloud.net')
    assert status == 'Waiting for validation', f'Test failed. Status is {status}, it should be "Waiting for validation".'


def test_registerWithGoogleWrongAccreditation(test_setup):
    delete_parentFromParentList('rok.teacher')
    title = registerWithGoogleOrBlocksiWrongAccreditation(1, 'rok.teacher@blocksicloud.net',
                                                          'august201123', 'student355@blocksicloud.net')
    assert title == 'Prijava – Google Računi', f'Title is not same as predicted {title}'


def test_registerWithBlocksi(test_setup):
    delete_parentFromParentList('rok.teacher')
    status = registerWithGoogleOrBlocksi(
        0, 'rok.teacher@blocksicloud.net', 'august2011', 'student355@blocksicloud.net')
    assert status == 'Waiting for validation', f'Test failed. Status is {status}, it should be "Waiting for validation".'


def test_registerWithBlocksiWrongAccreditation(test_setup):
    delete_parentFromParentList('rok.teacher')
    status = registerWithGoogleOrBlocksiWrongAccreditation(
        0, 'rok.teacher@blocksicloud.net', 'blocksitemp234', 'student355@blocksicloud.net')
    assert status == 'Blocksi Parent Dashboard', f'Test failed. Status is {status}, it should be "Waiting for validation".'
