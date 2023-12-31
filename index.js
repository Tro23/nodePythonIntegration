const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000

function start( ){
    app.get('/', (req, res) => {
 
        //response write
        //res.write("Streamer Engine is churning data... please wait for the results");
        
        var dataToSend;
        // spawn new child process to call the python script
        const python = spawn('python', ['streamer_model.py']);
        // collect data from script
        python.stdout.on('data', function (data) {
         console.log('Pipe data from python script ...');
         dataToSend = data.toString();
        });
        // in close event we are sure that the stream from child process is closed
        python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to the browser
        res.send(dataToSend)
        });
        
       })
       app.listen(port, () => console.log(`Example app listening on port 
       ${port}!`))
}

module.exports = start;   // server as a module
