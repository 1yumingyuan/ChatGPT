import tkinter as tk

# 列表中存储的是90行诗及一些12字绝句
poems = [
    "心疼非病，病在无声。",
    "灵魂安宁，世界方明。",
    "笑语藏忧，悲欢并行。",
    "情绪无常，若潮起落。",
    "心绪如春，舞动轻轻。",
    "忧虑如秋，心叶落静。",
    "心海广阔，思绪浩渺。",
    "焦虑如风，吹动心潮。",
    "孤独如雪，覆盖心田。",
    "心痛如雨，独自承载。",
    # ...... 这里省略了部分诗句
    "心愿如云，轻舒密布。",
    "情感如山，高耸未摧。",
    "心灵如夜，静谧深邃。",
    "心力如日，照亮前途。",
    "心声如梦，映照现实。",
    "心境如河，流淌无息。",
    "心神如星，璀璨闪烁。",
    "心态如海，波澜壮阔。",
    "心中有光，照亮黑暗。",
    "心动如鹿，不易平息。",
    "心醉如酒，醉人心扉。",
    "心痒如羽，轻拂面颊。",
    "心难如谜，解不可破。",
    "心如冰凉，难以抚慰。",
    "心似火热，难以熄灭。",
    "心境如歌，曲折而美。",
    "心之所向，坚韧无比。",
    "心如明镜，映射真我。",
    "心健如铁，不轻易折。",
    "心健是福，祝君常欢。",
    "王者如狮，狮王之威。",
    "春风十里，不如你。",
    "千山鸟飞绝，万径人踪灭。",
    "孤舟蓑笠翁，独钓寒江雪。",
    "黄沙百战穿金甲，不破楼兰终不还。",
    "草长莺飞二月天，拂堤杨柳醉春烟。",
    "海上生明月，天涯共此时。",
    "青山依旧在，几度夕阳红。"
]

def create_app():
    # 创建窗口
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # 设置全屏

    # 创建并配置标签，用于显示诗句
    label = tk.Label(root, text="", font=("Helvetica", 24), wraplength=root.winfo_screenwidth())
    label.pack(expand=True)

    def update_poem():
        # 如果诗句列表为空，显示结束信息
        if not poems:
            label.config(text="诗句已经全部展示完毕")
            return
        # 取出并删除列表的第一个元素，然后显示在标签上
        poem = poems.pop(0)
        label.config(text=poem)
        # 5秒后更新诗句
        root.after(5000, update_poem)

    # 创建并配置退出按钮
    button = tk.Button(root, text="退出", command=root.destroy, font=("Helvetica", 24))
    button.pack()

    update_poem()  # 开始更新诗句

    # 开始主循环
    root.mainloop()

# 运行程序
create_app()
