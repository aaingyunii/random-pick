def random_pick(members):
    import random
    if not members:
        return "팀원 입력이 정상적이지 않습니다. 다시 실행하세요"

    presenter = random.choice(members)
    
    return f"발표자는 {presenter} 입니다" 

team_members = []

while True:
    member = input("팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):\n ")

    if not member:
        break

    team_members.append(member)

result = random_pick(team_members)
print(result)
    
