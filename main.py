#!/usr/bin/env python3
from railway.route import Route
from vehicle.train import Train
from data.map import MRTStations, MRTLines

if __name__ == "__main__":
    print("Started")

    start_station   = MRTStations.get_station_by_name("jurong east")
    end_station     = MRTStations.get_station_by_name("marina bay")
    trans_station   = MRTStations.get_station_by_name("city hall")
    start_line      = MRTLines.get_line_by_name("ewl")
    end_line        = MRTLines.get_line_by_name("nsl")

    route = Route(start_station, end_station, start_line, end_line, trans_station)

    train = Train()
    train.start(route)
