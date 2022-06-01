from pathlib import Path

import pytest

import pvxarray  # noqa: F401


@pytest.fixture
def bahamas_rgb():
    return Path(Path(__file__).parent, "data", "bahamas_rgb.tif").absolute()
