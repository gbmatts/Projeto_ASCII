# main.py

import os

from ascii_to_image import processar_imagem_ascii
from ascii_video import extrair_frames_ascii


def exibir_menu():
    """
    Exibe as opções do menu principal no terminal.
    """
    print("\n" + "=" * 50)
    print("        CONVERSOR ASCII - PROJETO PYTHON")
    print("=" * 50)
    print("1. Converter imagem para ASCII")
    print("2. Converter vídeo para ASCII")
    print("0. Sair")
    print("=" * 50)
       

def limpar_terminal():
    """
    Limpa o terminal para melhor visualização.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Função principal do programa. Gerencia o menu e chamadas.
    """
    while True:
        limpar_terminal()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            caminho = input("Digite o caminho da imagem (dentro de /assets): ").strip()
            caminho_completo = os.path.join("assets", caminho)
            if os.path.exists(caminho_completo):
                processar_imagem_ascii(caminho_completo)
            else:
                print("❌ Arquivo de imagem não encontrado.")
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            caminho = input("Digite o caminho do vídeo (dentro de /assets): ").strip()
            caminho_completo = os.path.join("assets", caminho)
            if os.path.exists(caminho_completo):
                extrair_frames_ascii(caminho_completo)
            else:
                print("❌ Arquivo de vídeo não encontrado.")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("\nEncerrando o programa... Até mais!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
