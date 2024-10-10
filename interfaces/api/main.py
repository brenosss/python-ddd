from fastapi import FastAPI

app = FastAPI()


@app.post("/products")
def create_product():
    return {"status": "under construction"}


@app.get("/products/{id}")
def retrieve_product(id: int):
    return {"product_id": id}
