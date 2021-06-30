# -*- coding: utf-8 -*-

import json
import numpy as np
import os
str1='D:\\20210508_C_S_I_DQ_10_TZ_08'
path = str1+'.json'
if(os.path.exists(str1)==0):
    os.mkdir(str1)
with open(path, 'r', encoding='utf8')as fp:  # 打开json文件
    json_data = json.load(fp)
    for count, L in enumerate(json_data):
        print(json_data[L]['filename'])
        filename = json_data[L]['filename'][0:-4]
        # 由于via标注的时候是所有图片的标签集中在一个json文件，我的目标是一个图片生成一个
        # 所以要把每个图片的名字保存下来
        region = json_data[L]['regions']
        test = []
        slot=[1,2,1,90]
        for K in region:
            reg = K['shape_attributes']
            point_X = reg['all_points_x']
            point_Y = reg['all_points_y']
            if(point_Y!=None):
                resultpos = list(zip(point_X, point_Y))
                resultpos = np.array(resultpos)
                resultpos = resultpos.tolist()
            # 为了跟labelme中的坐标相同， 对xy坐标先合成，转为numpy再转会List
                dict1 = {"name": "t_chart", "marks": resultpos}
                test.append(dict1)
                print('test=', test)
                one = {"objects": test,"slot": slot}
                #with open('D://res/' + filename + '.json', 'w', encoding='utf-8') as f:
                with open(str1 + '//'+filename + '.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(one, ensure_ascii=False, indent=1))  # 最后保持