from airflow.models import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import json
from pandas import json_normalize

default_args = {
    'start_date': datetime(2022, 1, 1),
    'owner': 'malam'
}

def _processing_user(ti):
    users=ti.xcom_pull(task_ids=['extracting_user'])
    if not len(users) or 'results' not in users[0]:
        raise ValueError('User is not empty')
    user=users[0]['results'][0]
    processed_user=json_normalize({
        'firstName': user['name']['first'],
        'lastName': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email']
    })

    processed_user.to_csv("/tmp/processed_user.csv",index=None,header=False)


with DAG("user_processing", schedule_interval="@daily",start_date=datetime(2022, 1, 1)) as dag:
    creating_table=PostgresOperator(
    task_id='creating_table',
    postgres_conn_id='postgres_db',
    sql='''
    create table if not exists users(
    firstname text not null,
    lastname text not null,
    country text not null,
    username text not null,
    password text not null,
    email text not null primary  key );
    '''
    )

    is_api_available=HttpSensor(
        task_id="is_api_available",
        http_conn_id="user_api",
        endpoint="api/"
    )

    extracting_user=SimpleHttpOperator(
        task_id="extracting_user",
        http_conn_id="user_api",
        endpoint="api/",
        method="GET",
        response_filter= lambda response : json.loads(response.text),
        log_response=True
    )

    processing_user=PythonOperator(
        task_id='processing_user',
        python_callable=_processing_user
    )

    storing_user=BashOperator(
        task_id='storing_user',
        bash_command='/d/development/POC/workflow/api-postgres-pipeline/loading_csv_postgres.sh '
    )

    creating_table >> is_api_available >> extracting_user >> processing_user >> storing_user

