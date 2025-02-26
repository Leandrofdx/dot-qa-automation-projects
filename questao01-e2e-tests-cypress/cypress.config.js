const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://www.amazon.com.br/',
    chromeWebSecurity: false,
    testIsolation: false,
    reporter: "mochawesome",
    reporterOptions: {
      reportDir: "results",
      overwrite: false,
      html: false,
      json: true
    },
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    defaultCommandTimeout: 5000,
  },
});
