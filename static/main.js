let socket = io();
socket.on("connect", () => {
  socket.emit("my event", {data: "Conected to the channel"})
});