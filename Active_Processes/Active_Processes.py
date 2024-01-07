import psutil
from colorama import *

#initialize colorama
init(autoreset=True)

def system_processes():
    #list of all running processes on the system
    processes = list(psutil.process_iter(['pid', 'name', 'memory_info']))

    #sort the processes by memory usage
    sort_process = sorted(processes, key=lambda x: x.info['memory_info'].rss, reverse=True)

    #create or open a text file for writing
    with open('process_info.txt', 'w') as file:
        #write header to the file
        file.write("Process ID | Name                                | Memory Usage (MB)\n")
        file.write("=" * 70 + "\n")

        #track seen names to highlight repeating ones in red
        seen_names = set()

        #write information about each process to the file and print to the console
        for process in sort_process:
            memory_info = process.info['memory_info']
            name = process.info['name']
            line = f"{process.info['pid']: <6} | {name[:40]: <40} | {memory_info.rss / (1024 * 1024):.2f}\n"

            #check if the name is repeating
            if name in seen_names:
                # highlight in red using colorama for console
                print(f"{Fore.RED}{line}{Style.RESET_ALL}", end='')
            else:
                print(line, end='')
            
            seen_names.add(name)

            #write uncolored line to the file
            file.write(line)

if __name__ == "__main__":
    system_processes()