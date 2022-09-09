class Solution:

    def salvePuzzle(self, init, targ):
        ''' 求解8数码问题
        参数：
        init - 初始状态 例如'123046758'
        targ - 目标状态 例如'012345678'
        返回值：
        clf - 由udlr组成的移动路径字符串
        '''

        def open_min(opl):  # 找到open列表中最小的一个
            k = opl[0]
            d = -1
            t = 0
            f_min = opl[0]['g'] + opl[0]['h']
            for i in opl:
                d = d + 1
                if i['g'] + i['h'] < f_min:
                    f_min = i['g'] + i['h']
                    k = i
                    t = d
            return k, t

        def find_fat(cll, f):  # 寻找父亲节点
            for i in cll:
                if i['ind'] == f:
                    return i

        def find_near(oc, node):  # 寻找邻近节点
            d = -1
            for i in oc:
                d = d + 1
                if i['val'] == node:
                    return d
            return -1

        start_node = init  # 开始节点

        end_node = targ  # 结束节点

        open_list = []  # open表

        close_list = []  # close表

        hx = self.calcDistH(start_node, end_node)  # h(x)

        # ind: 序号，当前点的序号 | g表示g(x)代数 | h表示h(x) | val表示值 | fat表示father指针 | pos表示(上u 下d 左l 右r)
        set1 = {'ind': 0, 'g': 0, 'h': hx, 'val': start_node, 'fat': -1, 'pos': ''}

        n = 0  # ind索引

        path_list = []  # 打印路径

        open_list.append(set1)  # 将开始节点添加到open_list

        best_set = {}  # 最好的字典

        best_node = ''  # 最好的节点

        index = 0  # 索引
        while n < 100000:

            best_set, index = open_min(open_list)  # 找到open_list最优的字典和索引

            best_node = best_set['val']  # 找到改最小字典的节点值

            if best_node == end_node:  # 如果最好的节点等于当前节点
                while True:  # 从终点开始逐步追踪父亲节点，一直找到开始节点
                    node_fat = best_set['fat']  # 找到父亲索引

                    path_list.append(best_set['pos'])  # 添加到路径列表中

                    if node_fat == -1:  # 一直找到开始节点
                        break

                    best_set = find_fat(close_list, node_fat)

            if path_list != []:  # 返回找到的结果路径，算法结束
                break

            del open_list[index]  # 将最小节点从open_list中删除

            close_list.append(best_set)  # 将最小节点从添加到close_list中

            ###  产生所有邻近节点
            fx = ['上', '下', '左', '右']

            for fxw in fx:  # 遍历最小节点所有的邻近节点
                index_0 = best_node.find('0')  # 找到0处的索引值

                index_row = int(index_0 / 3)  # 行
                indx_col = index_0 % 3  # 列

                if fxw == '上':  # 上移
                    index_row = index_row - 1
                if fxw == '下':  # 下移
                    index_row = index_row + 1
                if fxw == '左':  # 左移
                    indx_col = indx_col - 1
                if fxw == '右':  # 右移
                    indx_col = indx_col + 1

                # print('移动到的索引:',jh_index_0, '移动方向:',fxw, '行:', int(index_row), '列:', indx_col )

                if int(index_row) > 2 or int(index_row) < 0 or indx_col > 2 or indx_col < 0:  # 判断是否越界，即是否超出九宫格
                    continue

                jh_index_0 = 3 * int(index_row) + indx_col  # 移动之后的0的索引值

                near_node = self.moveMap(best_node, int(index_0), int(jh_index_0))  # 移动之后的邻近节点

                # g(n)是从开始结点到结点n的路径代价
                set2 = {'ind': 0, 'g': best_set['g'] + 1, 'h': 0, 'val': '', 'fat': best_set['ind'], 'pos': fxw}

                '''
                # 下面注释的代码本应当要实现以下功能：
                    + 如果该邻近节点在close_list中可以找到
                        + 因为节点相同，所以h(x)一样，则判断g(x)的大小进行操作 
                        + 这里的操作就是修改该节点的属性，g(x)和指向父亲的['fat']，再continue
                    + 如果该邻近节点在open_list中可以找到
                        + 因为节点相同，所以h(x)一样，则判断g(x)的大小进行操作 
                        + 这里的操作就是修改该节点的属性，g(x)和指向父亲的['fat']，再continue
                # 但是本人实力有限，实现不了。
                '''

                near_index = find_near(close_list, near_node)  # 在close_list找near_node的索引值

                if near_index != -1:  # 如果找到
                    '''
                    if set2['g'] < close_list[near_index]['g']:
                        close_list[near_index]['g'] = set2['g']
                        close_list[near_index]['fat'] = best_set['ind']
                    '''
                    continue

                near_index = find_near(open_list, near_node)  # 在open_list找near_node的索引值

                if near_index != -1:  # 如果找到
                    '''
                    if set2['g'] < open_list[near_index]['g']:
                        open_list[near_index]['g'] = set2['g']
                        open_list[near_index]['fat'] = best_set['ind']
                    '''
                    continue

                near_h = self.calcDistH(near_node, end_node)  # 计算h(x)
                n = n + 1
                set2['ind'] = n
                set2['h'] = near_h
                set2['val'] = near_node
                open_list.append(set2)  # 将节点m加入open_list中

        path_list.reverse()  # 逆序
        return ''.join(path_list)

    def calcDistH(self, src_map, dest_map):
        '''     启发式函数h(n)：是从结点n到目标结点的最小路径代价的估计值
        参数：
            src_map  - 当前8数码状态
            dest_map - 目标8数码状态
        返回值：
            clf - 当前状态到目标状态的启发式函数值
        '''
        sum = 0
        src_i = 0
        for i in src_map:  # 检索i
            src_i = src_i + 1
            dest_j = 0
            for j in dest_map:
                if i == '0':
                    break
                dest_j = dest_j + 1
                if i == j:
                    sum = sum + abs(src_i - dest_j)
        return sum

    def moveMap(self, cur_map, i, j):
        '''     状态转换（交换位置i和j）
        参数：
            cur_map - 当前8数码状态
            i - 当前8数码状态中空格0的位置索引
            j - 将空格0的位置i移动到位置j，位置j移动到位置i
        返回值：
            clf - 新的8数码状态
        '''
        i = int(i)
        j = int(j)
        cur_map = cur_map[:i] + cur_map[j] + cur_map[i + 1:]
        cur_map = cur_map[:j] + '0' + cur_map[j + 1:]
        return cur_map


solution = Solution()
# init - 初始状态
# targ - 目标状态
# path_list - 移动路径 例如 'lurddlurrulldrrdllurruldlu'
init = "623150478"
targ = "123456780"
path_list = solution.salvePuzzle(init, targ)
# print(path_list)
for i in range(0,len(path_list),5):
    print(path_list[i:i+5])
