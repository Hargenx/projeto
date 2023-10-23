import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';

const AddScreen = ({ navigation }) => {
  const [marcação, setMarcação] = useState({
    nome: '',
    data: '',
    hora: '',
    local: '',
    assunto: '',
  });

  const handleAddMarcação = () => {
    axios.post('http://seu-servidor/api/marcações', marcação)
      .then(() => {
        navigation.navigate('List');
      })
      .catch((error) => {
        console.error('Erro ao adicionar marcação: ' + error);
      });
  };

  return (
    <View>
      <Text>Adicionar Marcação:</Text>
      <TextInput
        placeholder="Nome"
        value={marcação.nome}
        onChangeText={(text) => setMarcação({ ...marcação, nome: text })}
      />
      <TextInput
        placeholder="Data"
        value={marcação.data}
        onChangeText={(text) => setMarcação({ ...marcação, data: text })}
      />
      <TextInput
        placeholder="Hora"
        value={marcação.hora}
        onChangeText={(text) => setMarcação({ ...marcação, hora: text })}
      />
      <TextInput
        placeholder="Local"
        value={marcação.local}
        onChangeText={(text) => setMarcação({ ...marcação, local: text })}
      />
      <TextInput
        placeholder="Assunto"
        value={marcação.assunto}
        onChangeText={(text) => setMarcação({ ...marcação, assunto: text })}
      />
      <Button title="Adicionar Marcação" onPress={handleAddMarcação} />
    </View>
  );
};

export default AddScreen;
