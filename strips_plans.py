strips_plans_joint = [
#Agent 1
[set(['in_hallA']),
set(['in_roomA']),
set(['in_roomA', 'taken_flagA']),
set(['in_hallA', 'taken_flagA']),
set(['in_hallB', 'taken_flagA']),
set(['in_roomB', 'taken_flagA']),
set(['in_roomB', 'taken_flagA', 'taken_flagB']),
set(['in_hallB', 'taken_flagA', 'taken_flagB']),
set(['in_hallA', 'taken_flagA', 'taken_flagB']),
set(['in_roomD', 'taken_flagA', 'taken_flagB'])],
#Agent 2
[set(['in_roomE']),
set(['in_roomE', 'taken_flagF']),
set(['in_roomC', 'taken_flagF']),
set(['in_roomC', 'taken_flagF', 'taken_flagC']),
set(['in_hallB', 'taken_flagF', 'taken_flagC']),
set(['in_hallA', 'taken_flagF', 'taken_flagC']),
set(['in_roomD', 'taken_flagF', 'taken_flagC']),
set(['in_roomD', 'taken_flagF', 'taken_flagC', 'taken_flagD'])]
]

strips_plans_individual = [
#Agent 1
[set(['in_hallA']),
set(['in_hallB']),
set(['in_roomC']),
set(['in_roomC', 'taken_flagC']),
set(['in_roomE', 'taken_flagC']),
set(['in_roomE', 'taken_flagC', 'taken_flagE']),
set(['in_roomE', 'taken_flagC', 'taken_flagE', 'taken_flagF']),
set(['in_roomC', 'taken_flagC', 'taken_flagE', 'taken_flagF']),
set(['in_hallB', 'taken_flagC', 'taken_flagE', 'taken_flagF']),
set(['in_roomB', 'taken_flagC', 'taken_flagE', 'taken_flagF']),
set(['in_roomB', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB']),
set(['in_hallB', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB']),
set(['in_hallA', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB']),
set(['in_roomA', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB']),
set(['in_roomA', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB', 'taken_flagA']),
set(['in_hallA', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB', 'taken_flagA']),
set(['in_roomD', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB', 'taken_flagA']),
set(['in_roomD', 'taken_flagC', 'taken_flagE', 'taken_flagF', 'taken_flagB', 'taken_flagA', 'taken_flagD'])],
#Agent 2
[set(['in_roomE']),
set(['in_roomE', 'taken_flagF']),
set(['in_roomE', 'taken_flagF', 'taken_flagE']),
set(['in_roomC', 'taken_flagF', 'taken_flagE']),
set(['in_roomC', 'taken_flagF', 'taken_flagE', 'taken_flagC']),
set(['in_hallB', 'taken_flagF', 'taken_flagE', 'taken_flagC']),
set(['in_roomB', 'taken_flagF', 'taken_flagE', 'taken_flagC']),
set(['in_roomB', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB']),
set(['in_hallB', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB']),
set(['in_hallA', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB']),
set(['in_roomA', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB']),
set(['in_roomA', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB', 'taken_flagA']),
set(['in_hallA', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB', 'taken_flagA']),
set(['in_roomD', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB', 'taken_flagA']),
set(['in_roomD', 'taken_flagF', 'taken_flagE', 'taken_flagC', 'taken_flagB', 'taken_flagA', 'taken_flagD'])]
]





