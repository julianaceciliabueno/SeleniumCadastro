# minhas importacoes
import time
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker('pt_BR')


class Test_logindiario_segunda_parte():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                       'C:\\Users\\Juliana.bueno\\Desktop\\CadastroClude\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_primeira_parte(self):
        self.driver.get("https://qa.clude.com.br/cluder/Login/Index2")
        self.driver.maximize_window()


        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys('876543210@uorak.com')
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        wait = WebDriverWait(self.driver, 10)

        # Segunda parte de Login
        self.driver.find_element(By.NAME, "dataNascimento").click()
        self.driver.find_element(By.NAME, "dataNascimento").send_keys("16/08/1994")
        self.driver.find_element(By.XPATH, "//input[@value='F']").click()
        self.driver.find_element(By.NAME, "cep").click()
        self.driver.find_element(By.NAME, "cep").send_keys("06033-000")
        self.driver.find_element(By.NAME, "logradouro").click()
        # self.driver.find_element(By.NAME, 'logradouro').send_keys('Rua da Fonte')

        self.driver.find_element(By.NAME, 'cidade').click()
        # self.driver.find_element(By.NAME, 'cidade').send_keys('Osasco')

        dropdown = self.driver.find_element(By.NAME, "estado")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paulo']").click()

        self.driver.find_element(By.NAME, 'bairro').click()
        # self.driver.find_element(By.NAME, 'bairro').send_keys('Jardim DAbril')

        self.driver.find_element(By.NAME, "numero").click()
        self.driver.find_element(By.NAME, "numero").send_keys("12")
        self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Próximo')]")
        self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Próximo')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(@class,'dropdown-toggle admin-notification')]").click()
        self.driver.find_element(By.LINK_TEXT, "Sair").click()

        print("Primeira parte do cadastro feito")

        # fim do programa
        self.driver.close()

class Test_Segunda_Parte():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                'C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get('https://qa.clude.com.br/cluder/Login/Index2')
        self.driver.maximize_window()

    # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys('876543210@uorak.com')
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH,
                        "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.NAME, "14").click()
        self.driver.find_element(By.NAME, "14").send_keys("168")

        self.driver.find_element(By.NAME, "15").click()
        self.driver.find_element(By.NAME, "15").send_keys("68")

        self.driver.find_element(By.XPATH, "//input[@value='201']").click()

        self.driver.find_element(By.XPATH, "//input[@value='1516']").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()
        wait = WebDriverWait(self.driver, 10)
        print("Segunda parte do cadastro feito")

    # fim do programa
        self.driver.close()

class Test_Terceira_Parte():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                'C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get('https://qa.clude.com.br/cluder/Login/Index2')
        self.driver.maximize_window()


    # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys('876543210@uorak.com')
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH,
                                "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-close']").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()
        time.sleep(3)
        # Escolha a data da consulta
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'30')])[1]"))).click()
            print("foi escolhido o dia 30")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'31')])[1]"))).click()
            print("foi escolhido o dia 31")

        # Escolha o horario da consulta
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'09:20')])[12]"))).click()
            print("foi escolhido o horário 09:20")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'10:00')])[12]"))).click()
            print("foi escolhido o horário 10:00")

        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()
        self.driver.find_element(By.ID, "btnConfirmarAgendamento").click()
        # /html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[4]/button[1]
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Ok, entendi')]")
        self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Ok, entendi')]").click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//label[contains(.,'Agora não')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Vamos lá')]").click()
        print("cadastro concluído")
    # fim do programa
        self.driver.close()