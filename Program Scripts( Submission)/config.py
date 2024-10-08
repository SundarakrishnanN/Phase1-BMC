
locations_config = {
    'Stn_HD_1': #verified 
    {
        'regions': {
            'J1': [(0, 0), (180, 0), (180, 810), (0, 810)],  # J1
            'J2': [(180, 0), (1260, 0), (1260, 130), (180, 130)],  # J2
            'J3': [(1260, 0), (1440, 0), (1440, 810), (1260, 810)],
      
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

    'Sty_Wll_Ldge_FIX_3':  #verifeid
    {
      'regions': {
            'J1': [(0, 0), (890, 0), (890, 215), (0, 215)],
            'J2': [(0, 570), (935, 570), (935, 250), (0, 250)],
      
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'SBI_Bnk_JN_FIX_1':  #verified
    {
        'regions': {
                'J1':[(20, 275), (835, 475),(870, 770), (20, 733)],#A , J1
                'J2':[(392, 19), (392, 165), (837, 264), (902, 14)], #B , J2
                'J3':[(1061, 217), (1420, 209), (1420, 779), (880, 779)]
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AC': ['J1', 'J3'],
            'BA': ['J2', 'J1'],
            'BC': ['J2', 'J3'],
            'CA': ['J3', 'J1'],
            'CB': ['J3', 'J2'],

        }
    },

    'SBI_Bnk_JN_FIX_3':  #verified
    {
        'regions': {
            'J1': [(397, 22), (900, 22), (1228, 216), (321, 216)],#A , J1
            'J2': [(291, 263), (1400, 260), (1381, 777), (163, 675)], #B , J2#B , J2
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    '18th_Crs_BsStp_JN_FIX_2': #Verified
    {
        'regions': {
            'J1': [(16, 295), (1198, 293), (1196, 597), (11, 600)],
            'J2': [(260, 247), (258, 76), (1203, 75), (1194, 247)],
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    }, 

    '18th_Crs_Bus_Stop_FIX_2': #verified
    {   
        'regions': {
            'J1':[(15, 125), (325, 180), (325, 690), (21, 791)],#A , J1
            'J2':[(947, 160), (203, 150), (284, 10), (665, 10)], #b and #c , J2
            'J3':[(918, 174), (1255, 224), (1408, 330), (1408, 499)],#d , J3
            'J4':[(100, 780), (1436, 800), (1436, 639), (1250, 400)],#e , J4
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AD': ['J1', 'J3'],
            'CD': ['J2', 'J3'],
            'EB': ['J4', 'J2'],
            'ED': ['J4', 'J3'],
        }
    }, 

    'Ayyappa_Temple_FIX_1': #verified
    {
        'regions': {
            'J1':[(28, 390), (34, 774), (1438, 791), (1438, 227)],#J1 , A
            'J2':[(53,380), (1385, 210), (1074, 13), (69, 24)], #J2 , B     
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Devasandra_Sgnl_JN_FIX_1': #verified
    {
        'regions': {
            'J1':[(9, 260), (1156, 300), (1156, 784), (18, 784)], #J1, A    
            'J2':[(27, 10),(1133, 10), (1150, 280),(8,240)],#J2 , B
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Devasandra_Sgnl_JN_FIX_3': # verified
    {
       'regions': {
            'J1': [(0, 3), (158, 167), (390, 781), (2, 783)],
            'J2': [(26, 3), (145, 120), (469, 100), (430, 0)],
            'J3': [(564, 12), (1200, 15), (1150, 198), (583, 191)],
            'J4': [(1210, 119), (873, 783), (1438, 779), (1432, 111)],
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AD':['J1', 'J4'],
            'CA': ['J3', 'J1'],
            'CD':['J3', 'J4'],
            'DA':['J4', 'J1'],
            'DB':['J4', 'J2'],

         

        }
    },

    'Mattikere_JN_FIX_1': { #verified
        'regions': {
            'J1':[(14, 81), (250, 81), (250, 800), (9, 800)],#J1
            'J2':[(387, 34), (650, 61), (1333, 410), (276, 191)], #J2
            'J3':[(1210, 500), (1210, 799), (1426, 799), (1421, 404)],#J3
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AD': ['J1', 'J3'],
            'CA': ['J2', 'J1'],
            'CD': ['J2', 'J3'],
            'DA': ['J3', 'J1'],
            'DB': ['J3', 'J2'],

        }
    },

    'Mattikere_JN_FIX_2': { #verified
        'regions': {
            'J1':[(215, 16), (162, 128), (845, 134), (601, 21)],#J1 A, B
            'J2':[(1430, 130), (850, 130), (1250, 320), (1430, 420)],#J2 c
            'J3':[(20, 350), (1430, 430), (1430, 790),(13, 790)],#J3 d
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BD': ['J1', 'J3'],
            'CA': ['J2', 'J1'],
            'CD': ['J2', 'J3'],
            'DA': ['J3', 'J1'],
            'DC': ['J3', 'J2'],

        }
    },

    'Mattikere_JN_FIX_3': #verified
    {
        'regions': {
            'J1': [(30, 5), (280, 5), (550, 805), (30, 805)], # felt good as it is
            'J2': [(287 , 5), (1250, 5), (1250, 805), (557, 805)],
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Mattikere_JN_HD_1': {  #verified
        'regions': {
            'J1':[(17, 135), (205, 80), (316, 472), (16, 800)], #J1, A
            'J2':[(1350, 53), (1350, 192), (430, 192), (430, 16)],#J2 B
            'J3':[(1425, 240), (1200, 240), (1200, 567), (1426, 795)],#J3 C
            'J4':[(50, 799), (250, 567), (1178, 583), (1415, 801)] #J4 D
        },
        'turning_patterns': {
            'AC': ['J1', 'J3'],
            'BA': ['J2', 'J1'],
            'BD': ['J2', 'J4'],
            'CA': ['J3', 'J1'],
            'CD': ['J3', 'J4'],
        }
    },

    'HP_Ptrl_Bnk_BEL_Rd_FIX_2': #verified
    {
        'regions': {
            'J1':[(500, 355), (1425, 140), (1427, 800), (511, 797)], #J1 , A
            'J2':[(1300, 140), (500, 345), (464, 21), (1025, 11)], #J2 , B
            
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Kuvempu_Circle_FIX_1': #verified
    {
        'regions': {
            'J1':[(12, 22), (13, 794), (1205, 798), (1300, 550)], #A , J1
            'J2':[(40, 10), (1430, 480), (1430, 10), (936, 10)], #B , J2     
        },
        'turning_patterns': {
            'BA': ['J2', 'J1'],
        }
    },

    'Kuvempu_Circle_FIX_2': #verified
    {
        'regions': {
            'J1':[(11, 22), (18, 626), (1405, 6), (632, 7)], #J1 A
            'J2':[(20, 640), (1425, 10), (1425, 793), (20, 793)], #J2 B 
            
        },
        'turning_patterns': {
            'BA': ['J2', 'J1'],
        }
    },

    'MS_Ramaiah_JN_FIX_1': #verified
    {
        'regions': {
            'J1':[(14, 24), (1307, 19), (960, 350), (14, 350)], #J1 A
            'J2':[(1422, 24), (1320, 24), (1036, 360), (1430, 794)], #J2 B
            'J3':[(14, 370), (960, 370), (1394, 794), (22, 781)], #J3 C
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AC': ['J1', 'J3'],

        }
    },

    'MS_Ramaiah_JN_FIX_2': #verified
    {
        'regions': {
            'J1':[(312, 52), (12, 18), (14, 800), (306, 575)],#J1 A , B
            'J2':[(350, 14), (375, 135), (1001, 144), (802, 14)], #J2 C, D
            'J3':[(1235, 470), (1431, 470), (1416, 200), (1110, 150)],#J3 E
            'J5':[(1060, 480), (1420, 480), (1420, 800), (1060, 640)],#J5 F
            'J4':[(40, 800), (250, 650), (1050, 650), (1400, 800)],#J4 G, H
        },
        'turning_patterns': {
            'BC': ['J1', 'J2'],
            'BE': ['J1', 'J3'],
            'BG': ['J1', 'J4'],
            'DA': ['J2', 'J1'],
            'DE': ['J2', 'J3'],
            'DG': ['J2', 'J5'],
            'FA': ['J5', 'J1'],
            'FC': ['J5', 'J2'],
            'FG': ['J5', 'J4'],
            'HA': ['J4', 'J1'],
            'HC': ['J4', 'J2'],
            'HE': ['J5', 'J3'],
        }
    },

    'Ramaiah_BsStp_JN_FIX_1': #verified
    {
        'regions': {
            'J1':[(11, 366), (9, 786), (1200, 790), (1266, 385)],#J1 A
            'J2':[(300, 70), (300, 353), (1200, 358), (1326, 39)], #J2 B
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Ramaiah_BsStp_JN_FIX_2': #verified
    {
        'regions': {
            'J1':[(14, 340), (30, 781), (1417, 786), (1425, 340)], #J1 A
            'J2':[(9, 10), (17, 333), (1426, 333), (1416, 10)], #J2 B
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },
    'Dari_Anjaneya_Temple': { #verified
        'regions': {
            'J1':[(13, 550), (456, 238), (542, 12), (13, 13)], #J1 A
            'J2':[(602, 16), (503, 229), (1220, 180), (966, 18)], #J2 B
            'J3':[(1427, 60), (1200, 212), (1200, 500), (1427, 793)], #J3 C
            'J4':[(13, 560), (1230, 563), (1405, 797), (21, 788)], #J4 D
        },
        'turning_patterns': {
            'BC': ['J2', 'J3'],
            'BD': ['J2', 'J4'],
            'AD': ['J1', 'J4'],
            'AC': ['J1', 'J3'],
            'CD': ['J3', 'J4'],
        }
    },

    'Nanjudi_House': { #verified
        'regions': {
            'J1':[(170, 420), (418, 209), (735, 230), (732, 420)],#J1 A
            'J2':[(836, 374), (1064, 272), (1416, 343), (1404, 499)], #J2 B
            'J3':[(1427, 793), (1422, 505), (19, 505), (17, 795)], #J3 C
        },
        'turning_patterns': {
            'AC': ['J1', 'J3'],
            'BC': ['J2', 'J3'],
            'CA': ['J3', 'J1'],
            'CB': ['J3', 'J2'],
        }
    },

    'Buddha_Vihara_Temple':  #verified
    {
        'regions': {
            'J1': [(29, 18), (856, 14), (1423, 339), (17, 350)],
            'J2': [(13, 378), (1420, 387), (1425, 793), (17, 796)],
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'Sundaranagar_Entrance':  #verified
    {
        'regions': {
            'J1':[(606, 30), (1110, 21), (1434, 219), (565, 214)], #J1 A
            'J2':[(562, 259), (1433, 259), (1423, 772), (557, 787)], #J2 B
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },

    'ISRO_Junction': {  #verified ISRO
         'regions': {
            'J1':[(19, 20), (200, 360), (212, 585), (12, 585)], #J1 A
            'J2':[(50, 67), (246, 384), (1082, 375), (1166, 67)], #J2 B
            'J3':[(1130, 215), (1130, 500), (1432, 720), (1432, 195)], #J3 C
            'J4':[(10, 791), (10, 612), (1260, 628), (1425, 802)], #J4 D
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'AC': ['J1', 'J3'],
            'BC': ['J2', 'J3'],
            'BD': ['J2', 'J4'],
        }
    },

    '80ft_Road':  #verified
    {
        'regions': {
            'J1':[(7, 347), (1420, 348), (1370, 26), (15, 21)], #J1 A
            'J2':[(11, 374), (9, 793), (1410, 790), (1420, 402)], #J2 B
        },
        'turning_patterns': {
            'AB': ['J1', 'J2'],
            'BA': ['J2', 'J1'],
        }
    },
}