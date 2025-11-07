class Chatbot:
  def __init__(self):
    self.responses = {
      # 인사
      "안녕": "안녕하세요! 😊 무엇을 도와드릴까요?",
      "안녕하세요": "안녕하세요! 😊 무엇을 도와드릴까요?",
      "하이": "하이! 👋 반가워요!",
      "hello": "Hi there! 👋 How can I help you?",
      "hi": "Hello! 😊 What can I do for you today?",
      
      # 안부
      "잘 지내?": "저는 프로그램이지만 물어봐 주셔서 감사해요! 당신은 어떠세요?",
      "어떻게 지내?": "잘 지내고 있어요! 😊 당신은 어떠신가요?",
      "how are you?": "I'm just a program, but thanks for asking! How about you?",
      "how are you": "I'm doing great! Thanks for asking! 😊",
      
      # 소개
      "이름이 뭐야?": "저는 AI 챗봇이에요. 여러분을 도와드리기 위해 만들어졌습니다! 🤖",
      "이름이 뭐야": "저는 AI 챗봇이에요. 여러분을 도와드리기 위해 만들어졌습니다! 🤖",
      "넌 누구야?": "저는 AI 챗봇입니다. 대화하고 질문에 답변하는 것을 좋아해요! 💬",
      "넌 누구야": "저는 AI 챗봇입니다. 대화하고 질문에 답변하는 것을 좋아해요! 💬",
      "what's your name?": "I'm an AI Chatbot! Nice to meet you! 🤖",
      "what's your name": "I'm an AI Chatbot! Nice to meet you! 🤖",
      "who are you?": "I'm an AI chatbot created to assist and chat with you! 💬",
      "who are you": "I'm an AI chatbot created to assist and chat with you! 💬",
      
      # 기능 소개
      "뭐 할 수 있어?": "간단한 대화를 나눌 수 있어요! 날씨, 취미, 일상 등에 대해 물어보세요! 💡",
      "뭐 할 수 있어": "간단한 대화를 나눌 수 있어요! 날씨, 취미, 일상 등에 대해 물어보세요! 💡",
      "무엇을 할 수 있어?": "대화를 나누고 질문에 답변할 수 있어요. 무엇이든 물어보세요! ✨",
      "what can you do?": "I can chat with you and answer various questions! Ask me anything! 💡",
      "what can you do": "I can chat with you and answer various questions! Ask me anything! 💡",
      
      # 날씨
      "날씨 어때?": "죄송해요, 실시간 날씨 정보는 제공하지 못해요. 날씨 앱을 확인해보세요! ☀️",
      "오늘 날씨": "죄송해요, 실시간 날씨 정보는 제공하지 못해요. 날씨 앱을 확인해보세요! ☀️",
      "날씨": "죄송해요, 실시간 날씨 정보는 제공하지 못해요. 날씨 앱을 확인해보세요! ☀️",
      
      # 시간
      "몇 시야?": "죄송해요, 현재 시간을 알려드릴 수 없어요. 기기의 시계를 확인해주세요! ⏰",
      "지금 몇 시?": "죄송해요, 현재 시간을 알려드릴 수 없어요. 기기의 시계를 확인해주세요! ⏰",
      "what time is it?": "Sorry, I can't tell you the current time. Please check your device! ⏰",
      
      # 감사 인사
      "고마워": "천만에요! 😊 또 질문이 있으시면 언제든지 물어보세요!",
      "고맙습니다": "천만에요! 😊 도움이 되어 기뻐요!",
      "감사합니다": "별말씀을요! 항상 도와드릴 준비가 되어 있어요! 🙏",
      "감사": "별말씀을요! 항상 도와드릴 준비가 되어 있어요! 🙏",
      "thanks": "You're welcome! Feel free to ask me anything! 😊",
      "thank you": "You're very welcome! Happy to help! 🙏",
      
      # 작별 인사
      "잘가": "안녕히 가세요! 좋은 하루 되세요! 👋",
      "안녕히 가세요": "안녕히 가세요! 좋은 하루 되세요! 👋",
      "바이": "바이! 또 만나요! 👋",
      "bye": "Goodbye! Have a great day! 👋",
      "goodbye": "Goodbye! See you next time! 👋",
      "see you": "See you! Take care! 👋",
      
      # 기분/감정
      "기분 좋아": "그렇다니 정말 기쁘네요! 😄",
      "기분 나빠": "어머, 무슨 일이 있으셨나요? 이야기 나누고 싶으시면 말씀해주세요. 🥺",
      "슬퍼": "힘내세요! 💪 언제나 좋은 일만 있을 순 없지만, 분명 더 나은 날이 올 거예요!",
      "행복해": "와! 정말 좋네요! 😄 그 행복이 계속되길 바랄게요!",
      
      # 농담/재미
      "농담해줘": "프로그래머가 술집에 갔어요. 맥주 한잔 주세요. 아니 두잔... 아니 false! 🍺😄",
      "재미있는 얘기": "왜 개발자는 안경을 쓸까요? C#를 못봐서요! 😎",
      "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
      
      # 칭찬
      "멋지다": "감사합니다! 😊 당신도 멋져요!",
      "대단해": "고마워요! 🙌 함께 대화하니 즐겁네요!",
      "최고야": "감사합니다! 😄 당신이 최고예요!",
      
      # 도움 요청
      "도와줘": "물론이죠! 무엇을 도와드릴까요? 🤗",
      "도움": "언제든지 도와드릴게요! 무엇이 필요하신가요? 💪",
      "help": "Of course! What do you need help with? 🤗",
      
      # 기타
      "ㅋㅋ": "ㅋㅋㅋ 재미있으시네요! 😄",
      "ㅎㅎ": "ㅎㅎ 즐거우시군요! 😊",
      "좋아": "좋아요! 👍",
      "싫어": "아쉽네요. 더 나은 도움을 드리지 못해 죄송해요. 😢",
      "yes": "Great! 👍",
      "no": "Okay, no problem! 👌",
      "ok": "Okay! 👌",
      "ㅇㅋ": "오케이! 👌"
    }

  def _get_response_internal(self, user_input):
    """사용자 입력에 대한 응답을 반환합니다."""
    user_input_lower = user_input.lower().strip()
    
    # 정확한 매칭 먼저 시도
    if user_input_lower in self.responses:
      return self.responses[user_input_lower]
    
    # 부분 매칭 시도 (키워드 포함)
    for key, value in self.responses.items():
      if key in user_input_lower or user_input_lower in key:
        return value
    
    # 매칭되는 것이 없을 때
    default_responses = [
      "죄송해요, 이해하지 못했어요. 다른 질문을 해주세요! 🤔",
      "음... 잘 모르겠어요. 다르게 질문해주실 수 있나요? 🙏",
      "아직 그 부분은 배우지 못했어요. 다른 것을 물어봐주세요! 📚",
      "흠... 이해가 안 가네요. 좀 더 자세히 말씀해주시겠어요? 🤷"
    ]
    import random
    return random.choice(default_responses)

# 싱글톤 인스턴스 생성
_chatbot_instance = Chatbot()

def get_response(user_input):
  """사용자 입력에 대한 챗봇 응답을 반환합니다."""
  return _chatbot_instance._get_response_internal(user_input)