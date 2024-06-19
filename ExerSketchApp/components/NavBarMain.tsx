import { View, Image, Pressable } from 'react-native'
import { RootStackParamList } from '@/app';
import { StackNavigationProp } from '@react-navigation/stack';
import data from "@/data/scores.json"
import { userScore } from '@/types/userScore';
import { NativeStackScreenProps } from "@react-navigation/native-stack";
import { NavigationProp } from "@react-navigation/native";

const NavBarMain = ({ navigation }: {navigation : NavigationProp<RootStackParamList>}) => {

    const scores: userScore[] = data;
    return(
        <View style={{backgroundColor: "#EFF6EE", 
        width: "90%",margin: "auto", height: "10%",justifyContent: "space-evenly", flexDirection: "row"}}>
        
        <Pressable onPress={() => navigation.navigate("Home")}>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/home.png')}/>
        </Pressable>

        <Pressable onPress={() => navigation.navigate("Leaderboard")}>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/trophy.png')}/>
        </Pressable>

        <Pressable onPress={() => navigation.navigate("Profile")}>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/profile.png')}/>
        </Pressable>

        </View>
    );
};
export default NavBarMain;