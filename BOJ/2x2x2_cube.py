import sys
import copy

block = list(map(int, sys.stdin.readline().split()))
block = [0] + block

def check_aligned(input_block):
    for i in range(1, 25, 4):
        if input_block[i] == input_block[i + 1] == input_block[i + 2] == input_block[i + 3]:
            pass
        else:
            return False
    return True

def case_1(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[24], block[22]
    block[24], block[22] = block[9], block[11]
    block[9], block[11] = block[5], block[7]
    block[5], block[7] = block[1], block[3]
    block[1], block[3] = temp_a, temp_b
    return check_aligned(block)

def case_2(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[23], block[21]
    block[23], block[21] = block[10], block[12]
    block[10], block[12] = block[6], block[8]
    block[6], block[8] = block[2], block[4]
    block[2], block[4] = temp_a, temp_b
    return check_aligned(block)


def case_3(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[24], block[22]
    block[24], block[22] = block[1], block[3]
    block[1], block[3] = block[5], block[7]
    block[5], block[7] = block[9], block[11]
    block[9], block[11] = temp_a, temp_b
    return check_aligned(block)

def case_4(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[23], block[21]
    block[23], block[21] = block[2],block[4]
    block[2], block[4] = block[6], block[8]
    block[6], block[8] = block[10], block[12]
    block[10], block[12] = temp_a, temp_b
    return check_aligned(block)

def case_5(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[21], block[22]
    block[21], block[22] = block[17], block[18]
    block[17], block[18] = block[5], block[6]
    block[5], block[6] = block[13], block[14]
    block[13], block[14] = temp_b, temp_a
    return check_aligned(block)

def case_6(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[23], block[24]
    block[23], block[24] = block[19], block[20]
    block[19], block[20] = block[7], block[8]
    block[7], block[8] = block[15], block[16]
    block[15], block[16] = temp_b, temp_a
    return check_aligned(block)

def case_7(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[13], block[14]
    block[13], block[14] = block[5], block[6]
    block[5], block[6] = block[17], block[18]
    block[17], block[18] = block[21], block[22]
    block[21], block[22] = temp_b, temp_a
    return check_aligned(block)

def case_8(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[15], block[16]
    block[15], block[16] = block[7], block[8]
    block[7], block[8] = block[19], block[20]
    block[19], block[20] = block[23], block[24]
    block[23], block[24] = temp_b, temp_a
    return check_aligned(block)

def case_9(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[3], block[4]
    block[3], block[4] = block[17], block[19]
    block[17], block[19] = block[9], block[10]
    block[9], block[10] = block[14], block[16]
    block[14], block[16] = temp_b, temp_a
    return check_aligned(block)

def case_10(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[3], block[4]
    block[3], block[4] = block[14], block[16]
    block[14], block[16] = block[9], block[10]
    block[9], block[10] = block[17], block[19]
    block[17], block[19] = temp_b, temp_a
    return check_aligned(block)

def case_11(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[1], block[2]
    block[1], block[2] = block[13], block[15]
    block[13], block[15] = block[11], block[12]
    block[11], block[12] = block[22], block[24]
    block[22], block[24] = temp_b, temp_a
    return check_aligned(block)

def case_12(input_block):
    block = copy.deepcopy(input_block)
    temp_a, temp_b = block[1], block[2]
    block[1], block[2] = block[22], block[24]
    block[22], block[24] = block[11], block[12]
    block[11], block[12] = block[13], block[15]
    block[13], block[15] = temp_b, temp_a
    return check_aligned(block)


if case_1(block) or case_2(block) or case_3(block) or case_4(block) or case_5(block) or case_6(block) or case_7(block) or case_8(block) or case_9(block) or case_10(block) or case_11(block) or case_12(block):
    print(1)
else:
    print(0)