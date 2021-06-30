# -*- coding: utf-8 -*-

import json
import numpy as np
import os
str1='D:\\20210508_C_S_I_DQ_10_TZ_08'
path = str1+'.json'
if(os.path.exists(str1)==0):
    os.mkdir(str1)
slot1=[]
n=0
with open(path, 'r', encoding='utf8')as fp:  # 打开json文件
    json_data = json.load(fp)
    for count, L in enumerate(json_data):
        print(json_data[L]['filename'])
        filename = json_data[L]['filename'][0:-4]
        # 由于via标注的时候是所有图片的标签集中在一个json文件，我的目标是一个图片生成一个
        # 所以要把每个图片的名字保存下来
        region = json_data[L]['regions']
        test = []
        type=['0']
        for K in region:
            reg = K['shape_attributes']
            point_X = reg['all_points_x']
            point_Y = reg['all_points_y']
            ps_style=K['region_attributes']
            style=ps_style['style of parking slot']
            if(style=="T" or "I" or "U"):
                angle=90
            else:
                angle=45
            if(point_X!=None):
                resultpos = list(zip(point_X, point_Y))
                #resultpos=list(zip(resultpos[0],resultpos[1]))
                src=resultpos[1]
                dst=((resultpos[0][0]+resultpos[2][0])/2,(resultpos[0][1]+resultpos[2][1])/2)
                #dst=resultpos[0]
                resultpos = np.append(src, dst)
                resultpos=np.append(resultpos,0)
                resultpos = np.array(resultpos*1.0)
                resultpos = resultpos.tolist()
            # 为了跟labelme中的坐标相同， 对xy坐标先合成，转为numpy再转会List
                #dict1 = {"marks": resultpos}
                test.append(resultpos)
                print('test=', test)
                one = {"marks": test}
                n=n+1
                #with open('D://res/' + filename + '.json', 'w', encoding='utf-8') as f:
        # count1 = int(len(one['marks']))
        # count2=int((len(one['marks']))/2)
            #for i in range(0,count1):
        for j in range(1,n,2):
            slot= [j, j + 1, 1, angle]
            #slot1 = np.append(slot1, slot)
            slot1.append(slot)
            slot1 = np.array(slot1)
                #print(slot1)
        #if(slot!=None):
            slot1=slot1.tolist()
            one1={"slot":slot1}
            #one2 = dict( one.items() + one1.items())
            one2 = dict(one, **one1)
            path1 = str1 + '//' + filename + '.json'
            with open(path1, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(one2, ensure_ascii=False, indent=1))  # 最后保持
        n = 0
        slot1 = []
