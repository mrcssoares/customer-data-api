from src.config import SessionLocal
from src.models import Product
import random
import string


def create_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_products():
    db = SessionLocal()
    for i in range(100):
        title = create_random_string(10)
        image = f"https://example.com/{title}.png"
        price = random.randint(10, 1000)
        review_score = random.randint(0, 5)
        product = Product(
            title=title, image=image, price=price, review_score=review_score)
        db.add(product)
    db.commit()


create_products()
