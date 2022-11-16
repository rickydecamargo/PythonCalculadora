#Essa automação inicializa a calculadora e multiplica 99 x 99 e depois fecha a aplicação.

import pyautogui as posicaoMouse

# Tempo de esperar para encontrar o icone do Windows:
posicaoMouse.sleep(2)

# Movendo o mouse para o icone do Windows:
posicaoMouse.moveTo(x=27, y=749)

# Clicando no Icone do Windows:
posicaoMouse.click(x=27, y=749)

# Esperar carregar a barra de tarefas:
posicaoMouse.sleep(4)

# Abrindo a Calculadora:
posicaoMouse.typewrite('Calculadora')

# Movendo o mouse para o icone da Calculadora:
posicaoMouse.moveTo(x=159, y=366)

# Clicando no icone da Calculadora:
posicaoMouse.click(x=120, y=215)

# Esperar carregar a barra de tarefas:
posicaoMouse.sleep(5)

# Clicando no numero 9:
posicaoMouse.click(x=600, y=430)

# Esperar digitar o primeiro numero (9)
posicaoMouse.sleep(1)

# Clicando no numero 9
posicaoMouse.click(x=600, y=430)

# Esperar digitar o segundo numero (9):
posicaoMouse.sleep(2)

# Clicando no botao multiplicacao:
posicaoMouse.click(x=860, y=470)

# Esperar clicar na multiplicacao:
posicaoMouse.sleep(2)

# Clicando no terceiro numero 9:
posicaoMouse.click(x=600, y=430)

# Esperar digitar o terceiro numero (9):
posicaoMouse.sleep(1)

# Clicando no quarto numero:
posicaoMouse.click(x=600, y=430)

# Esperar digitar o quarto numero (9):
posicaoMouse.sleep(2)

# Clicando no em Igual:
posicaoMouse.click(x=850, y=655)

# Esperar digitar o terceiro numero (9):
posicaoMouse.sleep(5)

# Clicando no numero em Fechar:
posicaoMouse.click(x=1325, y=20)

print('Aplicativo Calculadora Fechado.')
