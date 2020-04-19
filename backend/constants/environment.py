import os

def _initialize_environment():
    os.environ['DATABASE_NAME']="PDSA"
    os.environ['DATABASE_USER']="postgres"
    os.environ['DATABASE_PASSWORD']="12qw"
    os.environ['DATABASE_HOST']="localhost"
    os.environ['DATABASE_PORT']="5432"

    os.environ['DATA_STRUCTURE_MODE']="2"