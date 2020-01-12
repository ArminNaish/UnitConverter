import pytest
from ..unit_converter import convert

@pytest.mark.parametrize("value,from_unit, to_unit, expected", [
    (5, 'gram', 'kilogram', (5e-3, 'kilogram')),
    (5, 'milligram', 'gram', (5e-3, 'gram')),
    (5,'gram', 'milligram', (5e3, 'milligram')),
    (5, 'kilogram', 'gram', (5e3, 'gram')),
    (5, 'gigagram', 'megagram', (5e3, 'megagram')),
    (5, 'megagram', 'gigagram', (5e-3, 'gigagram')),
])
def test_factor_conversion(value, from_unit, to_unit, expected):
    actual = convert(value, from_unit, to_unit)
    assert actual == expected


@pytest.mark.parametrize("value,from_unit, to_unit, expected", [
    (68, 'degree fahrenheit', 'degree celsius', (20, 'degree celsius')),
    (20, 'degree celsius', 'degree fahrenheit', (68, 'degree fahrenheit'))
])
def test_offset_conversion(value, from_unit, to_unit, expected):
    actual = convert(value, from_unit, to_unit)
    assert actual == expected