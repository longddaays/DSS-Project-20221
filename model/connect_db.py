#pip install mysql-connector-python-rf
# pip install PyMySQL

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import mysql.connector

dbName = "test"

#example : tableName = "dss_data_prep"
def read_frame_from_db(tableName):
    sqlEngine       = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3600)
    dbConnection    = sqlEngine.connect()
    frame           = pd.read_sql("select * from " + dbName + '.' + tableName, dbConnection);
    pd.set_option('display.expand_frame_repr', False)
    print(frame)
    dbConnection.close()
    return frame

#example : csvName = "data/dss_data_prep.csv", tableName = "dss_data_prep"
def csvToDb(csvName, tableName):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=dbName
    )
    mycursor = mydb.cursor()
    mycursor.execute("drop table if exists " + tableName)

    df = pd.read_csv(csvName)
    dataFrame = pd.DataFrame(data=df)           
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/' + dbName, pool_recycle=3600)
    dbConnection = sqlEngine.connect()    
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='fail')
    dbConnection.close()

# csvToDb("data/dss_data_prep.csv", "dss_data_prep")
# read_frame_from_db("dss_data_prep")