<a href="https://redbeacon.cl/">
    <img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redbeaconopnsense.png?alt=media&token=dc6722c3-ca49-438d-87de-e95c9c9aadb3" alt="Redbeacon API logo" title="Redbeacon" align="right" height="60" />
</a>

RedBeacon API OPNsense
======================

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redOPN.png?alt=media&token=0c4db906-8ddc-49a0-acc9-b6adc1ee7a2a" width="640">

API de OPNsense para la comunidad. El uso de estas herramientas esta enfocado a Reglas de Firewall a Ambientes, permitiendo hacer bloqueos de direcciones ip atravez de IOC's  publicados en la aplicación RedBeacon, con las siguientes limitaciones:

- Envió restringido solo a ambientes de uso propio creados en la aplicación RedBeacon.
- Límite de un máximo de 5 Ambientes.

## Herramientas, Tecnologías y Paquetes

 - API OPNsense
 - Python

## Instalación

    npm install (para ambos proyectos)
    node index.js (API)
    ng serve (Portal Web)

## Configuración
Para hacer uso de esta API se necesita tener instalado previamente **OPNsense** en su servidor


## Uso de la API

A continuación, el detalle de las peticiones **GET** y **POST** que contempla la API, por supuesto estas pueden ser modificadas para mejoras u/o otros usos.
