<a href="https://redbeacon.cl/">
    <img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redbeaconopnsense.png?alt=media&token=dc6722c3-ca49-438d-87de-e95c9c9aadb3" alt="Redbeacon API logo" title="Redbeacon" align="right" height="60" />
</a>

RedBeacon API OPNsense
======================

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/PROMO.png?alt=media&token=1a44e21d-c005-4fb4-9f0d-c1542e7b99eb" width="640">

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

