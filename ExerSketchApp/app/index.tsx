import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StatusBar } from 'react-native';
import HomeScreen from '../screens/HomeScreen';
import LeaderboardScreen from '../screens/LeaderboardScreen';
import ProfileScreen from '../screens/ProfileScreen'
import { userScore } from '@/types/userScore';
import data from "../data/scores.json";

export type RootStackParamList = {
  Home: undefined,
  Leaderboard: undefined,
  Profile: undefined
}

const Stack = createNativeStackNavigator<RootStackParamList>();

export default function Index() {
  return (
<Stack.Navigator screenOptions={{ headerShown: false, animation: "none"}}>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Leaderboard" component={LeaderboardScreen}/>
  <Stack.Screen name="Profile" component={ProfileScreen}/>
</Stack.Navigator>
  );
}

