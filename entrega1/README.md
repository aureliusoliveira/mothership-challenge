# Entrega 1
## Consulta que retorne o ganho total da empresa por cliente
Resultado obtido executando o script __entrega1.sql__. A consulta foi construída utilizando-se CTEs por questões de legibilidade de código e estruturação. Não foi possível aferir perfomance devido ao pequeno conjunto de dados na tabela. Há um bloco comentado com uma ideia inical para a query. Talvez seja o caso de comparar as perfomances das duas propostas em conjuntos de dados maiores. Tendo a acreditar que a perfomance da proposta final com CTEs seja a mais eficiente, uma vez que os JOINs desta parecem menos 'custosos', visto que estariam juntando conjuntos menores a cada interação ao invés de varrer tabelas inteiras. Seria necessário entender melhor o plano de execução da query, caso a perfomance fosse um ponto de preocupação, o que não foi solicitado.
Minha principal dificuldade nesta atividade foi o de viabilizar um banco SQL SERVER como ambiente teste. Fui muito feliz em conseguir construí-lo utilizando um container Docker e a imagem [mcr.microsoft.com/mssql/server:2019-latest](https://hub.docker.com/_/microsoft-mssql-server "Docker Hub: Microsoft SQL Server").

### E se eu tivesse mais tempo?
* Eu criaria uma view utilizando a query proposta. Isso seria facilmente obtido usando o comando CREATE VIEW AS (query).
* Construiria um Dockerfile automatizando a construção do ambiente teste.
* Se eu tivesse ainda mais tempo... inventaria algo com Kubernetes. :P
