import re

pattern = r'(?:你觉得)?选((?:[^还是]+?)(?:还是[^还是]+?)*)(?:还是[^还是]+?)?好?\??'

def extract_choices(text):
    # 匹配整个字符串
    match = re.match(pattern, text)
    if match:
        # 提取全部选项
        choices_text = match.group(1)
        # 提取每个选项
        choices = re.findall(r'[^还是]+', choices_text)
        return choices
    else:
        return []

# 测试字符串
test_strings = [
    "你觉得选苹果还是香蕉还是橘子好?",
    "选A还是B还是C还是D好?",
    "选这个还是那个还是另外一个?",
    "选xx还是xx还是xx还是xx"
]

# 提取并打印结果
for s in test_strings:
    choices = extract_choices(s)
    print(f"原字符串: {s}")
    print(f"提取的选择: {choices}")
    print("-" * 40)