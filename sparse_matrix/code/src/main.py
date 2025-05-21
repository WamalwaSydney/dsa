from sparse_matrix import SparseMatrix

def main():
    print("Sparse Matrix Operations")
    print("Choose an operation: 1 - Add, 2 - Subtract, 3 - Multiply")
    choice = input("Enter choice (1/2/3): ")

    path1 = input("Enter path for first matrix file: ").strip()
    path2 = input("Enter path for second matrix file: ").strip()

    try:
        A = SparseMatrix.from_file(path1)
        B = SparseMatrix.from_file(path2)

        if choice == '1':
            C = A.add(B)
        elif choice == '2':
            C = A.subtract(B)
        elif choice == '3':
            C = A.multiply(B)
        else:
            print("Invalid choice.")
            return

        print("\nResult:")
        print(C)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
