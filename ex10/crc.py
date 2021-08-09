import sys

# CRC-3 Implementation
def crc(msg, div, code=None):
    if code is None:
     code = '0' * (len(div) - 1) # 0s as the degree of divisor.
    
    # Append the code to the message. If no code is given, default to '000'
    msg = msg + code

    # Convert msg and div into list form for easier handling
    msg = list(msg)
    div = list(div)

    # Loop over every message bit (minus the appended code)
    for i in range(len(msg)-len(code)):
        # If that messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(div)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    # Output the last error-checking code portion of the message generated
    return ''.join(msg[-len(code):])

if __name__ == "__main__":
    print("CRC Simulation.")
    msg = str(input("Message to Send (in Binary): "))
    div = str(input("Divisor (in Binary): ")) 
    code = crc(msg, div)
    
    print("")
    print("Output Code: {}".format(code))
    rec = str(input("Enter the Message Received (in Binary): "))

    if crc(rec, div, code) == '0' * (len(div) - 1):
        print("Success! CRC matches.")
    else:
        print("Failed! CRC Mismatch!")
