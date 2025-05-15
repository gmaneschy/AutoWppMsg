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

mensagem = """
 ⠀⠀⢀⣀⠤⠿⢤⢖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡔⢩⠂⠀⠒⠗⠈⠀⠉⠢⠄⣀⠠⠤⠄⠒⢖⡒⢒⠂⠤⢄⠀⠀⠀⠀
⠇⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠈⠈⡨⢀⠡⡪⠢⡀⠀
⠈⠒⠀⠤⠤⣄⡆⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠀⢕⠱⠀
⠀⠀⠀⠀⠀⠈⢳⣐⡐⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠇
⠀⠀⠀⠀⠀⠀⠀⠑⢤⢁⠀⠆⠀⠀⠀⠀⠀⢀⢰⠀⠀⠀⡀⢄⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡦⠄⡷⠢⠤⠤⠤⠤⢬⢈⡇⢠⣈⣰⠎⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣃⢸⡇⠀⠀⠀⠀⠀⠈⢪⢀⣺⡅⢈⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠶⡿⠤⠚⠁⠀⠀⠀⢀⣠⡤⢺⣥⠟⢡⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
"""

lista_contatos = ["Meu numero", "Gustavo Lino", "Miguel", "Rafael Maneschy", "Armário", "Dia das mães", "Tribo de Jean"]

# enviar a mensagem para o Meu numero para poder enviar
time.sleep(5)
# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]').click()
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

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

qtde_contatos = len(lista_contatos)
if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1
for i in range(qtde_blocos):
    # rodar o código de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]
    time.sleep(1)
    # Localize o elemento onde deseja clicar com o botão direito
    background = nav.find_element('xpath', '//*[@id="main"]/div[3]/div/div[2]/div[3]')

    # Crie uma instância de ActionChains
    action_chains = ActionChains(nav)

    # Mova o cursor do mouse para o elemento desejado
    action_chains.move_to_element(background)

    # Execute o clique com o botão direito do mouse
    action_chains.context_click().perform()
    time.sleep(2)
    # Clica Encaminhar
    nav.find_element('xpath', '//*[@id="app"]/div/span[6]/div/ul/div/div/li[2]/div').click()
    time.sleep(1)

    # Encontra todas as caixas de mensagem na conversa
    mensagens = nav.find_elements('xpath', '//*[@id="main"]/div[3]/div/div[2]/div[3]/div')

    # Pega a última mensagem (último elemento da lista)
    ultima_msg = mensagens[-1]

    # Clica na caixinha da última mensagem
    ultima_msg.click()

    # Clica em encaminhar
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    for nome in lista_enviar:
        # selecionar 5 contatos para enviar
        # escreve nome do contato
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(
            nome)
        time.sleep(1)
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(
            Keys.ENTER)
        time.sleep(1)
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(
            Keys.BACKSPACE)
        time.sleep(1)
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)