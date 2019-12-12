"""Airflow playgound dag."""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Jagadish',
    'depends_on_past': False,
    'start_date': datetime(2019, 12, 8),
    'email': None,
    'email_on_failure': False,
    'email_on_retries': False,
    'retries': 1,
    'retries_delay': timedelta(minutes=5),
}

dag = DAG(
    'playground',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 2',
    dag=dag,
    retries=3)

templated_command = '''
    {% for i in range(5) %}
        echo "{{ds}}"
        echo "{{params.my_param}}"
        echo "{{macros.ds_add(ds, 7)}}"
    {% endfor %}

'''

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'parameters I passed working fine'},
    dag=dag)


# t2.set_upstream(t1)
# t3.set_upstream(t1)

t1.set_downstream(t2)
t1.set_downstream(t3)
