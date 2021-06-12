from app.extensions import db, ma


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), default="Groceries", nullable=False)
    availability = db.Column(db.Boolean(), nullable=False)
    count = db.Column(db.Integer(), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Product-{self.id}\n \
        code {self.code}\n \
        name {self.name}\n \
        category {self.category}\n \
        availability {self.availability}\n \
        count {self.count}\n \
        cost {self.cost}\n \
        description {self.description}>"


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
