import pytest
from task2 import Point3D

@pytest.mark.parametrize("func, in_func, expected_res",[
    ("distance_to_point",[2,1,3], 2.449489742783178),
    ("distance_to_origin", "*[]",5.830951894845301),
    ("to_spherical_coordinates","*[]",(5.830951894845301, 45.0, 46.68614334171696)),
    ("to_cylindrical_coordinates", "*[]", (4.242640687119285, 45.0, 4)),
    ("find_closest_point", [[1, 3, 3], [2, 1, 2]], [1, 3, 3])
])
def test_task2(func, in_func, expected_res):
    point = Point3D()
    result = eval(f"point.{func}({in_func})")
    assert result == expected_res
