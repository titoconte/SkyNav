from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import pandas as pd

# Define the scope and the credentials file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

def get_google_sheets_service():
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

def read_sheet(spreadsheet_id, range_name):
    service = get_google_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return pd.DataFrame(values[1:], columns=values[0]) if values else pd.DataFrame()

def write_sheet(spreadsheet_id, range_name, values):
    service = get_google_sheets_service()
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

def append_to_sheet(spreadsheet_id, range_name, values):
    service = get_google_sheets_service()
    body = {
        'values': values
    }
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()