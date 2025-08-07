# ascii_image.py

import os
from PIL import Image
from ascii_utils import frame_to_ascii
from ascii_to_png import ascii_to_image
from ascii_to_html import ascii_to_html


def processar_imagem_ascii(caminho_imagem, pasta_saida=None, largura=120):
    """
    Converte uma imagem estática para arte ASCII e exporta nos formatos .txt, .png e .html.
    
    Parâmetros:
        caminho_imagem (str): Caminho para o arquivo da imagem.
        pasta_saida (str): Pasta de saída personalizada.
        largura (int): Largura em caracteres da arte ASCII. Padrão: 120.
    """
    try:
        # Abrindo a imagem com Pillow
        imagem = Image.open(caminho_imagem)
        nome_base = os.path.splitext(os.path.basename(caminho_imagem))[0]

        # Redimensionando proporcionalmente para largura padrão
        largura_original, altura_original = imagem.size
        proporcao = altura_original / largura_original
        nova_altura = int(largura * proporcao * 0.55)  # fator de ajuste para caracteres

        imagem = imagem.resize((largura, nova_altura))
        imagem = imagem.convert("RGB")  # Garante que tenha 3 canais

        # Obtém a lista de pixels e converte para ASCII
        from ascii_utils import pixels_to_ascii
        pixels = list(imagem.getdata())
        ascii_str = pixels_to_ascii(pixels, largura)

        # Pasta de saída personalizada ou padrão
        if pasta_saida is None:
            pasta_saida = os.path.join("outputs", nome_base)
        os.makedirs(pasta_saida, exist_ok=True)

        # Salvando .txt
        caminho_txt = os.path.join(pasta_saida, f"{nome_base}.txt")
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(ascii_str)
        print(f"✅ ASCII salvo como texto em: {caminho_txt}")

        # Salvando .png (imagem do ASCII)
        caminho_png = os.path.join(pasta_saida, f"{nome_base}.png")
        from ascii_to_png import ascii_to_image
        ascii_to_image(ascii_str, caminho_png, pixels=pixels)
        print(f"🖼️  ASCII salvo como imagem PNG em: {caminho_png}")

        # Salvando .html (colorido)
        caminho_html = os.path.join(pasta_saida, f"{nome_base}.html")
        from ascii_to_html import ascii_to_html
        ascii_to_html(ascii_str, caminho_html)
        print(f"🌐 ASCII salvo como HTML colorido em: {caminho_html}")

    except Exception as e:
        print(f"❌ Erro ao processar imagem: {e}")
