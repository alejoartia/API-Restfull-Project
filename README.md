# TestQuick

## Setup

lo primero es clonar el repositorio

```sh
$ git clone https://github.com/AlejandroCordobaM/TestQuick.git
$ cd TestQuick
```
crear el entorno virtual para instalar las dependencias dentro y activarlo

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate

´´´en linux:
$ python3 -m venv.env
$ source ../. env/bin/activate
```

despues instalar las dependencias 

(env)$ pip install -r requirements.txt

http://127.0.0.1:8000/Testquick/

o en su defecto correr el comando :  $python3 manage.py runserver 
(dentro del directorio del proyecto)


NOTA: en caso de que las migraciones no ejecuten correr los siguiente comandos
//genera el archivo de migraciones: $python manage.py makemigrations            
//ejecuta las migraciones en la bd: $python manage.py migrate                    


## para django admin 
$ http://localhost:8000/admin/

de .models fueron importadas Person, Clients, Products, Bills, BillProducts

admin.site.register(Person)
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Bills)
admin.site.register(BillProducts)

esto con el fin de actualizar las tablas y gestionarlas desde django admin


-------------------------------------------------------------------

# LETS' GO INSIDE

## 1) ENDPOINT PARA CREACION(registro) DE USUARIOS

*El enpoint es:*
 $ http://localhost:8000/api/create_user/1.0/

se puede probar la creacion de usuarios con el siguiente jSON :
nota: no olvide modificar los valores debido a que ese usuario ya esta creado
{
    "first_name": "Alejandro",
    "last_name": "cordoba",
    "username": "Back_developer",
    "email": "alejo.art@gmail.com",
    "password": 12345667
}


## 2) ENDPOINT QUE PERMITE INICIAR SESION CON JSON Web Token.

Para hacer login recuerde que debe estar deslogeado,se realizo un form para hacer mas facil el log sin embargo se puede hacer mediante una peticion HTTP

recuerde si no se encuentra logeado no podra acceder a las rutas de clientes, productos, bill
ya que no tendra el JSON Web Token

*El endpoint es:*

$ http://localhost:8000/login/

el usuario que puede usar para probar es:

    Username: alejandro
    password: 12345678

Nota: en su defecto crear otro usuario

En caso de estar logeado y se necesita deslogear se puede usar el siguiente endpoint:

$ http://localhost:8000/logout/  


## 3) LOS ENDPOINTS ESTAN ASEGURADOS (GENERAR TOKEN)

Aunque cada vez que se logea un usuario el siguiente enpoint permite generar un token
dependiendo el usuario.

$ http://localhost:8000/api_generate_token/


con metodo post se puede probar 
se puede cambiar los valores

        {
            "username": "alejandro",
            "password": "12345678"
        }


## CONSULTA DE PRODUCTOS, CLIENTES Y BILLS 


La relacion de la base de datos se documenta en el siguiente archivo:
$ DATABASE.txt 
dentro del repositorio 


Se puede usar un gestor de peticiones HTTP pero si pone el enpoint en el navegador sera capaz de enviar las peticiones desde alli debido al gestor de django, se crearon vistas basadas en clases para cada uno de estos.



### client:

Para crear o consultar clientes se puede usar el siguiente endopoint

$ http://localhost:8000/client/

ejemplo para enviar HTTP json,  recuerde quitar id( se crea automaticamente)
NOTA: recuerde cambiar los campos ya que estos ya estan creados 

    {
        "id": 1,
        "document": "1122654214",
        "first_name": "rosa",
        "last_name": "martinez",
        "email": "defef",
        "created_on": "2021-09-08",
        "update_at": "2021-09-08"
    }


### product:

Para crear o consultar productos  se puede usar el siguiente end point

$ http://localhost:8000/products/

ejemplo para enviar HTTP json,  recuerde quitar id( se crea automaticamente)
NOTA: recuerde cambiar los campos ya que estos ya estan creados 

    {
        "id": 1,
        "name": "85",
        "description": "sa",
        "price": 1200.0,
        "stock": 5,
        "created_on": "2021-09-08",
        "update_at": "2021-09-08"
    },

### bill:

para crear o consultar la factura se puede usar el siguiente end point:

$ http://localhost:8000/bills/

ejemplo para enviar HTTP json,  recuerde quitar id( se crea automaticamente)
NOTA: recuerde cambiar los campos ya que estos ya estan creados 


    {
        "id": 1,
        "client_id": 1,
        "company_name": "Seaboard",
        "nit": 42515481523,
        "code": "24",
        "created_on": "2021-09-08",
        "update_at": "2021-09-08"
    }



### bill products:

para crear o consultar la factura detallada se puede usar el siguiente end point:

$ http://localhost:8000/bills/products/

ejemplo para enviar HTTP json,  recuerde quitar id( se crea automaticamente)
NOTA: recuerde cambiar los campos ya que estos ya estan creados 

en bills products se recomienda usar el form ya que este detail se crea con llave foranea lo que quiere decir que se crea sin necesidad de enviar la peticion con JSON 


SIN EMBARGO SE DEJA EL EJEMPLO:
    
    
    {
        "id": 1,
        "bill_id": 1,
        "product_id": 1,
        "created_on": "2021-09-08",
        "update_at": "2021-09-08"
    }



## END POINTS DE CARGA DE ARCHIVO CSV 

En este punto el endpoint es el siguiente: 

$ http://localhost:8000/client/file

se creo un metodo que permite leer el archivo que se encuentra en la carpeta del proyecto

$ clients.csv

                    @api_view(['GET','POST'])
                    def saveClients(request):
                           file = request.FILES['clients']
                           request.readFile(file)
                           return JsonResponse('test', safe=False)

                    def readFile(file):
                           results = []
                           with open(str(file)) as File:
                               reader = csv.DictReader(File)
                               for row in reader:
                                   results.append(row)
                               print(results)
                               print(json.dumps(results))

            
este recibe el archivo, lo lee y lo transforma a formato JSON sin embargo aun no carga a CLIENTES, pero queda estructurado para finalizar la carga y luego la descarga de un archivo CSV 



________________________________________________________________________________________________________________________________________


## CONFIGURACION Y ESQUEMA DE BASES DE DATOS 


En este proyecto o prueba se uso la base de datos por defecto:

           DATABASES = {
               'default': {
                   'ENGINE': 'django.db.backends.sqlite3',
                   'NAME': BASE_DIR / 'db.sqlite3',
               }
           }


sin embargo si se quiere usar otra con Postgrest se recomienda:



            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'test',
                    'USER':'postgres',
                    'PASSWORD':'ROOT',
                    'HOST':'localhost',
                    'PORT':'5432'

                }
            }

## EL SIGUIENTE ES EL SCRIPT SQL PARA GENERAR LA BASE DE DATOS EN CASO DE NECESITARSE 
NOTA: DENTRO DEL REPOSITORIO HAY UNA IMAGEN CON EL ESQUEMA Y LAS RELACIONES DE LA BASE DE DATOS 

            CREATE DATABASE TEST;

            CREATE table IF NOT EXISTS clients (
            id serial PRIMARY KEY,
            document VARCHAR (50) UNIQUE NOT NULL,
            first_name VARCHAR (200) NOT NULL,
                last_name VARCHAR (200) NOT NULL,
            email VARCHAR (255) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT null DEFAULT now(),
            update_at TIMESTAMP NOT null DEFAULT now());

            CREATE table IF NOT EXISTS bills (
            id serial PRIMARY KEY,
            client_id INT NOT NULL,
            company_name VARCHAR (200) NOT NULL,
                nit INT NOT NULL,
            code VARCHAR (255) UNIQUE NOT NULL,
            created_on TIMESTAMP NOT null DEFAULT now(),
            update_at TIMESTAMP NOT null DEFAULT now(),
            FOREIGN KEY (client_id)
                  REFERENCES clients (id)
            );

            CREATE table IF NOT EXISTS products (
            id serial PRIMARY KEY,
            name VARCHAR (100) NOT NULL,
            description VARCHAR (250),
            price FLOAT4 NOT NULL,
                stock INT NOT NULL,
            created_on TIMESTAMP NOT null DEFAULT now(),
            update_at TIMESTAMP NOT null DEFAULT now());


            CREATE table IF NOT EXISTS billProducts (
            id serial PRIMARY KEY,
            bill_id INT NOT NULL,
            product_id INT NOT NULL,
            created_on TIMESTAMP NOT null DEFAULT now(),
            update_at TIMESTAMP NOT null DEFAULT now(),
            FOREIGN KEY (bill_id)
                  REFERENCES bills (id),
                FOREIGN KEY (product_id)
                  REFERENCES products (id));

            ---Poblado de datos incial

             INSERT INTO public.clients
            (id, "document", first_name, last_name, email, created_on, update_at)
            VALUES(1, '123654789', 'Alejandro', 'cordoba', 'prueba@gmail.com', '2021-09-06 23:52:22.446', '2021-09-06 23:52:22.446');


            INSERT INTO public.products
            (id, "name", description, price, stock, created_on, update_at)
            VALUES(1, 'papa', 'papas de pollo', 1500.0, 3, '2021-09-07 00:26:58.869', '2021-09-07 00:26:58.869');
            INSERT INTO public.products
            (id, "name", description, price, stock, created_on, update_at)
            VALUES(2, 'arroz', 'arroz del llano', 2000.0, 5, '2021-09-07 00:27:23.654', '2021-09-07 00:27:23.654');


             INSERT INTO public.bills
            (id, client_id, company_name, nit, code, created_on, update_at)
            VALUES(1, 1, 'yayas', 123456987, '1', '2021-09-07 00:28:02.365', '2021-09-07 00:28:02.365');


            INSERT INTO public.billsproducts
            (id, bill_id, product_id, created_on, update_at)
            VALUES(1, 1, 1, '2021-09-07 00:28:20.699', '2021-09-07 00:28:20.699');
            INSERT INTO public.billsproducts
            (id, bill_id, product_id, created_on, update_at)
            VALUES(2, 1, 2, '2021-09-07 00:28:20.699', '2021-09-07 00:28:20.699');


