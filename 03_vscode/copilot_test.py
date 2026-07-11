# Create a pandas dataframe containing product names, prices and quantities
import pandas as pd

df = pd.DataFrame({
    "Product Name": ["Product A", "Product B", "Product C"],
    "Price": [10.99, 20.99, 30.99],
    "Quantity": [100, 200, 300]
})

print(df)

