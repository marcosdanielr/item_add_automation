import tkinter as tk
from utils.convert_items_to_list import convert_items_to_list
import pyautogui
import pygetwindow as gw

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

    for item in items_to_list:
        print(item)
        pyautogui.press('enter', interval=0.04)
        pyautogui.write(f"/ci {item['id']}", interval=0.05)
        pyautogui.press('enter', interval=0.06)
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
