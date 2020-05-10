# Bureau Credit

## Problema

Armazenar, processar e disponibilizar grande volume de dados relacionados a crédito de pessoas (dados de dívida, fonte de rendas e movimentação). A aplicação deve ser escalável, segura, e a arquitetura usada deve ser em microsserviço.

## Arquitetura Proposta

<p align="center">
  <img src="https://github.com/kallebefelipe/bureau-credit/blob/master/images/arquitetura.png">
</p>

## 1. Armazenamento

## Base A

Para o armazenamento foram usados três bases de dados, a primeira Base A, é extremamente sensível e deve ser protegida com os maiores níveis de seguranças, mas o acesso a esses dados não precisa ser tão performático. O [PostgreSQL](https://www.postgresql.org/) foi escolhido, **pois possui funções e funções herdadas para definir e manter permissões**. O PostgreSQL possui suporte **SSL nativo** para conexões, para criptografar as comunicações cliente/servidor. Ele também tem seguração em nível de linha. Além disso, o PostgreSQL vem com um aprimoramento embutido chamado **SE-PostgreSQL** que fornece controles de acesso adicionais baseados na política de segurança do SELinux.

## Base B

A segunda, é a Base B que também possui dados críticos, mas ao contrário da Base A, o acesso precisa ser um pouco mais rápido. O PostgreSQL também é adequado nesse cenário, pois ele suporta uma variedade de otimizações de desempenho:

**shared_buffer**: esse parâmetro define quanto de memória dedicada será usada pelo PostgreSQL para cache.  
**effective_chace_size**: fornece uma estimativa da memória disponível para armazenamento em cache do disco.  
**maintenance_work_mem**: é uma configuração de memória usada para tarefas de manutenção.  
**checkpoint_timeout**: o parâmetro é usado para definir o tempo entre os pontos de verificação WAL.

## Base C

A última base, é a Base C, que não possui nenhum tipo de dado crítico, mas precisa de um acesso extremamente rápido. O banco não relacional **MongoDB** foi escolhido, devido ao seu **modelo de dados flexível** no formato de json, possui **alta escalabilidade** e **alta performance**. O MongoDB reduz a complexidade, número de consultas, melhorando o desempenho, e simplificando o crescimento a medida que os dados aumenta.

## 2. Tráfico

<p align="center">
  <img src="https://github.com/kallebefelipe/bureau-credit/blob/master/images/trafico.png">
</p>

## JSON

Json é uma formatação leve de troca de dados. Para seres humanos, é fácil de ler e escrever. Para máquinas é fácil de interpretar e gerir. **JSON** é em **formato texto** e completamente independente de linguagem. JSON está constituído em duas estruturas: uma coleção de pares **nomes/valor**; uma **lista** ordenada de valor. Exemplo:

```
{
  "chave": "valor"
}
```

## HTTP

**Hypertext Transfer Protocol (HTTP)** é um **protocolo** de camada de aplicação para **transmissão** de documentos hipermídia, como o HTML. Foi desenvolvido para comunicação entre navegadores web e servidores web, porém pode ser utilizado para outros propósitos também. Segue um modelo **cliente-servidor** clássico, onde um cliente abre uma conexão, executa uma **requisição** e espera até receber uma resposta. É também um protocolo sem estado ou **stateless** protocol, que significa que o servidor **não mantém nenhum dado entre duas requisições** (state).

## RESTful Web Service

A arquitetura **REST** foi originalmente projetada para se ajustar ao **protocolo HTTP** usado pelo Wold Wide Web. Os clientes **enviam solicitações** para as URIs usando os métodos definidos pelo protocolo HTTP:

**GET**: obter informação.
**POST**: criar novo recurso.
**PUT**: atualizar um recurso
**DELETE**: deletar um recurso.

Em geral, os dados fornecidos no corpo da solicitação são **JSON**.

## Microsserviço

Uma arquitetura monolítica é funcional, mas a medida que a aplicação vai crescendo, a aplicação passa a ser custosa demais, deploys demorados e um erro no sistema pode fazer com que toda aplicação pare de funcionar. Voltada a solucionar esse problema, existe a alternativa de desenvolvimento em **microsserviços** (microservices). Com esse estilo de arquitetura, os aplicativos são “quebrados” em diversos serviços que **executam seus próprios processos **e se c**omunicam por mecanismos leves.**

Os serviços possuem **deploys independentes**, **totalmente automatizados**, a aplicação pode ser escrita em diversas linguagens de programação e diferentes tecnologias de armazenamento.  Foi para implementação dos microsserviços o microframework [Flask](https://flask.palletsprojects.com/en/1.1.x/) que usa a linguagem Python, ele tem uma estrutura com **núcleo simples**, **extensível**, de **fácil e rápida implementação**, ideal para microsserviço.

## ORM 

O ORM utilizado junto ao Flask para integrar com o banco de dados PostgreSQL foi o **SQLAlchemy**, que é criado com Python, e fornece **flexibilidade** total do SQL,  e fornece todas as **garantias de segurança** necessárias para proteger as aplicações de ataques ao seus bancos de dados, garantindo a criação de aplicativos simples e seguros.

## Api gateway

Para centralizar as requisições de API, foi usado o [Nginx API Gateway](https://www.nginx.com/products/nginx/). Um **API Gateway** traz inúmeros benefícios para aplicação, tais como: **escalabilidade**, t**olerância a falhas**, **roteamento de rotas**, **limite de consulta aos seviços**, **logs centralizado**. Além disso não usar um API Gate​way na arquitetura de microsserviços deixa o processo de DevOps e gestão de informação bastante difíceis de serem geridos, a medida que a quantidade de microsserviço aumenta.

## Autenticação

Foi criado um servidor [Django](https://www.djangoproject.com/) para centralizar a autenticação dos usuários, nesse servidor está um banco de dados com todos os usuários do sistema, foi utilizado a autenticação do [Django Rest Framework](https://www.django-rest-framework.org/), com o tipo de autenticação **JWT** (Json Web Token). JWT é uma string de caracteres codificados que, caso  cliente e servidor estejam sob HTTPS, permite que somente o servidor que conhece o “segredo” possa ler o conteúdo do token e assim confirmar a autenticidade do cliente.

## Microsserviço 1

O primeiro serviço acessa dados da **Base A**, que contém **informações pessoais** de um determinado CPF.

endpoint: ```/pessoa/{CPF}```

```
payload = {
  "cpf": <number>,
  "nome": <string>,
  "endereco": {
    "rua": <string>,
    "numero": <number>,
    "bairro": <string>,
    "cidade": <string>,
    "estado": <string>,
    "pais": <string>
    }
  },
  "lista_dividas": [{
    "tipo": <choice> (cartao, financiamento, consignado,  cheque_especial),
    "valor": <number>,
  }]
}
```

## Microsserviço 2

O segundo serviço, acessa a **Base B** que contém dados para cálculo do **Score de Crédito**. O Score de Crédito é um **rating** utilizado por instituições de crédito (bancos, imobiliárias, etc) quando precisam analisar o **risco** envolvido em uma operação de crédito a uma entidade.

endpoint: ```/score/{CPF}```

```
payload = {
  "cpf": <number>,
  "idade": <number>,
  "lista_bens": [{
    "tipo": <choice> (carro, casa, terreno, poupança),
    "valor": <number>,
  }]
  "endereco": {
    "rua": <string>,
    "numero": <number>,
    "bairro": <string>,
    "cidade": <string>,
    "estado": <string>,
    "pais": <string>
    }
  },
  "fonte_renda": [{
    "tipo": <choice> (salario, aluguel, dividendos, proventos, royalties, patente),
    "valor": <number>,
  }]
}
```

## Microsserviço 3

O útimo serviço, acessa a **Base C** e tem como principal funcionalidade, **rastrear eventos** relacionados a um determinado CPF:

endpoint: ```/evento/{CPF}```

```
payload = {
  "cpf": <number>,
  "ultima_consulta": <datetime>,
  "compras_cartao": [{
    "data": <datetime>,
    "valor": <number>
  }],
  "movimentacoes": [
    "tipo": <choice> (pagamento, transferencia, saque),
    "valor": <number>
  ]
}
```

## Conteiners

O [Docker](https://www.docker.com/) fornece uma camada de abstração e automação para virtualização de sistema operacional usando isolamento de recurso do núcleo do linux, onde cada contêiner é independente para executar uma única instância do sistema operacional. Cada microsserviço foi implantado a partir de contêineres docker, com um contêiner com o banco de dados e outro com o serviço. Dessa forma é possível deploys independentes.


## 3. Disponibilização de Dados

<p align="center">
  <img src="https://github.com/kallebefelipe/bureau-credit/blob/master/images/disponibilizacao.png">
</p>

Os dados podem ser consumidos por meio de integração feita a partir de software de terceiros, utilizando a API disponível, também foi desenvolvido uma aplicação frontend usando dos frameworks [React](https://pt-br.reactjs.org/) e [Redux](https://redux.js.org/introduction/getting-started) da linguagem JavaScript, permitindo usuário consultar as informações disponíveis na API a partir de um CPF, a escolha do React foi devido a ser um framework atual, simples e extensível.


## Possíveis Interessados

* Pessoas Físicas  
* Bancos  
* Imobiliárias  
* Operadoras de cartão de crédito  
* Empresas de crédito  

## Tecnologias usadas

[Python](https://www.python.org/)  
[Flask](https://flask.palletsprojects.com/en/1.1.x/)  
[Django](https://www.djangoproject.com/)  
[Django Rest Framework](https://www.django-rest-framework.org/)  
[Rest Framework Jwt](https://github.com/jpadilla/django-rest-framework-jwt)  
[PostgreSQL](https://www.postgresql.org/)  
[MongoDB](https://www.mongodb.com/)  
[Nginx API Gateway](https://www.nginx.com/products/nginx/)  
[React](https://pt-br.reactjs.org/)  
[Redux](https://redux.js.org/introduction/getting-started)  
[Node](https://nodejs.org/en/)  
[Docker](https://www.docker.com/)  

## Referências

1- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)  
2- [Hypertext Transfer Procol (HTTP)](https://developer.mozilla.org/pt-BR/docs/Web/HTTP)  
3- [Introdução ao JSON](https://www.json.org/json-pt.html)  
4- [Experian Health Bringing Patient Identification into Modern Era with MongoDB](https://www.mongodb.com/press/experian-health-bringing-patient-identification-into-modern-era-with-mongodb)  
5- [MongoDB vs. MySQL](https://www.mongodb.com/compare/mongodb-mysql)  
6- [Tuning PostgreSQL Database Parameters to Optimize Performance](https://www.percona.com/blog/2018/08/31/tuning-postgresql-database-parameters-to-optimize-performance/)  
7- [How to Secure Your PostgreSQL Database](https://severalnines.com/database-blog/how-secure-your-postgresql-database-10-tips)
