"""Practice and Play with airflow bash operator."""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'jagadish',
    'email': None,
    'start_date': datetime(2019, 10, 9)
}

dag = DAG(
    'bash_playground', default_args=default_args, schedule_interval='@daily')

t1 = BashOperator(
    task_id='echo_who_am_i',
    bash_command='whoami',
    dag=dag,)
