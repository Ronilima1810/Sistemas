# Lumus File Translator

**Aplicativo desktop Python com interface Qt de estilo corporativo.** Projeto de tradução de documentos com seleção de idiomas, visualização do conteúdo, exportação e feedback sonoro.

[Visualizar interface demonstrativa](https://ronilima1810.github.io/formulario-de-matricula/portfolio-demos/?demo=tradutor) · [Código-fonte](tradutor.py)

> O preview web usa textos fictícios para demonstrar a experiência de uso. Ele não carrega arquivos nem executa o motor de tradução real.

## Produto

A interface PyQt5 original foi modernizada, preservando a lógica do tradutor: tema escuro profissional, tipografia Segoe UI, áreas de edição, botões destacados, seleção de idiomas e responsividade básica da janela desktop.

## Tecnologia

- **GUI:** PyQt5 e QSS (Qt Style Sheets);
- **Tradução:** `deep-translator`, com serviço externo de tradução;
- **Manipulação:** Python padrão, XML, BeautifulSoup;
- **Áudio:** Pygame para aviso de conclusão;
- **Distribuição:** fonte Python e executável legado incluído como referência.

## Instalação e execução

No Windows, instale Python 3.10+ e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python tradutor.py
```

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python tradutor.py
```

**A aplicação real requer internet para o serviço de tradução.** Revise políticas de privacidade antes de enviar documentos reais a serviços de terceiros.

## Interface e segurança

O redesign mudou apresentação, espaçamentos, temas, bordas e hierarquia visual, sem substituir o algoritmo principal de abertura, tradução e gravação de arquivos. Não armazena senhas ou chaves neste repositório.

O arquivo `tradutor.exe` existente é um binário anterior: **não foi recompilado por este redesign**. Para obter o novo visual, execute `tradutor.py` ou faça um novo build do executável após validar as dependências.
