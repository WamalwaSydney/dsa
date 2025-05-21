# Sparse Matrix Library

A lightweight Python implementation for efficiently handling sparse matrices - matrices where most elements are zero.

## Overview

This library provides a `SparseMatrix` class that implements core operations for sparse matrices using a memory-efficient dictionary-based storage format. Instead of storing all elements including zeros, it only stores non-zero values, making it suitable for very large matrices with relatively few non-zero entries.

## Features

- Memory-efficient sparse matrix representation
- File I/O support for loading and saving matrices
- Core matrix operations:
  - Addition
  - Subtraction
  - Multiplication
- Easy-to-use command-line interface

## Installation

Simply copy the `sparse_matrix.py` file to your project directory:

```bash
# Clone the repository or download sparse_matrix.py
git clone https://github.com/WamalwaSydney/dsa.git
# Or copy sparse_matrix.py directly to your project
```

## Usage

### As a Module

```python
from sparse_matrix import SparseMatrix

# Create matrices
A = SparseMatrix(3, 3)
A.set_element(0, 0, 5)
A.set_element(1, 2, 3)

B = SparseMatrix(3, 3)
B.set_element(0, 0, 2)
B.set_element(2, 1, 4)

# Perform operations
C = A.add(B)
D = A.subtract(B)
E = A.multiply(B)

# Get values
value = C.get_element(0, 0)  # Returns 7 (5+2)

# Save to file
with open("matrix.txt", "w") as f:
    f.write(str(C))
```

### Command Line Interface

The program provides a simple command-line interface to perform operations:

```bash
python sparse_matrix.py
```

This will prompt you to:
1. Choose an operation (add, subtract, or multiply)
2. Enter file paths for the input matrices
3. View the result or save it

## File Format

The file format for sparse matrices is:

```
rows=<number_of_rows>
cols=<number_of_columns>
(<row>, <col>, <value>)
(<row>, <col>, <value>)
...
```

Example:
```
rows=3
cols=3
(0, 0, 5)
(1, 2, 3)
```

## Performance

The implementation is optimized for sparse matrices where most elements are zero:
- Space complexity: O(N) where N is the number of non-zero elements
- Time complexity:
  - Addition/Subtraction: O(N₁ + N₂) where N₁, N₂ are non-zeros in each matrix
  - Multiplication: O(N₁ × N₂) in worst case, but often much better in practice

## Implementation Details

- Uses a dictionary `{(row, col): value}` to store non-zero elements
- Only stores non-zero values to save memory
- Implements optimized multiplication by using row-based indexing

## Example Files

Create example input files:

**matrix_a.txt**:
```
rows=3
cols=3
(0, 0, 5)
(1, 2, 3)
```

**matrix_b.txt**:
```
rows=3
cols=3
(0, 0, 2)
(2, 1, 4)
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
