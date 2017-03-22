#!/usr/bin/env python3
from railway.line import MRTLine
from railway.route import Route
from railway.station import MRTStation
from vehicle.train import Train

if __name__ == "__main__":
    print("Started")
    route = Route(MRTStation.JURONG_EAST, MRTStation.CHANGI, MRTLine.EWL, MRTLine.EWL)

    train = Train()
    train.start(route)

    print("Ended")