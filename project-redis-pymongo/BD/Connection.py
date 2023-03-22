import pymongo as pm

class Connection:

    def connection():
        mongoClient = pm.MongoClient("mongodb+srv://mongodb:<password>@cluster0.biiuuzo.mongodb.net/?retryWrites=true&w=majority")
        bd = mongoClient.vestibular
        coluna = bd.aprovados
        coluna.drop
    
