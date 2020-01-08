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
    
## Uso en RedBeacon

Una vez la API de opnsense este intalada procederemos a integrarla a la aplicación para ello haremos lo siguiente

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/1opnsense.png?alt=media&token=162d38b2-ab62-44ce-89e0-a6772ba1440c" width="640">

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/2opnsense.png?alt=media&token=82fc3bec-7ae0-4492-a36a-d1684235497b" width="640">

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/3opnsense.png?alt=media&token=d4259e8b-b312-4fbd-b83a-30ad7213d553" width="640">

Las claves API se administran en el administrador de usuarios (system_usermanager.php), vaya a la página del administrador de usuarios y seleccione un usuario. En algún lugar de la página encontrará la sección de API para este usuario.

<img src="https://docs.opnsense.org/_images/Usermanager_add_api_key.png" width="640">

Haga clic en el signo + para agregar una nueva clave. Cuando se crea la clave, recibirá una (descarga única) con las credenciales en un archivo de texto (con formato ini). El contenido de este archivo se ve así:

    key=w86XNZob/8Oq8aC5r0kbNarNtdpoQU781fyoeaOBQsBwkXUt
    secret=XeD26XVrJ5ilAc/EmglCRC+0j2e57tRsjHwFepOseySWLM53pJASeTA3

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/opnsense_phone1.jpeg?alt=media&token=07a4f297-eda2-4d55-9e25-f203f5300716" width="640">

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/opnsense_phone2.jpeg?alt=media&token=650c1c31-e8ea-4c90-b8a7-3460b70db39f" width="640">

