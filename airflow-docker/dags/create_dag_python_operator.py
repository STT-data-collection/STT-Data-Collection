from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner':'martinluther',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

def greet():
    print("hello there this is my first python operator dag")


def greet_with_age(age,ti):
    name = ti.xcom_pull(task_ids='get_nameo')
    print(f"Hello, my name is {name}. And I am {age} years old!..")


def get_name():
    return 'marto'

with DAG(
    dag_id='our_fourth_python_operator_dag',
    default_args=default_args,
    description='our first dag using python operator',
    start_date=datetime(2022,7,6,2),
    schedule_interval='@daily'
)as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet_with_age,
        op_kwargs={'age':24}
    )
    task2 = PythonOperator(
        task_id='get_nameo',
        python_callable=get_name,
    )
    task2 >> task1
