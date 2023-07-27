import os
clear = lambda: os.system("cls")
clear()

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(fruit_list)
    fruit_list.append("orange")
    print(fruit_list)
    for i in range(len(fruit_list)):
        if fruit_list[i] == "apple":
            fruit_list.insert(i, "cherry")
            print(fruit_list)
            break
    fruit_list.remove("banana")
    print(fruit_list)
    popped = fruit_list.pop()
    print(f"Popped element: {popped}\n{fruit_list}")
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)

if __name__ == "__main__":
    main()
