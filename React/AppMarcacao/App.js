import { createAppContainer } from 'react-navigation';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import { createStackNavigator } from 'react-navigation-stack';

import ListScreen from './screens/ListScreen';
import AddScreen from './screens/AddScreen';
import EditScreen from './screens/EditScreen';
import ViewScreen from './screens/ViewScreen';

const MainNavigator = createBottomTabNavigator(
  {
    List: createStackNavigator({ List: ListScreen }),
    Add: createStackNavigator({ Add: AddScreen }),
    Edit: createStackNavigator({ Edit: EditScreen }),
    View: createStackNavigator({ View: ViewScreen }),
  },
  {
    tabBarOptions: {
      activeTintColor: 'blue',
      inactiveTintColor: 'gray',
    },
  }
);

export default createAppContainer(MainNavigator);
