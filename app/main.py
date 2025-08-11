from fastapi import FastAPI
from app.routes import users, products, orders

app = FastAPI(title="Large FastAPI Project")

# Register routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Welcome to Large FastAPI Project"}
