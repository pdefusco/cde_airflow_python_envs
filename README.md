# CDE Airflow Python Environments

Create the CDE Files resource and load a yaml file to it.

```
%cde resource create --type files --name myYamlFiles

%cde resource upload --name myYamlFiles --local-path resources/sample.yaml
```

Create a CDE Python resource and activate the environment.

```
%cde resource create --name airflow_pyth_resource --type airflow-python-env

%cde resource upload --name airflow_pyth_resource --local-path resources/requirements.txt
```

Create pipeline resource and upload Airflow DAG to it.

```
%cde resource create --name my_pipeline_resource   

%cde resource upload --name my_pipeline_resource --local-path code/mydag.py

%cde resource upload --name my_pipeline_resource --local-path resources/utils.py
```

Allow a minute or two for the resource to finish building. You can check status with the describe command. Move on once the status changes to  "ready":

```
% cde resource describe --name airflow_pyth_resource                                        
{
  "name": "airflow_pyth_resource",
  "type": "airflow-python-env",
  "status": "ready",
  "signature": "b8f2df65fd68efbbf6d3074e857446dd685d1adc",
  "created": "2024-05-14T19:47:05Z",
  "modified": "2024-05-14T19:49:22Z",
  "retentionPolicy": "keep_indefinitely",
  "files": [
    {
      "path": "requirements.txt",
      "signature": "032692485118e8a3a72196114c6efc4e333c4673",
      "sizeBytes": 7,
      "created": "2024-05-14T19:49:22Z",
      "modified": "2024-05-14T19:49:22Z"
    }
  ],
  "pythonEnv": {
    "pythonVersion": "python3",
    "type": "airflow-python-env"
  },
  "pythonEnvInfo": {
    "statusReason": "Build completed",
    "sizeMb": 13,
    "buildDurationSeconds": 44,
    "numberOfFiles": 1172
  }
}
```

Activate Python Environment for Airflow Job.

```
cde airflow activate-pyenv --pyenv-resource-name airflow_pyth_resource
```

Create a CDE Airflow Job with the necessary dependencies.

```
%cde job create --name my_pipeline --type airflow --dag-file mydag.py --mount-1-resource my_pipeline_resource --airflow-file-mount-1-resource myYamlFiles

%cde job run --name my_pipeline
```

## References:

* Creating an Airflow pipeline with custom files using CDE CLI: https://docs.cloudera.com/data-engineering/cloud/orchestrate-workflows/topics/cde-cli-create-custom-pipeline.html
* Creating a custom Airflow Python environment: https://docs.cloudera.com/data-engineering/1.5.3/orchestrate-workflows/topics/cde-custom-python-airflow.html
