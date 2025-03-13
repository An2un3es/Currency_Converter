import tkinter as tk
from tkinter import ttk, messagebox
from currency import convert_currency, CURRENCIES  # Importando do módulo separado

# Criando a janela principal
root = tk.Tk()
root.title("Conversor de Moeda")
root.geometry("350x400")

# Entrada do valor
tk.Label(root, text="Valor:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Seleção da moeda base
tk.Label(root, text="Moeda Base:").pack()
base_currency_var = tk.StringVar(value="")
base_currency_menu = ttk.Combobox(root, textvariable=base_currency_var, values=CURRENCIES, state="readonly")
base_currency_menu.pack()

# Botão para converter
def on_convert():
    try:
        value = float(amount_entry.get())
        base = base_currency_var.get()
        result = convert_currency(base)
        if result:
            del result[base]  # Removendo a moeda base dos resultados
            result_text = f"{value} {base}:\n\n\n" + "\n".join([f"{curr}: {value * rate:.2f}" for curr, rate in result.items()])
            result_label.config(text=result_text)
            
            # Limpar campos após conversão bem-sucedida
            amount_entry.delete(0, tk.END)
            base_currency_menu.set("")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

tk.Button(root, text="Converter", command=on_convert).pack()

# Área de resultado
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10)
result_label.pack()

# Center window
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Rodar a interface
tk.mainloop()
