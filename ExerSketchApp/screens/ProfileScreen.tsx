import { View, Text, Button } from "react-native";
import NavBarMain from "@/components/NavBarMain";
import { NavigationProp } from "@react-navigation/native";
import { RootStackParamList } from "@/app";



export default function ProfileScreen( { navigation } : {navigation: NavigationProp<RootStackParamList>}){
    return(
    <View style={{flex: 1, backgroundColor: "#493657"}}>

    <View style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
       margin: "5%", marginBottom: "0%"}}>
        <Text style={{fontSize: 28}}>Welcome to the profile screen!</Text>
       </View>
       <NavBarMain navigation={navigation}></NavBarMain>
  </View>
    )
}