TECHNOLOGY = {
    'UT': 0,
    'EC': 1,
    0: 'UT',
    1: 'EC'
}

DATA_TYPE = {
    'All': 0, 
    'Amplitude': 1, 
    'Position': 2, 
    'Alarm': 3, 
    'Wall Thickness': 4, 
    'Wall Thickness Alarm': 5, 
    'Outer Diameter': 6,
    'Outer Diameter Alarm': 7,
    'Inner Diameter': 8,
    'Inner Diameter Alarm': 9,
    'XY Data': 10, #Start EC data types
    'X Data': 11, 
    'Y Data': 12, #End EC data types
    0: 'All',
    1: 'Amplitude',
    2: 'Position',
    3: 'Alarm',
    4: 'Wall Thickness',
    5: 'Wall Thickness Alarm',
    6: 'Outer Diameter',
    7: 'Outer Diameter Alarm',
    8: 'Inner Diameter',
    9: 'Inner Diameter Alarm',
    10: 'XY Data',
    11: 'X Data',
    12: 'Y Data'
}

MODE = {
    'All': 0, #Wildcard
    'Longitudinal': 1,
    'Transversal': 2,
    'Dimensional': 3,
    'Coupling': 4,
    'Long Wave': 5,
    'Lamination': 6,
    'Oblique': 7,
    'Shear Wave': 8,
    'EC': 9, #EC Types Wildcard
    'Head': 10, #Start RIS modes
    'Head Side': 11,
    'Web': 12,
    'Flange': 13,
    'Base': 14, #End RIS modes
    0: 'All',
    1: 'Longitudinal',
    2: 'Transversal',
    3: 'Dimensional',
    4: 'Coupling',
    5: 'Long Wave',
    6: 'Lamination',
    7: 'Oblique',
    8: 'Shear Wave',
    9: 'EC',
    10: 'Head',
    11: 'Head Side',
    12: 'Web',
    13: 'Flange',
    14: 'Base'
}

GROUP_TYPE = {
    'All': 0, #Wildcard
    'Normal': 1, #1-256
    'Global': 2, #1000-1031
    'Mapping': 3, #2500-2699
    'RL': 4, #Start EC group types
    'RH': 5, 
    'LD': 6, 
    'LO': 7, #End EC group types
    0: 'All',
    1: 'Normal',
    2: 'Global',
    3: 'Mapping',
    4: 'RL',
    5: 'RH',
    6: 'LD',
    7: 'LO'}

JUDGEMENT = {
    'Not Inspected': 0, 
    'Accepted': 1, 
    'Rejected': 2, 
    'Suspect': 3, #Emergency Stop
    'Data Mismatch': 4, #Deprecated
    'Algo Alarm': 5, #Internal Use Only
    0: 'Not Inspected',
    1: 'Accepted',
    2: 'Rejected',
    3: 'Suspect',
    4: 'Data Mismatch',
    5: 'Algo Alarm'
}

#ERROR IN DOCUMENTATION, SAME JSON VALUES
ORIENTATION = {
    'All': 0, #Wildcard
    'CW': 1, #Longitudinal Clockwise
    'CCW': 2, #Longitudinal Counter Clockwise
    'FW': 3, #Transversal Forward
    'BW': 4, #Transversal Backward
    'RH': 5, #Oblique Right Hand
    'LH': 6, #Oblique Left Hand
    'BR': 1, #RIS Brand
    'ST': 2, #RIS Stamp
    0: 'All',
    1: 'BR',
    2: 'ST',
    3: 'FW',
    4: 'BW',
    5: 'RH',
    6: 'LH',
}

INSPECTION_DIRECTION = {
    'Normal': 0,
    'Reverse': 1,
    0: 'Normal',
    1: 'Reverse'
}