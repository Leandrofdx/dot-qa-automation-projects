import requests  # Biblioteca para fazer requisições HTTP
import random  # Biblioteca para gerar números aleatórios
import pytest  # Framework de testes para Python
from jsonschema import validate, ValidationError  # Biblioteca para validação de schema JSON

# URL base da API
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Schema JSON para validar a resposta do endpoint POST
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

def test_get_posts():
    """
    Testa o endpoint GET /posts.
    """
    try:
        # Faz a requisição GET para a API
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Verifica erros HTTP (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Erro na requisição GET /posts: {e}")

    # Verifica se o tipo de conteúdo da resposta é JSON
    assert "application/json" in response.headers.get("Content-Type", ""), "GET /posts falhou: tipo de conteúdo incorreto"

    # Converte a resposta JSON em um objeto Python
    data = response.json()

    # Verifica se a resposta é uma lista não vazia
    assert isinstance(data, list) and len(data) > 0, "GET /posts falhou: resposta não é uma lista não vazia"

    # Verifica se cada item tem as chaves esperadas
    for post in data:
        assert all(key in post for key in ["userId", "id", "title", "body"]), "GET /posts falhou: resposta com estrutura incorreta"

def test_post_posts():
    """
    Testa o endpoint POST /posts.
    """
    # Gera dados aleatórios para o novo post
    user_id = random.randint(1, 10)
    title = " ".join(random.sample("abcdefghijklmnopqrstuvwxyz", 10))  # Garante espaços
    body = " ".join(random.sample("abcdefghijklmnopqrstuvwxyz., ", 20))  # Garante variação

    # Cria o payload (dados) para a requisição POST
    payload = {"userId": user_id, "title": title, "body": body}
    
    try:
        # Faz a requisição POST para a API
        response = requests.post(BASE_URL, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Erro na requisição POST /posts: {e}")

    # Verifica se o tipo de conteúdo da resposta é JSON
    assert "application/json" in response.headers.get("Content-Type", ""), "POST /posts falhou: tipo de conteúdo incorreto"

    # Converte a resposta JSON em um objeto Python
    data = response.json()

    try:
        # Valida o schema da resposta usando o POST_SCHEMA
        validate(instance=data, schema=POST_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"POST /posts falhou: schema da resposta inválido: {e}")

    # Verifica se os dados enviados são os mesmos recebidos na resposta (exceto o id)
    assert data["userId"] == user_id, "POST /posts falhou: userId incorreto"
    assert data["title"] == title, "POST /posts falhou: title incorreto"
    assert data["body"] == body, "POST /posts falhou: body incorreto"

    # Valida que o ID foi retornado, mas sem esperar um número específico (pois é fixo 101)
    assert isinstance(data["id"], int), "POST /posts falhou: ID não retornado corretamente"