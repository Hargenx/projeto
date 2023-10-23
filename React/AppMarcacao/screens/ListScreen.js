import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, ActivityIndicator } from 'react-native';
import axios from 'axios';

const ListScreen = ({ navigation }) => {
  const [marcações, setMarcações] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://seu-servidor/api/marcações')
      .then((response) => {
        setMarcações(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Erro ao obter as marcações: ' + error);
        setError('Erro ao obter as marcações. Tente novamente.');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <View>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  if (error) {
    return (
      <View>
        <Text>{error}</Text>
      </View>
    );
  }

  return (
    <View>
      <Text>Lista de Marcações:</Text>
      <FlatList
        data={marcações}
        keyExtractor={(item) => item._id}
        renderItem={({ item }) => (
          <View>
            <Text>Nome: {item.nome}</Text>
            <Text>Data: {item.data}</Text>
            <Text>Hora: {item.hora}</Text>
            <Text>Local: {item.local}</Text>
            <Text>Assunto: {item.assunto}</Text>
          </View>
        )}
      />
    </View>
  );
};

export default ListScreen;
