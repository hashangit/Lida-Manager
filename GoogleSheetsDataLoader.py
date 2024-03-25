import pandas as pd
import gspread
from gspread.exceptions import SpreadsheetNotFound, APIError, WorksheetNotFound

class GoogleSheetsDataLoader:
    GOOGLE_SHEET_ID = 'your_google_sheeet_id_here'

    def __init__(self, credentials_filename='client_secret.json'):
        self.credentials_filename = credentials_filename
        print("GoogleSheetsDataLoader embarks on the quest to harness the power of Google Sheets data.")
        self.initialize_google_sheets_client()
        self.open_spreadsheet()

    def initialize_google_sheets_client(self):
        try:
            self.gc = gspread.service_account(filename=self.credentials_filename)
            print("Magical connection established with the Google Sheets client.")
        except Exception as e:
            print(f"A tempest thwarted our attempt to initialize the Google Sheets client: {e}")

    def open_spreadsheet(self):
        if self.gc:
            try:
                print("Opening the grand tome of data...")
                self.sh = self.gc.open_by_key(self.GOOGLE_SHEET_ID)
                print("The tome lies open, filled with endless knowledge.")
            except SpreadsheetNotFound:
                print("Alas! The tome was not found. Verify your map (Google Sheet ID).")
            except APIError as e:
                print(f"The spirits of the API realm are restless: {e}")
            except Exception as e:
                print(f"An unforeseen mystic force has prevented us from opening the tome: {e}")
        else:
            print("Connection to the mystical realms of Google Sheets has not been established.")

    def load_worksheet_as_df(self, worksheet_name):
        if not self.sh:
            print("The tome remains closed; no connection has been established.")
            return pd.DataFrame()
        
        try:
            print(f"Summoning data from the scrolls of {worksheet_name}...")
            worksheet = self.sh.worksheet(worksheet_name)
            df = pd.DataFrame(worksheet.get_all_records())
            print(f"Data from the scrolls of {worksheet_name} has been summoned successfully.")
            return df
        except WorksheetNotFound:
            print(f"The scroll titled '{worksheet_name}' eludes us, nowhere to be found.")
        except APIError as e:
            print(f"The spirits of the API realm denied us: {e}")
        except Exception as e:
            print(f"An arcane obstacle has hindered our quest for the scroll of '{worksheet_name}': {e}")
            return pd.DataFrame()

    # Individual methods for loading each DataFrame as before, embarking on their specific quests
    def load_gads_df(self):
        return self.load_worksheet_as_df('GAds')
    
    def load_meta_ads_df(self):
        return self.load_worksheet_as_df('MetaAds')

    def load_purchase_data_df(self):
        return self.load_worksheet_as_df('Purchase_data')

    def load_c_data_df(self):
        return self.load_worksheet_as_df('Customer_data')

    def load_campaign_df(self):
        return self.load_worksheet_as_df('Campaigns')

    def load_t_campaign_df(self):
        return self.load_worksheet_as_df('Campaigns by theme')

    def load_themes_df(self):
        return self.load_worksheet_as_df('Themes')

    def load_all_data(self):
        print("Gathering all the scrolls, a quest to uncover all secrets at once...")
        return {
            'gads_df': self.load_gads_df(),
            'meta_ads_df': self.load_meta_ads_df(),
            'purchase_data_df': self.load_purchase_data_df(),
            'c_data_df': self.load_c_data_df(),
            'campaign_df': self.load_campaign_df(),
            't_campaign_df': self.load_t_campaign_df(),
            'themes_df': self.load_themes_df()
        }

# Usage example
# loader = GoogleSheetsDataLoader()

# To load all data at once
# all_data = loader.load_all_data()

# To load only the GAds data
# gads_df = loader.load_gads_df()
