# Add Virtual Column 🧮

A simple Python function that adds a new column to a DataFrame based on a math expression using existing columns.
Made as a small test task for data analyst interview.

---

## 💡 Idea

Sometimes you want to create a new column in a table using a formula — like `a + b * 2`.
This function lets you do that safely and easily.

It also checks that:

* All column names are valid (only letters and `_`)
* The formula (`role`) uses only existing columns and simple math symbols
* The new column name is also valid

If something is wrong — it just returns an empty DataFrame.

---

## 🧩 Example

```python
import pandas as pd
from your_file import add_virtual_column

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [10, 20, 30]
})

result = add_virtual_column(df, 'a + b * 2', 'sum')

print(result)
```

Output:

```
   a   b  sum
0  1  10   21
1  2  20   42
2  3  30   63
```

---

## ⚙️ Function logic (short version)

```python
def add_virtual_column(df, role, new_column):
    # 1. Check column names
    # 2. Check new column name
    # 3. Validate math expression (role)
    # 4. Extract columns used in the expression
    # 5. Evaluate and add result column
    # 6. Return new DataFrame (or empty if error)
```

---

## 🧠 Notes

* Only letters, `_`, `+`, `-`, `*`, `/`, and spaces are allowed in the formula
* It uses `pandas.eval()` under the hood
* If you mess up the expression or column names, it just gives back an empty DataFrame

---

Made with ☕ and `pandas` ❤️
