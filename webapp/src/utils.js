const MapUtils = {
    convertDirToMovementDir: function(fromDir, toDir){
        if (fromDir == toDir){
            return "STRAIGHT";
        }
        else if (fromDir == "NORTH"){
            if (toDir == "EAST"){
                return "RIGHT";
            }
            else if (toDir == "WEST"){
                return "LEFT";
            }
        }
        else if (fromDir == "EAST"){
            if (toDir == "SOUTH"){
                return "RIGHT";
            }
            else if (toDir == "NORTH"){
                return "LEFT";
            }
        }
        else if (fromDir == "SOUTH"){
            if (toDir == "WEST"){
                return "RIGHT";
            }
            else if (toDir == "EAST"){
                return "LEFT";
            }
        }
        else if (fromDir == "WEST"){
            if (toDir == "NORTH"){
                return "RIGHT";
            }
            else if (toDir == "SOUTH"){
                return "LEFT";
            }
        }

        // We don't support backwards.
        return "STRAIGHT";
    },

    findInterchangeFromStation: function(targetStation, lines){
        let stationLines = this.getLinesOfStation(targetStation);

        let interchanges = [];

        for (let line of lines){
            for (let stationLine of stationLines){
                if (line == stationLine){
                    continue;
                }

                for (let interchange of this.findInterchangeFromLines(line, stationLine)){
                    interchanges.push(interchange);
                }
            }
        }

        // Check and remove duplicates.
        interchanges = interchanges.filter(function (interchange, index, self) {
            return self.indexOf(interchange) == index;
        })

        return interchanges;
    },

    findInterchangeFromLines: function(line1, line2){
        let interchanges = [];

        for (let station1 of line1.stations){
            for (let station2 of line2.stations){
                if (station1 == station2){
                    interchanges.push(station1);
                }
            }
        }

        return interchanges;
    },

    getInterchangeTurnDirection: function(interchange, fromStation, toStation, fromLine, toLine) {
        let isTrainFacingOppOnFromLine = this.isTrainFacingOpp(fromStation, interchange, fromLine);
        let isTrainFacingOppOnToLine = this.isTrainFacingOpp(interchange, toStation, toLine);

        let fromDirection = null;
        let toDirection = null;

        if (!isTrainFacingOppOnFromLine){
            let previousStation = this.getStationOnLineByIndex(this.getIndexOfStationOnLine(interchange, fromLine) - 1, fromLine);
            fromDirection = previousStation.stationFlow[fromLine.name]["next"]
        }
        else{
            let previousStation = this.getStationOnLineByIndex(this.getIndexOfStationOnLine(interchange, fromLine) + 1, fromLine);
            fromDirection = previousStation.stationFlow[fromLine.name]["previous"]
        }

        if (!isTrainFacingOppOnToLine){
            toDirection = interchange.stationFlow[toLine.name]["next"]
        }
        else{
            toDirection = interchange.stationFlow[toLine.name]["previous"]
        }

        return this.convertDirToMovementDir(fromDirection, toDirection);
    },

    getStationById: function(id, stations){
        for (let station of stations){
            if (station["id"] == id){
                return station;
            }
        }
    },

    getLinesOfStation: function(targetStation, lines){
        let linesOfStation = [];

        for (let line of lines){
            for (let station of line.stations){
                if (station == targetStation){
                    linesOfStation.push(line);
                }
            }
        }

        return linesOfStation;
    },

    getStationOnLineByIndex: function(index, targetLine){
        for (let i = 0; i < targetLine.stations.length; i++){
            if (i == index){
                return targetLine.stations[i];
            }
        }
    },

    getIndexOfStationOnLine: function(targetStation, targetLine){
        for (let i = 0; i < targetLine.stations.length; i++){
            if (targetStation == targetLine.stations[i]){
                return i;
            }
        }
    },
    
    getPossibleRoutes: function(startStation, endStation, stations, lines){
        let routes = []

        let Route = function (startStation, endStation, startLine, endLine, transferStation, stationPath, movementFlow) {
            this.start_station = startStation;
            this.end_station = endStation;
            this.start_line = startLine;
            this.end_line = endLine;
            this.transfer_station = transferStation;
            this.station_path = stationPath;
            this.movement_flow = movementFlow;
        }

        let startStationLines = this.getLinesOfStation(startStation, lines);
        let endStationLines = this.getLinesOfStation(endStation, lines);

        for (let startLine of startStationLines){
            for (let endLine of endStationLines){
                if (startLine != endLine){ // Change of lines required.
                    let interchanges = this.findInterchangeFromLines(startLine, endLine);

                    for (let interchange of interchanges){
                        // Don't let the interchange be the start station or end station.
                        if (interchange == startStation || interchange == endStation){
                            continue;
                        }

                        let stationPath = [];
                        Array.prototype.push.apply(stationPath, this.generateStationPath(startStation, interchange, startLine));
                        Array.prototype.push.apply(stationPath, this.generateStationPath(interchange, endStation, endLine));

                        let movementFlow = [];
                        Array.prototype.push.apply(movementFlow, this.generateMovementFlow(startStation, interchange, startLine));
                        movementFlow.push(this.getInterchangeTurnDirection(interchange, startStation, endStation, startLine, endLine));
                        Array.prototype.push.apply(movementFlow, this.generateMovementFlow(interchange, endStation, endLine));

                        routes.push(new Route(
                            startStation,
                            endStation,
                            startLine,
                            endLine,
                            interchange,
                            stationPath,
                            movementFlow
                        ));
                    }
                }
                else{ // Direct path available
                    routes.push(new Route(
                        startStation,
                        endStation,
                        startLine,
                        endLine,
                        null,
                        this.generateStationPath(startStation, endStation, startLine),
                        this.generateMovementFlow(startStation, endStation, startLine)
                    ));
                }
            }
        }

        return routes;
    },

    generateStationPath: function(fromStation, toStation, line){
        let stationPath = [];

        let fromStationIndex = this.getIndexOfStationOnLine(fromStation, line);
        let toStationIndex = this.getIndexOfStationOnLine(toStation, line);

        let isTrainFacingOpp = this.isTrainFacingOpp(fromStation, toStation, line);
        if (!isTrainFacingOpp){
            for (let i = fromStationIndex + 1; i < toStationIndex + 1; i++){
                stationPath.push(line.stations[i]);
            }
        }
        else if (isTrainFacingOpp){
            for (let i = fromStationIndex - 1; i > toStationIndex - 1; i--){
                stationPath.push(line.stations[i]);
            }
        }

        return stationPath;
    },

    generateMovementFlow: function(fromStation, toStation, line){
        let stationFlow = []

        let fromStationIndex = this.getIndexOfStationOnLine(fromStation, line);
        let toStationIndex = this.getIndexOfStationOnLine(toStation, line);

        let isTrainFacingOpp = this.isTrainFacingOpp(fromStation, toStation, line);
        if (!isTrainFacingOpp){
            for (let i = fromStationIndex; i < toStationIndex; i++){
                stationFlow.push(line.stations[i].stationFlow[line.name]["next"]);
            }
        }
        else if (isTrainFacingOpp){
            for (let i = fromStationIndex; i > toStationIndex; i--){
                stationFlow.push(line.stations[i].stationFlow[line.name]["previous"]);
            }
        }

        let movementFlow = []
        for (let i = 0; i < stationFlow.length; i++){
            if (i + 1 == stationFlow.length){
                break;
            }

            let fromDir = stationFlow[i];
            let toDir = stationFlow[i + 1];

            movementFlow.push(this.convertDirToMovementDir(fromDir, toDir));
        }

        return movementFlow;
    },

    isTrainFacingOpp: function(fromStation, toStation, line){
        if (this.getIndexOfStationOnLine(fromStation, line) < this.getIndexOfStationOnLine(toStation, line)){
            return false;
        }
        else{
            return true;
        }
    }
}

export { MapUtils };