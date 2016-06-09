"""Uses pyinvoke to automate some error-prone admin tasks"""

from invoke import task, run

@task
def compile_scss():
    """Compile the SCSS and copy to relevant static directory"""
    run("mkdir -p ./static/basic_theme/css/")
    run("mkdir -p ./schedule_site/static/basic_theme/css/")
    run("pyscss ./scss/*.scss > ./static/basic_theme/css/style.css")
    run("cp ./static/basic_theme/css/style.css ./schedule_site/static/basic_theme/css/style.css")
