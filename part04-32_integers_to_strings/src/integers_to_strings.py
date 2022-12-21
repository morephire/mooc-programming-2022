def formatted(list) -> list:
    new = []
    for number in list:
        new.append(f"{number:.2f}")
    
    return new

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
