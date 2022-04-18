import time
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I am on the "{expected_title}" homepage')
def step_impl(context, expected_title):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("https://www.google.com")
    page_title = context.driver.title
    assert (expected_title == page_title)


@given(u'I entered "{term}" into the search field')
def step_impl(context, term):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys(term)


@when(u'I press enter')
def step_impl(context):
    search_button = context.driver.find_element_by_xpath("//div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    search_button.click()
    time.sleep(1)


@then(u'I Go to the search results page')
def step_impl(context):
    page_title = context.driver.title
    print(page_title)
    assert ("test automation - Buscar con Google" == page_title)


@then(u'The first three results contain the word "{key_word}"')
def step_impl(context, key_word):
    # results = context.driver.find_elements_by_partial_link_text('automation')
    results = context.driver.find_elements_by_xpath("//table[@class='AaVjTc']/tbody/tr/td/a")
    i = 0
    is_present = False
    while i < 3:
        link_text = results[i].text
        if not key_word in link_text: raise AssertionError
        is_present = False
        i += 1


@given(u'I search by "{link_text}"')
def step_impl(context, link_text):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("https://www.google.com")
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys(link_text)


@when(u'I click on the first link')
def step_impl(context):
    # element = context.driver.find_elements_by_xpath('//*[@id="tads"]/div[1]/div/div/div[1]/a/div[1]/span')
    # element.click()
    search_button = context.driver.find_element_by_xpath("//div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    search_button.click()
    time.sleep(5)
    # element = context.driver.find_element_by_partial_link_text('automation')
    element = context.driver.find_element_by_xpath("//table[@class='AaVjTc']/tbody/tr/td/a")
    element.click()
    time.sleep(2)


@then(u'I go to the page')
def step_impl(context):
    page_title = context.driver.title
    print(page_title)

@then(u'The title contains the word "{key}"')
def step_impl(context, key):
    time.sleep(2)
    if not key in context.driver.tile: raise AssertionError