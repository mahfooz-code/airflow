docker run --rm "debian:buster-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'

# Setting the right Airflow user
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

AIRFLOW_UID=50000

# Initialize the database
docker-compose up airflow-init

# Running airflow
docker-compose up

# Accessing the environment
docker-compose run airflow-worker airflow info

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/airflow.sh'
chmod +x airflow.sh
Now you can run commands easier.

./airflow.sh info


