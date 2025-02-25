# Automação de Testes Cypress para Amazon Brasil  

Este projeto contém testes automatizados usando **Cypress** para validar o fluxo de compra de livros na **Amazon Brasil**.  

## 📌 Descrição  

O objetivo deste projeto é garantir que o processo de **busca, seleção e adição de livros ao carrinho** na Amazon Brasil funcione corretamente. Os testes automatizados simulam o comportamento de um usuário real, validando os principais fluxos de compra e garantindo a estabilidade do sistema.  

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
   git clone https://github.com/Leandrofdx/qaDotCypress
   ```

2. **Navegue até o diretório do projeto:**  

   ```bash
   cd qaDotCypress
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
amazon-cypress-tests/
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

---