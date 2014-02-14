from __future__ import with_statement
from fabric.api import *


prod_server = 'gigas'


def prod():
    env.use_ssh_config = True
    env.hosts = [prod_server]
    env.root = '/home/javaguirre/taikoa'
    env.activate = 'source %s/env/bin/activate' % env.root
    env.gunicorn = 'taikoa'


def virtualenv(command):
    with cd(env.root):
        run(env.activate + ' && ' + command)


def git_pull():
    """Updates the repository."""
    with cd(env.root):
        run('git pull origin master')


def restart_daemon():
    with cd(env.root):
        run("sudo supervisorctl restart %s" % env.gunicorn)


def deploy():
    """Run the actual deployment steps: $ fab prod deploy"""
    with cd(env.root):
        git_pull()
        virtualenv("pip install -r %s/requirements.txt" % env.root)
    restart_daemon()
