from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'martinluther',
    'retires':5,
    'retry_delay':timedelta(minutes=2)
}


with DAG(
    dag_id='dag_with_catchup_backfill',
    default_args=default_args,
    description='this is our first airflow dag that we write',
    start_date=datetime(2021,7,6),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo simple bash command'
    )