# 选择词库
# 0: "默认", 1: "诗经", 2: "楚辞", 3: "论语",
# 4: "周易", 5: "唐诗", 6: "宋诗", 7: "宋词"
name_source = 4

# 姓，仅支持单姓
last_name = "甄"

# 不想要的字，结果中不会出现这些字
dislike_words = list(["丽", "离", "莉", "艳", "燕", "雁", "彦", "娜", "妃", "芬", "纷", "飞", "菲", "伶", "玲", "凌", "灵", "颖", "莹", "颖", "盈", "怡", "仪", "丛", "从", "露", "霜", "冰", "雪", "寒", "凝", "君", "晶", "蕊", "姬", "华", "笑", "超", "一", "斌", "梅", "鑫", "欣", "亮", "雅", "森", "振", "嘉", "哲", "志", "文", "颖", "明", "君", "芳", "娜", "刚", "静", "琴", "玲", "伟", "琳", "丹", "宇", "浩", "洪", "树", "永", "小", "昭", "立", "亚", "艾", "爱", "隘", "坷", "磊", "砾", "乐", "孕", "单", "嫘", "骊", "羚", "育", "陵", "媛", "熳", "奥", "宁", "媪", "崴", "囡", "南", "婺", "岫", "璧", "仝", "诞", "黝", "令", "焉", "毓", "婷", "晴", "瑶", "卢", "尔", "蜓", "傲", "婉", "容", "宛", "黑", "女", "鹳", "丫", "也", "娣", "嫒", "麟", "嫣", "尹", "山", "屹", "嵴", "幼", "幽", "引", "彤", "阿", "韦", "鸟", "螺", "黄", "烂", "男", "弟", "垚", "墁", "屿", "豆", "叆", "狁", "龙", "凤", "瑷", "稚", "胡", "六", "诺", "黟", "卿", "若", "真", "土", "野", "奴", "他", "田", "秋", "蔓", "涵", "香", "洁", "秀", "辰", "妤", "珍", "慧", "兰", "娜", "娥", "英", "屏", "眉", "彩", "枝", "霞", "黛", "梦", "欲", "越", "破", "光", "夜", "塊", "奠"])

# 需要的五行列表,不包含姓
wuxing_list = ["土火"]

# 最小笔画数, 需要避免9,19,20,34
min_stroke_count = 3

# 最大笔画数
max_stroke_count = 50

# 允许使用中吉，开启后将生成包含中吉配置的名字，生成的名字会更多
allow_general = False

# 是否开启三才五格
switch_wuge = True

# 是否筛选名字，仅输出名字库中存在的名字，可以过滤明显不合适的名字
name_validate = False

# 是否筛选性别，男/女，空则不筛选，仅当开启名字筛选时有效
gender = "女"

# 是否使用一般声调，默认使用好听的名字
allow_normal_shengdiao = False

##############################################################################################

# 填入姓名，查看三才五格配置，仅支持单姓复名
# 如果要起名，请保持该值为空
check_name = ""

# 是否显示名字来源
check_name_resource = True
