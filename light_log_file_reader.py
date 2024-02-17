import matplotlib.pyplot as plt
from itertools import cycle

progress = ["|","|", "/","/", "-","-", "\\","\\"]
progress_cycle = cycle(progress)

def next_progress():
    return next(progress_cycle)


data_file = "C:\\Users\\Michael.Michael-PC\\Documents\\Test Data\\Light_logs\\light_log.txt"

vis_ir_data = []
ir_data = []
start_data = []
end_data = []

with open(data_file, "r") as file_in:
    hdr = file_in.readline()
    for idx, line in enumerate(file_in):
        vis_ir = line.strip().split('\t')[0]
        ir     = line.strip().split('\t')[1]
        #print(f"{idx} - Visible/IR: {vis_ir} - IR: {ir}")
        vis_ir_data.append(int(vis_ir))
        if idx <= 825:
            start_data.append(int(vis_ir))
        if idx >= 38075:
            end_data.append(int(vis_ir))
        # if (idx%2) == 0:
        #     print("|\r",end="")
        # if (idx%2) != 0:
        #     print("-\r",end="")
        stat = next_progress()
        print(f"{stat}\r",end="")

            

        

print(f"{idx} lines of data.")

# plt.figure(1)
# plt.plot(vis_ir_data)
# plt.title("Full Data")

# plt.figure(2)
# plt.plot(start_data)
# plt.title("Start Data")

plt.figure(3)
plt.plot(end_data)
plt.title("End Data")

plt.show()
