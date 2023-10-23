import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';

const EditScreen = ({ navigation, route }) => {
  const [marcação, setMarcação] = useState(route.params.marcação);

  const handleEditMarcação = () => {
    axios.put(`http://seu-servidor/api/marcações/${marcação._id}`, marcação)
      .then(() => {
        navigation.navigate('List');
      })
      .catch((error) => {
        console.error('Erro ao editar marcação: ' + error);
      });
  };

  return (
    <View>
      <Text>Editar Marcação:</Text>
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
      <Button title="Editar Marcação" onPress={handleEditMarcação} />
    </View>
  );
};

export default EditScreen;
