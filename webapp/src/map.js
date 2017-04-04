import React from 'react';
import { MapUtils } from './utils';

class LineTag extends React.Component{
    render(){
        return <div className={"lineTag " + this.props.lineName}>{this.props.lineName}</div>
    }
}

class StationTag extends React.Component{
    render(){
        return (
            <div className="stationTag">
                {
                    this.props.linesOfStation.map((line, index) => {
                        return <LineTag key={index} lineName={line["name"]}/>
                    })
                }
                <div>{this.props.stationName}</div>   
            </div>
        );
    }
}

class StationButton extends React.Component{
    render(){
        let className = "stationButton";

        if (this.props.isSelected){
            className += " selected";
        }

        return <div className={className} data-stationId={this.props.stationId} onClick={this.props.onClickHandler}></div>;
    }
}

class Station extends React.Component{
    render(){
        const uniqueId = this.props.station["name"].replace(/\s/g, "");

        return (
            <div className="station" id={uniqueId}>
                <StationTag stationName={this.props.station["name"]} linesOfStation={this.props.linesOfStation}/>
                <StationButton stationId={this.props.station["id"]} isSelected={this.props.isSelected} onClickHandler={this.props.onClickHandler} />
            </div>
        );         
    }
}

class Map extends React.Component{
    render(){
        return ( 
            <div className="map">
                {
                    this.props.stations.map((station, index) => {
                        const linesOfStation = MapUtils.getLinesOfStation(station, this.props.lines);

                        let isSelected = false;
                        if (station == MapUtils.getStationById(this.props.startStationId, this.props.stations) || station == MapUtils.getStationById(this.props.endStationId, this.props.stations)){
                            isSelected = true;
                        }

                        return <Station key={index} station={station} linesOfStation={linesOfStation} isSelected={isSelected} onClickHandler={this.props.onClickHandler}/>;
                    })
                }
            </div>
        );
    }
}

export default Map;
