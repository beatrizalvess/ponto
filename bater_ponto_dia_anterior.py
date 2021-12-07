import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=r'./chromedriver', options = options)

#Acessar pontomais
driver.get("https://app.pontomaisweb.com.br/#/meu_ponto")

#Credênciais
campo_login_xpath = "/html/body/ng-view/div/div/form/div/div[1]/div/div/div/div/input"
campo_login = driver.find_element(By.XPATH, campo_login_xpath)
campo_login.clear()
campo_login.send_keys("beatriz.santos@itriad.org.br")

campo_password_xpath = "/html/body/ng-view/div/div/form/div/div[2]/div/div/div/div/input"
campo_password = driver.find_element(By.XPATH, campo_password_xpath)
campo_password.clear()
campo_password.send_keys("Resgate123")

botao_entrar_xpath = "/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button"
botao_entrar = driver.find_element(By.XPATH, botao_entrar_xpath)
botao_entrar.click()

time.sleep(6)

menu_meu_ponto_xpath = "/html/body/div[2]/div[2]/div/div/nav/div/ul/li[5]"
menu_meu_ponto = driver.find_element(By.XPATH, menu_meu_ponto_xpath)
menu_meu_ponto.click()

time.sleep(3)

botao_dia_anterior_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div/ng-view/div[2]/div[2]/table/tbody/tr[2]/td[14]/div/button[1]"
botao_dia_anterior = driver.find_element(By.XPATH, botao_dia_anterior_xpath)
botao_dia_anterior.click()

time.sleep(2)

botao_ajuste_de_ponto_xpath = "/html/body/div[1]/div/div/div/div/div/div/div/div[1]/button"
botao_ajuste_de_ponto = driver.find_element(By.XPATH, botao_ajuste_de_ponto_xpath)
botao_ajuste_de_ponto.click()

time.sleep(2)

#Adicionar ponto
botao_adicionar_ponto_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[1]/div[2]/div/button[2]"
botao_adicionar_ponto = driver.find_element(By.XPATH, botao_adicionar_ponto_xpath)
botao_adicionar_ponto.click()

botao_adicionar_ponto_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[1]/div[2]/div/button[2]"
botao_adicionar_ponto = driver.find_element(By.XPATH, botao_adicionar_ponto_xpath)
botao_adicionar_ponto.click()

botao_adicionar_ponto_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[1]/div[2]/div/button[2]"
botao_adicionar_ponto = driver.find_element(By.XPATH, botao_adicionar_ponto_xpath)
botao_adicionar_ponto.click()

botao_adicionar_ponto_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[1]/div[2]/div/button[2]"
botao_adicionar_ponto = driver.find_element(By.XPATH, botao_adicionar_ponto_xpath)
botao_adicionar_ponto.click()

#Adiocionar horários
campo_entrada_1_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/input"
campo_entrada_1 = driver.find_element(By.XPATH, campo_entrada_1_xpath)
campo_entrada_1.clear()
campo_entrada_1.send_keys("800a")

campo_saida_1_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/input"
campo_saida_1 = driver.find_element(By.XPATH, campo_saida_1_xpath)
campo_saida_1.clear()
campo_saida_1.send_keys("1200p")

campo_entrada_1_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/input"
campo_entrada_1 = driver.find_element(By.XPATH, campo_entrada_1_xpath)
campo_entrada_1.clear()
campo_entrada_1.send_keys("1300p")

campo_saida_1_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[2]/div[4]/div/div[1]/div[2]/div/input"
campo_saida_1 = driver.find_element(By.XPATH, campo_saida_1_xpath)
campo_saida_1.clear()
campo_saida_1.send_keys("1700p")

#Adicionar motivo da solicitação
campo_solicitacao_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[1]/div[4]/div/textarea"
campo_solicitacao = driver.find_element(By.XPATH, campo_solicitacao_xpath)
campo_solicitacao.clear()
campo_solicitacao.send_keys("Home Office.")

botao_propor_xpath = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/ng-view/div[2]/div/button[2]"
botao_propor = driver.find_element(By.XPATH, botao_propor_xpath)
botao_propor.click()

time.sleep(5)

driver.quit()
