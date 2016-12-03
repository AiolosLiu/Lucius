var http = require('http');

var mAction = {
    doAction:function(at){
        var moveJson  = {"motion":at};
        var data      = JSON.stringify(moveJson);
        console.log(data);
        
        var option = {
            host:'greencloud.itu.edu',
            port:'8080',
            path:'/CloudServerInterface/v2/hackathon/post',
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
        console.log("mAction done");
    }
}
module.exports=mAction;
