import json

# 探索数据的结构
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # json.load（）将数据转换成py能够处理的格式，这里是一个庞大的字典

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # json.dump（）接受一个Json数据对象和一个文件对象，并写入这个文件中。
    # indent=4 让dump()使用和数据结构匹配的缩进量来设置数据的格式



# 16.2.3创建地震列表
# dicts:字典
all_eq_dicts = all_eq_data['features']  # 提取features键相关联的数据，并将存储在all——all_eq_dicts
print(len(all_eq_dicts)) # 发生几次地震



# 16.2.4 提取震级
# mags = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)
#
# print(mags[:10])

# 16.2.5 提取位置数据
# 位置数据存储在"geometry"键下。
# 在"geometry"键关联的字典中,有一个"coordinates"键, 它关联到一个列表,而列表中的前两个值为经度和纬度。
# 下面演示了如何提取位置数据

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    x = lons,
    y = lats,
    labels = {'x': '经度', 'y': '纬度'}

print(mags[:10])
print(titles[:2])
print(lons[0:5])
print(lats[0:5])


import json

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:    #Ctrl + Shift + V    从最近的缓冲区粘贴
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])



