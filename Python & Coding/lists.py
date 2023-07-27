clients = []

new_client = ""

while new_client.lower() != "quit":
    new_client = input(" What is the name of client? ")
    clients.append(new_client)

for client in clients:
    if client.lower() != "quit":
        print(client)
