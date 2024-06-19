import { View } from "react-native";
import scores from "../data/scores.json";
import NavBarMain from "@/components/NavBarMain";
import GlobalLeaderboard from "@/components/GlobalLeaderboard";
import { RootStackParamList } from "@/app";
import { NavigationProp } from "@react-navigation/native";


export default function LeaderboardScreen( { navigation } : {navigation: NavigationProp<RootStackParamList>}){
    return(
    <View style={{flex: 1, backgroundColor: "#493657"}}>

    <View style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
       margin: "5%", marginBottom: "0%"}}>
        <GlobalLeaderboard scores={scores}></GlobalLeaderboard>
       </View>
       <NavBarMain navigation={navigation}></NavBarMain>
    
  </View>
    )
}