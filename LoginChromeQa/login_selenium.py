# minhas importacoes
import time
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker('pt_BR')


class Test_logindiario():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                       'C:\\Users\\Juliana.bueno\\Desktop\\CadastroClude\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_logindiario(self):
        self.driver.get("https://qa.clude.com.br/cluder/Login/Index2?ReturnUrl=%2fcluder")
        self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Não tem uma conta? Crie agora").click()
        self.driver.find_element(By.ID, "adopt-accept-all-button")
        self.driver.find_element(By.ID, "adopt-accept-all-button").click()
        wait = WebDriverWait(self.driver, 10)

        # Inicio do cadastro 1

        self.driver.find_element(By.ID, "nome").send_keys(fake.name())
        self.driver.find_element(By.ID, "cpf").click()
        self.driver.find_element(By.ID, "cpf").send_keys(fake.cpf())
        self.driver.find_element(By.ID, "dataNascimento").click()
        self.driver.find_element(By.ID, "dataNascimento").send_keys("16081994")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys('87654321@uorak.com')
        self.driver.find_element(By.ID, "telefone").click()
        self.driver.find_element(By.ID, "telefone").send_keys("(64) 97925-1946")
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-6:nth-child(1) .price-subtitle").click()
        self.driver.find_element(By.ID, "numerocartao").click()
        self.driver.find_element(By.ID, "numerocartao").send_keys("5356066320271893")
        self.driver.find_element(By.ID, "nomecartao").send_keys("teste cinco cinco")
        self.driver.find_element(By.ID, "validadecartao").send_keys("12/25")
        self.driver.find_element(By.ID, "cvv").click()
        self.driver.find_element(By.ID, "cvv").send_keys("111")
        self.driver.find_element(By.XPATH, "//div[@data-painel='pagamento']").click()
        self.driver.find_element(By.XPATH, "(//label[@for='aceitotermo'])[2]").click()

        # pausa para preencher o captcha
        toast = ToastNotifier()
        toast.show_toast("Atenção", "Responda o captchá manualmente!!", duration=5, threaded=True)
        time.sleep(40)
        # devido o probelma de layout, essa script vira mobile e rola a pagina até o final
        self.driver.set_window_size(360, 700)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//p[contains(.,'Confirmar e fazer parte do Clude')]")
        self.driver.find_element(By.XPATH, "//p[contains(.,'Confirmar e fazer parte do Clude')]").click()

        # self.driver.switch_to.frame(0)# sai da página para preencher o captcha
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        # self.driver.switch_to.default_content()# fim do Codigo para pegar o captcha, retorna para a pagina
        # self.driver.set_window_size(360, 700)

        # Inicio do cadastro 2
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.CSS_SELECTOR, ".btnSubmit:nth-child(1)").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "senha"))).click()
        self.driver.find_element(By.ID, "senha").send_keys("1616")
        self.driver.find_element(By.ID, "confirmacaoSenha").click()
        self.driver.find_element(By.ID, "confirmacaoSenha").send_keys("1616")
        self.driver.find_element(By.CSS_SELECTOR, ".btnSubmit").click()

        # fim do programa
        self.driver.close()
