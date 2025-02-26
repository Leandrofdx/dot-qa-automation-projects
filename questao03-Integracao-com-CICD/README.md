# 🚀 CI/CD Pipeline com GitHub Actions  

Este repositório contém uma **pipeline de integração contínua (CI)** configurada com **GitHub Actions** para executar testes automatizados de API (com Pytest) e testes End-to-End (E2E) no frontend (com Cypress).  

## 🔥 Visão Geral da Pipeline  

A pipeline é acionada nos seguintes eventos:  
- **Push na branch `main`**  
- **Abertura de Pull Requests para `main`**  

A pipeline está dividida nos seguintes **jobs**:  

1️⃣ **Testes de API (`test-python`)**: Executa testes automatizados usando Pytest.  
2️⃣ **Testes E2E (`test-cypress`)**: Executa testes de frontend com Cypress.  
3️⃣ **Notificação (`notify-results`)**: Comenta os resultados dos testes diretamente no Pull Request.  

---

## 📌 Fluxo da Pipeline  

### 🧪 Testes de API com Pytest (`test-python`)  
1. Faz o **checkout do código**.  
2. Configura a versão do **Python 3.9**.  
3. Instala as dependências do projeto.  
4. Executa os testes automatizados com **Pytest**, gerando um relatório em HTML.  
5. Faz o **upload do relatório de testes** como artefato do workflow.  

### 🌐 Testes E2E com Cypress (`test-cypress`)  
1. Faz o **checkout do código**.  
2. Configura a versão do **Node.js 18**.  
3. Instala as dependências do Cypress.  
4. Executa os testes E2E com Cypress.  
5. Faz o **upload do relatório de testes** como artefato do workflow.  

### 🔔 Notificação no Pull Request (`notify-results`)  
1. Aguarda a conclusão dos testes de API e Cypress.  
2. Comenta os resultados dos testes diretamente no **Pull Request**, informando se passaram ou falharam.  
3. Adiciona um link para os **relatórios gerados** como artefatos do workflow.  

---

## 📂 Estrutura do Repositório  

```bash
qa-automation-project/
├── .github/workflows/ci-pipeline.yml  # Configuração da pipeline
├── questao02-api-tests-python/        # Testes de API com Python + Pytest
├── questao01-e2e-tests-cypress/       # Testes E2E com Cypress
```

---

## 📊 Relatórios de Teste  

Os relatórios são gerados automaticamente e disponibilizados como artefatos do workflow:  
✅ **Relatório Pytest**: `questao02-api-tests-python/results/python-report.html`  
✅ **Relatório Cypress**: `questao01-e2e-tests-cypress/mochawesome-report/report-final.html`  

Os resultados dos testes são postados diretamente no Pull Request! 🚀  

---

## 📢 Como Executar Localmente  

### Testes de API com Pytest  
```bash
cd questao02-api-tests-python
pip install -r requirements.txt
pytest --html=results/python-report.html --self-contained-html
```

### Testes E2E com Cypress  
```bash
cd questao01-e2e-tests-cypress
npm install
npm run generate-all-reports
```

---

## 📌 Melhorias Futuras  
🔹 Implementar testes paralelos para melhorar o tempo de execução.  
🔹 Adicionar execução em diferentes navegadores no Cypress.  
🔹 Integrar testes de segurança automatizados.  

---

🚀 **Essa pipeline garante entregas mais confiáveis e automação contínua dos testes!**  