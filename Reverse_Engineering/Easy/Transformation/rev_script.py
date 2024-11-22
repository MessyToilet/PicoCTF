#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

encoded_string = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"

integers = [ord(char) for char in encoded_string]

print(f'Decoded UTF-8 to integers: {integers}')
 
decoded_flag = ''.join([chr(num >> 8) + chr(num & 0xFF) for num in integers])

print(f'Decoded flag: {decoded_flag}')

