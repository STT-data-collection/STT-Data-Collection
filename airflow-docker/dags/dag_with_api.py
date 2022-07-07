from datetime import timedelta,datetime
from airflow.decorators import dag,task

default_args={
    'owner':'martinluther',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

@dag(dag_id='dag_with_taskflow_api',
    default_args=default_args,
    start_date=datetime(2022,7,6),
    schedule_interval='@daily')
def hello_world():
    
    @task()
    def get_name():
        return 'Martin'
    
    @task()
    def get_age():
        return 25

    @task()
    def greet(name,age):
        print(
            f"Hello I am called {name} "
            f"and I am {age} years old"
        )

    name = get_name()
    age = get_age()
    greet(name,age)

greet_dag = hello_world()
