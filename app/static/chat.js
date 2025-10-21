(function(){
  const messagesEl = document.getElementById('messages');
  const input = document.getElementById('msgInput');
  const btn = document.getElementById('sendBtn');
  const status = document.getElementById('status');

  // create client id
  const clientId = 'client-' + Math.random().toString(36).slice(2, 9);
  const wsUrl = `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/${clientId}`;
  const ws = new WebSocket(wsUrl);

  function addMessage(text, who='bot') {
    const div = document.createElement('div');
    div.className = 'message ' + (who === 'user' ? 'user' : 'bot');
    div.innerText = text;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  ws.onopen = () => {
    status.innerText = 'connected';
    addMessage('Connected to server — say hi!', 'bot');
  };
  ws.onclose = () => {
    status.innerText = 'disconnected';
    addMessage('Disconnected from server', 'bot');
  };
  ws.onmessage = (ev) => {
    try {
      const data = JSON.parse(ev.data);
      if (data.sender === 'bot') {
        addMessage(data.message, 'bot');
      }
    } catch(e) {
      console.error('invalid msg', e);
    }
  };

  btn.addEventListener('click', send);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') send();
  });

  function send() {
    const text = input.value.trim();
    if (!text) return;
    // show user's message
    addMessage(text, 'user');
    // send to server
    ws.send(JSON.stringify({ message: text }));
    input.value = '';
    input.focus();
  }
})();


