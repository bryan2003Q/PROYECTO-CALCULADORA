# Calculadora CI/CD

Proyecto simple de calculadora web con interfaz y backend en Flask, pruebas automatizadas y pipeline CI/CD.

## Características
- Operaciones básicas: suma, resta, multiplicación y división.
- Interfaz web con HTML/CSS: [templates/index.html](templates/index.html).
- Backend en Flask con funciones: [`app.sumar`](app.py), [`app.restar`](app.py), [`app.multiplicar`](app.py), [`app.dividir`](app.py).
- Tests unitarios con pytest: [tests.py](tests.py).
- Dockerfile para contenedorización: [Dockerfile](Dockerfile).
- Workflow GitHub Actions para CI/CD: [.github/workflows/ci-cd.yaml](.github/workflows/ci-cd.yaml).
- Estilos: [static/style.css](static/style.css).
- Registro de cambios: [CHANGELOG.md](CHANGELOG.md)

## Requisitos
- Python 3.9+
- pip
- Docker (opcional, para despliegue)

Las dependencias están en [requirements.txt](requirements.txt).

## Uso local (desarrollo)
1. Instalar dependencias:
    
    ```sh
    pip install -r requirements.txt
    ```

2. Ejecutar la aplicación:

    ```sh
    python app.py
    ```

3. Abrir en el navegador: http://localhost:5000

## Ejecutar tests
Correr las pruebas unitarias con pytest:

```sh
pytest 

Los tests verifican las funciones definidas en app.sumar, app.restar, app.multiplicar y app.dividir.

Docker (construir y ejecutar)
Construir imagen:

docker build -t calculadora-devops:latest .

Ejecutar contenedor:

docker run -d -p 5000:5000 --name calculadora-web calculadora-devops:latest

CI/CD
El pipeline en .github/workflows/ci-cd.yaml realiza:

Instalación de dependencias y ejecución de tests (pytest).
Revisión de linting con ruff.
Construcción y push de imagen Docker.
Despliegue mediante SSH en una instancia remota (acciones y secretos configurables).
Estructura del proyecto
.gitignore
app.py — backend Flask y funciones: app.sumar, app.restar, app.multiplicar, app.dividir
CHANGELOG.md
Dockerfile
README.md
requirements.txt
tests.py
.github/workflows/ci-cd.yaml
static/style.css
templates/index.html
Contribuir
Crear una rama feature.
Añadir tests para nuevas funcionalidades.
Abrir PR y asegurarse de que CI pase antes de mergear.
Notas
La versión sigue SemVer: 
M
A
J
O
R
.
M
I
N
O
R
.
P
A
T
C
H
MAJOR.MINOR.PATCH.