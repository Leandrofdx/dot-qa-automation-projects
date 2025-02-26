# Automação de Testes Cypress para Amazon Brasil  

Este projeto contém testes automatizados usando **Cypress** para validar o fluxo de compra de livros na **Amazon Brasil**.  

## 📌 Descrição  

O objetivo deste projeto é garantir que o processo de **busca, seleção e adição de livros ao carrinho** na Amazon Brasil funcione corretamente. Os testes automatizados simulam o comportamento de um usuário real, validando os principais fluxos de compra e garantindo a estabilidade do sistema.  

## 🛠 História do Usuário  

**Título:** Compra de Livro na Amazon Brasil  

> Como um usuário da Amazon Brasil, eu quero buscar um livro específico, adicioná-lo ao carrinho e verificar se ele foi adicionado corretamente, para que eu possa comprá-lo com facilidade e confiança.  

## ✅ Critérios de Aceite  

- O usuário deve conseguir acessar a página inicial da Amazon Brasil.  
- O usuário deve conseguir buscar um livro específico pelo título.  
- O usuário deve conseguir selecionar o livro correto nos resultados da busca.  
- O usuário deve conseguir verificar se o livro selecionado é a edição desejada (idioma, autor).  
- O usuário deve conseguir selecionar a opção de capa comum do livro.  
- O usuário deve conseguir adicionar o livro ao carrinho.  
- O usuário deve conseguir verificar se o livro foi adicionado corretamente ao carrinho, confirmando o título e outros detalhes.  

## 🔍 Casos de Teste  

### **CT001: Busca e Adição de Livro ao Carrinho com Sucesso**  
**Pré-condições:**  
- Usuário está na página inicial da Amazon Brasil.  

**Passos:**  
1. Digitar o título do livro "AI Engineering: Building Applications with Foundation Models" no campo de busca e pressionar Enter.  
2. Clicar no livro correto nos resultados da busca.  
3. Verificar se o livro é a edição em inglês e do autor "Chip Huyen".  
4. Selecionar a opção "Capa Comum".  
5. Clicar no botão "Adicionar ao carrinho".  
6. Verificar se a mensagem "Adicionado ao carrinho" é exibida.  
7. Clicar no ícone do carrinho de compras.  
8. Verificar se o livro "AI Engineering: Building Applications with Foundation Models" está presente no carrinho.  

**Resultado esperado:**  
- O livro é adicionado ao carrinho com sucesso e exibido corretamente.  

---

### **CT002: Livro Não Encontrado na Busca**  
**Pré-condições:**  
- Usuário está na página inicial da Amazon Brasil.  

**Passos:**  
1. Digitar um título de livro inexistente no campo de busca e pressionar Enter.  
2. Verificar se uma mensagem de "Nenhum resultado encontrado" é exibida.  

**Resultado esperado:**  
- Uma mensagem de "Nenhum resultado encontrado" é exibida.  

---

### **CT003: Livro Indisponível (Fora de Estoque)**  
**Pré-condições:**  
- Usuário está na página do livro "AI Engineering: Building Applications with Foundation Models".  

**Passos:**  
1. Verificar se o livro está marcado como "Indisponível" ou "Fora de estoque".  
2. Tentar adicionar o livro ao carrinho.  
3. Verificar se uma mensagem de erro é exibida.  

**Resultado esperado:**  
- Uma mensagem de erro é exibida, informando que o livro está indisponível.  

---

### **CT004: Erro ao Adicionar Livro ao Carrinho**  
**Pré-condições:**  
- Usuário está na página do livro "AI Engineering: Building Applications with Foundation Models".  

**Passos:**  
1. Clicar no botão "Adicionar ao carrinho".  
2. Verificar se uma mensagem de erro genérica é exibida.  

**Resultado esperado:**  
- Uma mensagem de erro genérica é exibida.  

---

### **CT005: Remover Livro do Carrinho**  
**Pré-condições:**  
- O livro "AI Engineering: Building Applications with Foundation Models" está no carrinho.  

**Passos:**  
1. Acessar o carrinho de compras.  
2. Clicar no botão "Excluir" ou similar para remover o livro.  
3. Verificar se o livro foi removido do carrinho.  

**Resultado esperado:**  
- O livro é removido do carrinho com sucesso.  

---

### **CT006: Verificar Preço do Livro no Carrinho**  
**Pré-condições:**  
- O livro "AI Engineering: Building Applications with Foundation Models" está no carrinho.  

**Passos:**  
1. Acessar o carrinho de compras.  
2. Verificar se o preço exibido para o livro corresponde ao preço na página do produto.  

**Resultado esperado:**  
- O preço do livro no carrinho é o mesmo da página do produto.  

---

### **CT007: Navegação para a Página de Checkout**  
**Pré-condições:**  
- O livro "AI Engineering: Building Applications with Foundation Models" está no carrinho.  

**Passos:**  
1. Acessar o carrinho de compras.  
2. Clicar no botão "Finalizar compra" ou similar.  
3. Verificar se a página de checkout é exibida.  

**Resultado esperado:**  
- A página de checkout é exibida.  

---

## 🚀 Tecnologias Utilizadas  

- [Cypress](https://www.cypress.io/) - Framework de automação de testes  
- **JavaScript** - Linguagem utilizada nos testes  
- **JSON** - Utilizado para armazenar dados de teste (fixtures)  

## ⚙️ Pré-requisitos  

Antes de executar os testes, certifique-se de que possui:  

- [Node.js](https://nodejs.org/) instalado  
- [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/) instalado  

## 🛠 Como Configurar e Executar os Testes  

1. **Clone este repositório:**  

   ```bash
   git clone https://github.com/Leandrofdx/dot-qa-automation-projects.git
   ```

2. **Navegue até o diretório do projeto:**  

   ```bash
   cd dot-qa-automation-projects/questao01-e2e-tests-cypress
   ```

3. **Instale as dependências:**  

   ```bash
   npm install
   # ou
   yarn install
   ```

4. **Execute os testes:**  

   - Para abrir o **Cypress Test Runner** e rodar os testes manualmente:  

     ```bash
     npx cypress open
     ```
     No Cypress, selecione **E2E Testing** → **Electron** → **add_book_to_cart.cy.js**  

   - Para executar os testes em **modo headless** e gerar um relatório:  

     ```bash
     npm run generate-all-reports
     ```

     O relatório será gerado em:  

     ```
     mochawesome-report/report-final.html
     ```

## 📂 Estrutura do Projeto  

```bash
questao01-e2e-tests-cypress/
├── cypress/
│   ├── e2e/
│   │   └── add_book_to_cart.cy.js  # Arquivo de teste principal
│   ├── fixtures/
│   │   └── bookData.json           # Dados de teste (título do livro, autor, etc.)
├── cypress.config.js               # Arquivo de configuração do Cypress
├── package.json
├── README.md
```

## 📊 Relatório de Testes  

Os testes geram um **relatório HTML** interativo usando **mochawesome**. Após a execução dos testes em **modo headless**, você pode abrir o relatório em qualquer navegador acessando:  

```bash
mochawesome-report/report-final.html
```

## 📝 Licença  

Este projeto está sob a licença [MIT](LICENSE).  