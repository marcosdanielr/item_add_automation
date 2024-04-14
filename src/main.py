import tkinter as tk
from utils.convert_items_to_list import convert_items_to_list
import pyautogui
import pydirectinput
import pygetwindow as gw
import time

from components.button import Button
from components.textarea import TextArea
from components.checkbox import Checkbox

window = tk.Tk()
window.configure(bg='#282828')
pydirectinput.FAILSAFE = True

checkbox_value = tk.BooleanVar()

def run_script():
    textarea_value = textarea.get("1.0", "end-1c")

    items_to_list = convert_items_to_list(textarea_value)

    if len(items_to_list) <= 0:
        pyautogui.alert('Por favor, insira um texto válido!')
        return


    gf_windows = gw.getWindowsWithTitle("Grand Fantasia")

    if len(gf_windows) <= 0:
        pyautogui.alert('Precisa estar com o GF aberto!')
        return
    
    gf_window = gf_windows[0]
    gf_window.activate()

    pydirectinput.press("enter")

    for i, item in enumerate(items_to_list):

        if i == 0 and checkbox_value.get():
            pydirectinput.press("enter")
            time.sleep(0.2)
            pyautogui.write("/scbi", interval=0.04)
            time.sleep(0.2)
            pydirectinput.press("enter")

        pydirectinput.press("enter")
        time.sleep(0.2)
        pyautogui.write(f"/ci {item['id']}", interval=0.04)
        time.sleep(0.2)
        pydirectinput.press('enter')

        if i == len(items_to_list) - 1:
            pyautogui.alert("Pronto!")

ent = tk.Entry(window,width=10)

window.title("Item add automatization")

label = tk.Label(window, text="Cole seu texto de alquimia aqui! Ao clicar em confirmar, NÃO MEXA EM SEU PC ATÉ FINALIZAR", bg='#282828', fg='#FFFFFF')
label.pack()

textarea = TextArea(window, height=10, width=50)
textarea.pack(pady=20)

button = Button(window, text="Confirmar")
button.config(command=run_script)
button.pack(pady=20)

checkbox = Checkbox(window, text="Limpar inventário", variable=checkbox_value)
checkbox.pack()


window.mainloop()
