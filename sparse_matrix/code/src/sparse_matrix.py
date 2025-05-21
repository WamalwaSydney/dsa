class SparseMatrix:
    def __init__(self, num_rows=0, num_cols=0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = {}  # {(row, col): value}

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as f:
                rows_line = f.readline().strip()
                cols_line = f.readline().strip()

                if not rows_line.startswith("rows=") or not cols_line.startswith("cols="):
                    raise ValueError("Input file has wrong format")

                num_rows = int(rows_line.split('=')[1])
                num_cols = int(cols_line.split('=')[1])
                matrix = cls(num_rows, num_cols)

                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file has wrong format")
                    try:
                        r, c, v = map(int, line.strip('()').split(','))
                    except:
                        raise ValueError("Input file has wrong format")
                    if v != 0:
                        matrix.data[(r, c)] = v
            return matrix
        except Exception as e:
            raise ValueError(f"Input file has wrong format: {e}")

    def set_element(self, row, col, val):
        if val != 0:
            self.data[(row, col)] = val
        else:
            self.data.pop((row, col), None)

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def add(self, other):
        if (self.num_rows, self.num_cols) != (other.num_rows, other.num_cols):
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(self.num_rows, self.num_cols)
        result.data = self.data.copy()
        for (r, c), v in other.data.items():
            total = result.data.get((r, c), 0) + v
            if total:
                result.data[(r, c)] = total
            else:
                result.data.pop((r, c), None)
        return result

    def subtract(self, other):
        if (self.num_rows, self.num_cols) != (other.num_rows, other.num_cols):
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(self.num_rows, self.num_cols)
        result.data = self.data.copy()
        for (r, c), v in other.data.items():
            total = result.data.get((r, c), 0) - v
            if total:
                result.data[(r, c)] = total
            else:
                result.data.pop((r, c), None)
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result = SparseMatrix(self.num_rows, other.num_cols)

        # Build a row-based index for B: rows_B[k] = { j: B[k,j] }
        rows_B = {}
        for (r, c), v in other.data.items():
            rows_B.setdefault(r, {})[c] = v

        # For each nonzero in A at (i,k), only combine with nonzeros in B row k
        for (i, k), v1 in self.data.items():
            if k not in rows_B:
                continue
            for j, v2 in rows_B[k].items():
                new_val = result.data.get((i, j), 0) + v1 * v2
                if new_val:
                    result.data[(i, j)] = new_val
                else:
                    result.data.pop((i, j), None)

        return result

    def __str__(self):
        out = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (r, c), v in sorted(self.data.items()):
            out += f"({r}, {c}, {v})\n"
        return out
