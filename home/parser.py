from .models import LeadManagement
import pandas as pd



def load_csv(dataframe):
    for index, row in dataframe.iterrows():

        if pd.isnull(row["Name"]):
            continue
        if pd.isnull(row["Mobile"]):
            continue
        if pd.isnull(row["Status"]):
            continue
        lead = LeadManagement(
            name=row["Name"],
            mobile_number=row["Mobile"],
            status=row["Status"],
            address=row["Address"],
            industry=row["Industry"],
            website=row["Website"],
            contacts=row["Contacts"],
            pipelines=row["Pipelines"],
            notes=row["Notes"],

        )
        lead.save()
    return lead