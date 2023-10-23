import { connect, connection } from 'mongoose';

connect('mongodb://localhost:27017/marcaçõesDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = connection;

db.on('error', console.error.bind(console, 'Erro na conexão com o MongoDB:'));
db.once('open', () => {
  console.log('Conectado ao banco de dados MongoDB');
});
