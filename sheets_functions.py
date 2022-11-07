from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

SCANTRONS_sheet_id = "1ympYf521moNGqDCEfEsKtrMaqifwR4ejsy9T2InInF0"

# GRADES_sheet_id = "1cUblA6NLZiqS70gXs675ZO_68VeChRjuX7719pHF-q4"

def get_range(range_name):
    result = spreadsheet_service.spreadsheets().values().get(
    spreadsheetId=SCANTRONS_sheet_id, range=range_name).execute()
    rows = result.get("values", [])
    return rows

def read_data(data):
    print("{0} rows retrieved.".format(len(data)))
    print("{0} rows retrieved.".format(data))
    
def read_sheets():
    sheet_metadata = spreadsheet_service.spreadsheets().get(spreadsheetId=SCANTRONS_sheet_id).execute()
    sheets = sheet_metadata.get("sheets")
    sheet_names = []
    for sheet in sheets:
        sheet_names.append(sheet.get("properties").get("title"))
    sheet_names.remove("Answer Key")
    return sheet_names

