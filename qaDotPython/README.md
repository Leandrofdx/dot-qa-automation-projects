# API Test Automation with Python

Este projeto tem como objetivo testar a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts) utilizando **Python** e **Requests**. O teste realiza um GET na API e também um POST para criar dados fictícios, verificando se a resposta contém um ID único gerado pela API.

## Estrutura do Projeto

- **test_api.py**: Contém os testes para a API.
- **requirements.txt**: Lista as dependências necessárias para rodar o projeto.

## Pré-requisitos

- **Python 3.7+**
- **pip** (gerenciador de pacotes do Python)
- **Homebrew** (somente para macOS, se necessário)

## Como Configurar o Projeto

Siga os passos abaixo para configurar o ambiente de desenvolvimento e rodar os testes.

### Passo 1: Clone o Repositório

Se ainda não clonou o repositório, faça isso agora:

```bash
git clone https://github.com/Leandrofdx/qaDotPython
cd qaDotPython
```

### Passo 2: Configurar o Ambiente Virtual

Crie o ambiente virtual (Só precisa executar 1x):

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

- **No Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- **No macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### Passo 3: Instalar as Dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Passo 4: Rodar os Testes

Para rodar os testes, basta usar o comando `pytest`:

```bash
pytest test_api.py
```
Com relatório HTML disponivel como report.html

```bash
pytest --html=report.html
```

### Passo 5: Resultado esperado
```bash
test_api.py ..      [100%]
================== 2 passed in 1.49s ====================
```

### Passo 6: Desativar o Ambiente Virtual

Após rodar os testes, você pode desativar o ambiente virtual com o comando:

```bash
deactivate
```

## Licença

Este projeto está sob a licença [MIT](LICENSE).