import csv
from decimal import Decimal
import Calc

"""
    Test program for PHYS299 Summer 2020 Research Project
    With Dr. Stephen Rodrigue
    Author: Patrick Brown
"""

"""
    Module 2: Ladder Paradox, aka Barn-Pole Paradox
"""
v = Decimal(3.0)
c = Decimal(5.0)
g = Decimal(4.0)
velocity = Calc.ec.divide(v, c)
gamma = Calc.ec.divide(c, g)
filename = 'LadderData.csv'
barnFile = 'BarnFrame.csv'
ladderFile = 'LadderFrame.csv'

# Coordinates (Barn: (X, CT), Ladder: (X', CT'))
fields = ['Row', 'X', 'CT', 'X\'', 'CT\'']
ladder_dict = [{'Row': 1, 'X': -3, 'CT': -9, 'X\'': 3, 'CT\'': -9},
               {'Row': 2, 'X': 0, 'CT': -4, 'X\'': 3, 'CT\'': -5},
               {'Row': 3, 'X': 3, 'CT': 1, 'X\'': 3, 'CT\'': -1},
               {'Row': 4, 'X': -3, 'CT': -5, 'X\'': 0, 'CT\'': -4},
               {'Row': 5, 'X': 0, 'CT': 0, 'X\'': 0, 'CT\'': 0},
               {'Row': 6, 'X': 3, 'CT': 5, 'X\'': 0, 'CT\'': 4},
               {'Row': 7, 'X': -3, 'CT': -1, 'X\'': -3, 'CT\'': 1},
               {'Row': 8, 'X': 0, 'CT': 4, 'X\'': -3, 'CT\'': 5},
               {'Row': 9, 'X': 3, 'CT': 9, 'X\'': -3, 'CT\'': 9},
               {'Row': 10, 'X': -3, 'CT': 0, 'X\'': '', 'CT\'': ''},
               {'Row': 11, 'X': 3, 'CT': 0, 'X\'': '', 'CT\'': ''},
               {'Row': 12, 'X': '', 'CT': '', 'X\'': -3, 'CT\'': 0},
               {'Row': 13, 'X': '', 'CT': '', 'X\'': 3, 'CT\'': 0}]

# Barn Reference Frame SL Intervals (Barn at origin)
fields_bsl = ['Row', 'Barn Int', 'Ladder Int']
sl_barn_dict = [{'Row': 1, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 2, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 3, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 4, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 5, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 6, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 7, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 8, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 9, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 10, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 11, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 12, 'Barn Int': '', 'Ladder Int': ''},
                {'Row': 13, 'Barn Int': '', 'Ladder Int': ''}]

# Ladder Reference Frame SL Intervals (Ladder at origin)
fields_lsl = ['Row', 'Ladder Int', 'Barn Int']
sl_ladder_dict = [{'Row': 1, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 2, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 3, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 4, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 5, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 6, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 7, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 8, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 9, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 10, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 11, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 12, 'Ladder Int': '', 'Barn Int': ''},
                  {'Row': 13, 'Ladder Int': '', 'Barn Int': ''}]


ladder_dict[9]['X\''], ladder_dict[9]['CT\''] = Calc.getCoords(velocity, gamma,
                                                               ladder_dict[9]['X'], ladder_dict[9]['CT'], None, None)
ladder_dict[10]['X\''], ladder_dict[10]['CT\''] = Calc.getCoords(velocity, gamma,
                                                                 ladder_dict[10]['X'], ladder_dict[10]['CT'], None,
                                                                 None)
ladder_dict[11]['X'], ladder_dict[11]['CT'] = Calc.getCoords(velocity, gamma,
                                                             None, None, ladder_dict[11]['X\''],
                                                             ladder_dict[11]['CT\''])
ladder_dict[12]['X'], ladder_dict[12]['CT'] = Calc.getCoords(velocity, gamma,
                                                             None, None, ladder_dict[12]['X\''],
                                                             ladder_dict[12]['CT\''])

for rows, val in enumerate(sl_barn_dict):
    sl_barn_dict[rows+9]['Barn Int'] = Calc.getSpaceIntv(Calc.coordDiff(ladder_dict[rows+10]['X'], ladder_dict[rows+9]['X'],
                                                         ladder_dict[rows+10]['CT'], ladder_dict[rows+9]['CT']))
    sl_barn_dict[rows+9]['Ladder Int'] = Calc.getSpaceIntv(Calc.coordDiff(ladder_dict[rows+10]['X\''], ladder_dict[rows+9]['X\''],
                                                           ladder_dict[rows+10]['CT\''], ladder_dict[rows+9]['CT\'']))
    sl_ladder_dict[rows+9]['Ladder Int'] = Calc.getSpaceIntv(Calc.coordDiff(ladder_dict[rows+10]['X'], ladder_dict[rows+9]['X'],
                                                             ladder_dict[rows+10]['CT'], ladder_dict[rows+9]['CT']))
    sl_ladder_dict[rows+9]['Barn Int'] = Calc.getSpaceIntv(Calc.coordDiff(ladder_dict[rows+10]['X\''], ladder_dict[rows+9]['X\''],
                                                           ladder_dict[rows+10]['CT\''], ladder_dict[rows+9]['CT\'']))
    if rows+9 == 11 or rows+10 == 12:
        break

# writing to csv file
with open(filename, 'w', newline='') as csv_file:
    # creating a csv dict writer object
    writer = csv.DictWriter(csv_file, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(ladder_dict)
    csv_file.close()
    print('\r', filename, 'Complete\n')

with open(barnFile, 'w', newline='') as csv_file:
    # creating a csv dict writer object
    writer = csv.DictWriter(csv_file, fieldnames=fields_bsl)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(sl_barn_dict)
    csv_file.close()
    print('\r', barnFile, 'Complete\n')

with open(ladderFile, 'w', newline='') as csv_file:
    # creating a csv dict writer object
    writer = csv.DictWriter(csv_file, fieldnames=fields_lsl)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(sl_ladder_dict)
    csv_file.close()
    print('\r', ladderFile, 'Complete\n')
