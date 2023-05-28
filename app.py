from fastapi import FastAPI, HTTPException

from schemas.products import Products

app = FastAPI(
    title="Adventure Works API", description="a REST API for Santo Digital Hackathon"
)

products = []


# root endpoint
@app.get("/")
def read_root():
    return {"welcome": "Welcome to my REST API"}


# all products endpoint
@app.get("/products")
def get_products():
    return products


# single product endpoint
@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["productKey"] == id:
            return product
    raise HTTPException(status_code=404, detail="Item not found!")


# post product endpoint
@app.post("/products/")
def post_product(product: Products):
    # product.productKey = int(uuid())
    products.append(product.dict())

    return products[-1]


# update product endpoint
@app.put("/products/{id}")
def update_product(id: int, updatedProd: Products):
    for index, product in enumerate(products):
        if product["productKey"] == id:
            products[index]["productSKU"] = updatedProd.dict()["productSKU"]
            products[index]["productName"] = updatedProd.dict()["productName"]
            products[index]["modelName"] = updatedProd.dict()["modelName"]
            products[index]["productDesc"] = updatedProd.dict()["productDesc"]
            products[index]["productColor"] = updatedProd.dict()["productColor"]
            products[index]["productSize"] = updatedProd.dict()["productSize"]
            products[index]["productStyle"] = updatedProd.dict()["productStyle"]
            products[index]["productCost"] = updatedProd.dict()["productCost"]
            products[index]["productprice"] = updatedProd.dict()["productprice"]
            return {"message": "Product has been updated succesfully!"}
    raise HTTPException(status_code=404, detail="Item not found")


# delete product endpoint
@app.delete("/products/{id}")
def delete_post(id: int):
    for index, product in enumerate(products):
        if product["productKey"] == id:
            products.pop(index)
            return {"message": "Product has been deleted succesfully!"}
    raise HTTPException(status_code=404, detail="Item not found")
