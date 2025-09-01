document.addEventListener('DOMContentLoaded', () => {
  const checkBtn = document.getElementById('checkBtn');
  const newsInput = document.getElementById('newsInput');
  const resultDiv = document.getElementById('result');
  const spinner = document.getElementById('spinner');

  checkBtn.addEventListener('click', async () => {
    const newsText = newsInput.value.trim();

    if (!newsText) {
      alert('Please enter some news text!');
      return;
    }

    spinner.classList.remove('hidden');
    resultDiv.textContent = '';

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ news: newsText })
      });

      if (!response.ok) throw new Error(`Backend returned status ${response.status}`);

      const data = await response.json();
      spinner.classList.add('hidden');

      resultDiv.style.color =
        data.prediction === 'FAKE' ? '#e74c3c' :
        data.prediction === 'REAL' ? '#27ae60' : '#333';

      resultDiv.textContent = `Prediction: ${data.prediction}`;
    } catch (error) {
      spinner.classList.add('hidden');
      resultDiv.style.color = '#e67e22';
      resultDiv.textContent = `Error: ${error.message}`;
    }
  });
});
