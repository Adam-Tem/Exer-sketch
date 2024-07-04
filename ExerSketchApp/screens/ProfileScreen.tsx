import { View, Text, Button } from "react-native";
import NavBarMain from "@/components/NavBarMain";
import { NavigationProp } from "@react-navigation/native";
import { RootStackParamList } from "@/app";
import UploadGPXButton from "@/components/UploadGPXButton";
import { useEffect, useState } from "react";
import PostActivity from "@/components/PostActivity";
import * as DocumentPicker from 'expo-document-picker';



export default function ProfileScreen( { navigation } : {navigation: NavigationProp<RootStackParamList>}){
    
   const [file, setFile] = useState<DocumentPicker.DocumentPickerResult | null>(null);
   const [fileName, setFileName] = useState<string>("");
   const [isFile, setIsFile] = useState<boolean>(false);
   useEffect(() => {
      if(file){
         if(file.assets){
      setFileName(file.assets[0].name)
      setIsFile(true)

         }
      }
   })

   return(
    <View style={{flex: 1, backgroundColor: "#493657"}}>

    <View style={{flex: 1, backgroundColor: "#087E8B", width: "90%",
       margin: "5%", marginBottom: "0%"}}>
        <Text style={{fontSize: 28}}>Welcome to the profile screen!</Text>
        <UploadGPXButton setFile={setFile}></UploadGPXButton>
        <Text>{fileName}</Text>
        <PostActivity gpxFile={file} isFile={isFile}></PostActivity>
       </View>
       <NavBarMain navigation={navigation}></NavBarMain>
  </View>
    )
}