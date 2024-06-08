Brawl Stars Global Rankings

Este proyecto utiliza la API de Brawl Stars para mostrar los datos de los jugadores en una tabla HTML y un gráfico de barras utilizando Django y Chart.js.
API Utilizada

La API utilizada es la siguiente:

    API Endpoint: https://api.brawlstars.com/v1/rankings/global/players?limit=100
    Descripción: Esta API proporciona los datos de los jugadores clasificados globalmente en Brawl Stars, incluyendo su nombre, rango, trofeos (estadistica privada, por eso todods se mustran como 1) y club al que pertenecen.

Configuración y Uso

    Clona este repositorio en tu máquina local.

    Crea un entorno virtual y activarlo:

    bash

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate      # Para Windows

Instala las dependencias:

bash

pip install -r requirements.txt

Configura tu clave de API de Brawl Stars:

    Reemplaza 'TU_API_KEY' con tu clave de API en polls/views.py en la variable headers.

Ejecuta las migraciones:

bash

python manage.py migrate

Inicia el servidor:

bash

    python manage.py runserver

    Visita http://127.0.0.1:8000/rankings/ en tu navegador para ver los datos de los jugadores.

Estructura del Proyecto

    config/: Contiene la configuración del proyecto Django.
    polls/: La aplicación principal que muestra los datos de los jugadores.
        views.py: Contiene la lógica para obtener los datos de la API y renderizar la plantilla.
        templates/polls/index.html: La plantilla HTML que muestra los datos de los jugadores y el gráfico.
    requirements.txt: Archivo que lista todas las dependencias del proyecto.

Dependencias

    Django: 3.x
    requests: 2.x
    Chart.js: 2.x
