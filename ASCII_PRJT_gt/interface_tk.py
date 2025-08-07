# Histórico de conversões
import glob
historico_pastas = []
ultima_pasta_saida = None

def carregar_historico():
    historico = []
    # Busca pastas em outputs e ascii_saida que começam com 'ASCII-'
    for base in ["outputs", "ascii_saida"]:
        base_path = os.path.abspath(base)
        if os.path.exists(base_path):
            for pasta in glob.glob(os.path.join(base_path, "ASCII-*")):
                if os.path.isdir(pasta):
                    historico.append(pasta)
    # Ordena por data extraída do nome da pasta (formato ASCII-DD-MM-YYYY)
    def extrai_data(pasta):
        nome = os.path.basename(pasta)
        try:
            return datetime.datetime.strptime(nome[6:], "%d-%m-%Y")
        except Exception:
            return datetime.datetime.min
    historico.sort(key=extrai_data, reverse=True)
    return historico

def abrir_pasta_saida():
    global ultima_pasta_saida
    pasta = ultima_pasta_saida if ultima_pasta_saida else os.path.abspath("outputs")
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    import subprocess
    subprocess.Popen(f'explorer "{pasta}"')
# interface_tk.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime
from ascii_to_image import processar_imagem_ascii
from ascii_video import extrair_frames_ascii

def selecionar_arquivo(tipo):
    filepath = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Arquivos de imagem ou vídeo", "*.jpg *.png *.mp4 *.avi")]
    )

    if not filepath:
        return

    global ultima_pasta_saida, historico_pastas
    import datetime
    data_str = datetime.datetime.now().strftime("%d-%m-%Y")
    if tipo == "imagem":
        pasta_nome = f"ASCII-{data_str}"
        pasta_saida = os.path.abspath(os.path.join("outputs", pasta_nome))
        ultima_pasta_saida = pasta_saida
        # Passa pasta_saida para a função de conversão
        processar_imagem_ascii(filepath, pasta_saida)
        historico_pastas.append(pasta_saida)
        messagebox.showinfo("Concluído", f"Imagem convertida com sucesso!\nPasta: {pasta_saida}")
    elif tipo == "video":
        pasta_nome = f"ASCII-{data_str}"
        pasta_saida = os.path.abspath(os.path.join("ascii_saida", pasta_nome))
        ultima_pasta_saida = pasta_saida
        extrair_frames_ascii(filepath, output_base_dir=pasta_saida)
        historico_pastas.append(pasta_saida)
        messagebox.showinfo("Concluído", f"Vídeo convertido com sucesso!\nPasta: {pasta_saida}")

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Conversor ASCII - Gabriel")
    janela.geometry("600x400")
    janela.resizable(False, False)
    janela.configure(bg="#222831")

    # Carrega histórico ao abrir o menu
    global historico_pastas
    historico_pastas = carregar_historico()

    def abrir_pasta_hist(pasta):
        import subprocess
        subprocess.Popen(f'explorer "{pasta}"')

    def mostrar_historico():
        hist_win = tk.Toplevel(janela)
        hist_win.title("Histórico de Conversões")
        hist_win.geometry("400x300")
        hist_win.configure(bg="#222831")
        tk.Label(hist_win, text="Histórico de Conversões", font=("Consolas", 14, "bold"), fg="#FFD369", bg="#222831").pack(pady=10)
        # Atualiza histórico antes de mostrar
        historico = carregar_historico()
        for pasta in historico[:10]:
            nome = os.path.basename(pasta)
            btn = tk.Button(hist_win, text=nome, font=("Consolas", 11), bg="#FFD369", fg="#222831", activebackground="#393E46", activeforeground="#FFD369", command=lambda p=pasta: abrir_pasta_hist(p))
            btn.pack(pady=4)

    # Atalhos de teclado
    janela.bind("<Control-i>", lambda e: selecionar_arquivo("imagem"))
    janela.bind("<Control-v>", lambda e: selecionar_arquivo("video"))
    janela.bind("<Control-o>", lambda e: abrir_pasta_saida())
    janela.bind("<Control-h>", lambda e: mostrar_historico())
    # Função para hover nos botões (exceto pasta)
    def on_enter(btn, bg, fg):
        btn.config(bg=bg, fg=fg)

    def on_leave(btn, bg, fg):
        btn.config(bg=bg, fg=fg)


    # Chuva de ASCII no fundo
    import random
    canvas = tk.Canvas(janela, width=600, height=400, bg="#222831", highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    ascii_chars = list("@%#*+=-:. ")
    drops = [random.randint(0, 600) for _ in range(40)]
    y_positions = [random.randint(-400, 0) for _ in range(40)]

    def chuva_ascii():
        canvas.delete("ascii")
        for i in range(len(drops)):
            x = drops[i]
            y = y_positions[i]
            char = random.choice(ascii_chars)
            canvas.create_text(x, y, text=char, fill="#FFD369", font=("Consolas", 16), tags="ascii")
            y_positions[i] += random.randint(8, 18)
            if y_positions[i] > 400:
                y_positions[i] = random.randint(-100, 0)
                drops[i] = random.randint(0, 600)
        canvas.after(60, chuva_ascii)
    chuva_ascii()

    titulo = tk.Label(janela, text="Conversor de Mídia para ASCII", font=("Consolas", 18, "bold"), fg="#FFD369", bg="#222831")
    titulo.pack(pady=18)

    frame_botoes = tk.Frame(janela, bg="#222831")
    frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

    botao_imagem = tk.Button(frame_botoes, text="Converter Imagem", width=28, height=2, font=("Arial", 13), bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", command=lambda: selecionar_arquivo("imagem"))
    botao_imagem.grid(row=0, column=0, padx=12, pady=12)
    botao_imagem.bind("<Enter>", lambda e: on_enter(botao_imagem, "#FFD369", "#222831"))
    botao_imagem.bind("<Leave>", lambda e: on_leave(botao_imagem, "#393E46", "#FFD369"))

    botao_video = tk.Button(frame_botoes, text="Converter Vídeo", width=28, height=2, font=("Arial", 13), bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", command=lambda: selecionar_arquivo("video"))
    botao_video.grid(row=1, column=0, padx=12, pady=12)
    botao_video.bind("<Enter>", lambda e: on_enter(botao_video, "#FFD369", "#222831"))
    botao_video.bind("<Leave>", lambda e: on_leave(botao_video, "#393E46", "#FFD369"))

    botao_pasta = tk.Button(frame_botoes, text="Abrir Pasta de Saída", width=28, height=2, font=("Arial", 13), bg="#FFD369", fg="#222831", activebackground="#393E46", activeforeground="#FFD369", command=abrir_pasta_saida)
    botao_pasta.grid(row=2, column=0, padx=12, pady=12)
    # Sem hover para o botão de pasta

    botao_hist = tk.Button(frame_botoes, text="Histórico de Conversões", width=28, height=2, font=("Arial", 13), bg="#FFD369", fg="#222831", activebackground="#393E46", activeforeground="#FFD369", command=mostrar_historico)
    botao_hist.grid(row=3, column=0, padx=12, pady=12)

    rodape = tk.Label(janela, text="Feito por gbzin | ASCII Converter", font=("Consolas", 10, "bold"), fg="#FFD369", bg="#222831")
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
