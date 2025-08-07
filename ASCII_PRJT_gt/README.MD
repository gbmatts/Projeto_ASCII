# Conversor de Mídia para ASCII 

Transforme suas imagens e vídeos em arte ASCII colorida com apenas alguns cliques ou comandos! Este projeto em Python faz mágica: converte qualquer mídia em texto estiloso, HTML colorido e PNG colorido automaticamente. Sim, até o PNG fica colorido igual ao original!

## O que esse projeto faz?

- Converte vídeos em frames ASCII (cada frame vira arte!)
- Converte imagens estáticas em ASCII
- Exporta tudo para:
  - Texto (`.txt`)
  - HTML colorido (`.html`)
  - PNG colorido (`.png`)
- Organiza os resultados em pastas automáticas
- Tem interface gráfica (Tkinter) e modo terminal (CLI)

## Estrutura do Projeto

```
ASCII_PRJT/
├── ascii_image.py         # Conversão de imagens
├── ascii_video.py         # Conversão de vídeos
├── ascii_to_html.py       # Renderização em HTML
├── ascii_to_png.py        # Renderização em PNG colorido
├── ascii_utils.py         # Funções utilitárias (pixels, ASCII, escala)
├── interface_tk.py        # Interface gráfica
├── main.py                # Menu de terminal
├── requirements.txt       # Bibliotecas necessárias
├── outputs/               # Resultados gerados
└── README.md              # Você está aqui!
```

## Como usar rapidinho

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ascii_converter.git
   cd ascii_converter
   ```
2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode a interface gráfica:
   ```bash
   python interface_tk.py
   ```
5. Ou use o terminal:
   ```bash
   python main.py
   ```

## Principais dependências

```
opencv-python
Pillow
numpy
```

## Observações legais

- PNG gerado é colorido automaticamente, igual ao original!
- Os resultados vão para a pasta `outputs/`, organizados por nome de arquivo.
- O código é todo comentado e fácil de entender.
- Aceita imagens e vídeos populares (JPG, PNG, MP4, AVI...)
- Se der erro, confira se instalou as dependências e se o arquivo existe.

---

Converte a porra toda pra ASCII. VUMBORA!
