# QuetziLabsDashboard

*Lado Administrativo de QuetziLabs*

Requisito primordial es el contar con **Python 3.8**, debido a las versiones de las librerias que se utilizan

+ Antes de Correr este programa, es necesario instalar las librerias necesarias, esto escribiendo en la raiz del proyecto
```
pip install -r requeriments.txt
```

## Python 3.8.0
***

|   Nombre   |   pip install   |   version   |
|------|:----:|-----:|
|   Django   | django | 3.0.1 |
|PyJWT|pyjwt|1.7.1|
|MYSQL Client|mysqlclient|1.4.6|
### Execute apps' settings (views,models for databases,changes in settings.py,etc) [before running]
```
manage.py makemigrations
```
```
manage.py migrate
```

### Start server

**Windows**
```
manage.py runserver
```
**Linux**
```
python manage.py runserver
```
