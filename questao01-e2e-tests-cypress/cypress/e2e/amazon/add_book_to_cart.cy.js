/// <reference types="cypress" />

// Descreve o conjunto de testes "Amazon Book Purchase Test"
describe('Amazon Book Purchase Test', () => {

    beforeEach(() => {
        // Visita a página inicial da Amazon Brasil
        cy.visit('/');
    });

    it('Should search for the book and add it to the cart', () => {

        // Carrega os dados do livro do arquivo de fixture 'bookData.json'
        cy.fixture('bookData').then((book) => {

            // Preenche o campo de busca com o título do livro e pressiona Enter
            cy.get('#twotabsearchtextbox').type(`${book.bookTitle}{enter}`);

            // Seleciona o livro e verifica se está visível e atribui um alias 'bookResult'
            cy.get(`[aria-label=\"${book.bookTitle}\"]`).as('bookResult').should('be.visible');

            // Clica no livro selecionado
            cy.get('@bookResult').click();

            // Dentro do elemento com ID 'bylineInfo'
            cy.get('#bylineInfo').within(() => {

                // Verifica se o texto 'Inglês' (definido na fixture) está visível
                cy.contains(book.englishLanguage).should('be.visible');

                // Verifica se o nome do autor (definido na fixture) está visível
                cy.contains(book.author).should('be.visible');
            });

            // Dentro do elemento com ID 'formats'
            cy.get('#formats').within(() => {

                // Verifica se o texto 'Capa Comum' (definido na fixture) está visível e clica nele
                cy.contains(book.commonCover).should('be.visible').click();
            });

            // Clica no botão 'Adicionar ao carrinho'
            cy.get('#add-to-cart-button').click();

            // Verifica se a mensagem 'Adicionado ao carrinho' (definida na fixture) está visível
            cy.contains(book.addedToCart).should('be.visible');

            // Clica no ícone do carrinho de compras
            cy.get('#nav-cart').click();

            //TODO: Adicionar validação de que o livro foi adicionado ao carrinho etc...
        });
    });
});