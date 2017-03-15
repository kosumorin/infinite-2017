from railway.station import Station, StationPath
from railway.line import Line
from utils.color import Color

class MRTStation(object):
    PASIR_RIS = Station("Pasir Ris")
    CHANGI = Station("Changi")
    TANAH_MERAH = Station("Tanah Merah")
    BEDOK = Station("Bedok")
    PAYA_LEBAR = Station("Paya Lebar")
    KALLANG = Station("Kallang")
    BUGIS = Station("Bugis")
    CITY_HALL = Station("City Hall")
    OUTRAM_PARK = Station("Outram Park")
    BUONA_VISTA = Station("Buona Vista")
    CLEMENTI = Station("Clementi")
    JURONG_EAST = Station("Jurong East")
    MARINA_BAY = Station("Marina Bay")
    DHOBY_GHAUT = Station("Dhoby Ghaut")
    SOMERSET = Station("Somerset")
    ORCHARD = Station("Orchard")
    NEWTON = Station("Newton")
    TOA_PAYOH = Station("Toa Payoh")
    BISHAN = Station("Bishan")
    YISHUN = Station("Yishun")
    WOODLANDS = Station("Woodlands")
    CHUA_CHU_KANG = Station("Chua Chu Kang")
    PROMENADE = Station("Promenade")
    ESPLANADE = Station("Esplanade")
    STADIUM = Station("Stadium")
    SERANGOON = Station("Serangoon")
    BOTANIC_GARDENS = Station("Botanic Gardens")
    HOLLAND_VILLAGE = Station("Holland Village")
    HAW_PAR_VILLA = Station("Haw Par Villa")
    HABOURFRONT = Station("Habourfront")

    '''
            *********************************************************************************
                                    EWL STATION PATHS FOR EWL STATIONS
            *********************************************************************************
    '''

    JURONG_EAST.EWL_station_path = StationPath(up=CLEMENTI, left=CHUA_CHU_KANG)
    CLEMENTI.EWL_station_path = StationPath(up=BUONA_VISTA, down=JURONG_EAST)
    BUONA_VISTA.EWL_station_path = StationPath(up=OUTRAM_PARK, left=HOLLAND_VILLAGE, right=HAW_PAR_VILLA, down=CLEMENTI)
    OUTRAM_PARK.EWL_station_path = StationPath(up=CITY_HALL, down=BUONA_VISTA)
    CITY_HALL.EWL_station_path = StationPath(up=BUGIS, left=DHOBY_GHAUT, right=MARINA_BAY, down=OUTRAM_PARK)
    BUGIS.EWL_station_path = StationPath(up=KALLANG, down=CITY_HALL)
    KALLANG.EWL_station_path = StationPath(up=PAYA_LEBAR, down=BUGIS)
    PAYA_LEBAR.EWL_station_path = StationPath(up=BEDOK, left=SERANGOON, right=STADIUM, down=KALLANG)
    BEDOK.EWL_station_path = StationPath(up=TANAH_MERAH, down=PAYA_LEBAR)
    TANAH_MERAH.EWL_station_path = StationPath(up=CHANGI, left=PASIR_RIS, down=BEDOK)
    CHANGI.EWL_station_path = StationPath(down=TANAH_MERAH)
    PASIR_RIS.EWL_station_path = StationPath(down=TANAH_MERAH)

    '''
        *********************************************************************************
                                NSL STATION PATHS FOR NSL STATIONS
        *********************************************************************************
    '''
    JURONG_EAST.NSL_station_path = StationPath(up=CHUA_CHU_KANG, right=CLEMENTI)
    CHUA_CHU_KANG.NSL_station_path = StationPath(up=WOODLANDS, down=JURONG_EAST)
    WOODLANDS.NSL_station_path = StationPath(up=YISHUN, down=CHUA_CHU_KANG)
    YISHUN.NSL_station_path = StationPath(up=BISHAN, down=WOODLANDS)
    BISHAN.NSL_station_path = StationPath(up=TOA_PAYOH, left=SERANGOON, right=BOTANIC_GARDENS, down=YISHUN)
    TOA_PAYOH.NSL_station_path = StationPath(up=NEWTON, down=BISHAN)
    NEWTON.NSL_station_path = StationPath(up=ORCHARD, down=TOA_PAYOH)
    ORCHARD.NSL_station_path = StationPath(up=SOMERSET, down=NEWTON)
    SOMERSET.NSL_station_path = StationPath(up=DHOBY_GHAUT, down=ORCHARD)
    DHOBY_GHAUT.NSL_station_path = StationPath(up=CITY_HALL, left=ESPLANADE, down=SOMERSET)
    CITY_HALL.NSL_station_path = StationPath(up=MARINA_BAY, left=BUGIS, right=OUTRAM_PARK, down=DHOBY_GHAUT)
    MARINA_BAY.NSL_station_path = StationPath(left=PROMENADE, down=CITY_HALL)

    '''
        *********************************************************************************
                                CCL STATION PATHS FOR CCL STATIONS
        *********************************************************************************
    '''
    HABOURFRONT.CCL_station_path = StationPath(up=HAW_PAR_VILLA)
    HAW_PAR_VILLA.CCL_station_path = StationPath(up=BUONA_VISTA, down=HABOURFRONT)
    BUONA_VISTA.CCL_station_path = StationPath(up=HOLLAND_VILLAGE, left=CLEMENTI, right=OUTRAM_PARK, down=HABOURFRONT)
    HOLLAND_VILLAGE.CCL_station_path = StationPath(up=BOTANIC_GARDENS, down=BUONA_VISTA)
    BOTANIC_GARDENS.CCL_station_path = StationPath(up=BISHAN, down=HOLLAND_VILLAGE)
    BISHAN.CCL_station_path = StationPath(up=SERANGOON, left=YISHUN, right=TOA_PAYOH, down=BOTANIC_GARDENS)
    SERANGOON.CCL_station_path = StationPath(up=PAYA_LEBAR, down=BISHAN)
    PAYA_LEBAR.CCL_station_path = StationPath(up=STADIUM, left=BEDOK, right=KALLANG, down=SERANGOON)
    STADIUM.CCL_station_path = StationPath(up=PROMENADE, down=PAYA_LEBAR)
    PROMENADE.CCL_station_path = StationPath(up=MARINA_BAY, left=ESPLANADE, down=STADIUM)
    ESPLANADE.CCL_station_path = StationPath(up=DHOBY_GHAUT, down=PROMENADE)
    DHOBY_GHAUT.CCL_station_path = StationPath(down=ESPLANADE)
    MARINA_BAY.CCL_station_path = StationPath(down=PROMENADE)


class MRTLine(object):
    EWL = Line(name="East West Line", color=Color.GREEN, stations=[
        MRTStation.JURONG_EAST,
        MRTStation.CLEMENTI,
        MRTStation.BUONA_VISTA,
        MRTStation.OUTRAM_PARK,
        MRTStation.CITY_HALL,
        MRTStation.BUGIS,
        MRTStation.KALLANG,
        MRTStation.PAYA_LEBAR,
        MRTStation.BEDOK,
        MRTStation.TANAH_MERAH,
        MRTStation.PASIR_RIS,
        MRTStation.CHANGI
    ])

    NSL = Line(name="North South Line", color=Color.RED, stations=[
        MRTStation.JURONG_EAST,
        MRTStation.CHUA_CHU_KANG,
        MRTStation.WOODLANDS,
        MRTStation.YISHUN,
        MRTStation.BISHAN,
        MRTStation.TOA_PAYOH,
        MRTStation.NEWTON,
        MRTStation.ORCHARD,
        MRTStation.SOMERSET,
        MRTStation.DHOBY_GHAUT,
        MRTStation.CITY_HALL,
        MRTStation.MARINA_BAY
    ])

    CCL = Line(name="Circle Line", color=Color.YELLOW, stations=[
        MRTStation.HABOURFRONT,
        MRTStation.HAW_PAR_VILLA,
        MRTStation.BUONA_VISTA,
        MRTStation.HOLLAND_VILLAGE,
        MRTStation.BOTANIC_GARDENS,
        MRTStation.BISHAN,
        MRTStation.SERANGOON,
        MRTStation.PAYA_LEBAR,
        MRTStation.STADIUM,
        MRTStation.ESPLANADE,
        MRTStation.DHOBY_GHAUT
    ])
