# minhas importacoes
import time
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier


# browser escolhido
browser = webdriver.Firefox()
browser.get('https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f')


class Test_logindiario():
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=
                                        "C:\\Users\\Juliana.bueno\\Desktop\\AutomacaoWebCludeSelenium\\drivers\\geckodriver.exe")

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f")
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("testediariofox1207@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        WebDriverWait(driver, 20)

        # self.driver.find_element(By.NAME, "dataNascimento").click()
        # self.driver.find_element(By.NAME, "dataNascimento").send_keys("16/08/1994")
        # self.driver.find_element(By.XPATH, "//input[@value='F']").click()
        # self.driver.find_element(By.NAME, "cep").click()
        # self.driver.find_element(By.NAME, "cep").send_keys("06033-000")
        # self.driver.find_element(By.NAME, "logradouro").click()
        # # self.driver.find_element(By.NAME, 'logradouro').send_keys('Rua da Fonte')
        #
        # self.driver.find_element(By.NAME, 'cidade').click()
        # # self.driver.find_element(By.NAME, 'cidade').send_keys('Osasco')
        #
        # dropdown = self.driver.find_element(By.NAME, "estado")
        # dropdown.find_element(By.XPATH, "//option[. = 'São Paulo']").click()
        #
        # self.driver.find_element(By.NAME, 'bairro').click()
        # # self.driver.find_element(By.NAME, 'bairro').send_keys('Jardim DAbril')
        #
        # self.driver.find_element(By.NAME, "numero").click()
        # self.driver.find_element(By.NAME, "numero").send_keys("12")
        # self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Próximo')]")
        # self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Próximo')]").click()

        # time.sleep(5)
        # self.driver.find_element(By.NAME, "14").click()
        # self.driver.find_element(By.NAME, "14").send_keys("168")
        #
        # self.driver.find_element(By.NAME, "15").click()
        # self.driver.find_element(By.NAME, "15").send_keys("68")
        #
        # self.driver.find_element(By.XPATH, "//input[@value='201']").click()
        #
        # self.driver.find_element(By.XPATH, "//input[@value='1516']").click()
        # self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH, "//i[@class='fa fa-close']").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[contains(.,'Próximo')]").click()

        toast = ToastNotifier()
        toast.show_toast("Atenção", "escolha uma data e hora manualmente!!", duration=10, threaded=True)
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Próximo')]").click()

        toast = ToastNotifier()
        toast.show_toast("Atenção", "Resolva o captcha manualmente!!", duration=10, threaded=True)
        time.sleep(15)
        # self.driver.switch_to.frame(2)
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        # self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "btnConfirmarAgendamento").click()
        # self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Ok, entendi')]").click()
        # self.driver.find_element(By.XPATH, "//label[@class='mt-3 btnDismiss'][contains(.,'Agora não')]")
        # self.driver.find_element(By.XPATH, "//button[@class='btnSubmit'][contains(.,'Vamos lá')]").click()
        # self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(3)").click()
        # self.driver.find_element(By.ID, "btnCancelarConsulta").click()
        # self.driver.find_element(By.ID, "modalCancelamentoConsultaBtnSucesso").click()

        # fim do programa
        self.driver.close()