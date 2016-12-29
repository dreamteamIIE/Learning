/**
 * Created by wuzewei on 16/12/29.
 */

//console.log("hello world");
//phantom.exit();

// 网页截图
//var page = require('webpage').create();
//page.open('http://www.baidu.com',function(status) {
//    console.log('Status: ' + status);
//    if(status == 'success')
//    {
//        page.render('example.png');
//    }
//    phantom.exit();
//});


// 测试网页加载速度
//var page = require('webpage').create(),
//    system = require('system'),
//    t, address;
//
//if (system.args.length == 1) {
//    console.log('Usage: loadspeed.js <some URL>');
//    phantom.exit();
//}
//
//t = Date.now();
//address = system.args[1];
//page.open(address, function(status){
//    if (status != 'success') {
//        console.log('Fail to load the address');
//    }
//    else {
//        t = Date.now() -t ;
//        console.log('Loading ' + system.args[1]);
//        console.log('Loading time ' + t + ' msec');
//    }
//    phantom.exit();
//})


// 返回百度title
//var url = 'http://www.baidu.com';
//var page = require('webpage').create();
//page.open(url, function(status){
//    var title = page.evaluate(function(){
//        return document.title;
//    });
//    console.log('Page title is '+title);
//    console.log(page);
//    phantom.exit();
//});


// 输出控制台消息
//var url = "http://www.baidu.com";
//var page = require('webpage').create();
//page.onConsoleMessage = function(msg){
//    console.log(msg);
//};
//page.open(url, function(status){
//    page.evaluate(function(status){
//        console.log(document.title);
//    });
//    phantom.exit();
//});

// 输出网页为pdf
//var url = 'http://www.baidu.com'
//var page = require('webpage').create();
//page.open(url, function(status){
//   page.render('baidu.pdf');
//});
//phantom.exit();


//// 网络监听
//var url = 'http://www.cuiqingcai.com';
//var page = require('webpage').create();
//page.onResourceRequested = function(request){
//    console.log('Request: ' + JSON.stringify(request,undefined,4));
//};
//page.onResourceReceived = function (response){
//    console.log('Receive: ' + JSON.stringify(response, undefined, 4));
//};
//page.open(url);
//phantom.exit();


////页面自动化处理
//var page = require('webpage').create();
//console.log('The default usr agent is :' + page.settings.userAgent);
//page.settings.userAgent = 'SpecialAgent';
//page.open('http://www.httpuseragent.org',function(status){
//    if (status != 'success') {
//        console.log('Unable to access network');
//    }
//    else {
//        var ua = page.evaluate(function(){
//            return document.getElementById('myagent').textContent;
//        });
//        console.log(ua);
//    }
//    phantom.exit();
//});

