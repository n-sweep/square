from square.client import Client


def get_client(token_path):
    with open(token_path, 'r') as f:
        token = f.read()

    return Client(
        access_token=token,
        environment='production',
    )


def get_locations(client):
    result = client.locations.list_locations()

    if result.is_success():
        return result.body['locations']

    elif result.is_error():
        print('Error calling LocationsApi.listlocations')
        return result.errors


def get_all_orders(client):
    locations = get_locations(client)
    body = {'location_ids': [locations[0]['id']]}
    result = client.orders.search_orders(body)

    if result.is_success():
        return result.body['orders']

    elif result.is_error():
        print('Error calling LocationsApi.listlocations')
        return result.errors


def main():
    # Create an instance of the API Client
    # and initialize it with the credentials
    # for the Square account whose assets you want to manage

    client = get_client('/home/n/.config/square/token')
    orders = get_all_orders(client)

    count = 0
    total = 0
    for order in orders:
        m = order['total_money']['amount']
        total += m
        count += 1

    print(total * 0.01)


if __name__ == "__main__":
    main()
