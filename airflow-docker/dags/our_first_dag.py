from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'martinluther',
    'retires':5,
    'retry_delay':timedelta(minutes=2)
}


with DAG(
    dag_id='our_second_dag',
    default_args=default_args,
    description='this is our first airflow dag that we write',
    start_date=datetime(2021,7,7,15),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task!'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey am task 2 and I shall be running after task 1'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey am task 3 and i shall be running immediately after task 1 just like task 2'
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)