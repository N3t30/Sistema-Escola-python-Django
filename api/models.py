from django.db import models

# CRIANDO CLASSES


class Base(models.Model):
    # variavel criacao pegar do models data e hora
    criacao = models.DateTimeField(auto_now_add=True)
    # Atualizacao criacao pegar do models data e hora
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    # OBRIGAÇÃO TER UMA URL UNICA
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    # FUNÇÃO DE CONSTRUTOR
    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(
        Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    NOME = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank == True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        oberbose_name = 'Avaliação'
        oberbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']

        def __str__(self):
            return f'{self.nome} avaliou o vurso {self.curso} com nota {self.avaliacao}'
