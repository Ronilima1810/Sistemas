Tradutor de Arquivos
Este projeto é uma aplicação de tradução de arquivos de texto, construída com PyQt5 para a interface gráfica e a API Google Translator para realizar as traduções. Ele permite que os usuários carreguem arquivos de texto com diversas extensões, traduzam o conteúdo para o idioma desejado e salvem o resultado em um novo arquivo. A aplicação também oferece suporte para reprodução de áudio para indicar a conclusão da tradução.

Funcionalidades
Suporte a múltiplos formatos de arquivo: Aceita arquivos de texto como .txt, .html, .log, .xml, e outros.
Seleção de idiomas: O usuário pode escolher o idioma de entrada e o idioma de saída para a tradução. Suporta vários idiomas, incluindo inglês, português, espanhol, francês, alemão, entre outros.
Tradução de grandes textos: A aplicação é capaz de traduzir textos com mais de 3 mil caracteres, dividindo automaticamente o conteúdo em partes menores para garantir a tradução eficiente.
Interface gráfica intuitiva: Utiliza PyQt5 para criar uma interface limpa e funcional, com elementos de interação como caixas de texto e botões.
Reprodução de áudio: Ao concluir a tradução, a aplicação reproduz um som para informar ao usuário que a operação foi concluída com sucesso.
Salvar arquivo traduzido: O arquivo traduzido pode ser salvo em seu formato original.
Como usar
Abrir um arquivo: Clique no botão "Abrir Arquivo" e selecione o arquivo de texto que deseja traduzir. O aplicativo suporta arquivos com as extensões .txt, .html, .log, .xml e outros.
Selecionar os idiomas: Selecione o idioma de origem e o idioma de destino para a tradução. A tradução automática será realizada com a ajuda da API Google Translator.
Traduzir o arquivo: Após carregar o arquivo e escolher os idiomas, clique em "Traduzir Arquivo". O conteúdo será traduzido e exibido na caixa de texto. A aplicação lida com textos maiores que 3 mil caracteres, dividindo-os em partes para tradução.
Salvar o arquivo traduzido: Clique em "Salvar Arquivo" para salvar o conteúdo traduzido em um novo arquivo de texto.
Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/tradutor-arquivos.git
Navegue até o diretório do projeto:

bash
Copiar
Editar
cd tradutor-arquivos
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o aplicativo:

bash
Copiar
Editar
python tradutor_app.py
Dependências
PyQt5: Para a interface gráfica.
pygame: Para a reprodução de áudio.
deep_translator: Para a tradução de texto utilizando a API do Google.
Você pode instalar as dependências utilizando o arquivo requirements.txt.

Contribuição
Contribuições são bem-vindas! Se você tiver melhorias, correções de bugs ou novos recursos que gostaria de adicionar, fique à vontade para abrir um pull request.

Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

