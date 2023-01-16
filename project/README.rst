===============================================================================
Get hottest month and city
===============================================================================

Usage
----------------------------------------------------------
python3 -m hottest_month_and_city archive.zip GlobalLandTemperaturesByMajorCity.csv 1980

script returns the hottest month and city in dict 
{"hottest_month": month, "hottest_city": city}


Installation
----------------------------------------------
This project uses both conda and Poetry for Python (and external)
packaging and dependency management. Therefore, the whole project
environment setting process consists of the following steps:

1. Installing conda distribtive
2. Installing Poetry
3. Inital Poetry setup
4. Installing list of necessary packages via Poetry & conda combination

We assume that you've already
successfully installed conda to your workstation. If you have any questions,
please refer to `this guide <https://wiki.ml-devs.com/ru/sandbox/conventions/dev-environment>`_.

Sysytem requirements
----------------------------------------------------------------
You need tools:

* git 2.28+
* python 3.9.2+ (<3.10)
* conda 4.10.2+
* poetry 1.1.12

Poetry installation
-------------------------------------------------------------------------------
**Deactivate any conda environment before Poetry installation.**

Recommended way for Linux OS:

.. code::

  curl -sSL https://install.python-poetry.org | python -

Recommended way for Windows OS:

.. code::

  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -


Poetry initial setup
-------------------------------------------------------------------------------
- Configure Poetry **(should be done once globally)**:

.. code::

    poetry config virtualenvs.in-project false
    poetry config virtualenvs.path <conda-install-path>/envs

Packages installation
-------------------------------------------------------------------------------
- Create and activate *conda* virtual environment for development:

.. code::

    conda env create -f devenv.yaml
    conda activate env_name

- Install dependencies with Poetry:

.. code::

    poetry install