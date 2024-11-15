import heapq
        
def get_weights(graph: dict[str, dict]) -> list:
    for vertex in graph.values():
        for weight in vertex.values():
            return list(weight.keys())
    return []


def default_distance(weights: list[str], key: str) -> dict:
    return {
        weight: float('infinity') if weight == key else 0
        for weight in weights
    }
    
    
def dijkstra(graph: dict[str, dict[str, dict]], start: str, key: str) -> dict:
    weights_list = get_weights(graph)
    distances = {
        vertex: {
            **default_distance(weights_list, key),
            'path': []
        }
        for vertex in graph
    }
    distances[start][key] = 0
    queue = [(0, start, {k: 0 for k in weights_list})]

    while queue:
        current_distance_value, current_vertex, current_distance = heapq.heappop(queue)

        if current_distance_value > distances[current_vertex][key]:
            continue

        for neighbor, weights in graph[current_vertex].items():
            distance_value = current_distance_value + weights[key]

            if distance_value < distances[neighbor][key]:
                for weight in weights_list:
                    distances[neighbor][weight] = current_distance[weight] + weights[weight]
                    
                distances[neighbor]['path'].append(current_vertex)

                heapq.heappush(queue, (distance_value, neighbor, distances[neighbor]))

    return distances

def prepare_graph(graph: dict[str, list[dict[str, dict]]], key: str):
    new_graph = {}
    for node, vertexes in graph.items():
        new_graph[node] = {}

        for connected_node, weights in vertexes:
            if connected_node not in new_graph[node]:
                new_graph[node][connected_node] = weights
            
            if weights[key] < new_graph[node][connected_node][key]:
                new_graph[node][connected_node] = weights
                
    return new_graph

def get_variants(graph:dict, start: str, finish: str) -> list[dict]:
    variants = []
    for key in ['cost', 'days', 'opt']:
        variant = dijkstra(prepare_graph(graph, key), start, key).get(finish)
        variant['type'] = key
        variants.append(variant)
        
    return variants