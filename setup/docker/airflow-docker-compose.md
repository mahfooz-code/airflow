# You can also check if you have enough memory by running this command:

    docker run --rm "debian:buster-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'

# Downloading docker compose file created by airflow
    
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'

# mounting the folder

    mkdir -p ./dags ./logs ./plugins
    ./dags - you can put your DAG files here.
    ./logs - contains logs from task execution and scheduler.
    ./plugins - you can put your custom plugins here.


# Setting the right Airflow user
    your host user id and needs to have group id set to 0. 
    Otherwise the files created in dags, logs and plugins will be created with root user.
    
    echo -e "AIRFLOW_UID=$(id -u)" > .env


# Manually user can be set
    
    AIRFLOW_UID=50000


# Initializing airflow metastore database

    docker-compose up airflow-init

# Starting up docker cluster

    docker-compose up

# Accessing the docker environment
    
    docker-compose run airflow-worker airflow info

# Accessing docker info using script by downloading and setting it up as given below.

    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/airflow.sh'
    chmod +x airflow.sh
    ./airflow.sh info

#   To enter interactive bash shell in the container
    ./airflow.sh bash

#   To enter python to enter python container.

    ./airflow.sh python

# Cleaning-up the environment
    docker-compose down --volumes --remove-orphans
    docker-compose down --volumes --rmi all


# Environment variables supported by Docker Compose


    _AIRFLOW_WWW_USER_USERNAME
    _AIRFLOW_WWW_USER_PASSWORD
    _PIP_ADDITIONAL_REQUIREMENTS
    AIRFLOW_IMAGE_NAME
    AIRFLOW_UID







