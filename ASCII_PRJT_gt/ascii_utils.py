# Função para converter lista de pixels (imagem estática Pillow) em ASCII
def pixels_to_ascii(pixels, largura):
    """
    Converte uma lista de pixels (RGB) em arte ASCII, respeitando a largura.

    Parâmetros:
    - pixels: lista de tuplas (R, G, B)
    - largura: largura da imagem em caracteres

    Retorna:
    - string com arte ASCII
    """
    ascii_str = ""
    for i in range(0, len(pixels), largura):
        linha = pixels[i:i+largura]
        for pixel in linha:
            ascii_str += pixel_to_ascii(pixel)
        ascii_str += "\n"
    return ascii_str
# ascii_utils.py

import cv2

# Mapeamento de tons de cinza para caracteres ASCII, do mais escuro ao mais claro
ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(pixel):
    """
    Converte um pixel RGB em um caractere ASCII baseado na intensidade de brilho.

    Parâmetros:
    - pixel: tupla (R, G, B)

    Retorna:
    - caractere ASCII correspondente
    """
    r, g, b = pixel
    # Calcula a intensidade média (tom de cinza)
    intensidade = int((r + g + b) / 3)

    # Normaliza o índice para o tamanho da lista de caracteres
    index = int(intensidade / 255 * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[index]


def frame_to_ascii(frame):
    """
    Converte um frame (imagem RGB ou BGR) para uma string ASCII.

    Parâmetros:
    - frame: matriz da imagem (NumPy array)

    Retorna:
    - string com arte ASCII
    """
    # Converte para RGB se estiver em BGR (padrão OpenCV)
    if len(frame.shape) == 3:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame_rgb = frame

    altura, largura, _ = frame_rgb.shape
    ascii_str = ""

    # Itera linha por linha, pixel por pixel
    for y in range(altura):
        for x in range(largura):
            pixel = frame_rgb[y, x]
            ascii_str += pixel_to_ascii(pixel)
        ascii_str += "\n"

    return ascii_str
