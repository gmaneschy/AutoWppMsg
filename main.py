from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
service = Service()
nav = webdriver.Chrome(service = service)

time.sleep(5)
nav.get("https://web.whatsapp.com")
time.sleep(10)
mensagem = """O bostil é intankável!
Não aguento mais viver no bostil!
Petistas malditos!!!😡😡😡
"""

lista_contatos = ["Meu numero", "Gustavo Lino", "Miguel", "Armário", "Dia das mães", "Tribo de Jean"]

# enviar a mensagem para o Meu numero para poder enviar
time.sleep(5)
# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
time.sleep(0.5)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div/div/div/p').send_keys("Meu numero")
time.sleep(0.5)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div/div/div/p').send_keys(Keys.ENTER)
time.sleep(1)

# escrever mensagem
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + "v")
time.sleep(0.5)

# dar um enter
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

# encaminhar mensagem
lista_elementos = nav.find_elements('class name', '_amk6 _amlo')
for item in lista_elementos:
    mensagem = mensagem.replace("\n","")
    texto = item.text.replace("\n","")
    if mensagem in texto:
        elemento = item
        ActionChains(nav).move_to_element(elemento).perform()
        elemento.find_element('class name', 'xa11xnq').click()
        nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[5]/div').click()
        nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[2]/span').click()
        break



time.sleep(500)