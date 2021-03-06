# encoding: utf-8
import pytest

from catalog import create_app


def test_create_app():
    try:
        create_app()
    except SystemExit:
        # Clean git repository doesn't have `local_config.py`, so it is fine
        # if we get SystemExit error.
        pass


@pytest.mark.parametrize('flask_config_name', ['production', 'development', 'testing'])
def test_create_app_passing_flask_config_name(flask_config_name):
    create_app(flask_config_name=flask_config_name)


@pytest.mark.parametrize('flask_config_name', ['production', 'development', 'testing'])
def test_create_app_passing_FLASK_CONFIG_env(monkeypatch, flask_config_name):
    monkeypatch.setenv('CATALOG_CONFIG', flask_config_name)
    create_app()


def test_create_app_with_conflicting_config(monkeypatch):
    monkeypatch.setenv('CATALOG_CONFIG', 'production')
    with pytest.raises(AssertionError):
        create_app('development')


def test_create_app_with_non_existing_config():
    with pytest.raises(KeyError):
        create_app('non-existing-config')
