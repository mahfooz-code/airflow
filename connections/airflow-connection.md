# Syntax

    airflow connections [-h] COMMAND

## list airflow connection

    docker exec  -it airflow_docker-airflow-worker-1 airflow connections list

## Get the connection details

    docker exec  \
        -it airflow_docker-airflow-worker-1 \
        airflow connections \
        get postgres_db

## Creating connection in airflow

    airflow connections add \
        --conn-type postgres \
        --conn-host localhost \
        --conn-login postgres \
        --conn-password mysecretpassword \
        my_postgres
