import React from 'react';
import { View, Text, Button } from 'react-native';
import axios from 'axios';

const ViewScreen = ({ route, navigation }) => {
  const marcação = route.params.marcação;

  const handleDeleteMarcação = () => {
    axios.delete(`http://seu-servidor/api/marcações/${marcação._id}`)
      .then(() => {
        navigation.navigate('List');
      })
      .catch((error) => {
        console.error('Erro ao excluir marcação: ' + error);
      });
  };

  return (
    <View>
      <Text>Visualizar Marcação:</Text>
      <Text>Nome: {marcação.nome}</Text>
      <Text>Data: {marcação.data}</Text>
      <Text>Hora: {marcação.hora}</Text>
      <Text>Local: {marcação.local}</Text>
      <Text>Assunto: {marcação.assunto}</Text>
      <Button title="Excluir Marcação" onPress={handleDeleteMarcação} />
    </View>
  );
};

export default ViewScreen;
