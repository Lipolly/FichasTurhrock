### Documentos Turhrock
Este é um programa simples para criar e gerenciar um banco de dados de magias para um jogo de RPG.

#Funcionalidades
O programa permite a adição de novas magias e sua posterior impressão em um documento PDF formatado, bem como a busca por magias específicas no banco de dados.

#Instalação
Antes de executar o programa, certifique-se de ter o Python 3 e os seguintes pacotes instalados:

    sqlite3
    pylatex

Para instalar o pylatex, você pode utilizar o seguinte comando:

__pip install pylatex__

#Como usar
Ao executar o programa, você terá acesso a um menu com as seguintes opções:

    __Adicionar nova magia__
    __Imprimir todas as magias em um documento PDF__
    __Procurar magia__
    __Sair__

Para adicionar uma nova magia, selecione a opção 1 no menu e insira as informações solicitadas. Ao final, a nova magia será adicionada ao banco de dados.

Para imprimir todas as magias em um documento PDF, selecione a opção 2. O documento será salvo na pasta bin com o nome Grimorio.pdf.

Para procurar uma magia específica, selecione a opção 3 e digite o nome da magia desejada. O programa exibirá as informações da magia encontrada.
Estrutura do código

O código consiste em um arquivo principal magias.py e um arquivo auxiliar init.py. O arquivo magias.py contém as funções para adicionar, imprimir e procurar magias.

As magias são armazenadas em um banco de dados SQLite, cujo nome é magias.db. As informações de cada magia são armazenadas em uma tabela magias.

O documento PDF é criado utilizando a biblioteca pylatex, que permite criar e editar arquivos LaTeX de maneira programática.
