# 这里有两部分，一部分是真实数据，另一部分是虚拟数据，这里主要是进行数据处理
import numpy as np
import math

class BlockSrht():
    @staticmethod
    def genBlockData(data, blocks_num):
        m,n = data.shape
        blocks = np.array_split(data, blocks_num, axis=1)
        padded_blocks = []  # 创建一个空的列表来保存填充后的块
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
            padded_blocks.append(block)  # 将填充后的块添加到列表中
        print("blocks:", padded_blocks)  # 输出填充后的块
        return padded_blocks  # 返回填充后的块
    @staticmethod
    def getTrace(data):
        imp_num = np.sum(np.abs(data))
        return imp_num
    
    @staticmethod
    def select_columns(blocks, k):
        # 计算每个块的元素和
        block_sums = [np.sum(block) for block in blocks]
        print("block_sums: ", block_sums)
        total_sum = np.sum(block_sums)

        # 根据元素和的大小来确定每个块抽取的列数
        block_cols = [int(np.round(block_sum / total_sum * k)) for block_sum in block_sums]
        print("block_cols: ", block_cols)
        # 对每个块进行随机不放回的抽取
        selected_columns = []
        for block, cols in zip(blocks, block_cols):
            if cols > 0:
                indices = np.random.choice(block.shape[1], cols, replace=False)
                print("indices: ",indices)
                selected_columns.append(block[:, indices])
                
        # 将所有选中的列合并成一个大的数组
        result = np.concatenate(selected_columns, axis=1)

        return result
    
    
if __name__ == '__main__':
    # 创建一个矩阵A
    A = np.array([[1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18]])
    matrix = np.random.random((3, 10))
    blocks = BlockSrht.genBlockData(matrix, 2)
    blocks = np.array(blocks)
    print("blocks.shape", len(blocks))
    
    imp_num = BlockSrht.getTrace(blocks)
    print("imp_num: ", imp_num)
    
    result = BlockSrht.select_columns(blocks, 3)
    print(result)
