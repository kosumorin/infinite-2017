window.onload = function () {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/map", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200){
            MRT.convertMapJSON(JSON.parse(xhr.responseText));
            ReactDOM.render(React.createElement(App, null), document.getElementById('app'));
        }
    }
    xhr.send(null)
};

var MRT = {
    lines : [],
    stations : [],
    convertDirToMovementDir : function (fromDir, toDir){
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
    convertMapJSON : function (mapJSON){
        var stations = mapJSON["stations"];

        for (let station of stations){
            let stationObj = {
                id : station["id"],
                name : station["name"],
                stationFlow : station["station_flow"]
            }

            this.stations.push(stationObj);
        }

        var lines = mapJSON["lines"];

        for (let line of lines){
            let lineStations = (() => {
                let stations = [];

                for (let id of line["station_ids"]){
                    stations.push(this.getStationById(id));
                }

                return stations;
            })();

            let lineObj = {
                name : line["name"],
                color : line["color"],
                stations : lineStations
            }

            this.lines.push(lineObj);
        }
    },
    findInterchangeFromStation : function (station){
        let stationLines = this.getLinesOfStation(station);

        let interchanges = [];

        for (let line of this.lines){
            for (let stationLine of stationLines){
                if (line == stationLine){
                    continue;
                }

                for (let interchange of this.findInterchangeFromLines(line, stationLine)){
                    interchanges.push(interchange);
                }
            }
        }

        interchanges = interchanges.filter(function (interchange, index, self) {
            return self.indexOf(interchange) == index;
        })

        return interchanges;
    },
    findInterchangeFromLines : function (line1, line2){
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
    getInterchangeTurnDirection : function(interchange, fromStation, toStation, fromLine, toLine) {
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

        if (!isTrainFacingOppOnFromLine){
            toDirection = interchange.stationFlow[toLine.name]["next"]
        }
        else{
            toDirection = interchange.stationFlow[toLine.name]["previous"]
        }

        return this.convertDirToMovementDir(fromDirection, toDirection);
    },
    getStationById : function (id){
        for (let station of this.stations){
            if (station["id"] == id){
                return station;
            }
        }
    },
    getStationByName : function (name){
        for (let station of this.stations){
            if (station["name"].toUpperCase() == name.toUpperCase()){
                return station;
            }
        }
    },
    getLinesOfStation : function (targetStation){
        let lines = [];

        for (let line of this.lines){
            for (let station of line.stations){
                if (station == targetStation){
                    lines.push(line);
                }
            }
        }

        return lines;
    },
    getStationOnLineByIndex : function (index, line){
        for (let i = 0; i < line.stations.length; i++){
            if (i == index){
                return line.stations[i];
            }
        }
    },
    getIndexOfStationOnLine : function (station, line){
        for (let i = 0; i < line.stations.length; i++){
            if (station == line.stations[i]){
                return i;
            }
        }
    },
    getLineByName : function (name){
        for (let line of this.lines){
            if (line["name"].toUpperCase() == name.toUpperCase()) {
                return line;
            }
        }
    },
    getPossibleRoutes : function (startStation, endStation){
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

        let startStationLines = this.getLinesOfStation(startStation);
        let endStationLines = this.getLinesOfStation(endStation);

        for (let startLine of startStationLines){
            for (let endLine of endStationLines){
                if (startLine != endLine){ // Change of lines required.
                    let interchanges = this.findInterchangeFromLines(startLine, endLine);

                    for (let interchange of interchanges){
                        // Don't let the interchange be the start station.
                        if (interchange == startStation){
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
                        {},
                        this.generateStationPath(startStation, endStation, startLine),
                        this.generateMovementFlow(startStation, endStation, startLine)
                    ));
                }
            }
        }

        return routes;
    },
    generateStationPath : function (fromStation, toStation, line){
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
    generateMovementFlow : function (fromStation, toStation, line){
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
    isTrainFacingOpp : function (fromStation, toStation, line){
        if (this.getIndexOfStationOnLine(fromStation, line) < this.getIndexOfStationOnLine(toStation, line)){
            return false;
        }
        else{
            return true;
        }
    }
};

class StationItem extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return React.createElement("option", null, this.props.name);
    }
}

class StationSelector extends React.Component{
    constructor(props){
        super(props);

        this.stations = props.stations.map((station, index) => {
            return React.createElement(StationItem, {key: index+1, name: station.name})
        });
        this.stations.unshift(React.createElement(StationItem, {key: "0", name: ""}));
    }

    render(){
        return (
            React.createElement("select", {onChange: this.props.handler},
                this.stations
            )
        );
    }
}

class RouteItem extends React.Component{
    constructor(props){
        super(props);

        // Check for first elem. First elem is empty. (Dirty hack up mah sleeves)
        if (props.route["start_station"] === "") {
            return;
        }

        const startStation = props.route["start_station"]["name"];
        const endStation = props.route["end_station"]["name"];
        const transStation = props.route["transfer_station"]["name"];

        this.routeInfo = "";

        if (transStation == null){
            this.routeInfo = startStation + " -> " + endStation;
        }
        else {
            this.routeInfo = startStation + " -> " + transStation + " -> " + endStation;
        }
    }

    render(){
        return React.createElement("option", null, this.routeInfo);
    }
}

class RouteSelector extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            React.createElement("select", {onChange: this.props.handler},

                    this.props.routes.map((route) => {
                        // The only way that I can make a unique key so that React will update properly
                        const key = route["start_station"]["id"] + "|"   + route["transfer_station"]["id"] + "|" + route["end_station"]["id"];
                        return React.createElement(RouteItem, {key: key, route: route});
                    })

            )
        );
    }
}

class TripForm extends React.Component{
    constructor(props){
        super(props);
        this.state = {startStation:'', endStation: '', selectedRoute: null, routes: []};
        this.handleStartStationChange = this.handleStartStationChange.bind(this);
        this.handleEndStationChange = this.handleEndStationChange.bind(this);
        this.handleRouteChange = this.handleRouteChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.getRoutes = this.getRoutes.bind(this);
    }

    handleStartStationChange(event){
        this.setState({startStation: event.target.value}, this.getRoutes);
    }

    handleEndStationChange(event){
        this.setState({endStation: event.target.value}, this.getRoutes);
    }

    getRoutes(){
        const startStation = MRT.getStationByName(this.state.startStation);
        const endStation = MRT.getStationByName(this.state.endStation);

        const possibleRoutes = MRT.getPossibleRoutes(startStation, endStation);
        possibleRoutes.unshift({
            start_station: "",
            end_station: "",
            start_line: "",
            end_line: "",
            transfer_station: "",
            station_path: "",
            movement_flow: ""
        });

        this.setState({routes: possibleRoutes});
    }

    handleRouteChange(event){
        const selectedRouteIndex = event.target.selectedIndex;
        this.setState({selectedRoute: this.state.routes[selectedRouteIndex]});
    }

    handleSubmit(event){
        const route = this.state.selectedRoute;

        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/start", true);
        xhr.send(JSON.stringify(route));
    }

    render(){
        return (
            React.createElement("div", {className: "tripForm"},
                React.createElement("div", {className: "row"},
                    React.createElement("h6", null, "👇 Choose starting station 👇")
                ),
                React.createElement("div", {className: "row"},
                    React.createElement("div", {className: "eight columns"},
                        React.createElement(StationSelector, {id: "startStationSelector", handler: this.handleStartStationChange, stations: this.props.stations})
                    )
                ),
                React.createElement("div", {className: "row"},
                    React.createElement("h6", null, "👇 Choose destination station 👇")
                ),
                React.createElement("div", {className: "row"},
                    React.createElement("div", {className: "eight columns"},
                        React.createElement(StationSelector, {id: "endStationSelector", handler: this.handleEndStationChange, stations: this.props.stations})
                    )
                ),
                React.createElement("div", {className: "row"},
                    React.createElement("h6", null, "👇 Choose a route! 👇")
                ),
                React.createElement("div", {className: "row"},
                    React.createElement("div", {className: "eight columns"},
                        React.createElement(RouteSelector, {id: "routeSelector", handler: this.handleRouteChange, routes: this.state.routes})
                    )
                ),
                React.createElement("div", {className: "row start"},
                    React.createElement("input", {type: "submit", value: "Start!", onClick: this.handleSubmit})
                )
            )
        );
    }
}

class App extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        return (
            React.createElement("div", null,
                React.createElement("div", {className: "container"},
                    React.createElement("div", {className: "row"},
                        React.createElement("img", {src: "./static/img/overflow-logo.png", id: "logo"})
                    ),
                    React.createElement(TripForm, {stations: MRT.stations})
                )
            )
        );
    }
}
