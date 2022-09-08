# minhas importacoes
import time
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker('pt_BR')

# Escolha do browser
browser = webdriver.Firefox()
browser.get('https://empresas.clude.com.br/Login?ReturnUrl=%2f')


class Test_logindiario():
    def setup_method(self):
        self.driver = webdriver.Chrome("C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\geckodriver.exe")

    def teardown_method(self):
        self.driver.quit()

    # Inicio do login
    def test_producao(self):
        self.driver.get("https://empresas.clude.com.br/Login?ReturnUrl=%2f")
        self.driver.set_window_size(1366, 705)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("juliana.bueno@clude.com.br")
        self.driver.find_element(By.ID, "Password").click()
        self.driver.find_element(By.ID, "Password").send_keys("Luiz@1608")
        self.driver.find_element(By.NAME, "process").click()
        # Inicio do cadastro 1
        self.driver.find_element(By.CSS_SELECTOR, ".panel > .panel-body").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary-roxo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-roxo-light .items").click()

        # pausa para preencher o pop up

        toast = ToastNotifier()
        toast.show_toast("Atenção", "Click ok no pop-up!!", duration=10, threaded=True)

        time.sleep(20)

        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary-roxo").click()
        self.driver.find_element(By.LINK_TEXT, "Cadastrar usuário").click()
        # Inicio do cadastro 2
        self.driver.find_element(By.NAME, "Nome").click()
        self.driver.find_element(By.NAME, "Nome").send_keys(fake.name())
        self.driver.find_element(By.ID, "cpf").click()
        self.driver.find_element(By.ID, "cpf").send_keys(fake.cpf())
        # coloque um email sempre com o final @uorak.com
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("produ@uorak.com")
        self.driver.find_element(By.ID, "sexo[f]").click()
        self.driver.find_element(By.ID, "telefone").click()
        self.driver.find_element(By.ID, "telefone").send_keys("(64) 97925-1946")
        self.driver.find_element(By.ID, "departamento").send_keys("TI – Tecnologia da Informação")
        dropdown = self.driver.find_element(By.NAME, "PLano")
        dropdown.find_element(By.XPATH, "//option[@value='1']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        # Fim do programa
        self.driver.close()
