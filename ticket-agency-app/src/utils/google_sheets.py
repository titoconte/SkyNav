import pandas as pd
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import os
# import picklecd 

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = '1aXr4z12EV185-dxRs1ufxebV2a6BXh0t_u30VPlmQ7k'

def get_credentials():
    """Gets credentials from service account JSON file."""
    try:
        # Update this path to your service account JSON file location
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__),'service-account-key.json')
        
        if not os.path.exists(SERVICE_ACCOUNT_FILE):
            raise FileNotFoundError(f"Service account file '{SERVICE_ACCOUNT_FILE}' not found")
        
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )
        return credentials
    
    except Exception as e:
        print(f"Error getting credentials: {e}")
        return None

def insert_data_row_sheet(sheet_name, values):
    """
    Insert data into Google Sheets using service account authentication
    """
    try:
        creds = get_credentials()
        if not creds:
            raise Exception("Failed to get credentials")

        authed_session = AuthorizedSession(creds)
        
        url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_name}!B2:append'
        
        params = {
            'valueInputOption': 'RAW',
            'insertDataOption': 'INSERT_ROWS',
        }
        
        body = {
            'values': values if isinstance(values, list) else [[values]]
        }
        
        response = authed_session.post(url, params=params, json=body)
        response.raise_for_status()
        print("Data successfully inserted!")
        return response.json()
    
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return None

def update_row_sheet(sheet_name, num, values):
    """
    Update data in a specific row of Google Sheets using service account authentication
    
    Args:
        spreadsheet_id (str): The ID of the spreadsheet
        sheet_name (str): Name of the sheet
        row_number (int): The row number to update
        values (list): List of values to update in the row
    """
    try:
        clear_all_row_sheet(spreadsheet_id, sheet_name,num)
        insert_data_row_sheet(spreadsheet_id, sheet_name, values)
    except Exception as e:
        print(f"An error occurred while updating row {row_number}: {e}")
        return None

def read_sheet(sheet_name):
    """
    Get data into Google Sheets using service account authentication
    """
    try:
        creds = get_credentials()
        if not creds:
            raise Exception("Failed to get credentials")

        authed_session = AuthorizedSession(creds)
        
        url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_name}!A:P'
                
        response = authed_session.get(url)
        response.raise_for_status()
        print("Data successfully read!")
        data = response.json()['values'][1:]
        df = pd.DataFrame(data)
        df.columns = df.iloc[0,:]
        df = df.iloc[1:,:]
        return df
    
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return None

def clear_all_row_sheet(sheet_name,num):
    """
    Get data into Google Sheets using service account authentication
    """
    try:
        creds = get_credentials()
        if not creds:
            raise Exception("Failed to get credentials")

        authed_session = AuthorizedSession(creds)
        
        url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_name}!A{num}:P{num}:clear'
                
        response = authed_session.post(url)
        response.raise_for_status()
        print("Data successfully inserted!")
        
        return response.json()
    
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return None

# Example usage:
# sheet_name = "Milheiros"
if __name__=="__main__":
    df = read_sheet('Agencias')
    print(df)