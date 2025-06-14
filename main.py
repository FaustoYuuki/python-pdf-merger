import os
import sys
from PyPDF2 import PdfMerger

NOME_ARQUIVO_SAIDA = "PDF_Unificado.pdf"

def obter_diretorio_script():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))

def unir_pdfs():
    try:
        diretorio = obter_diretorio_script()
        print(f"Procurando por PDFs na pasta: {diretorio}\n")

        lista_pdfs = [
            arquivo for arquivo in os.listdir(diretorio)
            if arquivo.lower().endswith(".pdf")
        ]

        if NOME_ARQUIVO_SAIDA in lista_pdfs:
            lista_pdfs.remove(NOME_ARQUIVO_SAIDA)
        lista_pdfs.sort()

        if not lista_pdfs:
            print("AVISO: Nenhum arquivo PDF foi encontrado para unir.")
        else:
            print("Iniciando a união dos seguintes arquivos (em ordem):")
            for pdf in lista_pdfs:
                print(f"  -> {pdf}")

            merger = PdfMerger()

            for pdf in lista_pdfs:
                caminho_completo = os.path.join(diretorio, pdf)
                merger.append(caminho_completo)

            caminho_saida = os.path.join(diretorio, NOME_ARQUIVO_SAIDA)
            merger.write(caminho_saida)
            merger.close()

            print("\n----------------------------------------------------")
            print(f"✅ SUCESSO! Arquivos unidos em: {NOME_ARQUIVO_SAIDA}")
            print("----------------------------------------------------")

    except Exception as e:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"❌ OCORREU UM ERRO:")
        print(e)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Verifique se os PDFs não estão corrompidos ou protegidos por senha.")

    finally:
        print("\nPressione ENTER para fechar esta janela.")
        input()

if __name__ == "__main__":
    unir_pdfs()