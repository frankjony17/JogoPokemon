# JogoPokemon

For Django python 3.6:
1.  cd JogoPokemon/postgresql
2.  sudo docker-compose up --build  
3.  cd JogoPokemon/DjangoRestApiPostgreSQL
4.  python3.6 -m venv pokemon-venv
5.  source pokemon-venv/bin/activate  
6.  pip install djangorestframework==3.11.0 django-cors-headers==3.4.0 psycopg2-binary==2.8.5 PyYAML==5.3.1
7.  python manage.py makemigrations pokemon
8.  python manage.py migrate pokemon
9.  python manage.py loaddata tipofixtures
10. python manage.py runserver 8080

For VueClientJogoPokemon (ts):
1. sudo npm i -g @vue/cli
3. cd freelance/JogoPokemon/VueClientJogoPokemon
4. npm install
5. npm run serve
