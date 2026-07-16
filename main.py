from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locale
from datetime import datetime, timedelta

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data = input("Digite a data: [dia-mês-ano] ")
data_objeto = datetime.strptime(data, "%d-%m-%Y") 
data_formatada = data_objeto.strftime("%d-%m-%Y")
intervalo = int(input("Digite o intervalo de dias a serem calculados: "))

intervalo_datas = []

for dias in range(1, intervalo + 1):
    um_dia = timedelta(days=dias)
    nova_data = data_objeto + um_dia
    nova_data_formatada = nova_data.strftime("%d-%m-%Y")
    intervalo_datas.append(nova_data_formatada) 

print(f"Buscando seu voo para o dia {data_formatada}")

url = f"https://123milhas.com/v2/busca?de=BEL&para=VCP&ida={data_formatada}&adultos=1&criancas=0&bebes=0&classe=3&is_loyalty=0"

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get(url)

localizar_precos = WebDriverWait(navegador, 35).until(
    EC.presence_of_all_elements_located(
        (By.XPATH,
    '//span[contains(@class, "renewed-flight-card__total--container__value")]')
    )
)

print("Localizei um VALOR")

for preco in localizar_precos:
    print(f"Valores encontrados para o dia {data_formatada}")
    print(f"R${preco.text}")

url = f"https://123milhas.com/v2/busca?de=BEL&para=VCP&ida={intervalo_datas[0]}&adultos=1&criancas=0&bebes=0&classe=3&is_loyalty=0"

navegador.get(url)

localizar_precos = WebDriverWait(navegador, 35).until(
    EC.presence_of_all_elements_located(
        (By.XPATH,
    '//span[contains(@class, "renewed-flight-card__total--container__value")]')
    )
)

print("Localizei um VALOR")

for preco in localizar_precos:
    print(f"Valores encontrados para o dia {intervalo_datas[0]}")
    print(f"R${preco.text}")

url = f"https://123milhas.com/v2/busca?de=BEL&para=VCP&ida={intervalo_datas[1]}&adultos=1&criancas=0&bebes=0&classe=3&is_loyalty=0"

navegador.get(url)


localizar_precos = WebDriverWait(navegador, 35).until(
    EC.presence_of_all_elements_located(
        (By.XPATH,
    '//span[contains(@class, "renewed-flight-card__total--container__value")]')
    )
)

print("Localizei um VALOR")

for preco in localizar_precos:
    print(f"Valores encontrados para o dia {intervalo_datas[1]}")
    print(f"R${preco.text}")


input("Pressione ENTER para fechar o navegador...")
