import json
import re

import opencc

from name import Name
from stroke_number import get_stroke_number
from config import switch_wuge

# 简体转繁体
s2tConverter = opencc.OpenCC('s2t.json')
# 繁体转简体
t2sConverter = opencc.OpenCC('t2s.json')

fuxingList = ["欧阳", "太史", "端木", "上官", "司马", "东方", "独孤", "南宫", "万俟", "闻人", "夏侯", "诸葛", "尉迟", "公羊", "赫连", "澹台", "皇甫", "宗政", "濮阳", "公冶", "太叔", "申屠", "公孙", "慕容", "仲孙", "钟离", "长孙", "宇文", "司徒", "鲜于", "司空", "闾丘", "子车", "亓官", "司寇", "巫马", "公西", "颛孙", "壤驷", "公良", "漆雕", "乐正", "宰父", "谷梁", "拓跋", "夹谷", "轩辕", "令狐", "段干", "百里", "呼延", "东郭", "南门", "羊舌", "微生", "公户", "公玉", "公仪", "梁丘", "公仲", "公上", "公门", "公山", "公坚", "左丘", "公伯", "西门", "公祖", "第五", "公乘", "贯丘", "公皙", "南荣", "东里", "东宫", "仲长", "子书", "子桑", "即墨", "达奚", "褚师"]


def get_source(source, validate, stroke_list):
    exist_name = dict()
    if validate:
        print('>>加载名字库...')
        get_name_valid('Chinese_Names', exist_name)

    names = set()
    # 默认
    if source == 0:
        print('>>加载全量姓名库...')
        get_name_dat('Chinese_Names', names, stroke_list)
    # 诗经
    elif source == 1:
        print('>>加载诗经...')
        get_name_json('诗经', names, 'content', stroke_list)
    # 楚辞
    elif source == 2:
        print('>>加载楚辞...')
        get_name_txt('楚辞', names, stroke_list)
    # 论语
    elif source == 3:
        print('>>加载论语...')
        get_name_json('论语', names, 'paragraphs', stroke_list)
    # 周易
    elif source == 4:
        print('>>加载周易...')
        get_name_txt('周易', names, stroke_list)
    # 唐诗
    elif source == 5:
        print('>>加载唐诗...')
        for i in range(0, 58000, 1000):
            get_name_json('唐诗/poet.tang.' + str(i), names, 'paragraphs', stroke_list)
    # 宋诗
    elif source == 6:
        print('>>加载宋诗...')
        for i in range(0, 255000, 1000):
            get_name_json('宋诗/poet.song.' + str(i), names, 'paragraphs', stroke_list)
    # 宋词
    elif source == 7:
        print('>>加载宋词...')
        for i in range(0, 22000, 1000):
            get_name_json('宋词/ci.song.' + str(i), names, 'paragraphs', stroke_list)
    else:
        print('词库号输入错误')

    print('>>筛选名字...')
    # 检查名字是否存在并添加性别
    if validate:
        if source != 0:
            names = get_intersect(names, exist_name)

    return names


def get_intersect(names, exist_name):
    result = set()
    for i in names:
        if i.first_name in exist_name.keys():
            i.gender = exist_name[i.first_name]
            result.add(i)
    return result


# 加载名字库
def get_name_valid(path, exist_names):
    with open('data/' + path + '.dat', encoding='utf-8') as f:
        for line in f:
            data = line.split(',')
            xing = data[0][:2]
            if xing in fuxingList:
                name = data[0][2:]
            else:
                name = data[0][1:]
            gender = data[1].replace('\n', '')
            if name in exist_names:
                if gender != exist_names.get(name) or gender == '未知':
                    exist_names[name] = '双'
            else:
                exist_names[name] = gender


def get_name_dat(path, names, stroke_list):
    sameName = set()
    with open('data/' + path + '.dat', encoding='utf-8') as f:
        for line in f:
            data = line.split(',')
            xing = data[0][:2]
            if xing in fuxingList:
                name = data[0][2:]
            else:
                name = data[0][1:]


            if name in sameName:
                continue
            sameName.add(name)
            # 转繁体
            # name = s2tConverter.convert(name)
            gender = data[1].strip()
            if len(name) == 2:
                if not switch_wuge:
                    names.add(Name(name, '', gender))
                else: 
                    # 转换笔画数
                    strokes = list()
                    strokes.append(get_stroke_number(name[0]))
                    strokes.append(get_stroke_number(name[1]))
                    # 判断是否包含指定笔画数
                    for stroke in stroke_list:
                        if stroke[0] == strokes[0] and stroke[1] == strokes[1]:
                            names.add(Name(name, '', gender))


def get_name_txt(path, names, stroke_list):
    with open('data/' + path + '.txt', encoding='utf-8') as f:
        line_list = f.readlines()
        size = len(line_list)
        progress = 0
        for i in range(0, size):
            # 生成进度
            if (i + 1) * 100 / size - progress >= 10:
                progress += 10
                print('>>正在生成名字...' + str(progress) + '%')
            # 转繁体
            string = s2tConverter.convert(line_list[i])
            if re.search(r'\w', string) is None:
                continue
            string_list = re.split('！？，。,.?! \n', string)
            check_and_add_names(names, string_list, stroke_list)


def get_name_json(path, names, column, stroke_list):
    with open('data/' + path + '.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        size = len(data)
        progress = 0
        for j in range(0, size):
            # 生成进度
            if (j + 1) * 100 / size - progress >= 10:
                progress += 10
                print('>>正在生成名字...' + str(progress) + '%')
            for string in data[j][column]:
                # 转繁体
                string = s2tConverter.convert(string)
                string_list = re.split('！？，。,.?! \n', string)
                check_and_add_names(names, string_list, stroke_list)


def check_and_add_names(names, string_list, stroke_list):
    for sentence in string_list:
        sentence = sentence.strip()
        # 转换笔画数
        strokes = list()
        wordList = list()
        for ch in sentence:
            if is_chinese(ch):
                wordList.append(ch)
                strokes.append(get_stroke_number(ch))
            else:
                strokes.append(0)
        # 判断是否包含指定笔画数
        if not switch_wuge:
            for k1, v1 in enumerate(wordList):
                for k2, v2 in enumerate(wordList):
                    if k1 == k2 or v1 == v2:
                        continue
                    names.add(Name(v1 + v2, sentence, ''))
        else:
            for stroke in stroke_list:
                if stroke[0] in strokes and stroke[1] in strokes:
                    index0 = strokes.index(stroke[0])
                    index1 = strokes.index(stroke[1])
                    if index0 < index1:
                        name0 = sentence[index0]
                        name1 = sentence[index1]
                        names.add(Name(name0 + name1, sentence, ''))

# 判断是否为汉字
def is_chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def check_resource(name):
    if len(name) != 3:
        return
    print('正在生成名字来源...\n')
    check_name_json('诗经', name, 'content')
    check_name_txt('楚辞', name)
    check_name_json('论语', name, 'paragraphs')
    check_name_txt('周易', name)
    for i in range(0, 58000, 1000):
        check_name_json('唐诗/poet.tang.' + str(i), name, 'paragraphs')
    for i in range(0, 255000, 1000):
        check_name_json('宋诗/poet.song.' + str(i), name, 'paragraphs')
    for i in range(0, 22000, 1000):
        check_name_json('宋词/ci.song.' + str(i), name, 'paragraphs')


def check_name_json(path, name, column):
    with open('data/' + path + '.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        size = len(data)
        for i in range(0, size):
            poem = data[i]
            for string in poem[column]:
                string_list = re.split('！？，。,.?! \n', string)
                title = path
                if path == '诗经':
                    title = '诗经 ' + poem['title'] + ' ' + poem['chapter'] + ' ' + poem['section']
                elif path == '论语':
                    title = '论语 ' + poem['chapter']
                elif path.startswith('唐诗'):
                    title = '唐诗 ' + poem['title'] + ' ' + poem['author']
                elif path.startswith('宋诗'):
                    title = '宋诗 ' + poem['title'] + ' ' + poem['author']
                elif path.startswith('宋词'):
                    title = '宋词 ' + poem['rhythmic'] + ' ' + poem['author']
                check_name_resource(title, name, string_list)


def check_name_txt(path, name):
    with open('data/' + path + '.txt', encoding='utf-8') as f:
        line_list = f.readlines()
        size = len(line_list)
        for i in range(0, size):
            if re.search(r'\w', line_list[i]) is None:
                continue
            string_list = re.split('！？，。,.?! \n', line_list[i])
            check_name_resource(path, name, string_list)


def check_name_resource(title, name, string_list):
    for sentence in string_list:
        if title.startswith('唐诗') or title.startswith('宋诗'):
            # 转简体
            title = t2sConverter.convert(title)
            sentence = t2sConverter.convert(sentence)
        if name[1] in sentence and name[2] in sentence:
            index0 = sentence.index(name[1])
            index1 = sentence.index(name[2])
            if index0 < index1:
                print(title)
                print(sentence.strip().replace(name[1], '「' + name[1] + '」') \
                      .replace(name[2], '「' + name[2] + '」') + '\n')
