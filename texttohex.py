def dec_to_binary(num: int, index: int) -> str:
    subtraction_list: List[int] = [128, 64, 32, 16, 8, 4, 2, 1]
    current_str = ""
    # returns if the index value is out of range.
    if index > 7:
        return current_str

    if (num - subtraction_list[index]) >= 0:
        # adds a 1 if the number can be subtracted.
        num = num - subtraction_list[index]
        current_str += "1"
        current_str += dec_to_binary(num, index + 1)
    else:
        # adds a 0 if the number cant be subtracted.
        current_str += "0"
        current_str += dec_to_binary(num, index + 1)
        
    return current_str

def bin_to_hex(num: int) -> str:

    current_str = ""
    
    bin_hex = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
        }
    
    remainder: int = num % 16
    num = int(num / 16)

    current_str += bin_hex[remainder]

    if num != 0:
        current_str = bin_to_hex(num) + current_str

    return current_str
    
def text_to_binary(text: str) -> bool:
    # makes each character into their decimal counterpart and puts it into a list
    decimal_list = [ord(char) for char in text]
    # does the same but turns the decimal counterpart into binary
    binary_list = [dec_to_binary(char, 0) for char in decimal_list]
    print(' '.join(binary_list))
    return True

def text_to_hex(text: str) -> bool:
    # makes each character into their decimal counterpart and puts it into a list
    decimal_list = [ord(char) for char in text]
    hex_list = [bin_to_hex(char) for char in decimal_list]
    print(' '.join(hex_list))
    return True

def invalid_op(text: str) -> bool:
    return False


def perform_operation(chosen_op: str, text: str) -> bool:

    ops = {
        "binary": text_to_binary,
        "hexadecimal": text_to_hex,
        "hex": text_to_hex
        }

    chosen_op_function = ops.get(chosen_op, invalid_op)
    return chosen_op_function(text)

if __name__ == "__main__":
    
    text: str = input("What text would you like to convert? ")
    choice: str = ""
    continue_bool: bool = False
    
    # loops over the choice for the conversion unless the operation is done.
    while continue_bool == False:
        
        choice = input("What would you like to convert the text to? ")
        continue_bool = perform_operation(choice, text)
        
