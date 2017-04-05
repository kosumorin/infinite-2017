import React from 'react';
import { StationInfo } from './map';

class Route extends React.Component{
    render(){
        let className = this.props.isSelected ? "route selected" : "route";
        let element = null;

        if (this.props.route["transfer_station"] == null){
            let startStationName = this.props.route["start_station"]["name"];
            let endStationName = this.props.route["end_station"]["name"];

            let lineName = this.props.route["start_line"]["name"]; 
            
            element = (
                <div className={className} data-routeIndex={this.props.routeIndex} onClick={this.props.onClickHandler}>
                    <StationInfo stationName={startStationName} lineNames={[lineName]}/>
                    <div className="arrow"></div>
                    <StationInfo stationName={endStationName} lineNames={[lineName]}/>
                </div> 
            );
        }
        else{
            let startStationName = this.props.route["start_station"]["name"];
            let transferStationName = this.props.route["transfer_station"]["name"];
            let endStationName = this.props.route["end_station"]["name"]; 

            let startLineName = this.props.route["start_line"]["name"];
            let endLineName = this.props.route["end_line"]["name"];

            element = (
                <div className={className} data-routeIndex={this.props.routeIndex} onClick={this.props.onClickHandler}>
                    <StationInfo stationName={startStationName} lineNames={[startLineName]}/>
                    <div className="arrow"></div>
                    <StationInfo stationName={transferStationName} lineNames={[startLineName, endLineName]}/>
                    <div className="arrow"></div>
                    <StationInfo stationName={endStationName} lineNames={[endLineName]}/>
                </div> 
            );
        }

        return element;
    }
}

class RoutePicker extends React.Component{
    render(){
        return (
            <div className="routePicker">
                {
                    this.props.routes.map((route, index) => {
                        let isSelected = false;
                        if (index == this.props.selectedRouteIndex){
                            isSelected = true;
                        }

                        return <Route key={index} routeIndex={index} route={route} isSelected={isSelected} onClickHandler={this.props.onClickHandler}/>;
                    })
                }
            </div>
        );
    }
}

export default RoutePicker;