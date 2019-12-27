<a href="https://redbeacon.cl/">
    <img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redbeaconopnsense.png?alt=media&token=dc6722c3-ca49-438d-87de-e95c9c9aadb3" alt="Redbeacon API logo" title="Redbeacon" align="right" height="60" />
</a>

RedBeacon API OPNsense
======================

<img src="https://firebasestorage.googleapis.com/v0/b/ark-not.appspot.com/o/redOPN.png?alt=media&token=0c4db906-8ddc-49a0-acc9-b6adc1ee7a2a" width="640">

API de **OPNsense** para la comunidad. El uso de estas herramientas esta enfocado a Reglas de Firewall a Ambientes, permitiendo hacer bloqueos de direcciones ip atravez de IOC's  publicados en la aplicación **RedBeacon**, con las siguientes limitaciones:

- Envió restringido solo a ambientes de uso propio creados en la aplicación **RedBeacon**.
- Límite de un máximo de 5 Ambientes.

## Herramientas y Tecnologías

 - API **OPNsense**
 - FreeBSD
 - Python
 
## Configuración
Para hacer uso de esta API se necesita tener instalado previamente **OPNsense** en su servidor.

## Instalación

Comandos esenciales requeridos en la consola de **OPNsense**:

| Nombre | Observaciones |
| --- | --- |
| `8` | Opción Shell de OPNsense |
| `pkg install python3` | Instalar Python 3 |
| `python3 —version` | Verificar instalación Python 3 |
| `python3 -m venv apisense` | Crear ambiente virtual |
| `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` | Descargar PIP |
| `python get-pip.py` | Instalar PIP |
| `pip install virtualenv` | Instalar VIRTUALENV |
| `virtualenv —version` | Verificar instalación VIRTUALENV |
| `mkdir -p /opt/API` | Crear directorio donde alojaremos la API |
| `cd /opt/API/usr/bin/` | - |
| `virtualenv -p python3 /opt/API` | - |
| `source /opt/API/bin/activate.csh` | Activar directorio |
| `pip install flask` | Instalar FLASK |
| `pip install request` | Instalar REQUEST |
| `pip install json` | Instalar JSON |
| `cd /opt/API` | - |
| `git clone https://github.com/arkavia/RedBeacon-Api-OPNsense.git` | Clonar GitHub de la API |
| `exit` | Salir de la shell |
    
## Uso de la API
Comandos esenciales para ejecutar la API:

| Nombre | Observaciones |
| --- | --- |
| `8` | Opción Shell de OPNsense |
| `source /opt/API/bin/activate.csh` | Activar directorio |
| `python /opt/API/RedBeacon-Api-OPNsense/api.py` | Ejecutar la API |
