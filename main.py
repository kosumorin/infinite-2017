#!/usr/bin/env python3
from train.driver import MRTDriver
from train.train import Train
from train.route import Route
from railway.line import MRTLine
from railway.station import MRTStation

if __name__ == "__main__":
    route = Route(MRTStation.JURONG_EAST, MRTStation.CHANGI, MRTLine.EWL, MRTLine.EWL)

    train = Train()
    train.add_listener(MRTDriver(route))

    while True:
        train.step()