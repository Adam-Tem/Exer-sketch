import { View, StyleSheet, Text, TextInput, Button } from "react-native";
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

const PostActivity= ({gpxFile}: {gpxFile: DocumentPicker.DocumentPickerResult | null}) => {

    
    const handleTitleChange = (input: string) =>{
        setTitle(input)
    }

    const [title, setTitle] = useState<string>("")

    return(
        <View style={PostActivityStyling.body}>

            <Text style={PostActivityStyling.subHeader}>Title:</Text>
            <TextInput style={PostActivityStyling.inputBox}
            onChangeText={handleTitleChange}></TextInput>

            
            <Button title="Upload new post" onPress={() => uploadActivity(title, gpxFile)}></Button>
        </View>
    )
}
export default PostActivity;