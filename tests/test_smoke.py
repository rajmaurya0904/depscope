"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import depscope


def test_version_is_set() -> None:
    assert depscope.__version__
