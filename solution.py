import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    pattern = r'^[A-Za-z_]+$'
    if not all(re.match(pattern, col) for col in df.columns):
        return pd.DataFrame()
        
    if not re.match(pattern, new_column):
        return pd.DataFrame()
    
    if not re.match(r'^[A-Za-z_+\-* /]+$', role):
        return pd.DataFrame()
        
    columns_in_expr = re.findall(r'[A-Za-z_]+', role)

    if not all(col in df.columns for col in columns_in_expr):
        return pd.DataFrame()

    result = df.copy()

    try:
        result[new_column] = result.eval(role)
    except Exception:
        return pd.DataFrame()

    return result
