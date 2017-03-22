#!/usr/bin/env python3
from railway.line import MRTLine
from railway.route import Route
from railway.station import MRTStation
from train.driver import MRTDriver
from train.train import Train

if __name__ == "__main__":
    route = Route(MRTStation.JURONG_EAST, MRTStation.CHANGI, MRTLine.EWL, MRTLine.EWL)

    train = Train()
    train.add_listener(MRTDriver(route))

    while True:
        train.step()