from MemoryFiles.Memory import Memory as MemoryAPI

def get_input(prompt: str) -> str:
    value = input(prompt).strip()
    if not value:
        print("Input cannot be empty.")
        return None
    return value

def store_data(memory_api: MemoryAPI):
    address = get_input("Enter address: ")
    if not address:
        return
    data = get_input("Enter data to store: ")
    if not data:
        return
    success = memory_api.store_data(int(address), data)
    print("Data stored successfully." if success else "Failed to store data.")

def read_data(memory_api: MemoryAPI):
    address = get_input("Enter address to read: ")
    if not address:
        return
    data = memory_api.read_data(int(address))
    print(f"Data at address {address}: {data}")


def dump_memory(memory_api: MemoryAPI):
    success = memory_api.dump()
    print("Memory dumped successfully." if success else "Failed to dump memory_api.")


def memoryCLI():
    memory_api = MemoryAPI()
    options = {
        '1': ("Store Data", store_data),
        '2': ("Read Data", read_data),
        '3': ("Dump Memory", dump_memory),
        '4': ("Exit", None)
    }

    while True:
        print("\nMemory Console App")
        for key, (description, _) in options.items():
            print(f"{key}. {description}")

        choice = get_input("Choose an option (1-4): ")
        if not choice or choice not in options:
            print("Invalid option. Please choose a valid option.")
            continue

        if choice == '4':
            print("Exiting...")
            break

        # Execute the corresponding function
        _, action = options[choice]
        if action:
            action(memory_api)
