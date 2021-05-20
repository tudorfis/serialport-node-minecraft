var SerialPort = require('serialport');
// var io = require('socket.io').listen(3000);

var serialPort = new SerialPort("COM8", {
    baudRate: 9600,
    parser: new SerialPort.parsers.Readline("\n")
}, true);

// io.sockets.on('connection', function(socket){
//     socket.on('message', function(msg){
//         console.log(msg);
//     });

//     socket.on('disconnected', function(){
//         console.log('disconnected');
//     });
// });

// var clearData = "";
// var readData = "";

serialPort.on('open',function(){
    console.log('open');
    
    serialPort.on('data', function(data){
        console.log(data);
        // readData += data.toString();
        // io.sockets.emit('message',data);
    });
});