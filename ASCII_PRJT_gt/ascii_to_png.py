# ascii_to_png.py

from PIL import Image, ImageDraw, ImageFont
import os



def ascii_to_image(ascii_text, output_path, font_path=None, font_size=10, bg_color="black", font_color="white", pixels=None):
    """
    Converte texto ASCII em uma imagem PNG.
    Se pixels for fornecido, cada caractere será desenhado com a cor do pixel original.

    Parâmetros:
    - ascii_text: string contendo a arte ASCII
    - output_path: caminho completo para salvar a imagem PNG
    - font_path: caminho da fonte TTF (opcional)
    - font_size: tamanho da fonte
    - bg_color: cor do fundo
    - font_color: cor do texto
    - pixels: lista de tuplas RGB (opcional, para colorido)
    """

    lines = ascii_text.split("\n")
    max_width = max(len(line) for line in lines)
    height = len(lines)

    font = ImageFont.load_default() if font_path is None else ImageFont.truetype(font_path, font_size)

    bbox = font.getbbox("A")
    char_width = (bbox[2] - bbox[0]) * 1.6
    char_height = bbox[3] - bbox[1]
    image_width = int(char_width * max_width)
    image_height = int(char_height * height)

    image = Image.new("RGB", (image_width, image_height), color=bg_color)
    draw = ImageDraw.Draw(image)

    if pixels is not None:
        # Desenha cada caractere com a cor do pixel
        idx = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if idx < len(pixels):
                    color = pixels[idx]
                else:
                    color = font_color
                draw.text((j * char_width, i * char_height), char, font=font, fill=color)
                idx += 1
    else:
        # Escreve cada linha na imagem com cor única
        for i, line in enumerate(lines):
            draw.text((0, i * char_height), line, font=font, fill=font_color)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print(f"[✔] Imagem ASCII salva em: {output_path}")
