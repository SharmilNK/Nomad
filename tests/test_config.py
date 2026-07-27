"""Smoke tests for nomad.config.

These require no OpenAI API key and no Raspberry Pi hardware — they only check
that paths, environment defaults, and directory creation behave as expected.
"""
import importlib

import pytest


def test_config_imports():
    cfg = importlib.import_module("nomad.config")
    assert cfg.PROJECT_ROOT.name
    assert cfg.DATA_DIR == cfg.PROJECT_ROOT / "data"
    # A few derived directories should live under DATA_DIR.
    assert cfg.DB_DIR.parent == cfg.DATA_DIR
    assert cfg.SAMPLES_DIR.parent == cfg.DATA_DIR


def test_default_env_values(monkeypatch):
    monkeypatch.delenv("PI_HOST", raising=False)
    monkeypatch.delenv("VISION_POLL_INTERVAL", raising=False)
    monkeypatch.delenv("SIGN_CONFIDENCE_THRESHOLD", raising=False)

    import nomad.config as cfg
    importlib.reload(cfg)

    assert cfg.PI_HOST.startswith("http")
    assert isinstance(cfg.VISION_POLL_INTERVAL, int)
    assert isinstance(cfg.IMAGE_POLL_INTERVAL, int)
    assert cfg.SIGN_CONFIDENCE_THRESHOLD == pytest.approx(0.3)


def test_ensure_dirs_creates_directories(tmp_path, monkeypatch):
    import nomad.config as cfg
    importlib.reload(cfg)

    targets = (tmp_path / "a", tmp_path / "b" / "c")
    monkeypatch.setattr(cfg, "ALL_DIRS", targets)
    cfg.ensure_dirs()

    for target in targets:
        assert target.is_dir()
