import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

input_file = open(args.path, 'r')
input_data = input_file.read()

if len(input_data) == 0:
    exit()

msg = []

for i in range(0, len(input_data)):
    curr_ch = input_data[i]
    if len(msg) == 0:
        msg.append(curr_ch)
    else:
        prev_ch = msg[-1]
        if curr_ch == prev_ch:
            msg.pop()
        else:
            msg.append(curr_ch)

print("".join(msg))
