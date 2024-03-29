from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

import json


def GetData(account_name,access_key):
    # Documentation https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python
    # Table storage design https://docs.microsoft.com/en-us/rest/api/storageservices/designing-a-scalable-partitioning-strategy-for-azure-table-storage
    # table/entity design - 1mb entity limit, up to 252 key/value pair properties https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-overview
    table_service = TableService(account_name=account_name,account_key=access_key)
    
    # Read a value
    task = table_service.get_entity('league', 'bert@example.org', 'Volleyball 2018')
    test="a"

    # Update a value
    task = {'PartitionKey': 'bert@example.org', 'RowKey': 'Volleyball 2018',
        'CreateDate': '2019-11-12T00:01:01.00Z'}
    table_service.update_entity('league', task)
    


if __name__ == '__main__':
    secrets = json.load(open('secrets.json', 'r'))
    account_name = secrets["azure_table_storage"]["account_name"]
    access_key = secrets["azure_table_storage"]["access_key"]

    GetData(account_name,access_key)