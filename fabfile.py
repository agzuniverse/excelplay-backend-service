import os
from fabric import Connection, task

PROJECT_BASE = "/home/agz/excelplay-backend-service/"


@task
def deploy(ctx):
    with Connection(
        os.environ["HOST"],
        user="agz",
        connect_kwargs={"key_filename": os.environ["DEPLOY_KEY_FILE"]},
    ) as c:
        with c.cd(PROJECT_BASE):
            c.run("docker-compose down")
            c.run("git pull origin master --recurse-submodules --rebase")
            c.run("sudo docker-compose -f prod.docker-compose.yml up --build -d")
