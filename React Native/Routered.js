import React, { Component } from 'react';
import { Router, Scene } from 'react-native-router-flux';

import App from './App';
import MainPage from './MainPage';
import Camera1 from './Camera1'
import Camera2 from './Camera2'

export default class Routered extends Component {
  render() {
    return (
      <Router>
        <Scene key='Root'>
            
        
            <Scene key="App" component={App}    hideNavBar />
            <Scene key="MainPage" component={MainPage}  initial  hideNavBar />
            <Scene key="Camera1" component={Camera1}    hideNavBar />
            <Scene key="Camera2" component={Camera2}    hideNavBar />
            
           
        </Scene>
      </Router>
    )
  }
}