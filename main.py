#!/usr/bin/env python3
from train.driver import EWLDriver, NSLDriver, CCLDriver
from train.train import Train

if __name__ == "__main__":
    train = Train()
    train.set_listener(EWLDriver())

    while True:
        train.step()