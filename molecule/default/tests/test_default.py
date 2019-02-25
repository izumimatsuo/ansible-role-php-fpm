import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_php_is_installed(host):
    package = host.package("php")
    assert package.is_installed
    assert package.version.startswith("5.4")


def test_php_fpm_is_installed(host):
    package = host.package("php-fpm")
    assert package.is_installed
    assert package.version.startswith("5.4")


def test_php_fpm_running_and_enabled(host):
    service = host.service("php-fpm")
    assert service.is_running
    assert service.is_enabled


def test_php_fpm_is_listen(host):
    assert host.socket("tcp://127.0.0.1:9000").is_listening
