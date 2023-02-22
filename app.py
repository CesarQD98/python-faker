from faker import Faker
from settings import *
import json
import random

fake = Faker("es_MX")

lista_data = []


def imprimirLenLista(lista: list):
    print(len(lista))


def generarFakeData(cantidad: int):
    output_data = []

    for _ in range(cantidad):
        id = fake.bothify(text="???-###")
        title = fake.company()
        price = round(random.random() * 10 + 1, 2)
        description = fake.text(max_nb_chars=20)

        product_string = {
            PRODUCTO_FIELDS[0]: id,
            PRODUCTO_FIELDS[1]: title,
            PRODUCTO_FIELDS[2]: price,
            PRODUCTO_FIELDS[3]: description,
            PRODUCTO_FIELDS[4]: [],
        }

        output_data.append(product_string)

    with open(OUTPUT_TXT_PATH, "w") as f:
        f.write("%s\n" % json.dumps(output_data, indent=2, ensure_ascii=False))
    f.close

    print("*** Han sido creadas %d instancias ***" % cantidad)

