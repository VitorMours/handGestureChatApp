let socketio = io();

const createMessage = (user, message) => {
  const content = 
  `
    <div clas="text">
    <span><strong>${user}:</strong> ${message}</span>
    <span class="timestamp">${new Date().toLocaleString()}</span>
    </div>
  `;
  return content;
}

const sendMessage = () => {
  message = document.getElementById("mensagem");
  if(message.value != ""){
    socketio.emit("message", {data: message.value});
    message.value = "";
  }
};


socketio.on("connect", () => {});

socketio.on("message", (user, message) => {
  const newMessage = createMessage(user, message);
  const messageContainer = document.getElementById("chat-area")
  messageContainer.innerHTML += newMessage;
});

document.getElementById("form-mensagem").addEventListener("submit", (e) => {
  e.preventDefault();
  sendMessage();
});