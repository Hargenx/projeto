from dataclasses import dataclass

@dataclass
class Jogo:
    id: int
    nome: str
    genero: str
    plataforma: str
    lancamento: int
