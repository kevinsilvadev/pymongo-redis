-> Objetivo do projeto:

	-> Alimentar um cache no Redis a partir de uma lista de aprovados em um vestibular armazenada no MongoDB Atlas;
	-> Apresentar o processo de sincronização do cache com o banco de dados MongoDB para atualizações em tempo real.

-> Passo 1: Montando o ambiente de desenvolvimento

	-> Criação de um projeto Python com pastas separadas para cada arquivo;
	-> Pasta BD contendo o arquivo "Connection";
	-> Pasta model contendo a classe Person para determinar cada estudante aprovado;
	-> Arquivo Program contendo a classe Program e o método main para executar o script.

-> Passo 2: Desenvolvimento

	-> Importação das seguintes classes e bibliotecas no arquivo Program:
		-> Bibliotecas: Faker, Random e Pymongo;
		-> Classes: Connection e Person;
		
	-> Uso da biblioteca Faker para gerar pessoas aleatórias;
	-> Uso da biblioteca Random para gerar várias pessoas aleatoriamente;
	-> Uso da biblioteca Pymongo para fazer a conexão com o MongoDB;
	-> Criação da função connection na classe Connection para realizar a conexão com o MongoDB, criar a collection e a coluna de aprovados e integrar com o Redis para monitorar cada operação;
	-> Criação da classe Person com os atributos de um estudante: nome, CPF, curso e aprovado;
	-> Criação de uma função para gerar várias pessoas aleatórias e adicionar na lista de aprovados no método main da classe Program;
	-> Criação de um loop na classe Connection para sincronizar os dados com o Redis e monitoramento das mudanças no MongoDB.

-> Apresentação dos resultados:

	-> O programa foi capaz de criar 5000 alunos fictícios e sincronizá-los em tempo real com o Redis;
	-> Inserções e atualizações no MongoDB foram refletidas no Redis;
	-> Remoções de documentos no MongoDB foram excluídas do Redis.




