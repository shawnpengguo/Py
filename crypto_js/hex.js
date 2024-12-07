const names = 'hello world'

const hex_number_map = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

for (let i = 0; i < names.length; i++) {
    let ascii = names.charCodeAt(i)
    const right_bit = ascii >> 4
    const left_bit = ascii & 0xF
    const rightNum = right_bit > 10 ? hex_number_map[right_bit] : right_bit
    const leftNum = left_bit  > 10 ? hex_number_map[left_bit] : left_bit
    console.log(ascii, rightNum, leftNum)
}

/**
 * h 104
 * 0110 1000
 * 0000 1111
 * 0000 1000 位与
 *    6 8
 * */