# minhas importacoes
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from win10toast import ToastNotifier
from faker import Faker
fake = Faker('pt_BR')

# browser escolhido
browser = webdriver.Chrome()
browser.get('https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f')


class Test_login():
    def setup_method(self):
        self.driver = webdriver.Chrome(
            executable_path='C:\\Users\\Juliana.bueno\\Desktop\\CadastroClude\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f")
        self.driver.maximize_window()


        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("produ1110822@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(10)

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
        print("Primeira parte do cadastro feito")

        # fim do programa
        self.driver.close()

class Test_PrimeiraParte():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                               'C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f")
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("produ1110822@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(10)


        # terceira parte de Login
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "14").click()
        self.driver.find_element(By.NAME, "14").send_keys("168")

        self.driver.find_element(By.NAME, "15").click()
        self.driver.find_element(By.NAME, "15").send_keys("68")

        self.driver.find_element(By.NAME, "71").click()
        self.driver.find_element(By.NAME, "350").click()

        self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()
        self.driver.implicitly_wait(10)


        self.driver.find_element(By.XPATH, "//i[@class='fa fa-close']").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()

        # Escolha a data da consulta
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'12')])[1]"))).click()
            print("foi escolhido o dia 12")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'30')])[1]"))).click()
            print("foi escolhido o dia 30")

        # Escolha o horario da consulta
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'16:20')])[12]"))).click()
            print("foi escolhido o horário 16:20")

        except TimeoutException:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[contains(.,'16:40')])[12]"))).click()
            print("foi escolhido o horário 16:40")

        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        toast = ToastNotifier()
        toast.show_toast("Atenção!!!", "Resolva o captcha manualmente", duration=10, threaded=True)
        time.sleep(30)
        self.driver.find_element(By.ID, "btnConfirmarAgendamento").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Ok, entendi')]")
        self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Ok, entendi')]").click()
        self.driver.find_element(By.XPATH, "//label[@class='mt-3 btnDismiss'][contains(.,'Agora não')]")
        self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Vamos lá')]").click()

        # # Cancelamento da consulta
        # self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(3)").click()
        # self.driver.find_element(By.ID, "btnCancelarConsulta").click()
        # self.driver.find_element(By.ID, "confirmarCancelamentoConsulta").click()

        # fim do programa
        self.driver.close()