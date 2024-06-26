
import pyautogui
from time import sleep

# Passo manual para automação:
# Abrir o aplicativo
pyautogui.doubleClick(394, 553)

# Para o código em Python:
# 1 - pyautogui
# 2 - pillow
# 3 - mouseinfo

# 1 - Clicar e digitar seu usuário
pyautogui.click(941, 538, duration=2)
pyautogui.write('jhonatan')

# 2 - Clicar e digitar sua senha
pyautogui.click(951, 581, duration=2)
pyautogui.write('123456')

# 3 - Clicar em entrar
pyautogui.click(826, 627, duration=2)

# 4 - Extrair produtos do arquivo
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        # Remover espaços em branco antes de dividir
        linha_sem_espaco = linha.strip()

        # Dividir a linha por vírgulas
        dados = linha_sem_espaco.split(',')

        # Atribuir valores às variáveis
        if len(dados) >= 3:  # Verifica se há pelo menos 3 elementos (produto, quantidade, valor)
            produto = dados[0]
            quantidade = dados[1]
            valor = dados[2]
        else:
            # Se a linha não tiver 3 elementos, exiba uma mensagem de aviso
            print(f"Linha inválida: {linha}")
            

        # 1 - Clicar e digitar o produto
        pyautogui.click(524, 515, duration=1)
        pyautogui.write(produto)

        # 2 - Clicar e digitar a quantidade
        pyautogui.click(528, 562, duration=1)
        pyautogui.write(quantidade)

        # 3 - Clicar e digitar o valor
        pyautogui.click(543, 609, duration=1)
        pyautogui.write(valor)

        # 4 - Clicar em registrar
        pyautogui.click(409, 843, duration=1)
        sleep(1)

# Feito a automação!
# Agora, migrar para a AWS

 