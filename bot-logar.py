import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from unidecode import unidecode
import string
import clipboard
import sys
import pyperclip

# configurando as variaves
# Inicializa a lista para armazenar os dados dos perfis
perfis = []

# Abre o arquivo "perfis.txt" para leitura
with open("perfis.txt", "r") as arquivo:
    # Inicializa um dicionário para armazenar as informações de um perfil
    perfil = {}

    # Lê o arquivo linha por linha
    for linha in arquivo:
        # Remove espaços em branco no início e no final da linha
        linha = linha.strip()

        # Verifica se a linha está vazia, o que indica o fim de um perfil
        if not linha:
            # Adiciona o perfil à lista de perfis
            perfis.append(perfil)

            # Reinicializa o dicionário para o próximo perfil
            perfil = {}
        else:
            # Divide a linha em chave e valor apenas se houver um ":" na linha
            if ":" in linha:
                chave, valor = linha.split(":", 1)
                chave = chave.strip()
                valor = valor.strip()
                # Armazena a informação no dicionário do perfil
                perfil[chave] = valor

# Inicializa um contador para a enumeração
contador = 1

# Imprime os dados de cada perfil
for perfil in perfis:
    print(f"Perfil {contador}:")
    print("Login:", perfil.get("FB-Email", "N/A"))
    print("Senha:", perfil.get("FB-Password", "N/A"))
    print("Chave:", perfil.get("2FA-Secret-Key", "N/A"))
    print()  # Adiciona uma linha em branco entre os perfis
    contador += 1  # Incrementa o contador para a próxima enumeração


if len(perfis) >= 3:
    # Acessa o primeiro perfil (índice 0) da lista
    perfil1 = perfis[0]
    login_perfil1 = perfil1.get("FB-Email", "N/A")
    senha_perfil1 = perfil1.get("FB-Password", "N/A")
    chave_perfil_1 = perfil1.get("2FA-Secret-Key", "N/A")

    # Acessa o segundo perfil (índice 1) da lista
    perfil2 = perfis[1]
    login_perfil2 = perfil2.get("FB-Email", "N/A")
    senha_perfil2 = perfil2.get("FB-Password", "N/A")
    chave_perfil_2 = perfil2.get("2FA-Secret-Key", "N/A")

    # Acessa o terceiro perfil (índice 2) da lista
    perfil3 = perfis[2]
    login_perfil3 = perfil3.get("FB-Email", "N/A")
    senha_perfil3 = perfil3.get("FB-Password", "N/A")
    chave_perfil_3 = perfil3.get("2FA-Secret-Key", "N/A")
else:
    print("Não há informações suficientes para acessar os perfis 1, 2 e 3.")

# vareaveis perfis - 1
login_perfil1 = perfil1.get("FB-Email", "N/A")
senha_perfil1 = perfil1.get("FB-Password", "N/A")
chave_perfil_1 = perfil1.get("2FA-Secret-Key", "N/A")

# vareaveis perfil  2
login_perfil2 = perfil2.get("FB-Email", "N/A")
senha_perfil2 = perfil2.get("FB-Password", "N/A")
chave_perfil_2 = perfil2.get("2FA-Secret-Key", "N/A")

#vareaveis perfil 3
login_perfil3 = perfil3.get("FB-Email", "N/A")
senha_perfil3 = perfil3.get("FB-Password", "N/A")
chave_perfil_3 = perfil3.get("2FA-Secret-Key", "N/A")

# Gerando Nomes Aleatorios
def gerar_nome_aleatorio():
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Laura", "Fernando", "Julia", "Rafael", "Camila", "Mariana", "Daniel", "Isabela", "Antônio", "Gabriela", "Gustavo", "Amanda", "Matheus", "Larissa", "Diego", "Carolina", "Henrique", "Beatriz", "Vinicius", "Natália", "Rodrigo", "Letícia", "Lucas", "Clara", "Felipe", "Isabella", "Guilherme", "Sophia", "Arthur", "Helena", "Rafaela", "Miguel", "Valentina", "Luisa", "Enzo", "Manuela", "Thiago", "Bianca", "Bernardo", "Lorena", "Joana", "Giovanni", "Alice", "Hugo", "Luiza", "Marcos", "Sofia"]
    nomes_sem_acento = [unidecode(nome) for nome in nomes]
    nome_aleatorio = random.choice(nomes_sem_acento)
    return nome_aleatorio

#GERANDO SOBRENOME ALEATORIOS
def gerar_sobrenome_brasileiro():
    sobrenomes = [
        "Almeida", "Andrade", "Araujo", "Barbosa", "Campos", "Cardoso", "Carvalho", "Cavalcanti", "Costa",
        "Ferreira", "Gomes", "Lima", "Machado", "Martins", "Melo", "Monteiro", "Moraes", "Nascimento", "Oliveira",
        "Pereira", "Ribeiro", "Rodrigues", "Santana", "Santos", "Silva", "Sousa", "Souza", "Teixeira", "Vieira"
    ]

    sobrenome_aleatorio = random.choice(sobrenomes)
    sobrenome_sem_acento = unidecode(sobrenome_aleatorio)
    return sobrenome_sem_acento

def gerar_tempo_aleatorio():
    tempo_aleatorio = random.randint(3, 5)
    time.sleep(tempo_aleatorio)
    return tempo_aleatorio
def gerar_numero():
    numero_aleatorio = random.randint(1, 28)
    return numero_aleatorio

def gerar_meis():
    meis = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
    meis_aleatorio = random.choice(meis)
    return  meis_aleatorio

def gerar_ano():
    ano_aleatorio = random.randint(1989, 2004)
    return ano_aleatorio


def gerar_senha():
    comprimento = random.randint(8, 15)
    caracteres_permitidos = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres_permitidos) for _ in range(comprimento))
    return senha

def gerar_numero_telefonico():
    ddd = random.choice(['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99'])
    parte_1 = str(random.randint(1000, 9999))
    parte_2 = str(random.randint(1000, 9999))
    return ddd + '9' + parte_1 + parte_2

def generate_random_filename():
    letters = random.choices(string.ascii_uppercase, k=3)
    numbers = random.choices(string.digits, k=3)
    filename = ''.join(letters + numbers)
    return filename

def iniciar_driver_com_user_agent(user_agents):
    user_agent = random.choice(user_agents)
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def sortear_nome(lista):
    nome_aleatorio = random.choice(lista)
    return nome_aleatorio


#lista de nomes de artitas e paginas
famoso_pg = [
"https://www.facebook.com/globo",
"https://www.facebook.com/portalr7",
"https://www.facebook.com/netflixbrasil",
"https://www.facebook.com/AFazendaRecord",
"https://www.facebook.com/UOL",
"https://www.facebook.com/metropolesdf",
"https://www.facebook.com/UOLNoticias",
"https://www.facebook.com/g1",
"https://www.facebook.com/memes",
"https://www.facebook.com/thenetflixmemes",
"https://www.facebook.com/WholesomeGirlfriendMemes",
"https://www.facebook.com/FofoqueiTv",
"https://www.facebook.com/fofocasdoleodias",
"https://www.facebook.com/euleodias",
"https://www.facebook.com/neymarjr",
"https://www.facebook.com/cr7cristianoronaldo",
"https://www.facebook.com/leomessi",
"https://www.facebook.com/Jojotodynho",
"https://www.facebook.com/mcpipokinha",
"https://www.facebook.com/TNTSportsBR",
"https://www.facebook.com/BigBrotherBrasil",
]

def sortear_nome(lista):
    nome_sorteado = random.choice(lista)
    # Remover espaços em branco do nome sorteado
    nome_sorteado = nome_sorteado.replace(" ", "")
    return nome_sorteado

def compartilhar():
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Compartilhar')]").click()
        gerar_tempo_aleatorio()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Compartilhar agora (Público)')]").click()
        gerar_tempo_aleatorio()
    except:
        print('erro proxima açao')
def scroll_mouse():
    gerar_tempo_aleatorio()
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    gerar_tempo_aleatorio()

#condiçao de curtir
def curtir():

    try:
        gerar_tempo_aleatorio()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Curtir')]").click()
        print("passou")
        gerar_tempo_aleatorio()

    except:
        gerar_tempo_aleatorio()
        driver.find_element(By.XPATH,'//*[@id="mount_0_0_Xy"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div').click()
        gerar_tempo_aleatorio()

# Chamar a função para sortear um nome aleatório
nome_sorteado = sortear_nome(famoso_pg)

# Imprimir o nome sorteado
print(nome_sorteado)


# Lista de User Agents de dispositivos Android
user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Edge/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 Edg/100.0.0.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 Edg/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 Edg/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36 OPR/100.0.0.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:100.0.0.0) Gecko/20100101 Firefox/100.0.0.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0.0.0) Gecko/20100101 Firefox/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/100.0.0.0 Chrome/100.0.0.0"

]

# Inicializando funcçoes
# Iniciando Funçoes
nome_arquivo = generate_random_filename()
numero_telefonico = gerar_numero_telefonico()
print(numero_telefonico)
senha_a = gerar_senha()
gerar_ano()
gerar_meis()
gerar_numero()
gerar_tempo_aleatorio()
gerar_nome_aleatorio()
gerar_sobrenome_brasileiro()

# Escolher um User Agent aleatório
random_user_agent = random.choice(user_agents)
# Configurar o serviço ChromeDriver
service = Service("C:/Users/Frankly 255/Desktop/driver/chromedriver-win64/chromedriver.exe")
service.start()

# Configurar as opções do Chrome para modo anônimo e User Agent
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_argument(f"user-agent={random_user_agent}")

# Abrir o navegador com o User Agent aleatório
driver = webdriver.Remote(service.service_url, options=chrome_options)

nome_arquivo = generate_random_filename()
numero_telefonico = gerar_numero_telefonico()
print(numero_telefonico)
senha_a = gerar_senha()
gerar_ano()
gerar_meis()
gerar_numero()
gerar_tempo_aleatorio()
gerar_nome_aleatorio()
gerar_sobrenome_brasileiro()


print(driver.title)

# criando uma nova Aba
driver.execute_script("window.open('', '_blank');")

# listando as janelas
janelas = driver.window_handles
gerar_tempo_aleatorio()

 # Mudando para a primeira Aba
driver.switch_to.window(janelas[0])

# entrando na pagina do facebook
driver.get('https://facebook.com/')
gerar_tempo_aleatorio()
# Email
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(login_perfil1)
gerar_tempo_aleatorio()
# Senha
driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys(senha_perfil1)
gerar_tempo_aleatorio()
# clicando no entra
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()



# Buscar codigo de autenticaçao
driver.switch_to.window(janelas[1])
# entrando no site

gerar_tempo_aleatorio()
driver.get("https://2fa-auth.com/")
gerar_tempo_aleatorio()

driver.find_element(By.XPATH,'//*[@id="ma"]').send_keys(chave_perfil_1)
gerar_tempo_aleatorio()

driver.find_element(By.XPATH,'//*[@id="get2fa"]').click()
gerar_tempo_aleatorio()

#pegando codigo
input_element = driver.find_element(By.CLASS_NAME,"isures-2fa--code")

# Obter o valor do elemento input
valor_do_input = input_element.get_attribute("value")

# Imprimir o valor
print(valor_do_input)
gerar_tempo_aleatorio()

driver.switch_to.window(janelas[0])

# pondo codigo no input do face
driver.find_element(By.XPATH,'//*[@id="approvals_code"]').send_keys(valor_do_input)
gerar_tempo_aleatorio()

# clicando no botao submit
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button').click()
gerar_tempo_aleatorio()

# clicando no continuar
driver.find_element(By.XPATH,'//*[@id="checkpointSubmitButton"]').click()
gerar_tempo_aleatorio()
time.sleep(10)
# colocando nomes no input
driver.get(f"{nome_sorteado}")
print("clicou")
gerar_tempo_aleatorio()

try:
    curtir()
except:
    scroll_mouse()

scroll_mouse()
try:
    curtir()
except:
    scroll_mouse()

compartilhar()
gerar_tempo_aleatorio()
try:
    curtir()
except:
    scroll_mouse()

scroll_mouse()

gerar_tempo_aleatorio()

nome_sorteado = sortear_nome(famoso_pg)
print(nome_sorteado)
driver.get(f"{nome_sorteado}")

funcoes = [curtir, compartilhar, scroll_mouse]
# Escolha aleatoriamente uma das funções
funcao_escolhida = random.choice(funcoes)
gerar_tempo_aleatorio()
funcao_escolhida = random.choice(funcoes)
gerar_tempo_aleatorio()


print('aiiiiiiiiiiiiiiii')

time.sleep(1000)