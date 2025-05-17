def solution(N):
    # Implement your solution here
    try:
        int(N)
    except TypeError:
        print("Error: Must integer type. {} is {}".format(N, type(N)))
        return 0

    binary_number = bin(N).replace("0b", "")
    parts = [len(p) for p in binary_number.split("1") if p]
    if parts and binary_number.count("1") > 1:
        if binary_number[-1] != "0":
            return max(parts)
        else:
            try:
                return max(parts[:-1])
            except ValueError:
                return 0

    return 0
