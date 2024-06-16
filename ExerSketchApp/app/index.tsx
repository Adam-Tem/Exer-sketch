import { View, StyleSheet} from "react-native";
import NavBarMain from "@/components/NavBarMain";
import GlobalLeaderboard from "@/components/GlobalLeaderboard";
import scores from "../data/scores.json";


export default function Index() {
  return (
    <View style={{flex: 1, backgroundColor: "#493657"}}>

      <View style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
         margin: "5%", marginBottom: "0%"}}>
          <GlobalLeaderboard scores={scores}></GlobalLeaderboard>
         </View>
         <NavBarMain></NavBarMain>
      
    </View>
  );
}

