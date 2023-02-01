# Entrega 4
## Arquitetura exemplo da ingestão anterior (ecossistema GCP)
Para responder esta aproveitei de uma Arquitetura Referência de um Data Pipeline de Analytics sugerido pelo time do Google Cloud em [Architecture Diagramming tool](https://googlecloudcheatsheet.withgoogle.com/architecture). 

![full_data_analytics_pipeline](/entrega4/full_data_analytics_pipeline.svg)

Selecionei as ferramentas que julguei necessárias, com base nas informações que foram fornecidas, para conceber uma ideia inicial.

![mothership_prop4](/entrega4/mothership_prop4.svg)

Essa arquitetura foi concebida visando o menor custo e a simplicidade. 
Em princípio, na camada de ingestão, meu plano é fazer com que as requisições da API sejam salvas em json numa _staging area_ num bucket de Cloud Storage (no caso do processamento batch) ou enviar tudo para um tópico de Notas Fiscais Eletronicas no Pub/Sub (no caso de streaming).
<p>Já no processamento, se os pipelines de dados forem construídos utilizando ferramentas como Hadoop ou Spark, é muito provável que precisaremos utilizar o Dataproc. Não sendo este o caso, podemos seguir com o Dataflow. Vale ressaltar, que se há previsão de que a complexidade dos pipelines(transformações, regras de negócio, orquestração, etc) aumente, talvez seja o caso de considerar a utilização do Cloud Composer (que basicamente é um Apache Airflow gerenciado pelo GCP). Ainda sobre as regras de negócio, a depender de complexidade, custos, sugiro a previsão de uso de Cloud Functions (onde se poderia rodar a entrega 3) ou Cloud Run (que poderia rodar os containers previstos nas entregas 1 e 2).
Por fim, a camada de armazenamento utilizando um Data Warehouse com Bigquery para futuras análise e/ou o BigTable.
Falando um pouco mais sobre o BigTable, penso neste NoSQL-database recebendo os JSONs de transações ![diretamente do BigQuery](https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/bigquery-to-bigtable/src/main/java/com/google/cloud/teleport/v2/templates/BigQueryToBigtable.java) ou ![vindo do Dataflow](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/main/java/dataflow-connector-examples). Estes JSONs de transações seriam armazenados numa coleção de NFes contendo a seguinte rowkey: <code>ProductName#NFeID#NFeNumber#CreateDateTimestamp#EmissionDateTimestamp</code>. Além disso, esta coleção teria uma família de colunas "Item", que teria duas filhas "Item.Value" e "Item.Quatity".

### E se eu tivesse mais tempo?
* Construiria um sandbox na camada gratuita para testar tudo isso que pensei. :P
* Estudaria a viabilidade de utilização de outras ferramentas especializadas como Dataprep e Workflows.
* Levantaria questões a cerca da proteção e manipulação de dados eventualmente sensíveis (o número de uma nota fiscal, pode estar relacionado ao CPF de um cliente).
* Estimaria custos e compararia valores de diferentes arquiteturas.
