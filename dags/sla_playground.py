"""Playground for SLA related tasks."""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Jagadish',
    'start_date': datetime(2019, 12, 8),
    'email': ['jagadish@nineleaps.com']
}

with DAG('sla_playground', schedule_interval='@daily', default_args=default_args, catchup=True) as dag:
    dummy_example = DummyOperator(task_id='dummy_example')

    sla_bash_example = BashOperator(
        task_id='sla_bash_example',
        bash_command='sleep 10',
        sla=timedelta(seconds=5))
