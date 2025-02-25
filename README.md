# 🚀 CI/CD para Automação de Testes - Cypress & Python

Este repositório utiliza **GitHub Actions** para automatizar a execução de testes de API e testes E2E, garantindo que qualquer alteração no código seja validada antes de ser integrada à branch principal.

---

## 📌 **Estrutura do CI/CD**

```
qa-automation-project/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml            # Configuração do pipeline no GitHub Actions
├── qaDotCypress/             # Testes E2E com Cypress
├── qaDotPython/              # Testes de API com Python
```

---

## ⚙️ **Como o CI/CD funciona?**

### 🔁 **Disparando os Testes Automaticamente**
O GitHub Actions executa os testes **automaticamente** quando ocorrem os seguintes eventos:
- **Push** para a branch `main`
- **Pull request** aberto para a branch `main`
- Execução manual via **GitHub Actions → Run Workflow**

---

## 🚀 **Pipeline do GitHub Actions**

O arquivo `.github/workflows/ci.yml` define os estágios do CI/CD, conforme descrito abaixo:

### **🔹 1. Configuração do Ambiente**
Cada job do pipeline roda em um ambiente isolado, garantindo que os testes sejam executados em um ambiente limpo e previsível. O pipeline realiza as seguintes configurações:
- **Checkout do código**: Obtém o código do repositório.
- **Configuração do Python**: Instala a versão `3.9` e instala dependências do projeto.
- **Configuração do Node.js**: Instala a versão `18` e instala dependências do Cypress.

### **🔹 2. Execução dos Testes**
Os testes são divididos em dois jobs:

#### 🧪 **Testes de API (Python - Pytest)**
1. Instala as dependências Python a partir do `requirements.txt`.
2. Executa os testes de API com `pytest`.
3. Gera um relatório HTML dos testes.
4. Faz upload do relatório para os artefatos do workflow.

#### 🌐 **Testes de Frontend (Cypress - E2E)**
1. Instala as dependências do projeto Cypress.
2. Executa os testes End-to-End.
3. Gera um relatório de testes em formato HTML.
4. Faz upload do relatório para os artefatos do workflow.

### **🔹 3. Notificação de Resultados**
Após a execução dos testes, um job adicional **notifica os resultados no pull request** (caso tenha sido disparado por um PR). Esse job:
- Aguarda a conclusão dos testes.
- Comenta no PR informando se os testes passaram ou falharam.
- Adiciona um link para os relatórios gerados.

---

## 📄 **Relatórios e Logs**
Os relatórios dos testes podem ser encontrados nos artefatos do workflow:
- **Testes de API (Python)**: `qaDotPython/results/python-report.html`
- **Testes de Cypress (E2E)**: `qaDotCypress/mochawesome-report/report-final.html`

Se algum teste falhar, os logs e os relatórios podem ser acessados diretamente no GitHub Actions para depuração.

---

## 🔧 **Como Configurar o CI/CD?**
Nenhuma configuração extra é necessária, pois o pipeline já está definido no **GitHub Actions**.  

Se precisar rodar manualmente:
1. Acesse **GitHub → Actions**
2. Selecione o workflow **CI/CD**
3. Clique em **Run Workflow**

---

## 📄 **Licença**
Este projeto está sob a licença [MIT](LICENSE).

