# Repositório feito para estudos de Banco de Dados e HTML/CSS

**Instituto Federal do Piauí - Campus Pedro II**

**Curso:** Análise e Desenvolvimento de Sistemas  
**Módulo:** III
**Disciplina:** Engenharia de Software II 
**Professor:** Willyams Moreira Saraiva


## Membros

| Matrícula       | Aluno             | 
|-----------------|-------------------|
| 2023123TADS00   | Paulo Braga       |
| 2023123TADS00   | Raimundo          | 
| 2023123TADS00   | Robson            | 
| 2023123TADS0003 | Valdemiro Gabriel | 
| 2023123TADS00   | Valfredo Costa    |
| 2023123TADS0037 | Yara Beatriz      | 

## Visão Geral do Projeto
  Este projeto configura uma aplicação web usando Flask para gerenciar clientes, produtos e vendas em um sistema de banco de dados (SQLite). Onde é fornecido funcionalidades para visualizar, adicionar, editar e excluir registros. Aplicação a qual possui rotas para exibir dados na página inicial, processar formulários de cadastro e edição, e remover registros com base em IDs específicos. Cada operação CRUD (Criar, Ler, Atualizar, Deletar) é implementada através de rotas dedicadas, e a aplicação é executada em modo de depuração com uma chave secreta para segurança.
  
**Principais Funcionalidades e Rotas**

**Importações e Configuração Inicial:**
   - Importa módulos necessários, incluindo Flask e SQLite.
   - Importa funções de módulos personalizados para CRUD (Criar, Ler, Atualizar e Deletar) operações.

**Rotas e Funções:**

   - **Página Inicial (`/`):**
     - Rota que exibe uma página inicial (`home.html`) com listas de clientes, produtos e vendas obtidas das funções `mostrarTabelaCliente()`, `mostrarTabelaProduto()` e `mostrarTabelaVenda()`.

   - **Cadastro de Clientes (`/addCliente`):**
     - Rota que recebe dados de um formulário para criar um novo cliente.
     - Os dados são inseridos no banco de dados através da função `inserirClientes()`.

   - **Cadastro de Produtos (`/addProduto`):**
     - Rota que recebe dados de um formulário para criar um novo produto.
     - Os dados são inseridos no banco de dados através da função `inserirProdutos()`.

   - **Cadastro de Vendas (`/addVenda`):**
     - Rota que recebe dados de um formulário para registrar uma nova venda.
     - Os dados são inseridos no banco de dados através da função `inserirVendas()`.

   - **Exclusão de Clientes (`/delCliente/<int:id>`):**
     - Rota que exclui um cliente com base no ID fornecido na URL.
     - Utiliza a função `delRegistroCliente()` para realizar a exclusão.

   - **Exclusão de Produtos (`/delProduto/<int:id>`):**
     - Rota que exclui um produto com base no ID fornecido na URL.
     - Utiliza a função `delRegistroProduto()` para realizar a exclusão.

   - **Exclusão de Vendas (`/delVenda/<int:id>`):**
     - Rota que exclui uma venda com base no ID fornecido na URL.
     - Utiliza a função `delRegistroVenda()` para realizar a exclusão.

   - **Edição de Clientes (`/editarCliente/<int:id>`):**
     - Rota que permite editar as informações de um cliente.
     - Mostra um formulário com os dados atuais do cliente (para métodos GET) e atualiza os dados no banco de dados (para métodos POST) através da função `updateCliente()`.

   - **Edição de Produtos (`/editarProduto/<int:id>`):**
     - Rota que permite editar as informações de um produto. Mostra um formulário com os dados atuais do produto (para métodos GET) e atualiza os dados no banco de dados (para métodos POST) através da função `updateProduto()`.

   - **Edição de Vendas (`/editarVenda/<int:id>`):**
     - Rota que permite editar as informações de uma venda.
     - Mostra um formulário com os dados atuais da venda (para métodos GET) e atualiza os dados no banco de dados (para métodos POST) através da função `updateVenda()`.
     - Inclui uma verificação para garantir que os IDs de cliente e produto estejam presentes antes de atualizar.
    

***Após a realização de cada rota em especifico o usuário é redirecionado a página inicial.***


**Configuração e Execução:**
   - Define uma chave secreta (`app.secret_key`) para proteger sessões e executa o aplicativo Flask em modo de depuração.

## Objetivos do Projeto
- Criar uma aplicação web para gerenciar clientes, produtos e vendas em um sistema de banco de dados; e mostrar na tela para o usuário todas as informações necessárias.

## Principais Tecnologias Utilizadas
- Pyhton(Flask)
- SQLite
- HTML
- MKDOCS
- Git, GitHub
