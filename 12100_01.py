import copy

NSize = int(input())

Block = []
MaxValue = 0
for row in range(NSize):
    tmplist = list(input().split())
    Block.append([int(x) for x in tmplist])

def PrintBlock(block):
    for bl in block:
        print(" ".join([str(x) for x in bl]))

def FindMax(block):
    MaxBlock = 0
    for b_row in block:
        MaxTmp = max(b_row)
        if MaxTmp > MaxBlock:
            MaxBlock = MaxTmp
    return MaxBlock

def RollBlock(dir, block):
    global NSize

    if dir == 0:
        for b_idx, b_row in enumerate(block):
            b_list = []
            tf_sum = True
            for b_elt in b_row[::-1]:
                if b_elt != 0:
                    if b_list:
                        if b_list[-1] == b_elt and tf_sum:
                            b_list[-1] = b_list[-1] * 2
                            tf_sum = False
                        else:
                            b_list.append(b_elt)
                            tf_sum = True
                    else:
                        b_list.append(b_elt)
                        tf_sum = True
            for i in range(NSize-len(b_list)):
                b_list.append(0)
            b_list.reverse()
            block[b_idx]=b_list

    elif dir == 1:
        for n_col in range(NSize):
            b_list = []
            tf_sum = True
            for n_row in range(NSize):
                if block[n_row][n_col] != 0:
                    if b_list:
                        if b_list[-1] == block[n_row][n_col] and tf_sum:
                            b_list[-1] = b_list[-1]*2
                            tf_sum = False
                        else:
                            b_list.append(block[n_row][n_col])
                            tf_sum = True
                    else:
                        b_list.append(block[n_row][n_col])
                        tf_sum = True
            for i in range(NSize-len(b_list)):
                b_list.append(0)
            for n_row in range(NSize):
                block[n_row][n_col] = b_list[n_row]

    elif dir == 2:
        for b_idx, b_row in enumerate(block):
            b_list = []
            tf_sum = True
            for b_elt in b_row:
                if b_elt != 0:
                    if b_list:
                        if b_list[-1] == b_elt and tf_sum:
                            b_list[-1] = b_list[-1] * 2
                            tf_sum = False
                        else:
                            b_list.append(b_elt)
                            tf_sum = True
                    else:
                        b_list.append(b_elt)
                        tf_sum = True
            for i in range(NSize-len(b_list)):
                b_list.append(0)
            block[b_idx] = b_list

    elif dir == 3:
        for n_col in range(NSize):
            b_list = []
            tf_sum = True
            for n_row in range(NSize)[::-1]:
                if block[n_row][n_col] != 0:
                    if b_list:
                        if b_list[-1] == block[n_row][n_col] and tf_sum:
                            b_list[-1] = b_list[-1]*2
                            tf_sum = False
                        else:
                            b_list.append(block[n_row][n_col])
                            tf_sum = True
                    else:
                        b_list.append(block[n_row][n_col])
                        tf_sum = True
            for i in range(NSize-len(b_list)):
                b_list.append(0)
            b_list.reverse()
            for n_row in range(NSize):
                block[n_row][n_col] = b_list[n_row]

    else:
        raise ValueError("dir is not between 0 and 3: ", str(dir))
    
    return


def DFS(NTrial,block):
    global MaxValue

    if NTrial == 6:
    # if NTrial == 3:
        TmpMax = FindMax(block)
        if TmpMax > MaxValue:
            MaxValue = TmpMax
        return

    for dir in range(4):
        block_next = copy.deepcopy(block)
        RollBlock(dir, block_next)
        # print(NTrial,dir)
        # PrintBlock(block_next)
        # print()
        DFS(NTrial+1,block_next)


DFS(1,Block)
print(MaxValue)


# PrintBlock(Block)
# PrintBlock(RollBlock(0, Block))
# Block0 = copy.deepcopy(Block)
# RollBlock(0, Block0)
# PrintBlock(Block0)
# print()
# Block1 = copy.deepcopy(Block)
# RollBlock(1, Block1)
# PrintBlock(Block1)
# print()
# Block2 = copy.deepcopy(Block)
# RollBlock(2, Block2)
# PrintBlock(Block2)
# print()
# Block3 = copy.deepcopy(Block)
# RollBlock(3, Block3)
# PrintBlock(Block3)
# print()
# print(MaxValue)
# print(FindMax(Block))