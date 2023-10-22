# Bienvenidos al grupo 10 de desarrollo de software en la nube

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

7. Abrimos postman e importamos la documentación de los servicios
![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/5b464eac-702e-4d85-bea4-35de1af22a3c)

8. Procedemos a ejecutar cada servicio, cada servicio tiene configurado su endpoint, request requerida, solo es reemplazar lso datos en la request, parra falcilitar las pruebas, hemos adjuntado estos tres archivos de pruebae un archivo .zip que debe descomprimir [datos de prueba](https://uniandes-my.sharepoint.com/:u:/g/personal/k_maldonadod_uniandes_edu_co/ETTY7tAoSCNHlsqK7etI_iABK1YTLLGJXzXRgRcwIVgCDQ?e=h7tl6r), si deseas mas información de cada uno de lso servicios, pouedes ir a la sección de wiki -> [Documentación servicios de la aplicación](Identificación-de-riesgos)

# Instrucciones de la entrega documental

En la sección de la wiki del repositorio, en el menu lateral izquierdo podras encontrar:

* Documento de arquitectura de la aplicación
* Documento plan de pruebas
* Documentación servicios de la aplicación

![image](https://github.com/kevin96uniandes/MISO2023-desarrollo-nube/assets/123959005/19a19ac4-deeb-4036-9b4a-8886a307514a)
