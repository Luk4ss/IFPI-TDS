from typing import Union
from datetime import *

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# region Models


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class AcaoDTO(BaseModel):
    codigo: str
    valorUnitario: float
    quantidade: int
    taxaCorretagem: int
    operacao: str
    data: datetime
    taxaB3: float
    valorTotal: float


# endregion

# region Entidades
class Acao:
    def __init__(self, codigo, valorUnitario, quantidade, taxaCorretagem, taxaB3, operacao, data, valorTotal=0.0):
        self.codigo = codigo
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade
        self.taxaCorretagem = taxaCorretagem
        self.taxaB3 = taxaB3
        self.operacao = operacao
        self.data = data
        self.valorTotal = valorTotal


# endregion

acao1 = Acao("B3SA3", 12, 100, 2.50, 0.36, "COMPRA", datetime.today(), 1202.86)
acao2 = Acao("ITSA4", 9.50, 100, 2.50, 0.29, "COMPRA", datetime.today(), 952.78)
acao3 = Acao("B3SA3", 20, 100, 2.50, 0.60, "VENDA", datetime.today(), 1996.90)
acao4 = Acao("ITSA4", 15, 100, 2.50, 0.45, "VENDA", datetime.today(), 1497.05)

mock_data = [acao1, acao2, acao3, acao4]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", status_code=200)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/acoes")
def list_acoes():
    return mock_data


@app.post("/acoes", status_code=201)
def insert_acoes(acao: AcaoDTO):
    mock_data.append(acao)
    return acao
