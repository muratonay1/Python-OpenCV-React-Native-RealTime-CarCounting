import {View,Text,Alert,ImageBackground,Dimensions,Image,TouchableOpacity,Modal,TouchableHighlight} from 'react-native';
import React,{Component} from 'react';
import firebase from 'firebase';
import Icon1 from 'react-native-vector-icons/AntDesign';
console.disableYellowBox = true;
let width=Dimensions.get('window').width;
let height=Dimensions.get('window').height;
import {Actions, Router} from 'react-native-router-flux';
import RouterControl from './Routered';
export default class Camera2 extends Component{
    constructor(props){
        super(props);
        
        this.state={
          data_source:"",
          
        }
      }
    async UNSAFE_componentWillMount(){
    
        
        firebase.database().ref('ArabaSayac').once('value', (data)=>{
          var deger=data.toJSON();
          var x=deger.Sayac
          this.setState({'data_source':x})
        })
    
        firebase.database().ref('ArabaSayac').on('value', (data)=>{
          var deger=data.toJSON();
          var x=deger.Sayac2
          this.setState({'data_source':x})
        })
    
        setTimeout(()=>{
    
        })
        
      }

  
  render(){

    return(

      <View style={{flex:1,backgroundColor:'#313131',justifyContent:'center',alignItems:'center'}}>
        <View style={{flex:0.5,justifyContent:'center',alignItems:'center'}}>
            <Text style={{fontFamily:'Rajdhani-Regular',fontSize:35,color:'yellow',textAlign:'center'}}>Cam2</Text>
        </View>

        <View style={{flex:1}}>
        <ImageBackground style={{width: width, height: height*0.3}} source={require('./Photo/cam2.png')} >
          <Image
              style={{width: width, height: height*0.3}}
              source={require('./Photo/rec.jpg')}
              style={{width:width*0.1,height:height*0.05}}
          />
          
        </ImageBackground>
        </View>

        <View style={{flex:1}}>
            <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
                <Text style={{fontFamily:'Rajdhani-Regular',fontSize:40,color:'#4AC959',textAlign:'center'}}>{this.state.data_source}</Text>
            </View>

            <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
                <TouchableOpacity style={{backgroundColor:'#525252',justifyContent:'center',alignItems:'center',height:height*0.08,width:width*0.5,borderRadius:10}} onPress={()=>Actions.MainPage()}>
                    <Text style={{fontFamily:'Rajdhani-Regular',fontSize:15,color:'snow',textAlign:'center'}}>Geri</Text>
                </TouchableOpacity>
            </View>
        </View>
          
        
        

        
      </View>
    )
  }
}