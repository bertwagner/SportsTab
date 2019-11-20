from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import json
import bcrypt

azure_storage_credentials = None

def get_pepper():
    # TODO: Get pepper from Azure Key Vault
    # TODO: Generate a new pepper that's not in source control...
    return "3940C72988CD12E2"

def login(email,password):
    # Retrieve login information from our table
    table_service = TableService(account_name=azure_storage_credentials["account_name"],account_key=azure_storage_credentials["access_key"])
    user = table_service.get_entity('user', 'bert@example.org', '')

    email = user["PartitionKey"]
    pepper = get_pepper()
    password = bytes(str(password + pepper).encode('utf-8'))
    password_hash = user["PasswordHash"].encode('utf-8')
    
    # Calculate a hash of our password + pepper
    #hashed = bcrypt.hashpw(password_pepper,bcrypt.gensalt())
    

    #Login
    if bcrypt.checkpw(password,password_hash):
        print('Log in successful!')
        # TODO: generate and return JWT
    else:
        print('You have not logged in')
        # TODO: return error message

    


    asdf = "asdf"

if __name__ == '__main__':
    secrets = json.load(open('secrets.json', 'r'))
    account_name = secrets["azure_table_storage"]["account_name"]
    access_key = secrets["azure_table_storage"]["access_key"]
    azure_storage_credentials = {"account_name":account_name,"access_key":access_key}

    # Test data
    email = "bert@example.org"
    password = "P@ssword1"


    login(email,password)