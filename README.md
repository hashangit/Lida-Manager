
# Lida Data Analysis and Chat Application

This package provides a Streamlit application that integrates data loading, exploratory data analysis (EDA), and an interactive chat interface to engage with data. It's designed for users to easily load data from Google Sheets, perform EDA, and ask questions directly to the data through a chat interface, receiving visual responses.

## Features

- **Data Loading**: Load data directly from Google Sheets into Pandas DataFrames for analysis.
- **Exploratory Data Analysis**: Automatically generate visualizations based on the loaded data.
- **Chat with Data**: Interact with the data through a chat interface, asking questions and receiving data-driven insights and visualizations as responses.

## Installation

To get started with this package, clone this repository to your local machine. Ensure you have Python installed and proceed to set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

This application requires an `OPENAI_API_KEY` for using GPT models and a service account key file named `client_secret.json` from Google Cloud Platform to access Google Sheets data.

## Usage

To run the Streamlit application, navigate to the project directory and execute:

```bash
streamlit run app.py
```

Replace `app.py` with the actual filename of the Streamlit application if it's named differently.

### Configuration

- **Google Sheets Data Loader**: Ensure you have `client_secret.json` in your project directory for authentication with Google's API.
- **OpenAI API Key**: Set your OpenAI API key in an `.env` file in the root directory as follows:

  ```env
  OPENAI_API_KEY=your_openai_api_key_here
  ```

### Interacting with the Application

- **Load Data**: Data will be automatically loaded from the specified Google Sheet upon starting the app.
- **Explore Data**: Click on the "Analyze Data" button to perform EDA and view generated visualizations.
- **Chat with Data**: Use the sidebar to enter queries and interact with the data through the chat interface.

## Components

- `DataLoader`: Manages loading data from Google Sheets.
- `LidaEDA`: Handles exploratory data analysis and visualization generation.
- `LidaChat`: Processes user queries and generates visual responses.
- `GoogleSheetsDataLoader`: Specific implementation for loading data from Google Sheets.

## License

MIT License

Copyright (c) 2024 Hashan Wickramasinghe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.

