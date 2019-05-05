chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        data = JSON.parse(xhttp.responseText)
        chrome.storage.local.set({"keyurl":request.urlinfo,"keystatus":data.status},function() {
            console.log('Value stored'+request.urlinfo);
        });
        if(data.status == "malicious"){
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                chrome.tabs.sendMessage(tabs[0].id, { ismal: true }, function () {
                     console.log("done");
                });
           });
        }    
    }
  };
  xhttp.open("GET", "http://127.0.0.1:5000/api?url="+request.urlinfo, true);
  xhttp.send();
});