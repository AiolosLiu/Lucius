var http = require('http');

var mAction = {
    doAction:function(at){
        var moveJson  = {"motion":at};
        var data      = JSON.stringify(moveJson);
        console.log(data);
        
        var option = {
            //host:'216.38.137.43',
            url:'http://53be1e93.ngrok.io',
            method:'POST',
            headers:{
             "Content-Type": 'application/json',
             "Content-Length": data.length,
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER"
            }
        };
        
        var req = http.request(option, function(res) {
            res.on("data",function (chunk) {
                console.log(chunk);
            });
        })
        req.write(data);
        req.end();
    }
}
module.exports=mAction;
mAction.doAction("1");
