# 🛠 API Test Automation with Python  

Este projeto tem como objetivo testar a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts) utilizando **Python** e **Requests**. O teste realiza um **GET** na API para recuperar posts e um **POST** para criar novos dados fictícios, verificando se a resposta contém um **ID único gerado pela API**.

---

## 📌 História do Usuário  

### 🎯 Título: Teste de API do JSONPlaceholder  
**Como um testador de software**, eu quero **validar os endpoints GET e POST** da API JSONPlaceholder, para garantir que as respostas estejam no formato esperado e os dados sejam processados corretamente.  

---

## ✅ Critérios de Aceite  

- O usuário deve conseguir acessar o endpoint **GET /posts**.  
- O endpoint **GET /posts** deve retornar uma **lista de posts** com os campos `"userId"`, `"id"`, `"title"` e `"body"`.  
- O usuário deve conseguir realizar um **POST** no endpoint **/posts** com dados válidos.  
- O endpoint **POST /posts** deve retornar um **objeto JSON contendo os dados enviados, incluindo um `"id"`**.  

---

## 🧪 Casos de Teste  

### **CT001: Validação do Endpoint GET /posts**  
✅ **Pré-condições:** Nenhuma.  

🔹 **Passos:**  
1. Enviar uma requisição **GET** para o endpoint `/posts`.  
2. Verificar se o **status da resposta é 200**.  
3. Verificar se o **corpo da resposta é uma lista não vazia**.  
4. Verificar se **cada post possui os campos** `"userId"`, `"id"`, `"title"` e `"body"`.  

🔹 **Resultado esperado:**  
✔️ O endpoint **GET** retorna uma **lista de posts válidos**.  

---

### **CT002: Validação do Endpoint POST /posts**  
✅ **Pré-condições:** Nenhuma.  

🔹 **Passos:**  
1. Enviar uma requisição **POST** para o endpoint `/posts` com um JSON contendo `"userId"`, `"title"` e `"body"`.  
2. Verificar se o **status da resposta é 201**.  
3. Verificar se o **corpo da resposta contém os dados enviados e um campo "id"**.  
4. Validar o **schema do JSON retornado**.  

🔹 **Resultado esperado:**  
✔️ O endpoint **POST** retorna um **objeto JSON contendo os dados enviados e um "id"**.  

---

### **CT003: Erro ao Enviar Requisição POST sem Campos Obrigatórios**  
✅ **Pré-condições:** Nenhuma.  

🔹 **Passos:**  
1. Enviar uma requisição **POST** para o endpoint `/posts` **sem os campos "title" e "body"**.  
2. Verificar se o **status da resposta é 400 ou 422**.  
3. Verificar se é retornada **uma mensagem de erro adequada**.  

🔹 **Resultado esperado:**  
✔️ O endpoint retorna um **erro informando que campos obrigatórios estão ausentes**.  

---

### **CT004: Erro ao Acessar um Post Inexistente**  
✅ **Pré-condições:** Nenhuma.  

🔹 **Passos:**  
1. Enviar uma requisição **GET** para `/posts/99999` (um ID que não existe).  
2. Verificar se o **status da resposta é 404**.  
3. Verificar se a resposta contém **uma mensagem adequada**.  

🔹 **Resultado esperado:**  
✔️ O endpoint retorna um **erro 404 indicando que o post não foi encontrado**.  

---

### **CT005: Validação do Content-Type das Respostas**  
✅ **Pré-condições:** Nenhuma.  

🔹 **Passos:**  
1. Enviar uma requisição **GET** para `/posts`.  
2. Verificar se o cabeçalho **"Content-Type"** da resposta contém **"application/json"**.  

🔹 **Resultado esperado:**  
✔️ O **Content-Type da resposta é "application/json"**.  

---

## 🚀 Tecnologias Utilizadas  

- **Python 3.7+**  
- **Requests** - Biblioteca para requisições HTTP  
- **Pytest** - Framework de testes  
- **JSON Schema** - Validação de estrutura de dados  

---

## ⚙️ Como Configurar e Executar os Testes  

### **1️⃣ Clone o Repositório**  

```bash
git clone https://github.com/Leandrofdx/dot-qa-automation-projects.git
cd dot-qa-automation-projects/questao02-api-tests-python
```

### **2️⃣ Configurar o Ambiente Virtual**  

Crie o ambiente virtual (executar apenas uma vez):  

```bash
python3 -m venv venv
```

Ative o ambiente virtual:  

- **Windows**:  

  ```bash
  .\venv\Scripts\activate
  ```

- **macOS/Linux**:  

  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Instale as Dependências**  

```bash
pip install -r requirements.txt
```

### **4️⃣ Execute os Testes**  

Para rodar os testes, basta usar o comando **pytest**:  

```bash
pytest test_api.py
```

📌 **Gerar um relatório HTML dos testes**:  

```bash
pytest test_api.py --html=report.html
```

🔹 **Saída esperada no terminal:**  

```bash
test_api.py ..      [100%]
================== 2 passed in 1.49s ====================
```

### **5️⃣ Desativar o Ambiente Virtual**  

Após rodar os testes, você pode desativar o ambiente virtual com o comando:  

```bash
deactivate
```

---

## 📂 Estrutura do Projeto  

```bash
questao02-api-tests-python/
├── test_api.py               # Arquivo principal dos testes
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
├── venv/                     # Ambiente virtual (opcional)
```

---

## 📊 Relatório de Testes  

Os testes geram um **relatório HTML** interativo usando **pytest-html**. Após a execução dos testes, você pode abrir o relatório acessando:  

```bash
report.html
```

---

## 📝 Licença  

Este projeto está sob a licença [MIT](LICENSE).  