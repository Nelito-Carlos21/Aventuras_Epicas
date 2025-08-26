# Jogo de Aventura - Heróis

## Descrição
Este projeto contém uma classe `Heroi` que representa um herói de uma aventura. 
Cada herói possui as seguintes propriedades:
- `nome`: Nome do herói
- `idade`: Idade do herói
- `tipo`: Tipo do herói (mago, guerreiro, monge, ninja)

O método `atacar()` exibe uma mensagem personalizada de ataque de acordo com o tipo do herói:

| Tipo      | Ataque                  |
|-----------|------------------------|
| mago      | magia                  |
| guerreiro | espada                 |
| monge     | artes marciais         |
| ninja     | shuriken               |

## Como usar
1. Abra o arquivo `jogo.py`.
2. Crie instâncias da classe `Heroi` passando `nome`, `idade` e `tipo`.
3. Use o método `atacar()` para exibir a ação do herói.

Exemplo:
```python
heroi = Heroi("Gandalf", 100, "mago")
heroi.atacar()  # Saída: o mago atacou usando magia
```

## Observações
Caso seja passado um tipo de herói que não está na tabela, o ataque exibirá "golpe desconhecido".
