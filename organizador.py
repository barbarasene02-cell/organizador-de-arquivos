import os
import shutil

PASTA = "downloads_teste"


def criar_arquivos_de_teste():
    os.makedirs(PASTA, exist_ok=True)
    nomes = [
        "relatorio.pdf", "contrato.pdf",
        "planilha.xlsx", "notas.txt",
        "foto.jpg", "logo.png",
        "apresentacao.pptx", "musica.mp3",
    ]
    for nome in nomes:
        caminho = os.path.join(PASTA, nome)
        if not os.path.exists(caminho):
            open(caminho, "w").close()


def organizar_arquivos():
    contagem = {}

    for nome in os.listdir(PASTA):
        caminho_origem = os.path.join(PASTA, nome)

        if not os.path.isfile(caminho_origem):
            continue

        extensao = os.path.splitext(nome)[1].lower().lstrip(".")
        if extensao == "":
            extensao = "sem_extensao"

        pasta_destino = os.path.join(PASTA, extensao)
        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(caminho_origem, os.path.join(pasta_destino, nome))

        contagem[extensao] = contagem.get(extensao, 0) + 1

    print("Arquivos organizados:")
    for extensao, total in sorted(contagem.items()):
        print(f"  {extensao}: {total} arquivo(s)")


if __name__ == "__main__":
    criar_arquivos_de_teste()
    organizar_arquivos()