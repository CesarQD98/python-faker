from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(description="Prueba de ArgumentParser en Python", prog="bashrunner")
    parser.add_argument("-r", help="Cantidad de datos creados")
    return parser.parse_args()

a = parse_arguments()



