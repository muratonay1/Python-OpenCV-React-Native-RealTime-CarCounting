import {View,Text,Alert,ImageBackground,Dimensions,Image,TouchableOpacity,Modal,TouchableHighlight} from 'react-native';
import React,{Component} from 'react';
import firebase from 'firebase';
import Icon1 from 'react-native-vector-icons/AntDesign';
console.disableYellowBox = true;
let width=Dimensions.get('window').width;
let height=Dimensions.get('window').height;
import {Actions, Router} from 'react-native-router-flux';
import RouterControl from './Routered';
export default class App extends Component{
  componentWillMount(){
    var firebaseConfig = {
      apiKey: "AIzaSyDwOx9AwAkJm9IXxvGySXseV0W5joV8agw",
      authDomain: "carcounting-a39b1.firebaseapp.com",
      databaseURL: "https://carcounting-a39b1.firebaseio.com",
      projectId: "carcounting-a39b1",
      storageBucket: "carcounting-a39b1.appspot.com",
      messagingSenderId: "1049807557575",
      appId: "1:1049807557575:web:0e5e8338cf25e9d9083fe2",
      measurementId: "G-M5RD78JVNH"
    };
    firebase.initializeApp(firebaseConfig);
  }
  
  render(){

    return(

      <View style={{flex:1}}>
        
          
        <View style={{flex:10}}>
          
            <RouterControl/>
        </View>

        <View style={{flex:1,justifyContent:'flex-end',alignItems:'center',backgroundColor:'#313131'}}>
          <Text style={{fontSize:9,color:'#25D366'}}>İsmet Murat ONAY</Text>
          <Text style={{fontSize:9,color:'#25D366'}}>Contact Me: imuratony@gmail.com</Text>
          
        </View>


        
      </View>
    )
  }
}