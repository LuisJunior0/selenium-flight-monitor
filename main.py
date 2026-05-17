from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import locale
from datetime import datetime 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #padronizando formato PT-BR para encontrar no XPATH

inicio = input("Digite a data (Dia/Mes/Ano): ") #Pedindo para o Usuario a Data
data_objeto = datetime.strptime(inicio, "%d/%m/%Y") #Aqui convertemos para o formato dia/mes/ano
data_formatada = data_objeto.strftime("%#d de %B de %Y") #Formatando com a função strptime texto para formato tempo





print("iniciando navegador...")

navegador = webdriver.Chrome()

print("abrindo site...")

navegador.get("https://123milhas.com/")

print("site aberto")


navegador.maximize_window()

print("procurando span com texto...")

botao_Somenteida = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH,
    '//span[contains(text(), "Somente ida")]')
    )
)

print("elemento encontrado")

print("clicando...")

botao_Somenteida.click()

print("clicou")

botao_origem = WebDriverWait(navegador, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, 
    '//input[@placeholder="Busque por aeroporto"]')
    )
)

botao_origem[0].send_keys("Belém")

print("Digitou origem")


lista_belem = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//li//span[contains(text(), "Belém")]')
    )
)

lista_belem.click()

print("Click origem")


botao_origem[1].send_keys("Campinas - Viracopos (VCP)")

print("Digitou Destino")


lista_vcp = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH,
    '//li//span[contains(text(), "Campinas")]')
    )
)

lista_vcp.click()

print("Click Destino")


abrir_calendario = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, 
    '//input[@placeholder="Escolha a ida"]')
    )
)

abrir_calendario.click()

print("Abre Calendario")


data_ida = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH,
    f'//td[contains(@aria-label, "{data_formatada}")]') #Data Dinamica
    )
)

data_ida.click()

print("Clica na data")


buscar_voo = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH,
    '//span[contains(text(), "BUSCAR VOOS")]')
    )
)

buscar_voo.click()
print("Buscando seu VOO")

localizar_precos = WebDriverWait(navegador, 30).until(
    EC.presence_of_all_elements_located(
        (By.XPATH,
    '//span[contains(@class, "renewed-flight-card__total--container__value")]')
    )
)

print("Localizei um VALOR")

for preco in localizar_precos:
    print(f"Valor encontrado: R${preco.text}")



input("pressione ENTER para fechar....") 
