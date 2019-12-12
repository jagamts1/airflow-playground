"""Sub dags operator playground."""
from airflow import DAG
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from sub_dag import sub_dag


PARENT_DAG_NAME = 'parent_dag'
CHILD_DAG_NAME = 'child_dag'

default_args = {
    'owner': 'jagadish',
    'email': None,
    'start_date': datetime(2019, 10, 9)
}

with DAG(PARENT_DAG_NAME, start_date=datetime(2019, 12, 10), default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')

    sub_dag = SubDagOperator(task_id=CHILD_DAG_NAME, subdag=sub_dag(PARENT_DAG_NAME, CHILD_DAG_NAME, dag.start_date, dag.schedule_interval))

    end = DummyOperator(task_id='end')

    start >> sub_dag >> end