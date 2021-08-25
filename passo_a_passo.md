COMO UTILIZAR O CRUD:
1 - abre o terminal através do atalho:
ctrl+alt+t

2 - acessa a pasta através do atalho:
C:\Users\Acer>cd desktop/python-prova/ex_3

3 - acessa a máquina virtual:
C:\Users\Acer\Desktop\prova-python\ex_3>cd virtual/Scripts

4 - ativa a máquina virtual:
C:\Users\Acer\Desktop\prova-python\ex_3\virtual\Scripts>activate

5- retorna para o diretório ex_3 com a máquiva virtual ativada utilizando:
(virtual) C:\Users\Acer\Desktop\prova-python\ex_3\virtual\Scripts>cd ..
(virtual) C:\Users\Acer\Desktop\prova-python\ex_3\virtual>cd ..
(virtual) C:\Users\Acer\Desktop\prova-python\ex_3>

6- cria ao banco de dados usando:
(virtual) C:\Users\Acer\Desktop\prova-python\ex_3>python manage.py migrate

7- roda o programa usando:
(virtual) C:\Users\Acer\Desktop\prova-python\ex_3>python manage.py runserver

8 - acessa através da porta local host copiando o código abaixo em um browser:
http://127.0.0.1:8000/
