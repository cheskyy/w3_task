def buat_tangga(input_string):
    input_data = input_string.split()
    N = int(input_data[0])
    M = input_data[1]
    if M == "Aku":
        for i in range(1, N+1):
            print(' '.join(['I' if j % 2 == 0 else 'U' for j in range(i)]))
    elif M == "Kamu":
        for i in range(1, N+1):
            spaces = '  ' * (N - i)
            print(spaces + ' '.join(['I' if j % 2 == 0 else 'U' for j in range(i)]))
input_string = input()
buat_tangga(input_string)