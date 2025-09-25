from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI(title="Mobile App Logs API")

# Load dataset when the server starts
df = pd.read_csv("App_Logs.csv")
df = df.replace([np.nan, np.inf, -np.inf], None)
data_json = df.to_dict(orient="records")

@app.get("/data")
async def get_data():
    return {"data": data_json}

