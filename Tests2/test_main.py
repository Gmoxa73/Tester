import types
import pytest
from Netolya.Tester2.main2 import flat_generator

@pytest.mark.parametrize(
    'sp, res',
    (
        (
            [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None],
        ),
        (
            [['a', 'b', 't', 'd'], ['e', 'f', 'h', False, 1], [2, None]],
            ['a', 'b', 't', 'd', 'e', 'f', 'h', False, 1, 2, None],
        ),
        (
            [['a', 'b'], ['c', 'd', 'e', 'f', 'h', True, 1, 2, None]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', True, 1, 2, None],
        ),
    )
)
def test_flat_generator(sp, res):
    for flat_iterator_item, check_item in zip(
            flat_generator(sp),
            res
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(sp)) == res

    assert isinstance(flat_generator(sp), types.GeneratorType)