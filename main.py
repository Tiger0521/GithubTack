import requests
import sys

# 接受Github用户名参数的函数，用来获取并打印该用户的活动
def fetch_github_events(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Accept': 'application/vnd.github.v3+json'}   # 设置请求头，告诉Github API我们期望的响应格式为JSON
    response = requests.get(url, headers=headers)   # 发起GET请求，获取响应
    if response.status_code != 200:   # 如果响应状态码不是200，说明请求失败，打印错误信息并退出程序
        print(f"Failed to fetch events for {username}. Error: {response.status_code}")
        return
    events = response.json()   # 解析JSON响应内容
    if not events:
        print(f"No events found for {username}.")
        return   # 如果事件列表为空，说明该用户没有任何活动，退出程序
    for event in events:   # 遍历事件列表，打印每个事件的类型和时间
        event_type = event['type']
        event_time = event['created_at']
        print(f"{username} {event_type} at {event_time}")

# 主函数入口
if __name__ == '__main__':
    if len(sys.argv) != 2:   # 如果命令行参数个数不等于2，说明没有传入用户名参数，打印错误信息并退出程序
        print("Please provide a Github username as an argument.")
        sys.exit(1)

    username = sys.argv[1]   # 获取用户名参数
    fetch_github_events(username)   # 调用获取并打印用户活动的函数