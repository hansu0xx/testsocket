document.addEventListener('DOMContentLoaded', (event) => {
    
    const socket = io();

    // Listen for 'trading_data_update' events from the server
    socket.on('trading_data_update', function(data) {
        

console.log(data)
document.getElementById("message").innerText = data.time;
    });

    // You can add other Socket.IO events here if needed (e.g., 'connect', 'disconnect')
    socket.on('connect', () => {
        console.log('Connected to Socket.IO server');
    });

    socket.on('disconnect', (reason) => {
        console.log('Disconnected from Socket.IO server', reason);
    });
});
