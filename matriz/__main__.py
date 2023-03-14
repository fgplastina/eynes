import random


def _get_matrix():
    """
    Es mucho mas sencillo usar numpy pero no veo que permita o prohiba usarlo. Por eso decidi usar una forma mas "tradicional"
    Ejemplo con numpy:

        import numpy
        numpy.full((5,5), numpy.random.randint(0,100))

    """
    data = [[random.randrange(0,5) for i in range(5)] for j in range(5)]
    return data


def _search_consecutives_sequence_by_row(matrix):
    result =  ""

    for row in matrix:

        for element in range(len(row) - 3):

            if row[element:element+4] == [row[element], row[element]+1, row[element]+2, row[element]+3]:
                message = f"Secuencia creciente encontrada en la fila: {row[element:element+4]} en la posición: {(matrix.index(row), element)} - {(matrix.index(row), element+3)}"
                result = message

            elif row[element:element+4] == [row[element], row[element]-1, row[element]-2, row[element]-3]:
                message = f"Secuencia decreciente encontrada en la fila: {row[element:element+4]} en la posición: {(matrix.index(row), element)} - {(matrix.index(row), element+3)}"
                result = message if not result else f"{result} \n {message}"

    return result


def _search_consecutives_sequence_by_column(matrix):
    result = ""

    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]

        for element in range(len(column) - 3):

            if column[element:element+4] == [column[element], column[element]+1, column[element]+2, column[element]+3]:
                message = f"Secuencia creciente encontrada en la columna: {column[element:element+4]}, en la posición: {(element, j)} - {(element+3, j)}"
                result = message

            elif column[element:element+4] == [column[element], column[element]-1, column[element]-2, column[element]-3]:
                message = f"Secuencia decreciente encontrada en la columa: {column[element:element+4]}, en la posición: {(element, j)} - {(element+3, j)}"
                result = message if not result else f"{result} \n {message}"

    return result


def _show_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


def main():
    """
    Runtime principal para encontrar secuencias consecutivas en la matriz
    """
    matrix = _get_matrix()

    _show_matrix(matrix)

    result_by_row = _search_consecutives_sequence_by_row(matrix)
    result_by_column = _search_consecutives_sequence_by_column(matrix)

    if not result_by_column and not result_by_row:
        print("No se encontró ninguna secuencia consecutiva en la matriz")

    if result_by_row:
        print(result_by_row)

    if result_by_column:
        print(result_by_column)


if __name__ == "__main__":
    main()
