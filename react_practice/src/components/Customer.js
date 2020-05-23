import React from 'react';

class Customer extends React.Component{
    render(){
        return(
            <div>
               <CustomerProfile id={this.props.id} image={this.props.image} name={this.props.name}/>
               <CustomerInfo birthday={this.props.birthday} gender={this.props.gender} job={this.props.job}/>
            </div>

        )
        
    }
}

class CustomerProfile extends React.Component{
    render(){
        return(
            <div>
                <img src={this.props.img} alt="profile"/>
                <h2>{this.props.name}({this.props.id})</h2>
            </div>
        )
    }
}

class CustomerInfo extends React.Component{
    render(){
        return(
            <dic>
                <p>{this.props.birthday}</p>
                <p>{this.props.gender}</p>
                <p>{this.props.job}</p>
            </dic>
        )
    }
}

export default Customer;