import typer
from klikindomart import search_product, get_product_promo_list


def main(product: str):
    if product:
        data = search_product(product)
    else:
        data = get_product_promo_list()

    for item in data:
        typer.echo(f'Product Name: {item.get("product_name")}')
        typer.echo(f'Product Price: {item.get("price").get("product_price")}')
        typer.echo(f'Product Price: {item.get("price").get("product_discount_price")}')
        typer.echo(f'Product Price: {item.get("product_stock")}')
        typer.echo(f'Product Price: {item.get("product_from")}')
        typer.echo(f'Product Price: {item.get("product_link")}')
        typer.echo('                                          ')


if __name__ == "__main__":
    typer.run(main)
