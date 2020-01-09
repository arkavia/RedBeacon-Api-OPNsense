<a href="https://redbeacon.cl/">
    <img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redbeaconopnsense.png?alt=media&token=dc6722c3-ca49-438d-87de-e95c9c9aadb3" alt="Redbeacon API logo" title="Redbeacon" align="right" height="60" />
</a>

RedBeacon API OPNsense
======================

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/PROMO.png?alt=media&token=1a44e21d-c005-4fb4-9f0d-c1542e7b99eb" width="1080">

API de **OPNsense** para la comunidad. El uso de estas herramientas está enfocado a la seguridad perimetral de una red, permitiendo hacer bloqueos de direcciones IP's a través de IOC's  publicados en la aplicación **RedBeacon**.

**Beneficios:**

- **Personaliza** tus reglas de seguridad a tu medida a través de **OPNsense**.
- **Notificación y acción** de los principales y más importantes IOC's a través de **RedBeacon**.
- **Crea y elimina** tus ambientes de seguridad perimetral de red en tiempo real a través de **RedBeacon**.
- **Activa y desactiva** las reglas de tus ambientes de seguridad perimetral en tiempo real a través de **RedBeacon**.

**Restricciones:**

- Envió restringido solo a ambientes de uso propio creados en la aplicación **RedBeacon**.
- Límite de un máximo de **5** Ambientes.

## Herramientas y Tecnologías

 - API **OPNsense**
 - FreeBSD
 - Python
 
## Configuración
Para hacer uso de esta API se necesita tener instalado previamente **OPNsense** en su servidor.

## Instalación

Ingresar a la consola de **OPNsense** y seleccionar la opción 8(**shell**):

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redOPN.png?alt=media&token=0c4db906-8ddc-49a0-acc9-b6adc1ee7a2a" width="640">

Instalar los paquetes necesarios 

    $ pkg install python3
    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ python3 get-pip.py
    $ pip install virtualenv
    $ pip install flask
    $ pip install flask_cors
    $ pip install request
    $ pip install requests
    $ pip install json
    $ pkg install git

Preparar Python virtualenv 

    $ mkdir -p /root/API
    $ cd /root/API
    $ virtualenv -p python3 /root/API 
    $ source /root/API/bin/activate.csh

Clonar GitHub de la API

    $ cd /root/API
    $ git clone https://github.com/arkavia/RedBeacon-Api-OPNsense.git
    
## Uso de la API

Ejecutar la API

    $ source /root/API/bin/activate.csh
    $ python3 /root/API/RedBeacon-Api-OPNsense/api.py
    
## Integración en RedBeacon

Una vez la API de **OPNsense** este intalada procederemos a integrarla a la aplicación para ello haremos lo siguiente:


<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/Captura%20de%20Pantalla%202020-01-08%20a%20la(s)%2017.57.37.png?alt=media&token=e856f38a-f223-4d77-ac36-f8b568d6ebb8" width="1080">


Las claves API se administran en el administrador de usuarios, vaya a la página del administrador de usuarios(**System > Access > Users**) y seleccione un usuario. En algún lugar de la página encontrará la sección de API para este usuario.


<img src="https://docs.opnsense.org/_images/Usermanager_add_api_key.png" width="1080">


Haga clic en el signo **+** para agregar una nueva clave. Cuando se crea la clave, recibirá una (descarga única) con las credenciales en un archivo de texto (con formato ini). El contenido de este archivo se ve así:


    key=w86XNZob/8Oq8aC5r0kbNarNtdpoQU781fyoeaOBQsBwkXUt
    secret=XeD26XVrJ5ilAc/EmglCRC+0j2e57tRsjHwFepOseySWLM53pJASeTA3


Antes de que pueda comenzar, asegúrese de crear una copia de este archivo con las credenciales ya que serán de vital uso en los siguientes pasos.

Ingresamos a **RedBeacon**, en la pestaña de **Bloqueo Inteligente** Haga clic en el boton **+** para agregar un nuevo ambiente. Ingrese el nombre de alias con el que desea asociar el ambiente de seguridad perimetral(esto se vera reflejado en la pestaña de **Aliases** en el dashboard de **OPNsense**), en la casilla IP ingrese la IP asignada anteriormente en la consola como **WAN**, A continuación haga ingreso de las credenciales otorgadas anteriormente por **OPNsense** todo esto para conseguir el resultado mostrado en las siguientes imagenes:


<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/resopnred.png?alt=media&token=2f5253e0-c355-4986-92bc-87a3245fbcf2" width="1080">

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/Captura-de-Pantalla-2020-01-09-a-la(s)-11.51.50.png?alt=media&token=8c0b4da9-4de4-4546-ba1c-68be94bb36a1" width="1080">

Para finalizar la integración es de maxima importancia crear una regla personalizada en **OPNsense** asociándola con el alias creado, para esto accederemos a dicha pestaña en la plataforma(**Firewall > Rules > WAN**) y la crearemos con el fin de poder asociar el listado que contendra el alias con esta regla, permitiendo de esta manera poder tomar acciones en tiempo a través de IOC's  publicados en la aplicación **RedBeacon** de manera muy facil.

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/Captura-de-Pantalla-2020-01-09-a-la(s)-12.43.09.png?alt=media&token=9fcbbdd2-d1c1-498c-85f1-79f2c6286ac2" width="1080">


## Bloqueos en RedBeacon

1. Ingresamos a **RedBeacon**, en la pestaña de **Inicio** accedemos a una publicación con IOC's disponibles,
una vez en el detalle de la publicación iremos al final de la publicación a la sección **IoC**. 

2. haga clic en el ambiente que desea bloquear estas  direcciones IP's, se nos mostraran dos opciones de las cuales le daremos clic a **Bloquear IOC**.

3. una vez realizada la acción anterior se nos mostrara un mensaje dandonos a entender que la acción fue realizada satisfactoriamente.

> **NOTA: Cabe señalar que estos cambios se verán aplicados y reflejados automáticamente en OPNsense gracias a la regla asignada con anterioridad en dicha plataforma.**

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/opnred2.png?alt=media&token=1c0e052e-29b5-465a-b0a3-2371ac3f25a2" width="1080">

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/Captura%20de%20Pantalla%202020-01-09%20a%20la(s)%2012.35.15.png?alt=media&token=3d17e8c3-f7ce-4d22-b008-0984ee888b62" width="1080">
