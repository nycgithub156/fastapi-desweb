# Importa todos os modelos para que fiquem visíveis no pacote models 
from app.models.curso import Curso
from app.models.disciplina import Disciplina

# Explicita o que o pacote exporta
__all__ = ["Curso", "Disciplina"]