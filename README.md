# Currency_Converter_Web

This is a simple web-based currency converter built using Flask and the [ExchangeRate-Host API](https://exchangerate.host/). The application allows users to convert amounts between various currencies using live exchange rates.

## Features

- **Live Exchange Rates**: Uses the [ExchangeRate-Host API](https://exchangerate.host/) to fetch the latest exchange rates.
- **Currency Selection**: Allows users to select a base currency and a target currency.
- **Amount Conversion**: Converts the entered amount from the base currency to the target currency and displays the result.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installing Dependencies

To install the required dependencies, create a virtual environment and install the necessary packages:

1. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

   You can create the `requirements.txt` file with the following content:

   ```
   flask
   requests
   ```

## Running the Application

1. **Start the Flask Development Server**:
    ```bash
    python app.py
    ```

2. The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

- **Select the base currency**: Choose the currency from which you want to convert.
- **Select the target currency**: Choose the currency to which you want to convert.
- **Enter the amount**: Type in the amount you want to convert.
- **Click "Convert"**: The application will display the converted amount.
