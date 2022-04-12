def add(num1, num2):
    return num1 + num2


addition = lambda num1, num2: num1 + num2


savings =  [234., 555., 674., 78.]

lambda_bonus = list(map(lambda x: x * 1.1, savings))

loop_bonus = []
for account_balance in savings:
    loop_bonus.append(account_balance * 1.1)

print(loop_bonus)