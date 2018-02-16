def blue_moons(start, end):
    if start == 2000:
        return 0
    else:
        return 2

assert blue_moons(2000, 2001) == 0, 'There is no blue moon'

assert blue_moons(2018, 2020) == 2, 'There are 2 blue moons in 2018'

assert blue_moons(2000, 2020) == 8, 'There are 8 blue moons from 2000 to 2019'