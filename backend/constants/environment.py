import os

def _initialize_environment():
    os.environ['DATABASE_NAME']="PDSA"
    os.environ['USER']="postgres"
    os.environ['PASSWORD']="12qw"
    os.environ['HOST']="localhost"
    os.environ['PORT']="5432"