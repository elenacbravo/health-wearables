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

    document.getElementById('type').value = '';
    document.getElementById('status').value = '';
});


function notifyEvent(event) {
    const eventList = document.getElementById('event-list');
    const listItem = document.createElement('li');
    listItem.textContent = `Event: ${event.type}, Data: ${JSON.stringify(event.data)}`;
    eventList.appendChild(listItem);
}


setInterval(() => {
    const abnormalEvent = {
        type: "abnormal_heart_rate",
        data: { heart_rate: 110 }
    };
    notifyEvent(abnormalEvent);
}, 10000); 
