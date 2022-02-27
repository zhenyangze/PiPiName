all_wuxing_list = []
with open('data/wuxing.dat', encoding='utf-8') as f:
    for line in f:
        data = line.split(',')
        word = data[0]
        wuxing = data[2]
        all_wuxing_list[word] = wuxing

def checkNameWuxing(name, wuxing_list):
    nameWuxing = ""
    for item in name:
        nameWuxing = nameWuxing + all_wuxing_list.get(item, "")
    return nameWuxing in wuxing_list
