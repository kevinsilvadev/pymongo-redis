import pymongo as pm
import redis as rd
import json as j

class Connection:

    @staticmethod
    def connectionMongoDb():
        # ----------------- Connection MongoDB ------------------------#
        mongoClient = pm.MongoClient(
            "mongodb+srv://mongodb:<password>@cluster0.biiuuzo.mongodb.net/?retryWrites=true&w=majority")
        bd = mongoClient.vestibular
        coluna = bd.aprovados
       # coluna.drop()
        
        # ------------------- Connection Redis --------------------------#
        redis_client = rd.Redis(host="localhost", port=6379)
        
        # Sincronização inicial de dados
        for doc in coluna.find():
            key = str(doc["_id"])
            redis_client.set(key, j.dumps(doc, default=str))

            # Monitoramento de mudanças no MongoDB
        with coluna.watch(full_document="updateLookup") as change_stream:
            print("Entrou aqui")
            for change in change_stream:
                print("Entrou no for")
                print(change_stream)
                operation_type = change["operationType"]
                print(
                    f"\n\n{'=-'*75}\nOperation type executed: {operation_type}")

                if operation_type in ["insert", "update"]:
                    full_document = change["fullDocument"]
                    print(f"Full Document: {full_document}")

                    document_json = j.dumps(full_document, default=str)
                    key = str(full_document["_id"])
                    redis_client.set(key, document_json)
                    doc = redis_client.get(key)
                    print(f"Document in Redis: {doc}\n{'=-'*75}")
                    print(
                        f"Document {key} insert or update in Redis with sucess!")

                elif operation_type == "delete":
                    key = str(change['documentKey']['_id'])
                    result = redis_client.delete(key)
                    if result == 0:
                        print("Document not for removal")
                    else:
                        print(
                            f"\nDocument {key} deleted Redis\n{'=-'*75}")
        return coluna
