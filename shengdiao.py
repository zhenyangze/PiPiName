from pypinyin import pinyin, Style,lazy_pinyin

# 1、平仄平、仄平平、仄仄平
# 2、平平仄、平仄仄、仄平仄
# 3、平平平、仄仄仄

shengdiao_list = {
    '1': "平",
    '2': "平",
    '3': "仄",
    '4': "仄"
}

good_shengdiao = ['平仄平', '仄平平', '仄仄平']
normal_shengdiao = ['平平仄', '平仄仄', '仄平仄']
bad_shengdiao = ['平平平', '仄仄仄']

def checkNameShengdiao(name, allow_normal_shengdiao = False):
    shengdiaoList = lazy_pinyin(name, style=Style.TONE3)
    shengdiaoName = ''
    for i in shengdiaoList:
        shengdiao = i[-1]
        shengdiaoName += shengdiao_list[shengdiao]

    if shengdiaoName in good_shengdiao:
        return True
    if allow_normal_shengdiao and shengdiaoName in normal_shengdiao:
        return True
    return False
