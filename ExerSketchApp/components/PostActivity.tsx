import { View, StyleSheet, Text, TextInput, Button, Pressable } from "react-native";
import { useState } from "react";
import axios from "axios";
import * as DocumentPicker from 'expo-document-picker';

const PostActivityStyling = StyleSheet.create(
    {
        body: {
            flex: 1,
            width: "95%",
            height: 150
        },
        inputBox: {
            backgroundColor: "white",
            borderColor: "black",
            height: 30,
            width: "60%",
            padding: 5
        },
        subHeader: {
            fontSize: 22,
            color: "white",
            margin: 5,
        },
        button: {
            
            margin: "auto",
            marginTop: 20,
            width: "90%",
            padding: 10
        }
        
    }
)

const uploadActivity = (title: string, gpxFile: DocumentPicker.DocumentPickerResult | null) =>{


    const formData = new FormData();
    if(gpxFile)
    if (gpxFile.assets != null){

    formData.append("file", {
        uri: gpxFile.assets[0].uri,
        name: gpxFile.assets[0].name,
        type: 'application/gpx+xml',
    } as any
)}
formData.append("title", title)
    
    axios.post('http://192.168.0.38:5000/fileupload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }}
    ).then(response => console.log(response.data))
}

const buttonStyling = (isFile: boolean) => {
 
        return StyleSheet.create({
            buttonText: {
            color: isFile ? "white" : "#b1b1b1",
            textAlign: "center",
            fontSize: 28}})
            }

const PostActivity= ({gpxFile, isFile}: {gpxFile: DocumentPicker.DocumentPickerResult | null, isFile : boolean}) => {

    
    const handleTitleChange = (input: string) =>{
        setTitle(input)
    }

    const [title, setTitle] = useState<string>("")
    const styles = buttonStyling(isFile)
    const [bgColor, setBgColor] = useState<string>("blue")

    return(
        <View style={PostActivityStyling.body}>

            <Text style={PostActivityStyling.subHeader}>Title:</Text>
            <TextInput style={PostActivityStyling.inputBox}
            onChangeText={handleTitleChange}></TextInput>

            
            <Pressable  
            disabled={!isFile} 
            onPress={() => uploadActivity(title, gpxFile)}
            onPressIn={() => setBgColor("#04DDFF")}
            onPressOut={() => setBgColor("blue")}
            style={PostActivityStyling.button}  
                {...{backgroundColor: !isFile ? "#505050" : bgColor}}
            
            >
                <Text style={styles.buttonText}>Upload a File</Text>
            </Pressable>
        </View>
    )
}
export default PostActivity;