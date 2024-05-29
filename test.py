import os
import random
import datetime

# 生成随机的提交信息
def generate_commit_message():
    messages = [
        "Fix bug",
        "Add feature",
        "Refactor code",
        "Update documentation",
        "Optimize performance"
    ]
    return random.choice(messages)

# 生成随机的提交时间
def generate_commit_time():
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    return start_date + datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# 创建模拟提交历史
def create_fake_commits():
    num_commits = 100  # 生成的提交数量

    for i in range(num_commits):
        commit_message = generate_commit_message()
        commit_time = generate_commit_time().strftime('%Y-%m-%d %H:%M:%S')

        # 创建一个新文件，并添加到暂存区
        with open(f"file_{i}.txt", "w") as file:
            file.write(commit_message)
        os.system(f"git add file_{i}.txt")

        # 提交更改
        os.system(f"git commit --date='{commit_time}' -m '{commit_message}'")

# 主函数
def main():
    # 初始化Git仓库
    # os.system("git init")
    # 创建一些初始文件
    for i in range(5):
        with open(f"file_{i}.txt", "w") as file:
            file.write("Initial content")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
    os.system("git config --global user.eamil 'zhaozhongxiang@tju.edu.cn'")
    os.system("git config --global user.name yijiangqingfeng")

    # 生成假的提交历史
    create_fake_commits()

if __name__ == "__main__":
    main()
