import { View, Image, Pressable } from "react-native";
import * as DocumentPicker from 'expo-document-picker';
import { Dispatch, SetStateAction } from "react";

      
const uploadGPX = async (setFile: Dispatch<SetStateAction<DocumentPicker.DocumentPickerResult| null>>) =>{
    const response = await DocumentPicker.getDocumentAsync({type: 'application/gpx+xml'})
   console.log(response.assets)
   if (response.assets){
   setFile(response)}
 }

const UploadGPXButton = ({setFile}: {setFile: Dispatch<SetStateAction<DocumentPicker.DocumentPickerResult| null>>}) => {

    return(
    <View>
        <Pressable onPress={() => {uploadGPX(setFile)}}>
        <Image style={{margin:"auto", width: 70, height: 70}} source={require('../assets/images/plus.png')}/>
        </Pressable>
    </View>
    )}

export default UploadGPXButton;