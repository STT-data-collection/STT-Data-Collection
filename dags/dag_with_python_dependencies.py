from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args={
    'owner':'martinluther',
    'retry':5,
    'retry_delay':timedelta(minutes=2)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version {sklearn.__version__}")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies',
    start_date=datetime(2022,7,7),
    schedule_interval='@daily'
)as dag:
    get_learn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )
    get_learn