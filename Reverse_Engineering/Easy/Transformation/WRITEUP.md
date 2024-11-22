looking at the encryption script we can see:
    The flag is inputed,
    The strings in flag are paired, flag[i] and flag[i + 1]
    The pair is then combined into two integers
    The first integer is converted to unicode with ord() 
    Then the value is shifted 8 bits to the left
    Then the unicode value of the second integer is added
    The result is a single character representing both characters

To reverse this:
    we take each charater in the enc file
    Convert back to an integer
    The first characters unicode is found by shifting the intger 8 bits to the right
    The second characters unicode is found by masking the lower 8 bits: num & 0xFF
    Then we convert the unicode values back to strings
