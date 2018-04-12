import sys
from pathlib import Path

# configure paths
sys.path.append(str(Path('.')))

import pytest
from pytest import approx

from mylib import suma

def test_suma01():
    assert suma(1, 2, 3) == 6
    assert suma(0, 0, 0) == 0
    assert suma(-1, 1, -1, 1) == 0
    assert suma(1/4, 1/4, 1/4, 1/4) == 1
    assert suma(1/10, 1/10, 1/10) == approx(0.3)

def test_suma02():
    with pytest.raises(TypeError):
        suma(1, '1')
        suma(1, [1,2,3])
        suma(1, (1,2,3))