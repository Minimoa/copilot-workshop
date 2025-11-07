function _sendMessage() {
  const userInput = document.getElementById('user-input').value;
  const chatContainer = document.getElementById('chat-container');

  if (userInput.trim() === '') {
    return;
  }

  // 사용자 메시지 추가
  const userMessageDiv = document.createElement('div');
  userMessageDiv.className = 'message user-message';
  userMessageDiv.innerHTML = `
    <div class="message-content">
      <div class="message-text">${_escapeHtml(userInput)}</div>
    </div>
  `;
  chatContainer.appendChild(userMessageDiv);

  // 입력 필드 초기화
  document.getElementById('user-input').value = '';
  
  // 스크롤을 아래로
  chatContainer.scrollTop = chatContainer.scrollHeight;

  // 로딩 메시지 표시
  const loadingDiv = document.createElement('div');
  loadingDiv.className = 'message bot-message loading';
  loadingDiv.innerHTML = `
    <div class="message-content">
      <div class="message-text">
        <span class="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
    </div>
  `;
  chatContainer.appendChild(loadingDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  // 서버로 요청
  fetch('/ask', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: userInput })
  })
  .then(response => response.json())
  .then(data => {
    // 로딩 메시지 제거
    loadingDiv.remove();
    
    // 봇 메시지 추가
    const botMessageDiv = document.createElement('div');
    botMessageDiv.className = 'message bot-message';
    botMessageDiv.innerHTML = `
      <div class="message-content">
        <div class="message-text">${_escapeHtml(data.response)}</div>
      </div>
    `;
    chatContainer.appendChild(botMessageDiv);
    
    // 스크롤을 아래로
    chatContainer.scrollTop = chatContainer.scrollHeight;
  })
  .catch(error => {
    console.error('Error:', error);
    loadingDiv.remove();
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'message bot-message error';
    errorDiv.innerHTML = `
      <div class="message-content">
        <div class="message-text">오류가 발생했습니다. 다시 시도해주세요.</div>
      </div>
    `;
    chatContainer.appendChild(errorDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  });
}

function _escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

document.getElementById('send-button').addEventListener('click', _sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    _sendMessage();
  }
});