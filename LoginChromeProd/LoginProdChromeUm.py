# minhas importacoes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker('pt_BR')


# Escolha do browser
browser = webdriver.Chrome()
browser.get('https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f')


class Test_logindiario():
    def setup_method(self):
        self.driver = webdriver.Chrome(
            executable_path='C:\\Users\\Juliana.bueno\\Desktop\\CadastroClude\\drivers\\chromedriver.exe')
    def teardown_method(self):
        self.driver.quit()


    def test_logindiario(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//a[contains(.,'É colaborador de uma empresa?')]").click()


        # Inicio do cadastro 1

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "cpf"))).send_keys("410.376.982-31")
        self.driver.find_element(By.ID, "email").click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm'][contains(.,'CONTINUAR')]"))).click()
        self.driver.find_element(By.XPATH, "(//label[@for='aceitotermo'])[2]").click()

        # pausa para preencher o captcha

        toast = ToastNotifier()
        toast.show_toast("Atenção", "Responda o captchá manualmente!!", duration=10, threaded=True)
        time.sleep(40)
        self.driver.find_element(By.XPATH, "//p[contains(.,'Confirmar e fazer parte do Clude')]")
        self.driver.find_element(By.XPATH, "//p[contains(.,'Confirmar e fazer parte do Clude')]").click()

        # Inicio do cadastro 2
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btnSubmit:nth-child(1)"))).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "senha"))).click()
        # time.sleep(3)
        # self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.ID, "confirmacaoSenha").click()
        self.driver.find_element(By.ID, "confirmacaoSenha").send_keys("1616")
        self.driver.find_element(By.CSS_SELECTOR, ".btnSubmit").click()

        # fim do programa
        self.driver.close()
