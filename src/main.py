import tkinter as tk
from utils.convert_items_to_list import convert_items_to_list
import pyautogui
import pydirectinput


window = tk.Tk()

def run_script():
    input_value = input.get("1.0", "end-1c")

    items_to_list = convert_items_to_list(input_value)

    if len(items_to_list) <= 0:
        # pyautogui.alert('Por favor, insira um texto válido!')
        return


    # gf_windows = gw.getWindowsWithTitle("Grand Fantasia")

    # if gf_windows:
    #     gf_window = gf_windows[0]
    #     gf_window.activate()

    for item in items_to_list:
        pydirectinput.keyUp('enter')

        # pyautogui.press('enter', interval=1.25)
        # pyautogui.press('esc', interval=1.5)
    return
    


ent = tk.Entry(window,width=10)

window.title("Item add automatization")

label = tk.Label(window, text="Cole seu texto de alquimia aqui! Quando clicar em confirmar NÃO MEXA EM SEU PC ATÉ FINALIZAR")
label.pack()

input = tk.Text(window)
input.pack()

button = tk.Button(window, text="Confirmar", command=run_script)
button.pack()

window.mainloop()
