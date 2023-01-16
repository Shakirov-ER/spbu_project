import pytest

from hottest_month_and_city import get_hottest_month_and_city


@pytest.mark.parametrize(
    "year, expected_city, expected_month",
    [
        (1980, "Baghdad", 7),
        (1991, "Nagpur", 5),
    ],
)
def test_get_hottest_month_and_city(year: int, expected_city: str, expected_month: int):
    answer = get_hottest_month_and_city(
        "archive.zip", "GlobalLandTemperaturesByMajorCity.csv", year
    )

    assert answer["hottest_month"] == expected_month
    assert answer["hottest_city"] == expected_city
