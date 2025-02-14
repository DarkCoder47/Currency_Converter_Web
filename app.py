from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

class CurrencyConverter:
    def __init__(self):
        # URL for fetching live exchange rates
        self.url = 'https://api.exchangerate.host/latest'
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()  # Raise an exception for non-2xx status codes
            self.data = self.response.json()

            # Check if the 'rates' key exists in the response
            if 'rates' in self.data:
                self.rates = self.data['rates']
            else:
                self.rates = {}
                print("Error: 'rates' not found in the response.")
        except requests.exceptions.RequestException as e:
            # Handle network errors, API down, or invalid response
            print(f"Error fetching data from the API: {e}")
            self.rates = {}

    def convert(self, amount, base_currency, des_currency):
        if not self.rates:
            raise ValueError("Exchange rates data is unavailable.")
        
        if base_currency != 'EUR':
            amount = amount / self.rates.get(base_currency, 1)

        amount = round(amount * self.rates.get(des_currency, 1), 2)
        return amount

@app.route('/')
def index():
    converter = CurrencyConverter()
    currencies = list(converter.rates.keys()) if converter.rates else []
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form['amount']
    base_currency = request.form['base_currency']
    des_currency = request.form['des_currency']
    
    try:
        amount = float(amount)
        converter = CurrencyConverter()
        if converter.rates:
            converted_amount = converter.convert(amount, base_currency, des_currency)
            return jsonify({'success': True, 'converted_amount': converted_amount, 'amount': amount, 'base_currency': base_currency, 'des_currency': des_currency})
        else:
            return jsonify({'success': False, 'message': 'Exchange rates data is unavailable.'})
    except ValueError:
        return jsonify({'success': False, 'message': 'Please enter a valid amount!'})

if __name__ == '__main__':
    app.run(debug=True)
