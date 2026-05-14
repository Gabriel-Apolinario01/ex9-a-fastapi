from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API esta funcionando"}

@app.get("/usuarios")
def listar_usuarios():
    return {
        "usuarios": [
            "Gabriel",
            "Maria",
            "João"
        ]
    }

@app.get("/usuario/{id}")
def buscar_usuario(id: int):
    return {
        "id": id,
        "nome": "Usuário Teste"
    }

@app.post("/produto")
def criar_produto(nome: str, preco: float):
    return {
        "mensagem": "Produto criado",
        "nome": nome,
        "preco": preco
    }