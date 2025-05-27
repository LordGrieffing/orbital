import concurrent.futures
import numpy



def addOne(num):
    print(f"num current value: {num}")
    return num + 1




def main():
    
    num = 0
    futures = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
    
        
        for i in range(10):
            futures.append(executor.submit(addOne, num))

        
        Values = [f.result() for f in futures]



    print(Values)
    print(num)















if __name__ == "__main__":
    main()