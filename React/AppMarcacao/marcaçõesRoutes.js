import { Router } from 'express';
const router = Router();
import Marcação, { find, findById, findByIdAndUpdate, findByIdAndRemove } from './marcação'; // Importe o modelo de marcação definido

// Rota para listar todas as marcações
router.get('/', async (req, res) => {
  try {
    const marcações = await find();
    res.json(marcações);
  } catch (error) {
    console.error('Erro ao obter as marcações: ' + error);
    res.status(500).json({ error: 'Erro ao obter as marcações.' });
  }
});

// Rota para criar uma nova marcação
router.post('/', async (req, res) => {
  const novaMarcação = new Marcação(req.body);

  try {
    const marcaçãoSalva = await novaMarcação.save();
    res.status(201).json(marcaçãoSalva);
  } catch (error) {
    console.error('Erro ao adicionar marcação: ' + error);
    res.status(500).json({ error: 'Erro ao adicionar a marcação.' });
  }
});

// Rota para obter uma marcação por ID
router.get('/:id', async (req, res) => {
  const id = req.params.id;

  try {
    const marcação = await findById(id);
    if (!marcação) {
      res.status(404).json({ error: 'Marcação não encontrada.' });
    } else {
      res.json(marcação);
    }
  } catch (error) {
    console.error('Erro ao obter a marcação: ' + error);
    res.status(500).json({ error: 'Erro ao obter a marcação.' });
  }
});

// Rota para atualizar uma marcação por ID
router.put('/:id', async (req, res) => {
  const id = req.params.id;

  try {
    const marcaçãoAtualizada = await findByIdAndUpdate(id, req.body, { new: true });
    if (!marcaçãoAtualizada) {
      res.status(404).json({ error: 'Marcação não encontrada.' });
    } else {
      res.json(marcaçãoAtualizada);
    }
  } catch (error) {
    console.error('Erro ao atualizar a marcação: ' + error);
    res.status(500).json({ error: 'Erro ao atualizar a marcação.' });
  }
});

// Rota para excluir uma marcação por ID
router.delete('/:id', async (req, res) => {
  const id = req.params.id;

  try {
    const marcaçãoExcluída = await findByIdAndRemove(id);
    if (!marcaçãoExcluída) {
      res.status(404).json({ error: 'Marcação não encontrada.' });
    } else {
      res.json(marcaçãoExcluída);
    }
  } catch (error) {
    console.error('Erro ao excluir a marcação: ' + error);
    res.status(500).json({ error: 'Erro ao excluir a marcação.' });
  }
});

export default router;
