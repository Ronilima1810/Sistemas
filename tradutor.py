from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QHBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap, QBrush, QFont
from deep_translator import GoogleTranslator
import sys
import pygame
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def get_data_file_path(file_name):
    """Retorna o caminho correto do arquivo de dados dependendo se está rodando no PyInstaller ou não."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável gerado pelo PyInstaller
        return os.path.join(sys._MEIPASS, file_name)
    else:
        # Estamos no ambiente de desenvolvimento, então retornamos o caminho relativo
        return os.path.join(os.path.dirname(__file__), file_name)

class TradutorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tradutor de Arquivos")
        self.setGeometry(100, 100, 800, 600)

        # Configurar a imagem de fundo
        self.setAutoFillBackground(True)
        self.palette = QPalette()
        self.set_background()

        # Inicializar o mixer do pygame para som
        pygame.mixer.init()

        # Layout principal
        layout = QVBoxLayout()

        # Título
        titulo = QLabel("Tradutor de Arquivos")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Estilizando o título com a fonte Crowned (assumindo que está instalada ou fornecida)
        titulo.setStyleSheet("""
            color: black;
            margin: 20px 0;
        """)

        # Definir a fonte "Crowned" (caso esteja disponível no sistema ou seja fornecida)
        try:
            font = QFont("Crowned", 36)  # Definir tamanho 36 para a fonte
            titulo.setFont(font)
        except:
            print("Fonte 'Crowned' não encontrada, usando a fonte padrão.")

        # Seção de seleção de idiomas
        idioma_layout = QHBoxLayout()

        # Idioma de origem (em coluna)
        idioma_origem_layout = QVBoxLayout()
        idioma_origem_label = QLabel("Selecione o Idioma de entrada:")
        idioma_origem_label.setAlignment(Qt.AlignCenter)  # Centralizar o texto acima
        idioma_origem_layout.addWidget(idioma_origem_label)

        self.idioma_origem_var = QComboBox()
        self.idioma_origem_var.addItems(["auto", "en", "pt", "es", "fr", "de", "it", "ru", "ja", "zh"])
        self.idioma_origem_var.setFixedWidth(150)  # Reduzir o tamanho do menu suspenso
        self.idioma_origem_var.setStyleSheet("text-align: center;")  # Garantir que o texto fique centralizado
        idioma_origem_layout.addWidget(self.idioma_origem_var, alignment=Qt.AlignCenter)
        idioma_layout.addLayout(idioma_origem_layout)

        # Idioma de destino (em coluna)
        idioma_destino_layout = QVBoxLayout()
        idioma_destino_label = QLabel("Selecione o Idioma de saída:")
        idioma_destino_label.setAlignment(Qt.AlignCenter)  # Centralizar o texto acima
        idioma_destino_layout.addWidget(idioma_destino_label)

        self.idioma_destino_var = QComboBox()
        self.idioma_destino_var.addItems(["auto", "en", "pt", "es", "fr", "de", "it", "ru", "ja", "zh"])
        self.idioma_destino_var.setFixedWidth(150)  # Reduzir o tamanho do menu suspenso
        self.idioma_destino_var.setStyleSheet("text-align: center;")  # Garantir que o texto fique centralizado
        idioma_destino_layout.addWidget(self.idioma_destino_var, alignment=Qt.AlignCenter)
        idioma_layout.addLayout(idioma_destino_layout)

        layout.addLayout(idioma_layout)

        # Caixa de texto com fundo transparente e rolagem
        self.caixa_texto = QTextEdit(self)
        self.caixa_texto.setStyleSheet("background: rgba(255, 255, 255, 0.5); border: 1px solid gray;")
        layout.addWidget(self.caixa_texto)

        # Botões
        btn_layout = QHBoxLayout()

        btn_abrir = QPushButton("Abrir Arquivo")
        btn_abrir.clicked.connect(self.abrir_arquivo)
        btn_layout.addWidget(btn_abrir)

        btn_traduzir = QPushButton("Traduzir Arquivo")
        btn_traduzir.clicked.connect(self.traduzir_arquivo)
        btn_layout.addWidget(btn_traduzir)

        btn_salvar = QPushButton("Salvar Arquivo")
        btn_salvar.clicked.connect(self.salvar_arquivo)
        btn_layout.addWidget(btn_salvar)

        layout.addLayout(btn_layout)

        # Assinatura
        assinatura = QLabel("Criado por Roni o WB-DEV")
        assinatura.setAlignment(Qt.AlignCenter)
        layout.addWidget(assinatura)

        # Definindo o layout da janela
        self.setLayout(layout)

    def set_background(self):
        """Define o fundo para preencher a janela."""
        imagem_fundo = get_data_file_path("background.jpg")  # Usar o caminho obtido com get_data_file_path
        pixmap = QPixmap(imagem_fundo).scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(self.palette)

    def resizeEvent(self, event):
        """Redefine o fundo ao redimensionar a janela."""
        self.set_background()
        super().resizeEvent(event)

    def abrir_arquivo(self):
        options = QFileDialog.Options()
        arquivo, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Arquivos de Texto (*.txt);;Arquivos HTML (*.html);;Arquivos XML (*.xml);;Arquivos de Log (*.log);;Todos os Arquivos (*)", options=options)
        if arquivo:
            ext = arquivo.split('.')[-1].lower()
            
            try:
                if ext == "html":
                    # Para arquivos HTML, usamos BeautifulSoup para extrair o texto
                    with open(arquivo, 'r', encoding='utf-8') as file:
                        soup = BeautifulSoup(file, "lxml")
                        conteudo = soup.get_text()
                        self.caixa_texto.setPlainText(conteudo)
                
                elif ext == "xml":
                    # Para arquivos XML, usamos xml.etree.ElementTree para extrair o texto
                    with open(arquivo, 'r', encoding='utf-8') as file:
                        tree = ET.parse(file)
                        root = tree.getroot()
                        conteudo = "\n".join([elem.text for elem in root.iter() if elem.text])
                        self.caixa_texto.setPlainText(conteudo)
                
                elif ext == "log" or ext == "txt":
                    # Para arquivos de log ou texto simples
                    with open(arquivo, 'r', encoding='utf-8') as file:
                        conteudo = file.read()
                        self.caixa_texto.setPlainText(conteudo)

            except UnicodeDecodeError:
                # Tentar outra codificação caso a UTF-8 falhe
                try:
                    with open(arquivo, 'r', encoding='latin1') as file:
                        conteudo = file.read()
                        self.caixa_texto.setPlainText(conteudo)
                except Exception as e:
                    QMessageBox.warning(self, "Erro", f"Erro ao ler o arquivo: {str(e)}")
            except Exception as e:
                QMessageBox.warning(self, "Erro", f"Erro ao abrir o arquivo: {str(e)}")

    def traduzir_arquivo(self):
        idioma_origem = self.idioma_origem_var.currentText()
        idioma_destino = self.idioma_destino_var.currentText()

        if idioma_origem == idioma_destino:
            QMessageBox.warning(self, "Erro", "O idioma de origem e destino não podem ser iguais!")
            return

        conteudo = self.caixa_texto.toPlainText()
        if not conteudo:
            QMessageBox.warning(self, "Erro", "Nenhum conteúdo para traduzir!")
            return

        try:
            # Tradução em partes para evitar limites
            partes = [conteudo[i:i + 3000] for i in range(0, len(conteudo), 3000)]
            traducao = ""
            for parte in partes:
                traducao += GoogleTranslator(source=idioma_origem, target=idioma_destino).translate(parte)

            # Exibir a tradução na caixa de texto
            self.caixa_texto.setPlainText(traducao)

            # Reproduzir o som de conclusão da tradução
            self.tocar_audio('done_sound.mp3')  # Usando MP3 agora

        except Exception as e:
            QMessageBox.warning(self, "Erro durante a tradução", str(e))

    def salvar_arquivo(self):
        salvar_caminho, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Arquivos de Texto (*.txt);;Arquivos HTML (*.html);;Arquivos XML (*.xml);;Arquivos de Log (*.log);;Todos os Arquivos (*)")
        if salvar_caminho:
            conteudo = self.caixa_texto.toPlainText()
            ext = salvar_caminho.split('.')[-1].lower()
            
            if ext == "html":
                # Para salvar arquivos HTML, podemos encapsular o texto em uma estrutura básica de HTML
                with open(salvar_caminho, 'w', encoding='utf-8') as file:
                    file.write(f"<html><body>{conteudo}</body></html>")
                QMessageBox.information(self, "Arquivo Salvo", "Arquivo HTML salvo com sucesso.")
            
            elif ext == "xml":
                # Para salvar como XML, encapsulamos o conteúdo em uma estrutura XML
                root = ET.Element("root")
                ET.SubElement(root, "content").text = conteudo
                tree = ET.ElementTree(root)
                tree.write(salvar_caminho, encoding='utf-8', xml_declaration=True)
                QMessageBox.information(self, "Arquivo Salvo", "Arquivo XML salvo com sucesso.")
            
            else:
                # Para outros formatos, salvamos como texto simples
                with open(salvar_caminho, 'w', encoding='utf-8') as file:
                    file.write(conteudo)
                QMessageBox.information(self, "Arquivo Salvo", "Arquivo salvo com sucesso.")

    def tocar_audio(self, arquivo_audio):
        """Tocar um arquivo de áudio usando pygame."""
        try:
            som = get_data_file_path(arquivo_audio)
            pygame.mixer.music.load(som)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Erro ao tentar tocar o áudio: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TradutorApp()
    window.show()
    sys.exit(app.exec_())
