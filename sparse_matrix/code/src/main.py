from sparse_matrix import SparseMatrix
import time

def main():
    print("Sparse Matrix Operations")
    print("1 - Add\n2 - Subtract\n3 - Multiply")
    choice = input("Enter choice (1/2/3): ").strip()

    path1 = input("First matrix file path: ").strip()
    path2 = input("Second matrix file path: ").strip()

    try:
        print("Loading matrices...")
        t0 = time.time()
        A = SparseMatrix.from_file(path1)
        B = SparseMatrix.from_file(path2)
        load = time.time() - t0
        print(f"→ Loaded in {load:.2f}s.  A: {len(A.data)} nonzeros, B: {len(B.data)} nonzeros\n")

        op_start = time.time()
        if choice == '1':
            print("Adding…")
            C = A.add(B)
            op = "Addition"
        elif choice == '2':
            print("Subtracting…")
            C = A.subtract(B)
            op = "Subtraction"
        elif choice == '3':
            print("Multiplying…")
            C = A.multiply(B)
            op = "Multiplication"
        else:
            print("Invalid choice.")
            return

        op_time = time.time() - op_start
        print(f"→ {op} done in {op_time:.2f}s.  Result has {len(C.data)} nonzeros.")

        if input("Show result matrix? (y/n): ").lower().startswith('y'):
            print("\nResult:\n" + str(C))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
