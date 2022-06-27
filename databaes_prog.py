import datetime as dt
import pandas
import os
import sqlite3
#print(databaes_prog.__builtins__)

#print(os.getcwd())
os.chdir(r"S:\python projects\1-7-2021")

#==============================================
print("="*100)
FROM_FILE=pandas.read_excel(r"A1.xlsx")
print(FROM_FILE)
file_colum_number=FROM_FILE.shape[1]
#========================================CHECK_NUMBER_OF_COLUMES
if file_colum_number:
    num_of_colume=file_colum_number
else:
    num_of_colume=int(input("NUMBER OF COLUM========="))
#==========================================CHECK_NAME_COLUM
col_name_at_file=FROM_FILE.columns
check_col_name=[ i for i in col_name_at_file  if type(i)==str]
COLUM_TABLE=[]#=====================>
if len(check_col_name)==len(col_name_at_file):
    COLUM_TABLE=check_col_name
else:
    for i in range(num_of_colume):
        COLUM_TABLE.append(input(f"COLUM NUM {i+1}=====>"))
FROM_FILE.columns=COLUM_TABLE
#===========================================================
#==================DEFINE_OUR_DATAFRAME=====================
DF=pandas.DataFrame(columns=([j for j in COLUM_TABLE]))
for COL_NAME in COLUM_TABLE:
    DF[COL_NAME]=FROM_FILE[COL_NAME]
print("="*100)
print(DF)
print("="*100)
#==========================================================================================
#========================================================================================
#=======================================
print("="*50)
COMPELETE_DATE=dt.datetime.now()
print(COMPELETE_DATE)
#===========================================
print("="*50)
TOdate=dt.date.today()
print(TOdate)
print("="*50)
#===============================
#SEARCH ABOUT PAST DATE 
TIME_DELTA=dt.timedelta(days=50)
TIME_DELTA_HOUERS=dt.timedelta(hours=50)
PAST_DATE=TOdate-TIME_DELTA
print("DAY IN PAST",PAST_DATE.day)
print("DAY IN PAST",(PAST_DATE-TIME_DELTA_HOUERS).day)
#=====================
print("="*50)
#============================
#SEARCH ABOUT ADDING COMPELETLY DATE 
FU=dt.date(day=28,month=10,year=2021)
DEFFERENT_B_TWO_DEFF_DATE=FU-TOdate
print("HOW MANY SECOND UNTIL ",DEFFERENT_B_TWO_DEFF_DATE.total_seconds())
print("="*50)
#================================
SECOND=COMPELETE_DATE.second
MINT=COMPELETE_DATE.minute
dayform_month=COMPELETE_DATE.day
month_from_year=COMPELETE_DATE.month
year=COMPELETE_DATE.year
print("-"*50)
print("SECOND_==",SECOND)
print("MINT==",MINT)
print(dayform_month)
print(month_from_year)
print(year)
print("-"*50)
#DF["DATETIME"]=COMPELETE_DATE
#print(DF.columns.values)
#======================================================
DB=sqlite3.connect("FRIST.db")
CR=DB.cursor()
CR.execute(f"CREATE TABLE IF NOT EXISTS REPORT ( I INTEGER PRIMARY KEY) ")#({DF.columns.values[0]} INTEGER)")

for name in DF.columns.values :
    CR.execute(f"ALTER TABLE REPORT ADD COLUMN {name} INTEGER ")

#CR.execute("INSERT INTO REPORT (PRODUCT,'NEWTHING')")
DB.commit()
DB.close()