const groupName = JSON.parse(document.getElementById("group_name").textContent)
console.log("group name...", groupName)

var ws = new WebSocket('ws://' + window.location.host +'/ws/jwc/' + groupName +'/')

ws.onopen = function() {
    console.log('webSocket Open..')
};

ws.onclose = function(event) {
    console.error('Chat socket closed')
};

ws.onmessage = function(event) {
    console.log('message received from server...', event)
    const data = JSON.parse(event.data)
    // document.querySelector("#my-chats").appendChild('')
    // document.querySelector("#chat").value += (data.message + '\n')
    // $("#chats").load(window.location.href + " chats", function() { console.log("loaded") })
    location.reload(true);

};

document.getElementById("message-submit").onclick = function(event) {
    const messageInputDom = document.getElementById("message")
    const message = messageInputDom.value
    ws.send(JSON.stringify({
        'msg' : message
    }))
    messageInputDom.value = ''
}


