from argparse import ArgumentParser
from app import generarFakeData

def parse_arguments():
    parser = ArgumentParser(description="Prueba de ArgumentParser en Python", prog="bashrunner")
    parser.add_argument("-r", help="Cantidad de datos a crear")
    return parser.parse_args()

a = parse_arguments()

generarFakeData(int(a.r))



