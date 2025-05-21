class SparseMatrix:
    def __init__(self, num_rows=0, num_cols=0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = {}

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]

            if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                raise ValueError("Input file has wrong format")

            num_rows = int(lines[0].split('=')[1])
            num_cols = int(lines[1].split('=')[1])

            matrix = cls(num_rows, num_cols)

            for line in lines[2:]:
                if not line.startswith('(') or not line.endswith(')'):
                    raise ValueError("Input file has wrong format")
                try:
                    row, col, val = map(int, line.strip('()').split(','))
                    matrix.set_element(row, col, val)
                except:
                    raise ValueError("Input file has wrong format")
            return matrix
        except Exception as e:
            raise ValueError(f"Input file has wrong format: {e}")

    def set_element(self, row, col, val):
        if val != 0:
            self.data[(row, col)] = val
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = SparseMatrix(self.num_rows, self.num_cols)
        result.data = self.data.copy()
        for (row, col), val in other.data.items():
            result.set_element(row, col, result.get_element(row, col) + val)
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = SparseMatrix(self.num_rows, self.num_cols)
        result.data = self.data.copy()
        for (row, col), val in other.data.items():
            result.set_element(row, col, result.get_element(row, col) - val)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
    
        result = SparseMatrix(self.rows, other.cols)
    
        # Multiply using sparse property
        for (i, k), v1 in self.data.items():
            for j in range(other.cols):
                v2 = other.get_element(k, j)
                if v2 != 0:
                    current = result.get_element(i, j)
                    result.set_element(i, j, current + v1 * v2)
    
        return result


    def __str__(self):
        result = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (r, c), v in sorted(self.data.items()):
            result += f"({r}, {c}, {v})\n"
        return result
