# ascii_video.py

import cv2
import os
from ascii_utils import frame_to_ascii
from ascii_to_html import ascii_to_html
from datetime import datetime

# Tamanho fixo dos frames para padronizar a saída (evita erros)
FRAME_WIDTH = 120
FRAME_HEIGHT = 60

def extrair_frames_ascii(video_path, output_base_dir="ascii_saida", salvar_html=False):
    """
    Extrai os frames de um vídeo, converte para ASCII e salva em arquivos .txt.
    Opcionalmente, também salva em formato HTML.

    Parâmetros:
    - video_path: caminho do vídeo de entrada
    - output_base_dir: diretório base onde os frames serão salvos
    - salvar_html: se True, também salva cada frame como HTML estilizado
    """
    # Validação de entrada
    if not os.path.isfile(video_path):
        print(f"[ERRO] Vídeo não encontrado: {video_path}")
        return

    # Abre o vídeo com OpenCV
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"[ERRO] Não foi possível abrir o vídeo: {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"[INFO] Total de frames a processar: {total_frames}")

    # Cria pasta de saída personalizada ou padrão
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir, exist_ok=True)

    contador = 0

    while True:
        sucesso, frame = cap.read()
        if not sucesso:
            break

        # Redimensiona todos os frames para o mesmo tamanho
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

        # Converte o frame em arte ASCII
        ascii_art = frame_to_ascii(frame)

        # Salva como arquivo de texto
        nome_txt = os.path.join(output_base_dir, f"frame_{contador:04}.txt")
        with open(nome_txt, "w", encoding="utf-8") as f:
            f.write(ascii_art)

        # (Opcional) Salva também como HTML estilizado
        if salvar_html:
            nome_html = os.path.join(output_base_dir, f"frame_{contador:04}.html")
            ascii_to_html(ascii_art, nome_html)

        contador += 1

    cap.release()
    print(f"[✔] Conversão finalizada. Total de frames salvos: {contador}")
    print(f"[📁] Frames salvos na pasta: {output_base_dir}")
