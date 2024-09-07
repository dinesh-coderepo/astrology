document.addEventListener('DOMContentLoaded', () => {
    const zodiacForm = document.getElementById('zodiacForm');
    const resultDiv = document.getElementById('result');
    const zodiacSymbolElement = document.getElementById('zodiacSymbol');
    const zodiacSignElement = document.getElementById('zodiacSign');
    const zodiacInfoElement = document.getElementById('zodiacInfo');
    const dailyBenefitElement = document.getElementById('dailyBenefit');

    zodiacForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const birthDate = document.getElementById('birthDate').value;
        const zodiacType = document.getElementById('zodiacType').value;

        try {
            const response = await fetch('/get_zodiac', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ birthDate, zodiacType }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            zodiacSymbolElement.textContent = data.symbol;
            zodiacSignElement.textContent = `${data.sign} (${data.type.charAt(0).toUpperCase() + data.type.slice(1)})`;
            zodiacInfoElement.textContent = data.info;
            dailyBenefitElement.textContent = data.dailyBenefit;
            resultDiv.classList.remove('hidden');
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
});
