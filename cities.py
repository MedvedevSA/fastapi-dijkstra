import csv

        

def load() -> list[dict]:
    csv_file = 'data.csv'
    cities: list[dict] = []

    with open(csv_file) as csvfile:
        dict_reader = csv.DictReader(csvfile)
        for row in dict_reader:
            cities.append(dict(row))

    return cities

def cities_to_graph(cities: list[dict]) -> dict:
    graph = {}
    for city in cities:
        if city['from'] not in graph:
            graph[city['from']] = []
        
        if city['to'] not in graph:
            graph[city['to']] = []

        graph[city['from']].append((city['to'], {
                'cost': int(city['cost']),
                'days': int(city['days']),
                'opt': int(city['cost']) * 0.7 + int(city['days']) *0.3
            })
        )

    return graph