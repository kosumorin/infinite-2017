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

class StationInfo extends React.Component{
    render(){
        return (
            React.createElement("div", {className: "stationInfo"}, 
                
                    this.props.lineNames.map((lineName, index) => {
                        return React.createElement("div", {key: index, className: "lineTag " + lineName}, lineName)
                    }), 
                
                React.createElement("div", {className: "stationTag"}, this.props.stationName)
            )
        );
    }
}

class StationButton extends React.Component{
    render(){
        let className = "stationButton";

        if (this.props.isSelected){
            className += " selected";
        }

        return React.createElement("div", {className: className, "data-stationId": this.props.stationId, onClick: this.props.onClickHandler});
    }
}

class Station extends React.Component{
    render(){
        const uniqueId = this.props.station["name"].replace(/\s/g, "");

        return (
            React.createElement("div", {className: "station", id: uniqueId}, 
                React.createElement(StationInfo, {stationName: this.props.station["name"], lineNames: this.props.lineNames}), 
                React.createElement(StationButton, {stationId: this.props.station["id"], isSelected: this.props.isSelected, onClickHandler: this.props.onClickHandler})
            )
        );         
    }
}

class Map extends React.Component{
    render(){
        return ( 
            React.createElement("div", {className: "map"}, 
                
                    this.props.stations.map((station, index) => {
                        const lineNames = MapUtils.getLinesOfStation(station, this.props.lines).map((line) => {
                            return line["name"];
                        });

                        let isSelected = false;
                        if (station == MapUtils.getStationById(this.props.startStationId, this.props.stations) || station == MapUtils.getStationById(this.props.endStationId, this.props.stations)){
                            isSelected = true;
                        }

                        return React.createElement(Station, {key: index, station: station, lineNames: lineNames, isSelected: isSelected, onClickHandler: this.props.onClickHandler});
                    })
                
            )
        );
    }
}

class Route extends React.Component{
    render(){
        let className = this.props.isSelected ? "route selected" : "route";
        let element = null;

        if (this.props.route["transfer_station"] == null){
            let startStationName = this.props.route["start_station"]["name"];
            let endStationName = this.props.route["end_station"]["name"];

            let lineName = this.props.route["start_line"]["name"]; 
            
            element = (
                React.createElement("div", {className: className, "data-routeIndex": this.props.routeIndex, onClick: this.props.onClickHandler}, 
                    React.createElement(StationInfo, {stationName: startStationName, lineNames: [lineName]}), 
                    React.createElement("div", {className: "arrow"}), 
                    React.createElement(StationInfo, {stationName: endStationName, lineNames: [lineName]})
                ) 
            );
        }
        else{
            let startStationName = this.props.route["start_station"]["name"];
            let transferStationName = this.props.route["transfer_station"]["name"];
            let endStationName = this.props.route["end_station"]["name"]; 

            let startLineName = this.props.route["start_line"]["name"];
            let endLineName = this.props.route["end_line"]["name"];

            element = (
                React.createElement("div", {className: className, "data-routeIndex": this.props.routeIndex, onClick: this.props.onClickHandler}, 
                    React.createElement(StationInfo, {stationName: startStationName, lineNames: [startLineName]}), 
                    React.createElement("div", {className: "arrow"}), 
                    React.createElement(StationInfo, {stationName: transferStationName, lineNames: [startLineName, endLineName]}), 
                    React.createElement("div", {className: "arrow"}), 
                    React.createElement(StationInfo, {stationName: endStationName, lineNames: [endLineName]})
                ) 
            );
        }

        return element;
    }
}

class RoutePicker extends React.Component{
    render(){
        return (
            React.createElement("div", {className: "routePicker"}, 
                
                    this.props.routes.map((route, index) => {
                        let isSelected = false;
                        if (index == this.props.selectedRouteIndex){
                            isSelected = true;
                        }

                        return React.createElement(Route, {key: index, routeIndex: index, route: route, isSelected: isSelected, onClickHandler: this.props.onClickHandler});
                    })
                
            )
        );
    }
}

class MessageGuide extends React.Component{
    constructor(props){
        super(props);

        this.state = { messages: [] }
    }

    componentWillReceiveProps(nextProps){
        const stage = nextProps.currentStage;

        this.setState({ messages: [this.props.messages[stage]]});
    }

    render(){
        return (
            React.createElement("div", {className: "messageGuide"}, 
                
                    this.state.messages.map((message, index) => {
                        return React.createElement("h4", {key: this.props.messages.indexOf(message)}, message) 
                    })
                
            )
        );
    }
}

class ButtonGuide extends React.Component{
    render(){
        if (this.props.visibleAtStage.indexOf(this.props.currentStage) == -1){
            return null;    
        }
        else{
            return React.createElement("button", {id: "button", onClick: this.props.onClickHandler}, this.props.messages[this.props.currentStage]) 
        }
    }
}

class App extends React.Component{
    constructor(props){
        super(props);
        
        this.state = { 
            lines: [],
            stations: [], 
            stage: 0,
            startStationId: -1,
            endStationId: -1,
            routes: [],
            selectedRouteIndex: -1 
        };

        this.loadMapData                    = this.loadMapData.bind(this);
        this.sendRoute                      = this.sendRoute.bind(this);
        this.convertMapJSON                 = this.convertMapJSON.bind(this);
        this.onStationButtonClickHandler    = this.onStationButtonClickHandler.bind(this);
        this.onRouteClickHandler            = this.onRouteClickHandler.bind(this);
        this.goToNextStage                  = this.goToNextStage.bind(this);
    }

    componentWillMount(){
        this.loadMapData();
    }

    loadMapData(){
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "/map", true);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
                this.convertMapJSON(xhr.responseText);
            }
        }
        xhr.send(null);
    }

    sendRoute(route){
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/start");
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
                // Reload page when server has sucessfully accepted request
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify(route));
    }

    convertMapJSON(mapJSON){
        const map = JSON.parse(mapJSON);

        const stations = map["stations"];
        const convertedStations = [];

        for (let station of stations){
            let stationObj = {
                id : station["id"],
                name : station["name"],
                stationFlow : station["station_flow"]
            }

            convertedStations.push(stationObj);
        }

        const lines = map["lines"];
        const convertedLines = [];

        for (let line of lines){
            let lineStations = (() => {
                let stations = [];

                for (let id of line["station_ids"]){
                    stations.push(MapUtils.getStationById(id, convertedStations));
                }

                return stations;
            })();

            let lineObj = {
                name : line["name"],
                color : line["color"],
                stations : lineStations
            }

            convertedLines.push(lineObj);
        }

        this.setState({ lines: convertedLines, stations: convertedStations });
    }

    onStationButtonClickHandler(event){
        // From StationButton's div element.
        const stationId = event.target.attributes["data-stationId"].value;

        // Don't continue if the station selected is the same as the previous station.
        if (stationId == this.state.startStationId || stationId == this.state.endStationId){
            return;
        }

        // Choosing start station stage.
        if (this.state.stage === 0){
            this.setState({ startStationId: stationId }, this.goToNextStage);
        }
        // Choosing end station stage.
        else if (this.state.stage === 1){
            this.setState({ endStationId: stationId }, this.goToNextStage);            
        }
    }

    onRouteClickHandler(event){
        const routeIndex = event.target.attributes["data-routeIndex"].value;

        this.setState({ selectedRouteIndex: routeIndex });
    }

    goToNextStage(){
        /*
         *  Stage 0: choosing start station stage
         *  Stage 1: choosing end station stage
         *  Stage 2: choosing route stage
         *  Stage 3: moving stage
         */
        const currentStage = this.state.stage;

        // Don't continue if stations or route are not selected.
        if (currentStage === 0){
            if (this.state.startStationId == -1){
                return;
            }
        }
        else if (currentStage === 1){
            if (this.state.endStationId == -1){
                return;
            }
        }
        else if (currentStage === 3){
            if (this.state.selectedRouteIndex == -1){
                return;
            }
        }

        // Move on to next stage if all checks passed.
        if (currentStage < 3){
            this.setState({ stage: currentStage + 1 });
        }
        else{
            this.setState({ stage: 0 });            
        }

        // If next stage is 2, generate routes.
        if (currentStage + 1 === 2){
            let startStation = MapUtils.getStationById(this.state.startStationId, this.state.stations);
            let endStation = MapUtils.getStationById(this.state.endStationId, this.state.stations);

            this.setState({ routes: MapUtils.getPossibleRoutes(startStation, endStation, this.state.stations, this.state.lines)});
        }

        if (currentStage + 1 === 3){
            let selectedRoute = this.state.routes[this.state.selectedRouteIndex];

            this.sendRoute(selectedRoute);
        }
    }

    render(){
        return (
            React.createElement("div", {className: "container"}, 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "wrapped columns"}, 
                        React.createElement("img", {id: "logo", src: "/webapp/static/assets/overflow-logo.png"})
                    )
                ), 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "wrapped columns"}, 
                        React.createElement(MessageGuide, {currentStage: this.state.stage, messages: ["choose starting station", "choose destination station", " ", " "]})
                    )
                ), 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "twelve columns"}, 
                        React.createElement(Map, {stations: this.state.stations, lines: this.state.lines, onClickHandler: this.onStationButtonClickHandler, startStationId: this.state.startStationId, endStationId: this.state.endStationId})
                    )
                ), 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "wrapped columns"}, 
                        React.createElement(MessageGuide, {currentStage: this.state.stage, messages: [" ", " ", "pick a route", " "]})
                    )
                ), 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "twelve columns"}, 
                        this.state.stage == 2 ? React.createElement(RoutePicker, {routes: this.state.routes, onClickHandler: this.onRouteClickHandler, selectedRouteIndex: this.state.selectedRouteIndex}) : null
                    )
                ), 
                React.createElement("div", {className: "centered row"}, 
                    React.createElement("div", {className: "wrapped columns"}, 
                        React.createElement(ButtonGuide, {currentStage: this.state.stage, messages: [" ", " ", "go!", " "], visibleAtStage: [2], onClickHandler: this.goToNextStage})
                    )
                )
            )         
        );
    }
}

ReactDOM.render(React.createElement(App, null), document.getElementById("app"));
