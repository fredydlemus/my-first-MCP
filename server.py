from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-inventory")

products = {
    "P001": {"nombre": "Laptop", "stock": 15, "precio": 1200},
    "P002": {"nombre": "Mouse", "stock": 50, "precio": 25},
    "P003": {"nombre": "Teclado", "stock": 30, "precio": 45},
}

@mcp.tool()
def request_stock(product_id: str) -> dict:
    """Check the available stock of a product."""
    if product_id in products:
        return products[product_id]
    return {"error": f"Product {product_id} not found"}

@mcp.tool()
def update_restock(product_id: str, quantity: int) -> dict:
    """Update the stock quantity of a product."""
    if product_id not in products:
        return {"error": "Product not found"}
    products[product_id]["stock"] += quantity
    return {
        "message": "Stock updated",
        "new_stock": products[product_id]["stock"]
    }

@mcp.resource("inventory://products")
def list_products() -> str:
    """Return the complete product list."""
    return str(products)

if __name__ == "__main__":
    mcp.run()