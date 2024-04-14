import tkinter as tk
from utils.convert_items_to_list import convert_items_to_list
import pyautogui
import pydirectinput
import pygetwindow as gw
import time

from components.button import Button
from components.textarea import TextArea

window = tk.Tk()
window.configure(bg='#282828')

pyautogui.FAILSAFE = True

def run_script():
    pyautogui.FAILSAFE = True
    textarea_value = textarea.get("1.0", "end-1c")

    items_to_list = convert_items_to_list(textarea_value)

    if len(items_to_list) <= 0:
        pyautogui.alert('Por favor, insira um texto válido!')
        return


    gf_windows = gw.getWindowsWithTitle("Grand Fantasia")

    if gf_windows:
        gf_window = gf_windows[0]
        gf_window.activate()

    pydirectinput.press('enter')
    time.sleep(1)
    pyautogui.write("/scbi", interval=0.05)
    pydirectinput.press('enter')

    count = 0

    for i in range(len(items_to_list)):
        item = items_to_list[i]

        if i == 0:
            pydirectinput.press('enter')
            time.sleep(0.2)
            pyautogui.write("/scbi", interval=0.05)
            time.sleep(0.6)
            pydirectinput.press("enter")
            time.sleep(0.2)


        print("Iteração do loop")
        count += 1
        print(f"Iteração {count}")
        pydirectinput.press('enter')
        time.sleep(0.2)
        pyautogui.write(f"/ci {item['id']}", interval=0.05)
        time.sleep(0.6)
        pydirectinput.press('enter')
        time.sleep(0.2)
        print("escreveu")
    return

ent = tk.Entry(window,width=10)

window.title("Item add automatization")

label = tk.Label(window, text="Cole seu texto de alquimia aqui! Ao clicar em confirmar, NÃO MEXA EM SEU PC ATÉ FINALIZAR", bg='#282828', fg='#FFFFFF')
label.pack()

textarea = TextArea(window, height=10, width=50)
textarea.pack(pady=20)

button = Button(window, text="Confirmar")
button.config(command=run_script)
button.pack(pady=20)


window.mainloop()
