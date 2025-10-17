import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Safely adds a new virtual column to a DataFrame based on an expression of existing columns.
    """
    # Allow only letters and underscores in column names
    pattern = r'^[A-Za-z_]+$'
    if not all(re.match(pattern, col) for col in df.columns):
        return pd.DataFrame()
        
    # Validate new column name
    if not re.match(pattern, new_column):
        return pd.DataFrame()
    
    # Validate expression format (letters, math symbols, spaces)
    if not re.match(r'^[A-Za-z_+\-* /]+$', role):
        return pd.DataFrame()
        
    # Extract column names used in the expression
    columns_in_expr = re.findall(r'[A-Za-z_]+', role)

    # Check that all columns exist in the dataframe
    if not all(col in df.columns for col in columns_in_expr):
        return pd.DataFrame()

    # Copy dataframe to avoid modifying original
    result = df.copy()

    try:
        # Evaluate expression and create new column
        result[new_column] = result.eval(role)
    except Exception:
        # Return empty dataframe if evaluation fails
        return pd.DataFrame()

    # Return updated dataframe
    return result
