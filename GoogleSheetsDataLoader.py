import pandas as pd
import gspread
from gspread.exceptions import SpreadsheetNotFound, APIError, WorksheetNotFound

class GoogleSheetsDataLoader:
    GOOGLE_SHEET_ID = '1VbUa5AvOBgArjoigeuZbptKKoqpKKB5WPgcV77AYAIg'

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
    
    def load_gadst_df(self):
        return self.load_worksheet_as_df('GAdsT')

    def load_last_week_data(self):
        return self.load_worksheet_as_df('CB')

    def load_i_df(self):
        return self.load_worksheet_as_df('Indicative')

    def load_campaign_df(self):
        return self.load_worksheet_as_df('Campaigns')

    def load_t_campaign_df(self):
        return self.load_worksheet_as_df('Campaigns by Topics')

    def load_topics_df(self):
        return self.load_worksheet_as_df('Topics')

    def load_all_data(self):
        print("Gathering all the scrolls, a quest to uncover all secrets at once...")
        return {
            'gadst_df': self.load_gadst_df(),
            'last_week_data': self.load_last_week_data(),
            'i_df': self.load_i_df(),
            'campaign_df': self.load_campaign_df(),
            't_campaign_df': self.load_t_campaign_df(),
            'topics_df': self.load_topics_df()
        }

# Usage example
# loader = GoogleSheetsDataLoader()

# To load all data at once
# all_data = loader.load_all_data()

# To load only the GAds data
# gads_df = loader.load_gads_df()
