document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const type = document.getElementById('type').value;
    const status = document.getElementById('status').value;

    const response = await fetch('/wearables', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ type, status }),
    });

    const result = await response.json();
    alert(result.message);
});
