import unittest #библиотека unittest
from selenium import webdriver #библиотека selenium web driver
from selenium.webdriver.common.by import By #метод позволяющий искать селекторы
from selenium.webdriver.support.ui import WebDriverWait #метод отвечающий за неявные ожидания

#адрес страницы, которую мы будем открывать
hostname = 'https://mail.ru/'
#логин в почту
login = 'fbs_test1203@mail.ru'
#пароль в почту
password = '1Passw0rd'

#создаем класс нашей главной страницы
class MainPageMail(unittest.TestCase):

#метод определяющий выбор браузера и указывающий какой chromedriver использовать и где он лежит
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/romashov/Projects/Autotests/myvenv/bin/chromedriver')

#метод описывающий сам процесс заполнения формы входа
    def the_login_test(self):

        driver = self.driver #определяем драйвер
        wait = WebDriverWait(driver, 100) #выставляем ожидание
        driver.get(hostname) #запрашиваем страницу
        assert "Mail.Ru" in driver.title #проверяем что в заголовке Title загруженногй страницы есть упоминания mail.ru

        login_field = driver.find_element(By.XPATH, value="//input[@id='mailbox:login']") #селектор нахождения поля логин
        password_field = driver.find_element(By.XPATH, value="//input[@id='mailbox:password']") #селектор нахождения поля пароль
        submit_button = driver.find_element(By.XPATH, value="//input[@value='Войти']") #селектор нахождения кнопки sibmit

        login_field.send_keys(login) #с помощью метода send_keys передаем в поле логина наш логин
        password_field.send_keys(password) #с помощью метода send_keys передаем в поле пароль наш пароль
        submit_button.click() #с помощью метода click() нажимаем на кнопку submit

#метод определяющий закрытие сессии
    def tearDown(self):
        self.driver.quit()
