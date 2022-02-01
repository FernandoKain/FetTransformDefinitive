# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))



# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')

def mudaaba():
    pyautogui.hotkey('ctrl', 'pgdn')



def fun():
    print(variavel)

def fun2():
    global variavel
    variavel = "Outro valor"
    print(variavel)

fun()
fun2()
print(variavel)

# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
alttab2()
alttab()


# -------- Clica no seletor de salas ----------
pyautogui.click(x=100, y=70)

# --------------Ajusta para a primeira aula a ser copiada (Segunda - 1ª aula)
pyautogui.click(x=200, y=350)



def acresentavar():

    x = 4
    y = 4
    for i in range(x):
        up()
        x = x+1
    for i in range(y):
        down()
        y = y+1



