import pytest
from auto import Auto

@pytest.mark.parametrize("funct, in_func, expected_result",[
    ("go_to_city", [60,55], False),
    ("distance_to_gps_point", [40, 30], 17699.147518735397),
    ("trip_cost", "*[[40, 30], 40]", 141593.1801498832),
    ("time_trip", [20, 15], 88.55732210238973),
    ("price_loss","*[]", 2000000),
])
def test_auto(funct, in_func, expected_result):
    auto = Auto()
    result = eval(f"auto.{funct}({in_func})")
    assert result == expected_result