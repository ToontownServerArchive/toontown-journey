from .ElevatorConstants import *
from toontown.toonbase import ToontownGlobals


try:
    config = base.config
except:
    config = simbase.config

SuitBuildingInfo = (
    (
        (1, 1),# Amount of Floors
        (1, 3),# Suit Levels
        (4, 4),# Boss Suit Levels
        (13, 17),# Suit Level Pool(All cog levels on floor must add up to be between this)
        (1,)# Suit Level Pool Multipliers(Multiplies the Suit Level Pool, Each Value is a different floor) Index 0
    ),
    (
        (1, 2),
        (2, 4),
        (5, 5),
        (13, 17),
        (1, 1.2)
    ),#1
    (
        (1, 3),
        (3, 5),
        (6, 6),
        (13, 17),
        (1, 1.3, 1.6)
    ),#2
    (
        (2, 3),
        (4, 6),
        (7, 7),
        (13, 17),
        (1, 1.4, 1.8)
    ),#3
    (
        (2, 4),
        (5, 7),
        (8, 8),
        (13, 17),
        (1, 1.6, 1.8, 2)
    ),#4
    (
        (3, 4),
        (6, 8),
        (9, 9),
        (15, 18),
        (1, 1.6, 2, 2.4)
    ),#5
    (
        (3, 5),
        (7, 9),
        (10, 10),
        (20, 23),
        (1, 1.6, 1.8, 2.2, 2.4)
    ),#6
    (
        (4, 5),
        (8, 10),
        (11, 11),
        (23, 26),
        (1, 1.8, 2.4, 3, 3.2)
    ),#7
    (
        (5, 5),
        (9, 11),
        (12, 12),
        (29, 32),
        (1.4, 1.8,2.6, 3.4, 4)
    ),#8
    (
        (1, 1),
        (1, 12),
        (12, 12),
        (67, 67),
        (1, 1, 1, 1, 1)
    ),#9(VP Battle 1)
    (   (1, 1),
        (8, 12),
        (12, 12),
        (100, 100),
        (1, 1, 1, 1, 1)
    ),#10(VP Battle 2)
    (
        (1, 1),
        (1, 12),
        (12, 12),
        (100, 100),
        (1, 1, 1, 1, 1)
    ),#11
    (
        (1, 1),
        (8, 12),
        (12, 12),
        (150, 150),
        (1, 1, 1, 1, 1)
    ),#12
    (
        (1, 1),
        (8, 12),
        (12, 12),
        (275, 275),
      (1, 1, 1, 1, 1)
    ),#13
    (
        (1, 1),
        (9, 12),
        (12, 12),
        (206, 206),
        (1, 1, 1, 1, 1),
        (1,)
    ),#14
    (
        (1, 1),
        (1, 5),
        (5, 5),
        (33, 33),
        (1, 1, 1, 1, 1)
    ),#15
    (
        (1, 1),
        (4, 5),
        (5, 5),
        (50, 50),
        (1, 1, 1, 1, 1)
    ),#16
    (
        (1, 1),
        (11, 12),
        (12, 12),
        (206, 206),
        (1, 1, 1, 1, 1),
        (1,)
    ),#17
    (
        (1, 1),
        (7, 12),
        (12, 12),
        (50, 50),
        (1, 1, 1, 1, 1),
    ),# Brutal VP, First Round  18
    (
        (1, 1),
        (10, 12),
        (12, 12),
        (100, 100),
        (1, 1, 1, 1, 1),
        (1,),
    ),# Brutal VP, Second Round  19
    (
        (1, 1),
        (10, 12),
        (12, 12),
        (100, 100),
        (1, 1, 1, 1, 1),
        (1,),
    )# Brutal CFO  20
)    
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8

buildingMinMax = {
    ToontownGlobals.SillyStreet: [config.GetInt('silly-street-building-min', 2),
                                  config.GetInt('silly-street-building-max', 6)],
    ToontownGlobals.LoopyLane: [config.GetInt('loopy-lane-building-min', 2),
                                config.GetInt('loopy-lane-building-max', 6)],
    ToontownGlobals.PunchlinePlace: [config.GetInt('punchline-place-building-min', 2),
                                     config.GetInt('punchline-place-building-max', 6)],
    ToontownGlobals.BarnacleBoulevard: [config.GetInt('barnacle-boulevard-building-min', 3),
                                        config.GetInt('barnacle-boulevard-building-max', 7)],
    ToontownGlobals.SeaweedStreet: [config.GetInt('seaweed-street-building-min', 3),
                                    config.GetInt('seaweed-street-building-max', 7)],
    ToontownGlobals.LighthouseLane: [config.GetInt('lighthouse-lane-building-min', 3),
                                     config.GetInt('lighthouse-lane-building-max', 7)],
    ToontownGlobals.ElmStreet: [config.GetInt('elm-street-building-min', 2),
                                config.GetInt('elm-street-building-max', 6)],
    ToontownGlobals.MapleStreet: [config.GetInt('maple-street-building-min', 2),
                                  config.GetInt('maple-street-building-max', 6)],
    ToontownGlobals.OakStreet: [config.GetInt('oak-street-building-min', 2),
                                config.GetInt('oak-street-building-max', 6)],
    ToontownGlobals.AltoAvenue: [config.GetInt('alto-avenue-building-min', 3),
                                 config.GetInt('alto-avenue-building-max', 7)],
    ToontownGlobals.BaritoneBoulevard: [config.GetInt('baritone-boulevard-building-min', 3),
                                        config.GetInt('baritone-boulevard-building-max', 7)],
    ToontownGlobals.TenorTerrace: [config.GetInt('tenor-terrace-building-min', 3),
                                   config.GetInt('tenor-terrace-building-max', 7)],
    ToontownGlobals.WalrusWay: [config.GetInt('walrus-way-building-min', 5),
                                config.GetInt('walrus-way-building-max', 10)],
    ToontownGlobals.SleetStreet: [config.GetInt('sleet-street-building-min', 5),
                                  config.GetInt('sleet-street-building-max', 10)],
    ToontownGlobals.PolarPlace: [config.GetInt('polar-place-building-min', 5),
                                 config.GetInt('polar-place-building-max', 10)],
    ToontownGlobals.LullabyLane: [config.GetInt('lullaby-lane-building-min', 6),
                                  config.GetInt('lullaby-lane-building-max', 12)],
    ToontownGlobals.PajamaPlace: [config.GetInt('pajama-place-building-min', 6),
                                  config.GetInt('pajama-place-building-max', 12)],
    ToontownGlobals.SellbotHQ: (0, 0),
    ToontownGlobals.SellbotFactoryExt: (0, 0),
    ToontownGlobals.CashbotHQ: (0, 0),
    ToontownGlobals.LawbotHQ: (0, 0),
    ToontownGlobals.BossbotHQ: (0, 0)
}

buildingChance = {
    ToontownGlobals.SillyStreet: config.GetFloat('silly-street-building-chance', 50.0),
    ToontownGlobals.LoopyLane: config.GetFloat('loopy-lane-building-chance', 50.0),
    ToontownGlobals.PunchlinePlace: config.GetFloat('punchline-place-building-chance', 50.0),
    ToontownGlobals.BarnacleBoulevard: config.GetFloat('barnacle-boulevard-building-chance', 75.0),
    ToontownGlobals.SeaweedStreet: config.GetFloat('seaweed-street-building-chance', 75.0),
    ToontownGlobals.LighthouseLane: config.GetFloat('lighthouse-lane-building-chance', 75.0),
    ToontownGlobals.ElmStreet: config.GetFloat('elm-street-building-chance', 90.0),
    ToontownGlobals.MapleStreet: config.GetFloat('maple-street-building-chance', 90.0),
    ToontownGlobals.OakStreet: config.GetFloat('oak-street-building-chance', 90.0),
    ToontownGlobals.AltoAvenue: config.GetFloat('alto-avenue-building-chance', 95.0),
    ToontownGlobals.BaritoneBoulevard: config.GetFloat('baritone-boulevard-building-chance', 95.0),
    ToontownGlobals.TenorTerrace: config.GetFloat('tenor-terrace-building-chance', 95.0),
    ToontownGlobals.WalrusWay: config.GetFloat('walrus-way-building-chance', 100.0),
    ToontownGlobals.SleetStreet: config.GetFloat('sleet-street-building-chance', 100.0),
    ToontownGlobals.PolarPlace: config.GetFloat('polar-place-building-chance', 100.0),
    ToontownGlobals.LullabyLane: config.GetFloat('lullaby-lane-building-chance', 100.0),
    ToontownGlobals.PajamaPlace: config.GetFloat('pajama-place-building-chance', 100.0),
    ToontownGlobals.SellbotHQ: 0.0,
    ToontownGlobals.SellbotFactoryExt: 0.0,
    ToontownGlobals.CashbotHQ: 0.0,
    ToontownGlobals.LawbotHQ: 0.0,
    ToontownGlobals.BossbotHQ: 0.0
}
