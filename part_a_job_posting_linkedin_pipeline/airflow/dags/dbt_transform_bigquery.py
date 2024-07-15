from pathlib import Path

from airflow.utils.dates import days_ago
from airflow.datasets import Dataset

from cosmos import DbtDag
from cosmos.config import ExecutionConfig, ProfileConfig, ProjectConfig, RenderConfig


job_postings_dataset = Dataset("job_postings_dataset")

companies_dataset = Dataset("companies_dataset") 
salaries_dataset = Dataset("salaries_dataset")

                              
job_skills_dataset = Dataset("job_skills_dataset")
skills_dataset = Dataset("skills_dataset")

profile_config = ProfileConfig(
    profile_name="job_postings_project",
    target_name="dev",
    profiles_yml_filepath=Path('/usr/local/airflow/dags/dbt/profiles.yml')
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path='/usr/local/airflow/dags/dbt/'
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"/usr/local/airflow/dbt_venv/bin/dbt",
    ),
    operator_args={
        "install_deps": True,
    },

    # dag settings
    start_date=days_ago(1), 
    schedule=(job_postings_dataset | (companies_dataset) & (salaries_dataset) 
              | (job_skills_dataset) & (skills_dataset)),
    catchup=False,
    dag_id="dbt_transform_in_bigquery",
    tags=["dbt_transform_data_in_bigquery"],
)

