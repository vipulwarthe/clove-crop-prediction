from dask.distributed import Client

def start_cluster():
    client = Client()
    print(client)
    return client