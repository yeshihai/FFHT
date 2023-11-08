# 这里有两部分，一部分是真实数据，另一部分是虚拟数据，这里主要是进行数据处理
import numpy as np
import math

class BlockSrht():
    @staticmethod
    def genBlockData(data, blocks_num):
        m,n = data.shape
        blocks = np.array_split(data, blocks_num, axis=1)
        for i, block in enumerate(blocks):
            # 计算需要填充的列数
            cols = block.shape[1]
            next_power_of_2 = 2**np.ceil(np.log2(cols))
            padding_cols = int(next_power_of_2 - cols)
            # 使用0进行填充
            if padding_cols > 0:
                block = np.pad(block, ((0, 0), (0, padding_cols)), 'constant', constant_values=0)
            # 输出处理后的块
            print(f"Block {i+1}:")
            print(block)
            print("block.shape:", block.shape)
        return blocks
    @staticmethod
    def getTrace(data):
        imp_num = np.sum(np.abs(data))
        return imp_num
    
    
if __name__ == '__main__':
    # 创建一个矩阵A
    A = np.array([[1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18]])
    matrix = np.random.random((3, 10))
    blocks = BlockSrht.genBlockData(matrix, 2)
    print("blocks.shape", len(blocks))
    
    imp_num = BlockSrht.getTrace(blocks)
    print("imp_num: ", imp_num)
