"""Tests for the depscope package version."""

from depscope import __version__


def test_version_matches_init():
    assert __version__ == "0.1.1"