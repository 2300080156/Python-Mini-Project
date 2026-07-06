def add_book(c,bid,t,a,y): c[bid]=(t,a,y)
def borrow_book(c,b,bid):
    if bid in c and bid not in b: b.append(bid); print(f"Book {bid} borrowed.")
    elif bid in b: print(f"Book {bid} is already borrowed.")
    else: print(f"Book {bid} does not exist.")
def return_book(b,bid):
    if bid in b: b.remove(bid); print(f"Book {bid} returned.")
    else: print(f"Book {bid} was not borrowed.")
def register_member(m,i): m.add(i)
def show_available(c,b):
    print("\nAvailable Books:")
    for bid,d in c.items():
        if bid not in b:
            print(f"{bid} - {d[0]} by {d[1]} ({d[2]})")
def main():
    c={};b=[];m=set()
    add_book(c,101,"Python Basics","Guido",2021)
    add_book(c,102,"Data Structures","Mark",2020)
    add_book(c,103,"Machine Learning","Andrew",2022)
    add_book(c,104,"AI Fundamentals","John",2023)
    [register_member(m,i) for i in [1,2,3,2]]
    print("Members:",m)
    borrow_book(c,b,101);borrow_book(c,b,103)
    return_book(b,101)
    show_available(c,b)
    print("\nBorrowed Books:",b)
main()
