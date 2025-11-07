// 빈티지 애니메 효과를 위한 타이핑 애니메이션
function _typeWriter(element, text, speed = 30) {
  let i = 0;
  element.innerHTML = '<span class="cursor-blink">▸</span> ';
  
  function _type() {
    if (i < text.length) {
      element.innerHTML = '<span class="cursor-blink">▸</span> ' + text.substring(0, i + 1);
      i++;
      setTimeout(_type, speed);
    } else {
      // 타이핑 완료 후 커서 깜빡임 추가
      element.innerHTML = text + ' <span class="cursor-blink">█</span>';
    }
  }
  
  _type();
}

// 레트로 사운드 효과 (선택적)
function _playRetroSound(type) {
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  const gainNode = audioContext.createGain();
  
  oscillator.connect(gainNode);
  gainNode.connect(audioContext.destination);
  
  if (type === 'send') {
    oscillator.frequency.value = 800;
    gainNode.gain.value = 0.1;
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.1);
  } else if (type === 'error') {
    oscillator.frequency.value = 200;
    gainNode.gain.value = 0.1;
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.2);
  }
}