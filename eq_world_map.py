# import plotly.express as px   #plotly.express给图表定义数据的最简单的方式之一，但在数据处理中并不是最佳的。
#
# from eq_explore_data import lons, lats
#
# fig = px.scatter(
#     x=lons,
#     y=lats,
#     labels={'x':'经度','y':'纬度'},
#     range_x = [-200,200],
#     range_y = [-90,90],
#     width=800,
#     height=800,
#     title = '全球地震散点图',
# )
# fig.write_html('global_earthquakes.html')
# fig.show()


## 标准答案
import json
import plotly.express as px
from 练习.pandas import pandas库 as pd

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
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

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=('经度', '纬度', '位置', '震级')
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-250, 250],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'

)

if __name__ == '__main__':  # 在模块是被直接运行的，则该语句下代码块被运行，
    print(mags[:5])  # 如果所在模块是被导入到其他的python脚本中运行的，则该语句下代码块不被运行。
    print(title[:5])
    print(lons[:5])
    print(lats[:5])
