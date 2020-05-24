import pandas as pd
import uuid

def data_parse(data):
    root_path="/home/ubuntu/projects/bajrangpress/bajrangbali/downloads/"
    excel_name=str(uuid.uuid4())+'.xlsx'
    excel_path=root_path+excel_name
    writer = pd.ExcelWriter(excel_path,  
                       engine ='xlsxwriter') 
    for k in data:

        df=pd.DataFrame(data[k])
        # Write a dataframe to the worksheet. 
        df.to_excel(writer, sheet_name =k) 

    # Close the Pandas Excel writer 
    # object and output the Excel file. 
    writer.save() 
    return excel_name