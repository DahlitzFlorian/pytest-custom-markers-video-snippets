import pytest


@pytest.mark.cli
def test_cli_entrypoint():
    assert 1 == 1


@pytest.mark.smoke
def test_core_functionality():
    assert 1 == 1


@pytest.mark.slow
def test_complex_computation():
    assert 1 == 1


@pytest.mark.slow
def test_very_complex_computation():
    assert 1 == 1
