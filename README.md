# plpred

By Frederico Schmitt Kremer

a protein subcellular location prediction program

## Setup

```
$ make setup
```

## Project Structure

- `environment.yml`: configurações do ambiente do conda
- `requirements.txt`: bibliotecas a serem instaladas no Python
- `Makefile`: centralizar comandos, criar umas regrinhas (rules)
- `data/`: diretório de dados. Dados brutos guardados na pasta `data/raw/`, os dados processados na pasta `data/processed`e os modelos treinados na pasta `data/models`.
- `plpred`: arquivo onde está o código, correspondente ao arquivo `preprocessing.py`
- `plpred/models`:disponibiliza modelos preditivos baseados em *Random Forest*, *Gradient Boosting*, SVM e redes neurais (MLP).
