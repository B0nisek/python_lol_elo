from src.Enums import League, Division
from src.LolLpCalculator import calculate_lp


def test_calculation(league_from, division_from, league_to, division_to, expected):
    test_name = "{} {} -> {} {}".format(league_from.name, division_from.name,
                                        league_to.name, division_to.name)
    result = calculate_lp(league_from, division_from, league_to, division_to)
    assert_result(result, expected, test_name)


def assert_result(result, expected, test_name):
    if result == expected:
        print("{} - OK".format(test_name))
    else:
        print("{} - FAILED. Expected {} but was {}.".format(test_name, expected, result))


test_calculation(League.IRON, Division.III, League.IRON, Division.II, 140)
test_calculation(League.GOLD, Division.IV, League.GOLD, Division.I, 420)
test_calculation(League.PLATINUM, Division.I, League.DIAMOND, Division.IV, 160)
test_calculation(League.BRONZE, Division.III, League.GOLD, Division.II, 1300)
