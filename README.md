# Proyecto de Automatización de Pruebas con Selenium

Este proyecto está diseñado para realizar pruebas automatizadas sobre el sitio web **OpenCart Abstracta** utilizando **Selenium WebDriver** y **pytest**. Las pruebas incluyen acciones como registro de usuario, inicio de sesión, agregar productos al carrito y completar el proceso de checkout.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

- **Python 3.7 o superior**
- **pip** (gestor de paquetes de Python)
- **Chrome** (si se utiliza el navegador Chrome)
- **Chromedriver** (para la automatización con Chrome, se gestionará automáticamente con `webdriver-manager`)

## Clonando el repositorio

Para clonar el proyecto desde el repositorio, sigue estos pasos:

1. Abre una terminal y navega a la carpeta donde deseas clonar el proyecto.
2. Ejecuta el siguiente comando:

```bash
git clone https://github.com/Anderuiz/automation_project.git

## 
Aquí tienes el contenido completo de tu archivo README.md que puedes copiar y pegar directamente en un archivo de texto:

markdown
Copiar código
# Proyecto de Automatización de Pruebas con Selenium

Este proyecto está diseñado para realizar pruebas automatizadas sobre el sitio web **OpenCart Abstracta** utilizando **Selenium WebDriver** y **pytest**. Las pruebas incluyen acciones como registro de usuario, inicio de sesión, agregar productos al carrito y completar el proceso de checkout.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

- **Python 3.7 o superior**
- **pip** (gestor de paquetes de Python)
- **Chrome** (si se utiliza el navegador Chrome)
- **Chromedriver** (para la automatización con Chrome, se gestionará automáticamente con `webdriver-manager`)

## Clonando el repositorio

Para clonar el proyecto desde el repositorio, sigue estos pasos:

1. Abre una terminal y navega a la carpeta donde deseas clonar el proyecto.
2. Ejecuta el siguiente comando:

```bash
git clone https://github.com/Anderuiz/automation_project.git

## Navega al directorio del proyecto:
1. cd automation_project

## Una vez clonado el repositorio, instala las dependencias necesarias utilizando pip:
1.pip install -r requirements.txt

##El proyecto usa un archivo de configuración para definir los datos del usuario de prueba. El archivo config.py contiene la siguiente estructura:
1.BASE_URL = "https://opencart.abstracta.us/index.php?route=common/home"

TEST_USER = {
    "first_name": "Anderson",
    "last_name": "Ruiz",
    "email": "anderson.ruiz@linktic.com",
    "telephone": "3057831407",
    "password": "Colombia2025*",
    "product": "Canon EOS 5D",  # Producto a seleccionar
    "color": "15"  # Color a seleccionar
}

## Ejecución de las pruebas
1. Las pruebas están implementadas utilizando pytest. Para ejecutar las pruebas, simplemente corre el siguiente comando en la terminal:
pytest
