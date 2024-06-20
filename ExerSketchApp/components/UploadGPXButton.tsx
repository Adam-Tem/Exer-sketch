import { View, Image, Pressable } from "react-native";
import * as DocumentPicker from 'expo-document-picker';
import { Dispatch, SetStateAction } from "react";

      
const uploadGPX = async (setFile: Dispatch<SetStateAction<string>>) =>{
    const response = await DocumentPicker.getDocumentAsync({})
   console.log(response.assets)
   if (response.assets){
    console.log(response.assets[0]["uri"])
   setFile(response.assets[0]["uri"])}
 }

const UploadGPXButton = ({setFile}: {setFile: Dispatch<SetStateAction<string>>}) => {

    return(
    <View>
        <Pressable onPress={() => {uploadGPX(setFile)}}>
        <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/plus.png')}/>
        </Pressable>
    </View>
    )}

export default UploadGPXButton;