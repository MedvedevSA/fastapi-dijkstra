import uvicorn

from fastapi import FastAPI, HTTPException, status

import djikstra, cities

app = FastAPI()

cities_list = cities.load()


@app.get("/cities_from")
def get_cities_from():
    return {city["from"] for city in cities_list}


@app.get("/cities_to")
def get_cities_to():
    return {city["to"] for city in cities_list}


@app.get("/cities/{origin}/{destination}")
def get_cities_to(origin: str, destination: str):
    try:
        return djikstra.get_variants(
            cities.cities_to_graph(cities_list), origin, destination
        )
    except KeyError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Not Found {err}"
        )


if __name__ == "__main__":
    uvicorn.run(app)
