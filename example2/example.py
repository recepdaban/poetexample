import requests as rq


class Example:
    def check_request(self,url):
        req = rq.get(url)
        return req.status_code


"""
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


df = pd.DataFrame(

    {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss. Elizabeth",

        ],

        "Age": [22, 35, 58],

        "Sex": ["male", "male", "female"],

    }

)
 
table = pa.Table.from_pandas(df)

"""