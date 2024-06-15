import { View, Text , ScrollView} from "react-native";
import NavBarMain from "@/components/NavBarMain";

export default function Index() {
  return (
    <View style={{flex: 1, backgroundColor: "#493657"}}>

      <ScrollView style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
         margin: "5%", marginBottom: "0%"}}>
          <Text style={{ margin: "auto", paddingTop: "50%"}}>Hello</Text>
         </ScrollView>
         <NavBarMain></NavBarMain>
      
    </View>
  );
}
