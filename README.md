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
| `mkdir -p /opt/redbeacon-opnsense` | Crear directorio donde alojaremos el archivo .py |
| `cd /opt/redbeacon-opnsense/usr/bin/` | - |
| `virtualenv -p python3 /opt/redbeacon-opnsense` | - |
| `source /opt/redbeacon-opnsense/bin/activate.csh` | Activar directorio |
| `pip install flask` | Instalar FLASK |
| `pip install request` | Instalar REQUEST |
| `pip install json` | Instalar JSON |
| `echo > api.py` | - |
| `cat api.py` | Ver el contenido de el archivo apy.py |
| `vi api.py` | Editar el archivo apy.py |

Una vez ejecutados estos comandos procedemos a modificar el archivo **apy.py** ubicado en nuestro **OPNsense** remplazando su contenido por el entregado en este repositorio en el archivo **apy.py**, para hacer uso de este archivo ejecutamos el siguiente comando en la terminal de su pc: 

    $ git clone https://github.com/arkavia/phishing_test.git
    
## Uso de la API
Comandos esenciales para ejecutar la API:

| Nombre | Observaciones |
| --- | --- |
| `source /opt/redbeacon-opnsense/bin/activate.csh` | Activar directorio |
| `python api.py` | Ejecutar la API |
