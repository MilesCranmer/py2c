import numba
import os

os.environ['NUMBA_DUMP_LLVM'] = "1"

@numba.jit
def test(x, y):
    return x+y

test(5, 3)
