import { View, Text, Button, ScrollView, FlatList } from "react-native";
import NavBarMain from "@/components/NavBarMain";
import {activityData} from "@/types/activityData"
import { NavigationProp } from "@react-navigation/native";
import { RootStackParamList } from "@/app";
import { useEffect, useState } from "react";
import axios from 'axios';
import ActivityContainer from "@/components/AcitvityContainer";



export default function HomeScreen( { navigation } : {navigation: NavigationProp<RootStackParamList>}){

  const [data, setData] = useState<activityData[]>([])

  const fetchData = async () =>{
    try{
      const response = await axios.get("http://192.168.0.38:5000/activities")
      setData(response.data)
      console.log(data)
    }catch(error){
      console.log(error)
    }
  }

    return(
    <View style={{flex: 1, backgroundColor: "#493657"}}>

    <View style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
       margin: "5%", marginBottom: "0%"}}>
        <Text style={{fontSize: 28}}>Welcome to the home page!</Text>
        <Button title="get data" onPress={fetchData}></Button>
        <FlatList 
            data={data}
            renderItem={ ({item}) =>
              <ActivityContainer data={item}></ActivityContainer> 
            }
       />
       </View>
       <NavBarMain navigation={navigation}></NavBarMain>
  </View>
    )
}