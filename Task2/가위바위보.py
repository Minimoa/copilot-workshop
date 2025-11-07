import random
from itertools import count

def determine_winner(user_choice, computer_choice):
    """사용자와 컴퓨터의 선택을 비교하여 승패를 결정하는 함수"""
    if user_choice == computer_choice:
        return "Its a tie!"
    
    # 각 선택이 이길 수 있는 상대들
    winning_combinations = {
        "가위": ["보", "도마뱀"],      # Scissors cuts Paper, decapitates Lizard
        "바위": ["가위", "도마뱀"],    # Rock crushes Scissors, crushes Lizard
        "보": ["바위", "스팍"],        # Paper covers Rock, disproves Spock
        "도마뱀": ["보", "스팍"],      # Lizard eats Paper, poisons Spock
        "스팍": ["바위", "가위"]       # Spock vaporizes Rock, smashes Scissors
    }
    
    if computer_choice in winning_combinations[user_choice]:
        return "You Win!"
    else:
        return "You lose"

def play_game():
    """가위바위보 게임 메인 함수"""
    choices = ["가위", "바위", "보", "도마뱀", "스팍"]
    
    print("=== 가위바위보 게임 (Lizard & Spock 포함) ===")
    print("선택: 가위, 바위, 보, 도마뱀, 스팍 | 종료: exit")
    print()
    
    for _ in count():
        # 사용자 입력
        user_choice = input("당신의 선택 (종료하려면 'exit' 입력): ").strip()
        
        # 종료 조건
        if user_choice.strip().lower() == "exit":
            print("게임을 종료합니다. 감사합니다!")
            break
        
        # 유효한 입력인지 확인
        if user_choice not in choices:
            print("잘못된 입력입니다. '가위', '바위', '보', '도마뱀', '스팍' 중 하나를 입력하세요.")
            continue
        
        # 컴퓨터 선택
        computer_choice = random.choice(choices)
        
        # 결과 출력
        print(f"컴퓨터의 선택: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    play_game()
