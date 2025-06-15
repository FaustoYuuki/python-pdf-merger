#  Merger de PDFs em Python 🚀

Uma ferramenta de linha de comando simples para unir múltiplos arquivos PDF em um único documento. O projeto foi desenvolvido para ser fácil de usar, tanto para usuários finais (via um executável) quanto para outros desenvolvedores.

## ✨ Funcionalidades

-   Une todos os arquivos PDF localizados na mesma pasta do script/executável.
-   Gera um arquivo de saída chamado `PDF_Unificado.pdf`.
-   Disponível como um script Python ou um executável `.exe` para Windows.

---

## 👨‍💻 Para Desenvolvedores (Usando o Script `.py`)

Se você deseja executar o projeto a partir do código-fonte, siga os passos abaixo.

**Pré-requisitos:**
* Python 3.x instalado.
* Git (opcional, para clonar).

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
```

**2. Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Execute:**
Coloque os PDFs que deseja unir na pasta e rode o script:
```bash
python main.py
```

---

## 👩‍💼 Para Usuários Finais (Usando o `.exe`)

A maneira mais fácil de usar, sem precisar instalar Python.

1.  Vá para a seção de **[Releases](https://github.com/FaustoYuuki/python-pdf-merger/releases)** deste repositório.
2.  Baixe o arquivo `JuntarPDFs.exe` da versão mais recente.
3.  Coloque o arquivo `JuntarPDFs.exe` na mesma pasta onde estão os seus arquivos PDF.
4.  Dê um duplo clique no `JuntarPDFs.exe`.
5.  Aguarde a mensagem de sucesso. O arquivo `PDF_Unificado.pdf` será criado na mesma pasta.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
