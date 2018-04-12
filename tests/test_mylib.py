import sys
from pathlib import Path

# configure paths
sys.path.append(str(Path('.')))

from mylib import suma

def test_suma01():
    assert suma(1, 2, 3) == 6
    assert suma(0, 0, 0) == 0
    assert suma(-1, 1, -1, 1) == 0
    assert suma(1/4, 1/4, 1/4, 1/4) == 1