from banner import banner
banner("DEEP THOUGHTS", "RUSSELL")

def main():
    run_event_loop()

def run_event_loop():
    journal_data = []
    while True:
        command = input('[L]ist entries, [A]dd an entry,E[x]it:')

        if command.upper() == 'L':
            list_entries(journal_data)
        elif command.upper() == 'A':
            add_entries(journal_data)
        elif command.upper() =='X':
            break
        else:
            print('sorry I dont understand')





def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f'{num+1} - {entry}')

def add_entries(data):
    entry = input('type your entry, <ENTER> to exit: \n')
    data.append(entry)




main()