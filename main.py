import cv2
from sys import argv

def to_hex(arr):
    return arr[0] * 0x000001 + arr[1] * 0x000100 + arr[2] * 0x010000

imArray = cv2.imread(argv[1])
output = f"frame %= {len(imArray) // 8};\n"
for frame in range(0, len(imArray), 8):
    colors = set()
    for col in range(0, len(imArray[frame])):
        for row in range(frame, frame + 8):
            hex_val = to_hex(imArray[row][col])
            if hex_val != 0:
                colors.add(hex_val)
    output += f"if(frame == {frame // 8}) {{\n"
    for color in colors:
        output += "{\n"
        output += f"        uint8_t values_{hex(color)}[32] = {{"
        for col in range(0, len(imArray[frame])):
            num_represent = 0
            for row in range(frame, frame + 8):
                hex_color = to_hex(imArray[row][col])
                num_represent += 2 ** (row - frame) if hex_color == color else 0
            output += hex(num_represent)
            output += ", "
        output = output[0:-2]
        output += "};\n"
        output += f"        ColorData cd_{hex(color)} = new ColorData;\n"
        output += f"        ColorData_init(&cd_{hex(color)}, values_{hex(color)}, {hex(color)});\n"
        output += f"        displayColor(cd_{hex(color)});\n"
        output += "}\n"
    output += "}\n\n"


with open(argv[2], "w") as f:
    print(output, file=f)
