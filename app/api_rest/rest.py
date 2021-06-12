from app.api_rest import api_rest_bp
from app.models import *
from flask import jsonify, request
from flask_restful import Api, Resource, fields, reqparse

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

api = Api(api_rest_bp)
resource_fields = {
    "id": fields.Integer,
    "code": fields.String,
    "name": fields.String,
    "category": fields.String,
    "availability": fields.String,
    "count": fields.String,
    "cost": fields.String,
    "description": fields.Integer,
}

create_args = reqparse.RequestParser()
create_args.add_argument("code", type=str, help="Code of the Product")
create_args.add_argument("name", type=str, help="Name of the Product")
create_args.add_argument("category", type=str, help="Category of the Product")
create_args.add_argument("availability", type=str, help="Availability of the Product")
create_args.add_argument("count", type=str, help="Count of the Product")
create_args.add_argument("cost", type=str, help="Cost of the Product")
create_args.add_argument("description", type=str, help="Description of the Product")


update_args = reqparse.RequestParser()
update_args.add_argument("code", type=str, help="Code of the Product", required=True)
update_args.add_argument("name", type=str, help="Name of the Product", required=True)
update_args.add_argument("category", type=str, help="Category of the Product", required=True)
update_args.add_argument("availability", type=str, help="Availability of the Product", required=True)
update_args.add_argument("count", type=str, help="Count of the Product", required=True)
update_args.add_argument("cost", type=str, help="Cost of the Product", required=True)
update_args.add_argument("description", type=str, help="Description of the Product", required=True)


class ProductItem(Resource):
    def post(self):
        args = create_args.parse_args()
        availability = False
        if args["availability"]:
            availability = True

        new_product = Product(
            code=args["code"],
            name=args["name"],
            category=args["category"],
            availability=availability,
            count=args["count"],
            cost=args["cost"],
            description=args["description"],
        )
        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)

    def get(self, id=None):
        if id:
            product = Product.query.get(id)
            if not product:
                return "Product not found!", 404
            return product_schema.jsonify(product)
        else:
            all_products = Product.query.all()
            return products_schema.jsonify(all_products)

    def put(self, id):
        product = Product.query.get_or_404(id)
        if not product:
            return "Product not found!", 404

        args = update_args.parse_args()
        availability = False
        if args["availability"]:
            availability = True

        product.code = args["code"]
        product.name = args["name"]
        product.category = args["category"]
        product.availability = availability
        product.count = args["count"]
        product.cost = args["cost"]
        product.description = args["description"]

        db.session.commit()

        return product_schema.jsonify(product)

    def delete(self, id):
        product = Product.query.get(id)
        if not product:
            return "Product not found!", 404
        db.session.delete(product)
        db.session.commit()

        return product_schema.jsonify(product)


api.add_resource(ProductItem, "/products", "/products/<id>")
