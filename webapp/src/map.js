import React from 'react';
import { MapUtils } from './utils';

class StationInfo extends React.Component{
    render(){
        return (
            <div className="stationInfo">
                {
                    this.props.lineNames.map((lineName, index) => {
                        return <div key={index} className={"lineTag " + lineName}>{lineName}</div>
                    })
                }
                <div className="stationTag">{this.props.stationName}</div>
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
                <StationInfo stationName={this.props.station["name"]} lineNames={this.props.lineNames}/>
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
                        const lineNames = MapUtils.getLinesOfStation(station, this.props.lines).map((line) => {
                            return line["name"];
                        });

                        let isSelected = false;
                        if (station == MapUtils.getStationById(this.props.startStationId, this.props.stations) || station == MapUtils.getStationById(this.props.endStationId, this.props.stations)){
                            isSelected = true;
                        }

                        return <Station key={index} station={station} lineNames={lineNames} isSelected={isSelected} onClickHandler={this.props.onClickHandler}/>;
                    })
                }
            </div>
        );
    }
}

export { StationInfo };
export default Map;
