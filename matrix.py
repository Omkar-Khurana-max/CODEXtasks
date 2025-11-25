import numpy as np

def input_matrix(prompt):
    print(prompt)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter matrix values row by row (separated by spaces):")
    matrix = [list(map(float, input(f"Row {i+1}: ").split())) for i in range(rows)]
    return np.array(matrix)

def print_matrix(matrix, self):
    print("Result: \n")
    for row in matrix:
        print("  ".join(f"{val:8.2f}" for val in row))

def perform_operation():
    print("\n MATRIX OPERATIONS TOOL")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")

    choice = input("Select an operation (1-5): ")

    if choice in ["1", "2", "3"]:
        mat1 = input_matrix("Matrix 1:")
        mat2 = input_matrix("Matrix 2:")

        if choice == "1":
            if mat1.shape == mat2.shape:
                print_matrix(mat1 + mat2, "Result (A + B)")
            else:
                print("\n Matrices must have the same dimensions")

        elif choice == "2":
            if mat1.shape == mat2.shape:
                print_matrix(mat1 - mat2, "Result (A - B)")
            else:
                print("\n Matrices must have the same dimensions")

        elif choice == "3":
            if mat1.shape[1] == mat2.shape[0]:
                print_matrix(np.dot(mat1, mat2), "Result (A * B)")
            else:
                print("\n Columns of Matrix 1 must equal rows of Matrix 2")

    elif choice == "4":
        mat = input_matrix("Matrix:")
        print_matrix(mat.T, "Transpose")

    elif choice == "5":
        mat = input_matrix("Square Matrix:")
        if mat.shape[0] == mat.shape[1]:
            det = np.linalg.det(mat)
            print(f"\n Determinant: {det:.2f}")
        else:
            print("\n Determinant only works for square matrices")
    else:
        print("\n Invalid choice!")

def main():
    while True:
        perform_operation()
        again = input("\n Would you like to perform another operation? (y/n): ").lower()
        if again != 'y':
            print("\n --- Program End ---")
            break

if __name__ == "__main__":
    main()