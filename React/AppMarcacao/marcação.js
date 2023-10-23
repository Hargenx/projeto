import { Schema, model } from 'mongoose';

const marcaçãoSchema = new Schema({
  nome: String,
  data: Date,
  hora: String,
  local: String,
  assunto: String,
});

const Marcação = model('Marcação', marcaçãoSchema);

export default Marcação;
