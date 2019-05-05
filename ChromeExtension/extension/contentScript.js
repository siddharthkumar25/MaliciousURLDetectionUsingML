window.onload = function () {
    
    let url = window.location.href
    chrome.runtime.sendMessage({urlinfo:url})

    chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
      console.log(request.ismal)  
      if(request.ismal==true){
        
          
          alert("This Site May Contain Malicious Content")
        }
      });

}

