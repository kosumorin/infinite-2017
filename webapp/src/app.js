import React from 'react';
import Map from './map';
import RoutePicker from './route';
import { MapUtils } from './utils';

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

        this.guideMessage = [
            "choose starting station",
            "choose destination station",
            "choose preferred route"
        ];

        this.buttonMessage = [
            "next",
            "next",
            "go!"
        ]
        
        this.onStationButtonClickHandler    = this.onStationButtonClickHandler.bind(this);
        this.onRouteClickHandler            = this.onRouteClickHandler.bind(this);
        this.goToNextStage                  = this.goToNextStage.bind(this);
        this.loadMapData                    = this.loadMapData.bind(this);
        this.convertMapJSON                 = this.convertMapJSON.bind(this);
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
            this.setState({ startStationId: stationId });
        }
        // Choosing end station stage.
        else if (this.state.stage === 1){
            this.setState({ endStationId: stationId });            
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

        // Don't continue if stations are not selected.
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
    }

    render(){
        return (
            <div className="container">
                <div className="row">
                    <div className="twelve columns">
                        <h3>{this.guideMessage[this.state.stage]}</h3>
                    </div>
                </div>
                <div className="row">
                    <div className="twelve columns">                    
                        <Map stations={this.state.stations} lines={this.state.lines} onClickHandler={this.onStationButtonClickHandler} startStationId={this.state.startStationId} endStationId={this.state.endStationId}/>
                    </div>
                </div>
                <div className="row">
                    <div className="twelve columns">
                        <RoutePicker routes={this.state.routes} onClickHandler={this.onRouteClickHandler} selectedRouteIndex={this.state.selectedRouteIndex}/>
                    </div>
                </div>
                <div className="row">
                    <button onClick={this.goToNextStage}>{this.buttonMessage[this.state.stage]}</button>
                </div>
            </div>
        );
    }
}

export default App;