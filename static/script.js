document.getElementById('convertForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const amount = document.getElementById('amount').value;
    const base_currency = document.getElementById('base_currency').value;
    const des_currency = document.getElementById('des_currency').value;

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `amount=${amount}&base_currency=${base_currency}&des_currency=${des_currency}`
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.success) {
            resultDiv.style.backgroundColor = '#32CD32'; // Success Green
            resultDiv.innerHTML = `${data.amount} ${data.base_currency} = ${data.converted_amount} ${data.des_currency}`;
        } else {
            resultDiv.style.backgroundColor = '#FF6347'; // Error Red
            resultDiv.innerHTML = data.message;
        }
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
