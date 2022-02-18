from selenium import webdriver
from time import sleep


def test_scores_service(my_driver):
    my_driver.get("http://localhost:5000")
    my_driver.maximize_window()
    test = my_driver.find_element_by_xpath('//*[@id="tbody"]/tr[1]/td[2]').text
    if 1 <= int(test) <= 1000:
        return True
    else:
        return False


def main_function():
    my_driver = webdriver.Chrome(executable_path="chromedriver.exe")
    bool = test_scores_service(my_driver)
    if bool:
        return -1
    else:
        return 0

print(main_function())


