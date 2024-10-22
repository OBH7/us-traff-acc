# Ignore virtual environment directories
venv/
env/
.venv/

# Python bytecode and cache files
__pycache__/
*.pyc
*.pyo

# Ignore Airflow log files and local SQLite database
airflow/logs/
airflow/airflow.db
airflow/unittests.cfg
airflow.cfg

# Ignore any large data files or sensitive data (optional)
data/*.csv  # Ignoring CSV files in the data folder (remove if you want to include them)
data/*.parquet  # Ignore Parquet files (if you have any)

# Ignore Jupyter Notebook checkpoints
.ipynb_checkpoints/

# OS-specific files
.DS_Store  # MacOS specific
*.swp      # Swap files created by text editors like Vim
*.swo      # Swap files created by text editors

# Logs and output files
*.log
*.out
*.err

# Ignore additional temporary or build files (optional)
*.tmp
*.bak
*.old

# Ignore Airflow example DAGs (optional if you don’t want the example DAGs)
dags/example_dags/

# Ignore secret or config files (if applicable)
secrets/
.env  # If you use environment variables for sensitive data
