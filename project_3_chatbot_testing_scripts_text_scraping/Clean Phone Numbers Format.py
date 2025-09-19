# Let's clean the phone numbers column: clean phone numbers by removing special characters (-, /, |)
df2["Phone_Number"]=df2["Phone_Number"].str.replace(r'[^a-zA-Z0-9]','',regex=True)
#Else to remove all non-digit characters from phone numbers you can use 
#df['phone'] = df['phone'].str.replace(r'[-/|]', '', regex=True)
df2["Phone_Number"]=df2["Phone_Number"].apply( lambda x: str(x))
df2["Phone_Number"]=df2["Phone_Number"].apply( lambda x: x[0:3]+'-'+ x[3:6]+'-'+x[6:10])
df2