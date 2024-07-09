ML model deployment example
===========================

Complete code (including a trained model) to deploy and inference a machine learning model (built on the iris dataset) using Docker and FastAPI.

1. With terminal navigate to the root of this repository
--------------------------------------------------------

2. Build docker image
---------------------
.. code-block::

    docker build -t image_name .

3. Run container
----------------
.. code-block::

    docker run --name container_name -p 8000:8000 image_name

4. Output will contain
----------------------
INFO:     Uvicorn running on http://0.0.0.0:8000

Use this url in chrome to see the model frontend;
use http://0.0.0.0:8000/docs for testing the model in the web interface.

5. Query model
--------------
    
 #. Via web interface (chrome):
        http://0.0.0.0:8000/docs -> test model
    
 #. Via python client:
        client.py
    
 #. Via curl request:
        .. code-block::

            curl -X POST "http://0.0.0.0:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

Docker/ Docker compose usage
===========================

Basic Docker Compose Commands

Build Services
-----
.. code-block::

    docker-compose build
This command builds the images specified in the docker-compose.yml file.

Start Services
-----
.. code-block::

    docker-compose up
This command starts the services defined in the docker-compose.yml file. It builds the images if they are not already built.

Start Services in Detached Mode
-----
.. code-block::

    docker-compose up -d
This command starts the services in the background (detached mode).

Stop Services
-----
.. code-block::

    docker-compose stop
This command stops the running services without removing the containers.

Restart Services
-----
.. code-block::

    docker-compose restart
This command restarts the running services.

Remove Services
-----
.. code-block::

    docker-compose down
This command stops and removes the containers, networks, and volumes defined in the docker-compose.yml file.

Remove Services with Volumes
-----
.. code-block::

    docker-compose down -v
This command stops and removes the containers, networks, and volumes defined in the docker-compose.yml file, including the volumes associated with the services.

Credits: https://github.com/DanilZherebtsov/ml-docker-flask-api
