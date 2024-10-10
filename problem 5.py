print("Masukkan jumlah barang dan jenisnya :")
jumlah_item_ditoko = int(input())
store_items = {} #utk mnyimpn item/barang ditko dn jmlhnya
for _ in range(jumlah_item_ditoko): #item dn stok  masuk ke dlm dcty (list)
    item, quantity = input().split()
    store_items[item] = int(quantity)
n_c_item = int(input()) #jmlh brg yg dibeli charlie
C_items = [] #list utk nyimpn item yg dibeli charlie
for _ in range(n_c_item): #for utk memasukan item yang dibeli dn memprbarui persediaan di toko
    c_item, c_quantity = input().split()
    c_quantity = int(c_quantity)
    C_items.append(c_item)
    store_items[c_item] -= c_quantity
print("CHARLIE") #mencetak daftar brg yg di beli
print(" ".join(C_items))
print("STORAGE") #mencetak brg yg trsisa di toko stlh dibeli charlie
for item, quantity in store_items.items():
    print(f"{item}: {quantity}")