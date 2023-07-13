import pdb

def binary_num(num):
    """Simple binary converter for unsigned ints up to 256 bits
        input: num (unsigned int 256 bits maximum)
        returns: string of a binary num"""
    
    assert isinstance(num, int)
    assert num >= 0
    assert num < 2**256
    
    bin_str = '0' * 256

    max_bit = 0
    while(2**max_bit <= num/2):
        max_bit += 1

    remainder = num
    for i in range(max_bit,-1,-1):
        if(2**i <= remainder):
            bin_str = flip_bit(i, bin_str)
            remainder -= 2**i
    return bin_str


def flip_bit(bit_num, bin_str):
    """flips a bit in a string of 256 chars representing a binary num
        inputs:  bit_num (int):  the bit number to flip, 0 is first position
                 bin_str (str):  the binary string of length 256
        returns: (str) binary string of length 256"""
    
    # check everything is the correct format
    assert isinstance(bin_str, str)
    assert isinstance(bit_num, int)
    assert len(bin_str) == 256
    assert (bit_num >= 0 and bit_num < len(bin_str))
    for char in bin_str:
        if(char != '1' and char != '0'):
            raise ValueError
    
    bit = bin_str[bit_num]
    if(bit == '0'):
        return bin_str[:bit_num] + '1' + bin_str[bit_num+1:]
    else:
        return bin_str[:bit_num] + '0' + bin_str[bit_num+1:]
    

if __name__ == "__main__":
    for i in (2**p for p in range(0, 256)):
        print(f"{i}: {binary_num(i)}")