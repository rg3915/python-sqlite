python-sqlite
=============

Conteúdos sobre a manipulação de banco de dados SQLite3 em Python.

Leia o artigo [Gerenciando banco de dados SQLite3 com Python - Parte 1][0] e [Parte 2][4].

## Intermediario

A [parte 2][4] ensina como manipular banco de dados SQLite utilizando várias *classes* num **único** arquivo python, no caso estou usando o **Python3**. Mas funciona também no Python 2x.

Aqui usamos recursos mais sofisticados, um script para **gerar valores randômicos** para popular o banco e importação de dados externos em **csv**.

Veja no *requirements.txt* que eu usei os pacotes [names][2] (only Python<=3.3) e [rstr][3], o primeiro gera nomes randômicos e o segundo gera string e números randômicos.

### Configurando um VirtualEnv para Python 3

Não é obrigatório, mas como eu tenho no meu SO o Python 3.4, tive que criar um virtualenv, que se configura da seguinte forma:

Faça um clone deste repositório

``$ git clone https://github.com/rg3915/python-sqlite.git``

Crie o virtualenv com o nome **python-sqlite**

``$ virtualenv python-sqlite``

Habilite o python3

``$ virtualenv -p /usr/bin/python3 python-sqlite``

Vá para a pasta

``$ cd python-sqlite``

Ative o ambiente

``$ source bin/activate``

Seu prompt ficará assim (ou parecido)

``(python-sqlite)~/git/python-sqlite$ ``

Instale as dependências

``$ pip install -r requirements.txt``

Entre na pasta

``$ cd intermediario``

Agora vamos diminuir o caminho do prompt

``PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ "``

O prompt vai ficar assim:

``(python-sqlite):/intermediario$ ``

### Rodando a aplicação

Lendo a [parte 2][4] do artigo você verá que para rodar a aplicação basta executar

``$ python3 manager_db.py``

**Nota**: O arquivo ``manager_db_.py`` é o original. Se quiser pode renomeá-lo.

[0]: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
[2]: https://github.com/treyhunner/names
[3]: https://pypi.python.org/pypi/rstr/2.1.3
[4]: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html