window.onload = function ()
    {
    chrome.storage.local.get(['keyurl', 'keystatus'], function (result) {
        console.log(result.keyurl)
        console.log(result.keystatus)
        document.querySelector(".webname").textContent = result.keyurl
        if (result.keystatus == "benign") {
            status = "Safe"
            document.querySelector(".webstatus").textContent = status
        }else{
            status = "Malicious"
            document.querySelector(".webstatus").textContent = status
            document.querySelector(".webstatus").style.color = "red"
        }
    });
}

document.querySelectorAll(".devlink").forEach(function(a){
 a.onclick = function(){
    chrome.tabs.create({url:a.href});
 }
})