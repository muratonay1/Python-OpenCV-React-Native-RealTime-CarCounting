import {View,Text,Alert,ImageBackground,Dimensions,Image,TouchableOpacity,Modal,TouchableHighlight} from 'react-native';
import React,{Component} from 'react';
import firebase from 'firebase';
import Icon1 from 'react-native-vector-icons/AntDesign';
import { Actions } from 'react-native-router-flux';
console.disableYellowBox = true;
let width=Dimensions.get('window').width;
let height=Dimensions.get('window').height;

export default class MainPage extends Component{

  
  
  
  

  
  render(){

    return(

      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
        <ImageBackground source={require('./Photo/foto.png')} style={{width:width,height:150}} blurRadius={3}>
          <View style={{flex:1,alignItems:'center',justifyContent:'center'}}>
            <Text style={{color:'white',fontSize:25}}>Real-Time Car Counting App</Text>
          </View>
        </ImageBackground>
        
          
        <View style={{flex:1,justifyContent:'space-evenly',alignItems:'center',backgroundColor:'#313131',flexDirection:'row'}}>
          
          <View style={{flex:1,justifyContent:'center',alignItems:'center',top:-25}}>
            <Text style={{fontFamily:'Rajdhani-Regular',fontSize:15,color:'red'}}>Camera 1</Text>
            <TouchableOpacity onPress={()=>Actions.Camera1()}>
              <Image
              style={{width: 150, height: 100}}
              source={require('./Photo/cam1.png')}
              
              />
            </TouchableOpacity>
          </View>
          
          
          <View style={{flex:1,justifyContent:'center',alignItems:'center',top:-25}}>
            <Text style={{fontFamily:'Rajdhani-Regular',fontSize:15,color:'red'}}>Camera 2</Text>
            <TouchableOpacity onPress={()=>Actions.Camera2()}>
              <Image
              style={{width: 150, height: 103}}
              source={require('./Photo/cam2.png')}
              />
            </TouchableOpacity>
          </View>
          
        </View>
        
        
        


        
      </View>
    )
  }
}