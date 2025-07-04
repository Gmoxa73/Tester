import pytest
from Netolya.Tester3.main3 import solve

@pytest.mark.parametrize(
    'boys, girl, res',
    (
        (
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'] ,
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"
        ),
        (
            ['Peter', 'Alex', 'John', 'Arthur'],
            ['Peter', 'Alex', 'John', 'Arthur'],
            "Alex и Alex, Arthur и Arthur, John и John, Peter и Peter"
        ),
        (
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            ['Kate', 'Liza', 'Kira', 'Emma'],
            "Кто-то может остаться без пары!"
        ),
    )
)
def test_solve(boys, girl, res):
    result = solve(boys, girl)
    assert result == res

