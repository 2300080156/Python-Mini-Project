def add_item(item,cart=[]):
    cart.append(item);return cart
print(add_item("apple"));print(add_item("banana"));print(add_item("milk",["bread"]));print(add_item("eggs"))
def add_item_fixed(item,cart=None):
    if cart is None: cart=[]
    cart.append(item);return cart
def create_cart(owner,discount=0): return {"owner":owner,"items":[],"discount":discount}
def add_to_cart(cart,name,price,qty=1): cart["items"].append({"name":name,"price":price,"qty":qty})
def update_price(t,new):
    try:t[0]=new
    except TypeError: print("Cannot modify tuple because tuples are immutable.")
def calculate_total(cart):
    s=sum(i["price"]*i["qty"] for i in cart["items"])
    return s-s*cart["discount"]/100
c1=create_cart("Aarav",10);c2=create_cart("Priya")
add_to_cart(c1,"Laptop",50000);add_to_cart(c1,"Mouse",1000,2)
add_to_cart(c2,"Book",500,3);add_to_cart(c2,"Pen",20,5)
print(c1,calculate_total(c1));print(c2,calculate_total(c2));update_price((1000,),1200)
