var http = require('http');

var findAction = {
    find:function(pname){
        var nameJson = {"pname":pname};
        var data     = JSON.stringify(nameJson);
        console.log(data);
        var option   = {
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
            res.setEncoding('UTF-8');
            res.on('data', function (chunk) {
                console.log(chunk);
                var da2= JSON.parse(chunk);
                console.log(da2.result);
            });
        });
        req.write(data + "\n");

        req.end();
        console.log("find done")
    }
}
module.exports=findAction;
