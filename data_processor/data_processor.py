import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os


host = "host.docker.internal"
user = "postgres"
db_name = "ZNO2020"
password = "6667"



file_data = pd.read_csv("/usr/src/app/Odata2020File.csv",
                        sep=";",
                        decimal=",",
                        encoding="Windows-1251",
                        nrows=10000,
                        low_memory=False)


zno_results = pd.DataFrame(file_data,
                           columns=["Birth",
                                    "SEXTYPENAME",
                                    "REGNAME",
                                    "AREANAME",
                                    "TERNAME",
                                    "REGTYPENAME",
                                    "TerTypeName",
                                    "EONAME",
                                    "EOTYPENAME",
                                    "UkrTestStatus",
                                    "UkrBall100",
                                    "UkrBall12",
                                    "mathTestStatus",
                                    "mathBall100",
                                    "mathBall12",
                                    "engTestStatus",
                                    "engBall100",
                                    "engBall12"])


conn_string = f"postgresql://{user}:{password}@{host}/{db_name}"
db = create_engine(conn_string)
conn = db.connect()

zno_results.to_sql("zno_results", con=conn, if_exists="replace", index=True)

conn.close()
db.dispose()

conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host)
cursor = conn.cursor()

cursor.execute('SELECT * FROM zno_results WHERE "engBall100" >= 140 AND "UkrBall100" >= 180;')
data = cursor.fetchall()
# for i in data:
#     print(i)

conn.commit()
cursor.close()
conn.close()
