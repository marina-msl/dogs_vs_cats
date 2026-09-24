# dogs_vs_cats

Projeto de estudo de Machine Learning para classificar imagens de gatos e cachorros com TensorFlow/Keras.

## Arquivos

- `load_images3.ipynb`: notebook com os primeiros passos de carregamento dos dados.
- `load_images.py`: script de carregamento dos dados.

## Como executar

Instale as dependências no ambiente Python:

```sh
python -m pip install -r requirements.txt
```

Organize suas imagens localmente:

```text
dataset/
├── cats/
└── dogs/
```

Abra `load_images3.ipynb` em um ambiente com suporte a notebooks, selecione o ambiente Python e execute as células a partir da pasta do projeto. Alternativamente, execute `python load_images.py`.

O carregamento usa imagens de 128 × 128 pixels, lotes de 32 e uma divisão de 80% para treino e 20% para validação. As imagens são lidas em lotes para evitar carregar o dataset inteiro na memória.

O dataset, arquivos inválidos e ambientes virtuais não são incluídos no repositório. Esta versão salva contém a preparação dos datasets; o treinamento ainda não está registrado no notebook.
