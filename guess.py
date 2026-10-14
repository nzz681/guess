import random

def main():
    # 随机生成1~100整数
    secret_num = random.randint(1, 100)
    count = 0
    print("====猜数字小游戏====")
    print("系统已经生成1-100之间数字，请开始猜测！")
    while True:
        try:
            user_input = input("请输入你猜的数字：")
            guess = int(user_input)
            count += 1
            if guess > secret_num:
                print("大了")
            elif guess < secret_num:
                print("小了")
            else:
                print(f"恭喜猜中！你一共猜了{count}次")
                break
        except ValueError:
            print("输入不是有效数字，请重新输入！")

if __name__ == "__main__":
    main()