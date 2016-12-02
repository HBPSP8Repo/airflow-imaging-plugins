from setuptools import setup

setup(
    name="airflow_imaging_plugins",
    description="Airflow plugins to support Neuroimaging tasks.",
    author='LREN CHUV',
    author_email='ludovic.claude@chuv.ch',
    url='https://github.com/LREN-CHUV/airflow-imaging-plugins',
    license='Apache License 2.0',
    zip_safe=False,
    packages=['airflow_spm'],
    install_requires=[
        'airflow~=1.7.0'
    ]
)