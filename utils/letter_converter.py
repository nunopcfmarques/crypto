def string_to_numbers(s: str) -> list[int]:
    num_list = []
    for char in s:
        num = ord(char.lower()) - 97
        num_list.append(num)
    return num_list

def numbers_to_string(nums: list[int]) -> str:
    s = ''
    for num in nums:
        char = chr(num + 97)
        s += char
    return s
