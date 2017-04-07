import React from 'react';

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
            <div className="messageGuide">
                {
                    this.state.messages.map((message, index) => {
                        return <h4 key={this.props.messages.indexOf(message)}>{message}</h4> 
                    })
                }
            </div>
        );
    }
}

class ButtonGuide extends React.Component{
    render(){
        if (this.props.visibleAtStage.indexOf(this.props.currentStage) == -1){
            return null;    
        }
        else{
            return <button id="button" onClick={this.props.onClickHandler}>{this.props.messages[this.props.currentStage]}</button> 
        }
    }
}

export {MessageGuide, ButtonGuide};