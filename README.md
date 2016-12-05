[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/airflow-imaging-plugins/blob/master/LICENSE) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7a9c796392e4420495ee1fabd0fce9ae)](https://www.codacy.com/app/hbp-mip/airflow-imaging-plugins?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LREN-CHUV/airflow-imaging-plugins&amp;utm_campaign=Badge_Grade)

# Airflow Imaging plugins

Set of plugins helping to work with imaging data in Airflow.

Those include:

* airflow_spm.operators.SpmOperator: Executes SPM or just Matlab
* airflow_spm.operators.SpmPipelineOperator: Executes a pipeline on SPM, where a 'pipeline' is a function implemented in SPM
* airflow_freespace.operators.FreeSpaceSensor: Waits for enough free disk space on the disk.

## Installation

```
  pip install from git: pip install git+https://github.com/LREN-CHUV/airflow-imaging-plugins.git@master#egg=airflow_imaging_plugins
```

## Setup and configuration

### Airflow setup for MRI scans pipeline:

* In Airflow config file, add the [spm] section with the following entries:
   * SPM_DIR: root path to the installation of SPM
