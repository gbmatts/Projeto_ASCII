# ascii_to_html.py

import os


def ascii_to_html(ascii_text, output_path, font_color="#FFFFFF", bg_color="#000000", font_family="Courier New", font_size="12px"):
    """
    Converte uma string ASCII em um arquivo HTML estilizado.

    Parâmetros:
    - ascii_text: string contendo a arte ASCII
    - output_path: caminho do arquivo HTML de saída
    - font_color: cor do texto (em hexadecimal)
    - bg_color: cor de fundo (em hexadecimal)
    - font_family: fonte usada no HTML (monoespaçada recomendada)
    - font_size: tamanho da fonte
    """

    html_template = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>ASCII Art</title>
    <style>
        body {{
            background-color: {bg_color};
            color: {font_color};
            font-family: '{font_family}', monospace;
            font-size: {font_size};
            white-space: pre;
            margin: 20px;
        }}
    </style>
</head>
<body>
<pre>
{ascii_text}
</pre>
</body>
</html>
"""

    # Garante que a pasta existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Salva o arquivo HTML
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"[✔] HTML ASCII salvo em: {output_path}")
