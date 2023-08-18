import tkinter as tk
import openai  # Certifique-se de instalar a biblioteca openai: pip install openai

openai.api_key = "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"  # Substitua pelo seu próprio chave de API

def send_message():
    message = user_input.get()
    if message:
        chat_display.insert(tk.END, "Você: " + message + "\n")
        user_input.delete(0, tk.END)
        response = get_chatgpt_response(message)
        chat_display.insert(tk.END, "ChatGPT: " + response + "\n")

def get_chatgpt_response(input_message):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Substitua pelo modelo adequado
        prompt=input_message,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Configuração da janela principal
root = tk.Tk()
root.title("Bate-Papo com ChatGPT")

# Área de exibição de mensagens
chat_display = tk.Text(root)
chat_display.pack(fill=tk.BOTH, expand=True)

# Entrada de texto
user_input = tk.Entry(root, width=50)
user_input.pack()

# Botão de envio
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Inicia a interface gráfica
root.mainloop()
