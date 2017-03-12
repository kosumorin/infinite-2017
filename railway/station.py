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
PASIR_RIS       = Station("Pasir Ris",          EWL_id=12                           )
CHANGI          = Station("Changi",             EWL_id=11.1                         )
TANAH_MERAH     = Station("Tanah Merah",        EWL_id=11                           )
BEDOK           = Station("Bedok",              EWL_id=10                           )
PAYA_LEBAR      = Station("Paya Lebar",         EWL_id=9,               CCL_id=8    )
KALLANG         = Station("Kallang",            EWL_id=8                            )
BUGIS           = Station("Bugis",              EWL_id=7                            )
CITY_HALL       = Station("City Hall",          EWL_id=6,   NSL_id=11               )
OUTRAM_PARK     = Station("Outram Park",        EWL_id=5                            )
BUONA_VISTA     = Station("Buona Vista",        EWL_id=4,               CCL_id=3    )
CLEMENTI        = Station("Clementi",           EWL_id=2                            )
JURONG_EAST     = Station("Jurong East",        EWL_id=1,   NSL_id=1                )
MARINA_BAY      = Station("Marina Bay",                     NSL_id=12,  CCL_id=11   )
DHOBY_GHAUT     = Station("Marina Bay",                     NSL_id=10,  CCL_id=10.2 )
SOMERSET        = Station("Somerset",                       NSL_id=9                )
ORCAHRD         = Station("Orchard",                        NSL_id=8                )
NEWTON          = Station("Newton",                         NSL_id=7                )
TOA_PAYOH       = Station("Toa Payoh",                      NSL_id=6                )
BISHAN          = Station("Bishan",                         NSL_id=5,   CCL_id=6    )
YISHUN          = Station("Yishun",                         NSL_id=4                )
WOODLANDS       = Station("Woodlands",                      NSL_id=3                )
CHUA_CHU_KANG   = Station("Chua Chu Kang",                  NSL_id=2                )
PROMENADE       = Station("Promenade",                                  CCL_id=10   )
ESPLANADE       = Station("Esplanade",                                  CCL_id=10.1 )
STADIUM         = Station("Stadium",                                    CCL_id=9    )
SERANGOON       = Station("Serangoon",                                  CCL_id=7    )
BOTANIC_GARDENS = Station("Botanic Gardens",                            CCL_id=5    )
HOLLAND_VILLAGE = Station("Holland Village",                            CCL_id=4    )
HAW_PAR_VILLA   = Station("Haw Par Villa",                              CCL_id=2    )
HABOURFRONT     = Station("Habourfront",                                CCL_id=1    )
