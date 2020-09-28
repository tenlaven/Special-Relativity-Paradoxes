import csv
from decimal import Decimal
import Calc

"""
    Test program for PHYS299 Summer 2020 Research Project
    With Dr. Stephen Rodrigue
    Author: Patrick Brown
"""

"""
    Module 1: Twin Planet Paradox, aka Time Dilation Paradox
"""

# Initial velocity (will be user defined) (C = 1)
v = Decimal('21.00')
c = Decimal('29.00')
velocity_launch = Calc.ec.divide(v, c)  # (appx. 0.724137931)
# velocity_return = Calc.addVelocity(v, c)

print('\nTable 1: Earth Rest Frame Coordinates')
"""
    Table 1: Event Points in Earth Rest Frame
    Spacetime Coordinates x values are position,
    t values are time in LY, in relation to Earth,
    with target at origin, positions remain constant.
"""
# Coordinates
earth_x = Decimal('-21.00')
target_x = Decimal('0.00')
launch_t = Decimal('-29.00')
arrival_t = Decimal('0.00')
return_t = Decimal('29.00')

filename = "DataOutput.csv"
fields = ["Row", "Event Point", "Earth Frame", "Rocket Frame 1", "Rocket Frame 2", "Rocket Frame"]
table_one = [{'Row': '1', 'Event Point': 'Launch: Earth', 'Earth Frame': '({}, {})'.format(earth_x, launch_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '2', 'Event Point': 'Launch: Target', 'Earth Frame': '({}, {})'.format(target_x, launch_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '3', 'Event Point': 'Arrival: Earth', 'Earth Frame': '({}, {})'.format(earth_x, arrival_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '(), ()'},
             {'Row': '4', 'Event Point': 'Arrival: Target', 'Earth Frame': '({}, {})'.format(target_x, arrival_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '5', 'Event Point': 'Return: Earth', 'Earth Frame': '({}, {})'.format(earth_x, return_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '6', 'Event Point': 'Return: Target', 'Earth Frame': '({}, {})'.format(target_x, return_t),
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'}]

table_two = [{'Row': '1', 'Event Point': 'Launch: Earth', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '2', 'Event Point': 'Launch: Target', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '3', 'Event Point': 'Arrival: Earth', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '4', 'Event Point': 'Arrival: Target', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '5', 'Event Point': 'Return: Earth', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
             {'Row': '6', 'Event Point': 'Return: Target', 'Earth Frame': '()',
              'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'}]

table_three_a = [{'Row': '1', 'Event Point': 'Launch: Earth', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '2', 'Event Point': 'Launch: Target', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '3', 'Event Point': 'Arrival: Earth', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '4', 'Event Point': 'Arrival: Target', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '5', 'Event Point': 'Sum of Intervals', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'}]

table_three_b = [{'Row': '1', 'Event Point': 'Launch: Earth', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '2', 'Event Point': 'Launch: Target', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '3', 'Event Point': 'Arrival: Earth', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '4', 'Event Point': 'Arrival: Target', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'},
                 {'Row': '5', 'Event Point': 'Sum of Intervals', 'Earth Frame': '()',
                  'Rocket Frame 1': '()', 'Rocket Frame 2': '()', 'Rocket Frame': '()'}]
tables = (table_one, table_two, table_three_a, table_three_b)

##################################################
##################################################

print('\rTable 1: Rocket Rest Frame Coordinates')
"""
    Table 1: Event Points in Rocket Rest Frames
"""
# Coordinate Transformations
rocket_launch_earth = Calc.getCoords(velocity_launch, Calc.getGamma(velocity_launch), earth_x, launch_t, None, None)
rocket_launch_target = Calc.getCoords(velocity_launch, Calc.getGamma(velocity_launch), target_x, launch_t, None, None)
rocket_arrival_earth_a = Calc.getCoords(velocity_launch, Calc.getGamma(velocity_launch), earth_x, arrival_t, None, None)
rocket_arrival_earth_b = -rocket_arrival_earth_a[0], -rocket_arrival_earth_a[1]
rocket_arrival_target = Calc.getCoords(velocity_launch, Calc.getGamma(velocity_launch), target_x, arrival_t, None, None)
rocket_return_earth = Calc.getCoords(-velocity_launch, Calc.getGamma(velocity_launch), earth_x, return_t, None, None)
rocket_return_target = Calc.getCoords(velocity_launch, Calc.getGamma(velocity_launch), target_x, return_t, None, None)

table_one[0]['Rocket Frame'] = str(rocket_launch_earth)
table_one[1]['Rocket Frame'] = str(rocket_launch_target)
table_one[2]['Rocket Frame'] = f"{rocket_arrival_earth_a}; {rocket_arrival_earth_b}"
table_one[3]['Rocket Frame'] = str(rocket_arrival_target)  # .format(str(a_intv_a), str(a_intv_b))
table_one[4]['Rocket Frame'] = str(rocket_return_earth)
table_one[5]['Rocket Frame'] = str(rocket_return_target)
##################################################
##################################################

print('\rTable 2: Earth Rest Frames Spacelike Intervals')
"""
    Table 2: Earth to Target Event Points
    Generates Spacelike Interval for Earth Frame for:
    Earth(1) to Target(2)
    Earth(3) to Target(4)
    Earth(5) to Target(6)
"""
# Generate new coordinates
ltup = Calc.coordDiff(target_x, earth_x, launch_t, launch_t)
atup = Calc.coordDiff(target_x, earth_x, arrival_t, arrival_t)
rtup = Calc.coordDiff(target_x, earth_x, return_t, return_t)

# Calculate SL Intv.
l_intv = Calc.getSpaceIntv(ltup)
a_intv = Calc.getSpaceIntv(atup)
r_intv = Calc.getSpaceIntv(rtup)

table_two[0]['Earth Frame'] = str(ltup)
table_two[1]['Earth Frame'] = str(l_intv)
table_two[2]['Earth Frame'] = str(atup)
table_two[3]['Earth Frame'] = str(a_intv)
table_two[4]['Earth Frame'] = str(rtup)
table_two[5]['Earth Frame'] = str(r_intv)

##################################################
##################################################

print('\rTable 2: Rocket Rest Frames Spacelike Intervals')
"""
    Table 2: Rocket Event Points
    Generates Spacelike Interval for Rocket Frame for:
    Earth(1) to Target(2)
    Earth(3) to Target(4)
    Earth(5) to Target(6)
"""

# Generate new coordinates
ltup = Calc.coordDiff(rocket_launch_target[0], rocket_launch_earth[0], rocket_launch_target[1], rocket_launch_earth[1])
atup_a = Calc.coordDiff(rocket_arrival_target[0], rocket_arrival_earth_a[0], rocket_arrival_target[1],
                        rocket_arrival_earth_a[1])
atup_b = Calc.coordDiff(rocket_arrival_target[0], rocket_arrival_earth_b[0], rocket_arrival_target[1],
                        rocket_arrival_earth_b[1])
rtup = Calc.coordDiff(rocket_return_target[0], rocket_return_earth[0], rocket_return_target[1], rocket_return_earth[1])

# Calculate SL Intv.
l_intv = Calc.getSpaceIntv(ltup)
a_intv_a = Calc.getSpaceIntv(atup_a)
a_intv_b = Calc.getSpaceIntv(atup_b)
r_intv = Calc.getSpaceIntv(rtup)

table_two[0]['Rocket Frame'] = str(ltup)
table_two[1]['Rocket Frame'] = str(l_intv)
table_two[2]['Rocket Frame'] = str(atup)
table_two[3]['Rocket Frame'] = f"{a_intv_a}; {a_intv_b}"  # .format(str(a_intv_a), str(a_intv_b))
table_two[4]['Rocket Frame'] = str(rtup)
table_two[5]['Rocket Frame'] = str(r_intv)

##################################################
##################################################

print('\rTable 3a: Earth Rest Frames Timelike Intervals')
"""
    Table 3a: Earth Event Points
    Generates Timelike Intervals for:
    Earth/Target Launch (1/2) to Earth/Target Arrival (3/4) and
    Earth/Target Arrival (3/4) to Earth/Target Return (5/6)
"""

# Generate new coordinates
latup_e = Calc.coordDiff(earth_x, earth_x, arrival_t, launch_t)  # [E1>E3] (-21, -29) to (-21, 0) -> (0, 29)
latup_t = Calc.coordDiff(target_x, target_x, arrival_t, launch_t)  # [T2>T4] (0, -29) to (0, 0) -> (0, 29)
artup_e = Calc.coordDiff(earth_x, earth_x, return_t, arrival_t)  # [E3>E5] (-21, 0) to (-21, 29) -> (0, 29)
artup_t = Calc.coordDiff(target_x, target_x, return_t, arrival_t)  # [T4>T6] (0, 0) to (0, 29) -> (0, 29)

# Calculate TL Intv.
if latup_e == latup_t and artup_e == artup_t:
    la_intv = Calc.getTimeIntv(latup_e)
    ar_intv = Calc.getTimeIntv(artup_e)
    intv_sum = Calc.ec.add(la_intv, ar_intv)
else:
    raise Exception("One of these things is not like the other...")

table_three_a[0]['Earth Frame'] = str(latup_e)
table_three_a[1]['Earth Frame'] = str(la_intv)
table_three_a[2]['Earth Frame'] = str(artup_e)
table_three_a[3]['Earth Frame'] = str(ar_intv)
table_three_a[4]['Earth Frame'] = str(intv_sum)

##################################################
##################################################

print('\rTable 3a: Rocket Rest Frames Timelike Intervals')
"""
    Table 3a: Rocket Event Points
    Generates Timelike Intervals for:
    Earth/Target Launch (1/2) to Earth/Target Arrival (3/4) and
    Earth/Target Arrival (3/4) to Earth/Target Return (5/6)
"""

# Generate new coordinates
# Points used are before rocket rotation
latup_e = Calc.coordDiff(rocket_arrival_earth_a[0], rocket_launch_earth[0],  # [E1>E3] (0, -20) to (-30.45, 22.05)
                         rocket_arrival_earth_a[1], rocket_launch_earth[1])  # -> (-30.45, 42.05)
latup_t = Calc.coordDiff(rocket_arrival_earth_a[0], rocket_launch_earth[0],  # [T2>T4] (30.45, -42.05) to (0, 0)
                         rocket_arrival_earth_a[1], rocket_launch_earth[1])  # -> (-30.45, 42.05)
# Points used are after rocket rotation
artup_e = Calc.coordDiff(rocket_return_earth[0], rocket_arrival_earth_b[0],  # [E3>E5] (30.45, -22.05) to (0, 20)
                         rocket_return_earth[1], rocket_arrival_earth_b[1])  # -> (-30.45, 42.05)
artup_t = Calc.coordDiff(rocket_return_earth[0], rocket_arrival_earth_b[0],  # [T4>T6] (0, 0) to (-30.45, 42.05)
                         rocket_return_earth[1], rocket_arrival_earth_b[1])  # -> (-30.45, 42.05)

if latup_e == latup_t and artup_e == artup_t:
    la_intv = Calc.getTimeIntv(latup_e)
    ar_intv = Calc.getTimeIntv(artup_e)
    intv_sum = Calc.ec.add(la_intv, ar_intv)
else:
    raise Exception("One of these things is not like the other...")

table_three_a[0]['Rocket Frame'] = str(latup_e)
table_three_a[1]['Rocket Frame'] = str(la_intv)
table_three_a[2]['Rocket Frame'] = str(artup_e)
table_three_a[3]['Rocket Frame'] = str(ar_intv)
table_three_a[4]['Rocket Frame'] = str(intv_sum)

##################################################
##################################################

print('\rTable 3b: Earth Rest Frames Timelike Intervals')
"""
    Table 3b: Earth Event Points
    Generates Timelike Intervals for:
    Earth Launch (1) to Target Arrival (4) and
    Target Arrival (4) to Earth Return (5)
"""

# Generate new coordinates
latup = Calc.coordDiff(target_x, earth_x, arrival_t, launch_t)  # (-21, -29) to (0, 0) -> (21, 29)
artup = Calc.coordDiff(earth_x, target_x, return_t, arrival_t)  # (0, 0) to (-21, 29) -> (-21, 29)

# Calculate TL Intv.
la_intv = Calc.getTimeIntv(latup)
ar_intv = Calc.getTimeIntv(artup)
intv_sum = Calc.ec.add(la_intv, ar_intv)

table_three_b[0]['Earth Frame'] = str(latup)
table_three_b[1]['Earth Frame'] = str(la_intv)
table_three_b[2]['Earth Frame'] = str(artup)
table_three_b[3]['Earth Frame'] = str(ar_intv)
table_three_b[4]['Earth Frame'] = str(intv_sum)

##################################################
##################################################

print('\rTable 3b: Rocket Rest Frames Timelike Intervals')
"""
    Table 3b: Rocket Event Points
    Generates Timelike Intervals for:
    Earth Launch (1) to Target Arrival (4) and
    Target Arrival (4) to Earth Return (5)
"""

# Generate new coordinates
# Points used are before rocket rotation
latup = Calc.coordDiff(rocket_arrival_target[0], rocket_launch_earth[0],
                       rocket_arrival_target[1], rocket_launch_earth[1])
# Points used are after rocket rotation
artup = Calc.coordDiff(rocket_return_earth[0], rocket_arrival_target[0],
                       rocket_return_earth[1], rocket_arrival_target[1])
# Calculate TL Intv.
tl_intv_a = Calc.getTimeIntv(latup)
tl_intv_b = Calc.getTimeIntv(artup)
intv_sum = Calc.ec.add(tl_intv_a, tl_intv_b)

table_three_b[0]['Rocket Frame'] = str(latup)
table_three_b[1]['Rocket Frame'] = str(tl_intv_a)
table_three_b[2]['Rocket Frame'] = str(artup)
table_three_b[3]['Rocket Frame'] = str(tl_intv_b)
table_three_b[4]['Rocket Frame'] = str(intv_sum)
# format(rocket_launch_earth, '.2f')  "{}; {}".format(str(rocket_arrival_earth_a), str(rocket_arrival_earth_b))

# writing to csv file
with open(filename, 'w', newline='') as csv_file:
    # creating a csv dict writer object
    writer = csv.DictWriter(csv_file, fieldnames=fields)

    # writing headers (fieldnames)
    writer.writeheader()

    # writing data rows
    for i in tables:
        writer.writerows(i)

csv_file.close()
print('\r', filename, 'Complete\n')
