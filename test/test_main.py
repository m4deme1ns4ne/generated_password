import random
import pytest
import string

from src.main import generated_password

@pytest.mark.parametrize(
                'l',
    [
        num for num in range(5, 105)
    ]
)
def test_main(l):
    assert generated_password(l) != generated_password(l)
    assert generated_password(l) != ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(len(generated_password(l))))