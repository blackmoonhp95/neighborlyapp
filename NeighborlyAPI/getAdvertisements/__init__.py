import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
import traceback

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ.get('COSMOSDB_CON_STR')
        client = pymongo.MongoClient(url)
        database = client['neighborly']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except Exception as e:
        print("could not connect to mongodb")
        return func.HttpResponse(traceback.format_exc(), mimetype="application/json", status_code=400)

