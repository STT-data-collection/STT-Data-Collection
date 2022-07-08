from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'martinluther',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_cron_expression',
    start_date=datetime(2022,6,22),
    schedule_interval='5 3 * * Thu'
)as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo dag with cron expression'
    )
    task1