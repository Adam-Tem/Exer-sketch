import { View, StyleSheet, Text } from "react-native";
import {activityData} from "@/types/activityData"

const ActivityContainerStyling = StyleSheet.create(
    {
        body: {
            backgroundColor: "green",
            flex: 1,
            height: 300,
            width: "95%",
            margin: "auto",
            marginTop: 40,
            borderColor: "white",
            borderWidth: 2,

        },
        title: {
            color: "white",
            fontWeight: "bold",
            fontSize: 28,
            marginLeft: 10,
            marginTop: 5,
        },
        subText: {
            fontSize: 18,
            color: "red",
            margin: "auto"
        }
    }
)

type ActivityContainerProps = {
    data: activityData
}
const ActivityContainer: React.FC<ActivityContainerProps> = ({data}) => {

    return(
        <View style={ActivityContainerStyling.body}>
            <Text style={ActivityContainerStyling.title}>Activity {data.id}</Text>
            <Text style={ActivityContainerStyling.subText}>{data.score}</Text>

        </View>
    )
}
export default ActivityContainer;