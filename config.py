new_width = 1000  # New width
new_height = 1000  # New height
locations_config = {
    'STN_HD_1': 
    { #done
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(0, 0), (new_width//8, 0), (new_width//8, new_height), (0, new_height)],
            'J2': [(new_width//8, 0), (7*new_width//8, 0), (7*new_width//8, new_height//5), (new_width//8, new_height//5)],
            'J3': [(7*new_width//8, 0), (new_width, 0), (new_width, new_height), (7*new_width//8, new_height)],
      
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'Sty_Wll_Ldge_FIX_3': 
    { # done
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(16, 33), (556, 34), (556, 252), (18, 253)],
            'J2': [(16, 324), (555, 325), (555, 582), (16, 582)],  # Adjusted J2 as A
      
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'SBI_Bnk_JN_FIX_1': 
    { # done
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(5, 530), (560, 530), (560, 750), (5, 750)],
            'J2': [(250, 30), (650, 30), (650, 250), (250, 250)],
            'J3': [(820, 210), (990, 210), (990, 805), (820, 805)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'SBI_Bnk_JN_FIX_3': 
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(150, 145), (750, 145), (750, 365), (150, 365)],
            'J2': [(150, 480), (910, 480), (910, 700), (150, 700)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    '18th_Crs_BsStp_JN_FIX_2': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(180, 150), (830, 150), (830, 405), (180, 405)],
            'J2': [(10, 460), (830, 460), (830, 750), (10, 750)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    }, 

    '18th_Crs_Bus_Stop_FIX_2': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(15, 240), (160, 240), (160, 790), (15, 790)],
            'J2': [(200, 10), (650, 10), (650, 230), (200, 230)],
            'J3': [(745, 190), (930, 190), (930, 585), (745, 585)],
            'J4': [(185, 750), (980, 750), (980, 900), (185, 900)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    }, 

    'Ayyappa_Temple_FIX_1': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(210, 140), (990, 140), (990, 400), (210, 400)],
            'J2': [(210, 510), (990, 510), (990, 790), (210, 790)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Devasandra_Sgnl_JN_FIX_1': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(5, 182), (790, 181), (791, 430), (3, 433)],
            'J2': [(5, 487), (790, 485), (791, 771), (4, 765)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Devasandra_Sgnl_JN_FIX_3': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(60, 10), (800, 10), (800, 230), (60, 230)],
            'J2': [(0, 250), (150, 250), (150, 810), (0, 810)],
            'J3': [(815, 230), (1000, 230), (1000, 815), (815, 815)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'Mattikere_JN_FIX_1': { #check
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(230, 150), (970, 240), (970, 540), (230, 470)],
            'J2': [(5, 215), (150, 215), (150, 800), (5, 800)],
            'J3': [(840, 570), (985, 570), (985, 810), (840, 810)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'Mattikere_JN_FIX_2': { #done
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(110, 20), (640, 20), (640, 240), (110, 240)],
            'J2': [(825, 190), (995, 190), (995, 640) , (825, 640)],
            'J3': [(130, 750), (895, 750), (895, 825), (130, 825)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'Mattikere_JN_FIX_3': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(110, 5), (340, 5), (340, 850), (110, 850)],
            'J2': [(370, 5), (890, 5), (890, 855), (370, 855)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Mattikere_JN_HD_1': {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(15, 160), (175, 160), (175, 705), (15, 705)],
            'J2': [(300, 45), (780, 45), (780, 265), (300, 265)],
            'J3': [(840, 240), (1000, 240), (1000, 705), (840, 705)],
            'J4': [(130, 750), (895, 750), (895, 900), (130, 900)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'HP_Ptrl_Bnk_BEL_Rd_FIX_2': #done
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(250, 140), (1000, 140), (1000, 395), (250, 395)],
            'J2': [(420, 410), (1000, 410), (1000, 695), (420, 695)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Kuvempu_Circle_FIX_1': 
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(240, 5), (390, 5), (390, 910), (240, 910)],
            'J2': [(590, 8), (740, 8), (740, 910), (590, 910)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Kuvempu_Circle_FIX_2': 
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(240, 5), (390, 5), (390, 910), (240, 910)],
            'J2': [(590, 8), (740, 8), (740, 910), (590, 910)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'MS_Ramaiah_JN_FIX_1': {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(200, 150), (610, 150), (610, 440), (200, 440)],
            'J2': [(800, 170), (990, 170), (990, 820), (800, 820)],
            'J3': [(1, 720), (640, 720), (640, 900), (1, 900)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'MS_Ramaiah_JN_FIX_2': {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(10, 40), (160, 40), (160, 795), (10, 795)],
            'J2': [(240, 11), (630, 11), (630, 230), (240, 230)],
            'J3': [(820, 235), (970, 235), (970, 815), (820, 815)],
            'J4': [(175, 760), (775, 760), (775, 900), (175, 900)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'FA': ['J3', 'J1'],
            'FC': ['J3', 'J2'],

        }
    },

    'Ramaiah_BsStp_JN_FIX_1': 
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(220, 105), (915, 105), (915, 400), (220, 400)],
            'J2': [(30, 425), (730, 425), (730, 720), (30, 720)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },

    'Ramaiah_BsStp_JN_FIX_2': 
    {
        'video_path': r'/path',
        'new_width': 1000,
        'new_height': 1000,
        'regions': {
            'J1': [(290, 60), (990, 60), (990, 355), (290, 355)],
            'J2': [(250, 420), (990, 420), (990, 710), (250, 710)],
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'DA': ['J2', 'J1'],
        }
    },
}
