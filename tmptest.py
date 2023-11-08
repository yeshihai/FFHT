import numpy as np

# 创建一个矩阵A
A = np.array([[1, 2, 3, 4, 5, 6, 6],
              [7, 8, 9, 10, 11, 12, 12],
              [13, 14, 15, 16, 17, 18, 18]])

# 划分进k块中
k = 3
blocks = np.array_split(A, k, axis=1)

# 对每一块进行处理
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

