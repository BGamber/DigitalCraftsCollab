def blue_moons(start_month, start_day, start_year, end_year):
    days_per_month = {1: 31, 2: (28, 29), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    full_moons = []
    day = float(start_day)
    month = start_month
    for year in range(start_year, end_year):
        while month <= 12:
            if year % 4 == 0 and month == 2:
                days_this_month = days_per_month[month][1]
            elif year % 4 != 0 and month == 2:
                days_this_month = days_per_month[month][0]
            else:
                days_this_month = days_per_month[month]

            while int(day) <= days_this_month:
                full_moons.append((month, day, year))
                day += 29.538
            
            month += 1
            day -= float(days_this_month)
        month = 1

    total_blue_moons = 0
    prev_moon = full_moons[0]
    for moon in range(1, len(full_moons)):
        if full_moons[moon][0] == prev_moon[0] and full_moons[moon][2] == prev_moon[2]:
            total_blue_moons += 1
        prev_moon = full_moons[moon]

    return total_blue_moons

# print 'TEST 1:'
assert blue_moons(1, 21, 2000, 2001) == 0, 'There is no blue moon'
# print 'TEST 2:'
assert blue_moons(1, 2, 2018, 2020) == 2, 'There are 2 blue moons in 2018'
# print 'TEST 3:'
assert blue_moons(1, 21, 2000, 2020) == 8, 'There are 8 blue moons from 2000 to 2019'
# print 'TEST 4:'
assert blue_moons(1, 7, 2004, 2006) + blue_moons(1, 3, 2007, 2013) == 4, 'There should be 5 blue moons in these date ranges'

print blue_moons(1, 21, 2000, 3000)