
from fabric.api import env, task
from envassert import detect, package, port, process, user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()
    assert package.installed("ambari-server")
    assert port.is_listening(80)
    assert user.exists("ambari")
    assert process.is_up("ambari-server")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()