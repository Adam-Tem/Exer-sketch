import { View, Image, Pressable } from 'react-native'

const NavBarMain = () => {
    return(
        <View style={{backgroundColor: "#EFF6EE", 
        width: "90%",margin: "auto", height: "10%",justifyContent: "space-evenly", flexDirection: "row"}}>
        
        <Pressable>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/home.png')}/>
        </Pressable>

        <Pressable>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/trophy.png')}/>
        </Pressable>

        <Pressable>
            <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/profile.png')}/>
        </Pressable>

        </View>
    );
};
export default NavBarMain;