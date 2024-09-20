from os import system
from MemoryFiles.Memory import Memory as simpleMemory

def main() -> None:
    smem = simpleMemory()
    smem.store_data(int("01"), "1007")
    smem.store_data(int("00"), "2008")
    smem.store_data(int("20"), "2000")
    smem.dump()
    print(f"reading data: {smem.read_data(int("00"))}")
    print(f"reading data: {smem.read_data(int("20"))}")
    

if __name__ == "__main__":
    main()