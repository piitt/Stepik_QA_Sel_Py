import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example():
    import random
    assert random.choice([True, False])
    # assert False
