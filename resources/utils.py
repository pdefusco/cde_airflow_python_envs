"""
Utils for parsing Yaml files in Airflow DAG

Author: Paul de Fusco
"""

#Custom Python Method
def _my_parse_yaml(document):
    print(yaml.load(document, Loader=Loader))
