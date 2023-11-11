![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/5fd86533-2836-4112-9998-8ba7aaec9049)![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/7f6fce6e-e487-4851-aef9-5695ebb04dd8)# Bienvenidos al grupo 10 de desarrollo de software en la nube

### Integrantes

* Kevin Alexander Maldonado Delgado
* Jorge A. Romero Gutierrez
* Andres Esteban Silva Sanchez
* Luisa Johana Torres Moncano

Nuestra aplicación conversor esta diseñada para convertir archvios de video de estas tres extensiones .mp4, .webm y .avi

# Pasos para ejecutar nuestra aplicación en docker

### Requerimento
* Docker intalado: usualmente se instala instalando Docker Desktop https://docs.docker.com/desktop/install/windows-install/
* Git
* Postman

### Paso a paso

1. Creamos un folder en nuestro computador en el cual clonaremos nuestro proyecto, la ubicación de este folder puede ser la de nuestra preferencia
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/6645c331-94b3-4bc9-aeb0-f7b79d2e4bc8)

2. Usando el cmd o el powershell nos situamos en dicho folder y ejecutamos el comando **git clone https://github.com/kevin96uniandes/MISO2023-desarrollo-nube.git** , y esperamos a que el proyecto este clonado
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/4895f175-9bf2-4a2d-8706-8e24eea128bc)

3. Navegamos al folder principal de nuestra aplicación dentro del folder creado el cual deberia llamarse MISO2023-desarrollo-nube

4. En esta carpeta ejecutamos el comando docker-compose build
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/17353644-26b5-4850-8579-84846ba38e8d)

5. En esta misma carpeta ejecutamos el comando docker-compose up
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/0b34f96c-cf3c-4813-bac2-94d5c6f45a4e)

6. Si tenemos instalado Dcoker Compose, podemos ver en la pantalla principal **Containers** podamos ver en verde los contenedores MISO2023-desarrollo-nube
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/2f4b6cd4-4672-4554-ada5-8201b92d414d)

7. Abrimos postman en la sección de collections
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/aebe30a3-4868-419a-af7e-f9455683ca01)

8. Descargamos el archivo [coleccion postman](https://uniandes-my.sharepoint.com/:u:/g/personal/k_maldonadod_uniandes_edu_co/EcDKlsE6RONBuZCx2JQjUA0BJnTNtBwUAat8os7LTxnC3Q?e=2xVQ6N), hacemos click en import
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/4cbcd45a-ab17-411e-b599-a616a6ecd7f4)
 
9. Importamos el archivo descargado en el paso 8 "CICLO || -CLOUD.postamn_collection.json"

10. Una vez importado, deberiamos ver los siguientes servicios documentados
    
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/4631394e-4ea7-4131-824f-3a6e01558bda)

11. Procedemos a ejecutar cada servicio, cada servicio tiene configurado su endpoint, request requerida, solo es reemplazar lso datos en la request, parra falcilitar las pruebas, hemos adjuntado estos tres archivos de pruebae un archivo .zip que debe descomprimir [datos de prueba](https://uniandes-my.sharepoint.com/:u:/g/personal/k_maldonadod_uniandes_edu_co/ETTY7tAoSCNHlsqK7etI_iABK1YTLLGJXzXRgRcwIVgCDQ?e=h7tl6r), si deseas mas información de cada uno de lso servicios, pouedes ir a la sección de wiki -> [Documentación servicios de la aplicación](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/wiki/Documentacion-servicios)

# Pasos para ejecutar nuestra aplicación en GCP

1. Entramos al proyecto creado en Google Cloud GCP
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/4c3e649c-8e72-45d4-a298-090e058bc4e5)

2. Abrimos la consola ssh tanto para la maquina **maquina virtual worker** como la maquina **maquina virtual flask**

maquina virtual worker
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/3ec97205-4851-4d80-8ffe-06566f957b79)

maquina virtual flask
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/8b96c369-8526-4ca4-861b-b78876954312)

3. Ejecutamos el comando **sudo docker pull kevin9612/miso2023-desarrollo-nube-celery-worker** en la **maquina virtual worker**, esta imagen representa nuestro contenedor en Celery 

maquina virtual worker
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/3ec97205-4851-4d80-8ffe-06566f957b79)

4. Ejecutamos el comando **kevin9612/miso2023-desarrollo-nube-flask-app** en la **maquina virtual flask**, esta imagen representa nuestras APIS de flask

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/8b96c369-8526-4ca4-861b-b78876954312)

5. Ejecutamos los comandos *sudo docker compose up --build* en ambas maquinas

maquina virtual worker
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/ca68c9c9-fe4c-43b8-92f0-6db0a573cc5c)

maquina virtual flask
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/2ee818a0-9e38-45ec-9db4-54b24a9b41e1)

6. Ejecutamos en postman 

NOTA: las maquinas estan apagadas para no consumir los creditos

# Pasos para crear balanceador de carga y grupo de instancias en GCP

1. Creamos una imagen de un disco el cual tenga instalado previamente docker y docker-compose
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/51898bdd-f928-4895-8c6d-35959bf04cc2)

2. Creamos una imagen en base a este disco
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/bcd81543-3fa5-4315-8fce-f735780c4c16)

3. Creamos un image template para asociar al grupo de instancias, el disco de esta instancia debe ser creado en base a la imagen crada anteriormente 

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/ed192809-fb21-44d9-8bf7-0579fa210dc1)

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/b57156c1-c8d3-40eb-98ee-33c66c75c294)

4. Creamos un grupo de instancias el cual le asociamos nuestro template, y definimos que escale agregando y quitando instancias dinamicamente cuando la CPU sobrepase los 40%

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/b94fa95c-39ab-46d8-bd01-698b09660c75)

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/dae0cbc1-fff7-4ec8-9900-b905baac3162)

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/aea1d861-4d0c-4ca5-a786-cb9bc976444c)

5. Creamos el load balancer difiniendo una ip y puerto en el frontend, asociando al backend nuestro grupo de instancias

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/2a8d77ee-2d39-4315-ad4a-dd310efec1d8)

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/b9e6d371-2eb0-4e82-815e-7a6c4886cc9d)

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/529dc667-dc8b-404b-aee3-2b0fcc53f538)

6. Creamos nuestra base de datos en cloud SQL

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/776b61ca-5f2f-43ba-87b2-1c5467629d5c)

7. Creamos nuestro cloud storage

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/780afb1e-8ab0-4b93-922d-e37c26ba5fd6)

8. Ejecutamos en postman 

NOTA: las maquinas estan apagadas para no consumir los creditos
 
   
# Instrucciones de la entrega documental

En la sección de la wiki del repositorio, en el menu lateral izquierdo podras encontrar:

* Documento de arquitectura de la aplicación
* Documento plan de pruebas
* Documentación servicios de la aplicación
* Video explicando el uso de la aplicacion

  Tanto de la semana 1 como de la semana 2

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/c92aab8f-95e6-439c-a1cd-7c16d876763b)

