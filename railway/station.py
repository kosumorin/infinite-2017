class Station(object):
    def __init__(self, name: str, EWL_id: float = -1, NSL_id: float = -1, CCL_id: float = -1):
        self.name = name
        self.EWL_id = EWL_id
        self.NSL_id = NSL_id
        self.CCL_id = CCL_id
        self.EWL_station_path : 'StationPath' = None
        self.NSL_station_path : 'StationPath' = None
        self.CCL_station_path : 'StationPath' = None

class StationPath(object):
    def __init__(self, up: 'Station' = None, right: 'Station' = None, left: 'Station' = None, down: 'Station' = None):
        self.up = up
        self.right = right
        self.down = down
        self.left = left

'''
    *********************************************************************************
                            INITIALIZE ALL STATIONS WITH IDS
    *********************************************************************************
'''
PASIR_RIS       = Station(  "Pasir Ris",          EWL_id=12                             )
CHANGI          = Station(  "Changi",             EWL_id=11.1                           )
TANAH_MERAH     = Station(  "Tanah Merah",        EWL_id=11                             )
BEDOK           = Station(  "Bedok",              EWL_id=10                             )
PAYA_LEBAR      = Station(  "Paya Lebar",         EWL_id=9,               CCL_id=8      )
KALLANG         = Station(  "Kallang",            EWL_id=8                              )
BUGIS           = Station(  "Bugis",              EWL_id=7                              )
CITY_HALL       = Station(  "City Hall",          EWL_id=6,   NSL_id=11                 )
OUTRAM_PARK     = Station(  "Outram Park",        EWL_id=5                              )
BUONA_VISTA     = Station(  "Buona Vista",        EWL_id=4,               CCL_id=3      )
CLEMENTI        = Station(  "Clementi",           EWL_id=2                              )
JURONG_EAST     = Station(  "Jurong East",        EWL_id=1,   NSL_id=1                  )
MARINA_BAY      = Station(  "Marina Bay",                     NSL_id=12,  CCL_id=11     )
DHOBY_GHAUT     = Station(  "Dhoby Ghaut",                    NSL_id=10,  CCL_id=10.2   )
SOMERSET        = Station(  "Somerset",                       NSL_id=9                  )
ORCHARD         = Station(  "Orchard",                        NSL_id=8                  )
NEWTON          = Station(  "Newton",                         NSL_id=7                  )
TOA_PAYOH       = Station(  "Toa Payoh",                      NSL_id=6                  )
BISHAN          = Station(  "Bishan",                         NSL_id=5,   CCL_id=6      )
YISHUN          = Station(  "Yishun",                         NSL_id=4                  )
WOODLANDS       = Station(  "Woodlands",                      NSL_id=3                  )
CHUA_CHU_KANG   = Station(  "Chua Chu Kang",                  NSL_id=2                  )
PROMENADE       = Station(  "Promenade",                                  CCL_id=10     )
ESPLANADE       = Station(  "Esplanade",                                  CCL_id=10.1   )
STADIUM         = Station(  "Stadium",                                    CCL_id=9      )
SERANGOON       = Station(  "Serangoon",                                  CCL_id=7      )
BOTANIC_GARDENS = Station(  "Botanic Gardens",                            CCL_id=5      )
HOLLAND_VILLAGE = Station(  "Holland Village",                            CCL_id=4      )
HAW_PAR_VILLA   = Station(  "Haw Par Villa",                              CCL_id=2      )
HABOURFRONT     = Station(  "Habourfront",                                CCL_id=1      )


'''
    *********************************************************************************
                            EWL STATION PATHS FOR EWL STATIONS
    *********************************************************************************
'''
JURONG_EAST.EWL_station_path    = StationPath(  up=CLEMENTI,      left=CHUA_CHU_KANG                                                )
CLEMENTI.EWL_station_path       = StationPath(  up=BUONA_VISTA,                                                   down=JURONG_EAST  )
BUONA_VISTA.EWL_station_path    = StationPath(  up=OUTRAM_PARK,   left=HOLLAND_VILLAGE,   right=HAW_PAR_VILLA,    down=CLEMENTI     )
OUTRAM_PARK.EWL_station_path    = StationPath(  up=CITY_HALL,                                                     down=BUONA_VISTA  )
CITY_HALL.EWL_station_path      = StationPath(  up=BUGIS,         left=DHOBY_GHAUT,       right=MARINA_BAY,       down=OUTRAM_PARK  )
BUGIS.EWL_station_path          = StationPath(  up=KALLANG,                                                       down=CITY_HALL    )
KALLANG.EWL_station_path        = StationPath(  up=PAYA_LEBAR,                                                    down=BUGIS        )
PAYA_LEBAR.EWL_station_path     = StationPath(  up=BEDOK,         left=SERANGOON,         right=STADIUM,          down=KALLANG      )
BEDOK.EWL_station_path          = StationPath(  up=TANAH_MERAH,                                                   down=PAYA_LEBAR   )
TANAH_MERAH.EWL_station_path    = StationPath(  up=CHANGI,        left=PASIR_RIS,                                 down=BEDOK        )
CHANGI.EWL_station_path         = StationPath(                                                                    down=TANAH_MERAH  )
PASIR_RIS.EWL_station_path      = StationPath(                                                                    down=TANAH_MERAH  )

'''
    *********************************************************************************
                            NSL STATION PATHS FOR NSL STATIONS
    *********************************************************************************
'''
JURONG_EAST.NSL_station_path    = StationPath(  up=CHUA_CHU_KANG,                         right=CLEMENTI                              )
CHUA_CHU_KANG.NSL_station_path  = StationPath(  up=WOODLANDS,                                                     down=JURONG_EAST    )
WOODLANDS.NSL_station_path      = StationPath(  up=YISHUN,                                                        down=CHUA_CHU_KANG  )
YISHUN.NSL_station_path         = StationPath(  up=BISHAN,                                                        down=WOODLANDS      )
BISHAN.NSL_station_path         = StationPath(  up=TOA_PAYOH,     left=SERANGOON,         right=BOTANIC_GARDENS,  down=YISHUN         )
TOA_PAYOH.NSL_station_path      = StationPath(  up=NEWTON,                                                        down=BISHAN         )
NEWTON.NSL_station_path         = StationPath(  up=ORCHARD,                                                       down=TOA_PAYOH      )
ORCHARD.NSL_station_path        = StationPath(  up=SOMERSET,                                                      down=NEWTON         )
SOMERSET.NSL_station_path       = StationPath(  up=DHOBY_GHAUT,                                                   down=ORCHARD        )
DHOBY_GHAUT.NSL_station_path    = StationPath(  up=CITY_HALL,     left=ESPLANADE,                                 down=SOMERSET       )
CITY_HALL.NSL_station_path      = StationPath(  up=MARINA_BAY,    left=BUGIS,             right=OUTRAM_PARK,      down=DHOBY_GHAUT    )
MARINA_BAY.NSL_station_path     = StationPath(                    left=PROMENADE,                                 down=CITY_HALL      )

'''
    *********************************************************************************
                            CCL STATION PATHS FOR CCL STATIONS
    *********************************************************************************
'''
HABOURFRONT.CCL_station_path        = StationPath(  up=HAW_PAR_VILLA                                                                        )
HAW_PAR_VILLA.CCL_station_path      = StationPath(  up=BUONA_VISTA,                                                   down=HABOURFRONT      )
BUONA_VISTA.CCL_station_path        = StationPath(  up=HOLLAND_VILLAGE,     left=CLEMENTI,    right=OUTRAM_PARK,      down=HABOURFRONT      )
HOLLAND_VILLAGE.CCL_station_path    = StationPath(  up=BOTANIC_GARDENS,                                               down=BUONA_VISTA      )
BOTANIC_GARDENS.CCL_station_path    = StationPath(  up=BISHAN,                                                        down=HOLLAND_VILLAGE  )
BISHAN.CCL_station_path             = StationPath(  up=SERANGOON,           left=YISHUN,      right=TOA_PAYOH,        down=BOTANIC_GARDENS  )
SERANGOON.CCL_station_path          = StationPath(  up=PAYA_LEBAR,                                                    down=BISHAN           )
PAYA_LEBAR.CCL_station_path         = StationPath(  up=STADIUM,             left=BEDOK,       right=KALLANG,          down=SERANGOON        )
STADIUM.CCL_station_path            = StationPath(  up=PROMENADE,                                                     down=PAYA_LEBAR       )
PROMENADE.CCL_station_path          = StationPath(  up=MARINA_BAY,          left=ESPLANADE,                           down=STADIUM          )
ESPLANADE.CCL_station_path          = StationPath(  up=DHOBY_GHAUT,                                                   down=PROMENADE        )
DHOBY_GHAUT.CCL_station_path        = StationPath(                                                                    down=ESPLANADE        )
MARINA_BAY.CCL_station_path         = StationPath(                                                                    down=PROMENADE        )

'''
    *********************************************************************************
                                    LINE STATIONS
    *********************************************************************************
'''
EWL_STATIONS = [
    JURONG_EAST,
    CLEMENTI,
    BUONA_VISTA,
    OUTRAM_PARK,
    CITY_HALL,
    BUGIS,
    KALLANG,
    PAYA_LEBAR,
    BEDOK,
    TANAH_MERAH,
    PASIR_RIS,
    CHANGI
]

NSL_STATIONS = [
    JURONG_EAST,
    CHUA_CHU_KANG,
    WOODLANDS,
    YISHUN,
    BISHAN,
    TOA_PAYOH,
    NEWTON,
    ORCHARD,
    SOMERSET,
    DHOBY_GHAUT,
    CITY_HALL,
    MARINA_BAY
]

CCL_STATIONS = [
    HABOURFRONT,
    HAW_PAR_VILLA,
    BUONA_VISTA,
    HOLLAND_VILLAGE,
    BOTANIC_GARDENS,
    BISHAN,
    SERANGOON,
    PAYA_LEBAR,
    STADIUM,
    ESPLANADE,
    DHOBY_GHAUT
]