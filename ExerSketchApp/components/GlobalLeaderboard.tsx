import { FlatList, View, Text, StyleSheet, ScrollView } from "react-native";
import { userScore } from "@/types/userScore";

const leaderboardStyling = StyleSheet.create(
    {
        header: {
            color: "white",
            fontSize: 32
        },
        positionText : {
            fontSize: 32,
            fontWeight: "heavy"
        },
      idText : {
        color: "white",
        fontSize: 32,
      },
      scoreText : {
        color: "yellow",
        fontSize: 24,
      },
      scoreContainer : {
        flexDirection : "row",
        justifyContent: "space-around",
        marginTop: 20
      }

    })

    const orderScores = (scores: userScore[]): userScore[] => {
        return scores.slice().sort((a, b) => b.score - a.score);
    }

const GlobalLeaderboard = ({ scores }:{scores: userScore[]} ) => {

    const orderedScores = orderScores(scores);

    return(
    
        <View>
            <Text style={leaderboardStyling.header}>Global Leaderboard</Text>
    <FlatList
     
    data={orderedScores}
    renderItem={ ({item, index}) => {
        return(
            <View style={leaderboardStyling.scoreContainer}>
                <Text style={leaderboardStyling.positionText}>#{index + 1}</Text>
                <Text style={leaderboardStyling.idText}>{item.id.toString()}</Text>
                <Text style={leaderboardStyling.scoreText}>{item.score.toString()}</Text>
            </View>
        )
    } }

    />
    </View>
    )
}

export default GlobalLeaderboard;