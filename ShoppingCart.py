

class ShoppingCart(object):
    
    def __init__(self,str_CustomerName):
        self.str_CustomerName=str_CustomerName
        self.dict_CartContent={}

    def add_item(self,str_ProductName,dec_Price,int_Qty=1):
        self.str_ProductName=str_ProductName
        self.dec_Price=dec_Price
        self.int_Qty=int_Qty
        if self.Search_product(str_ProductName):
            self.Search_product(str_ProductName)['Qty']+=int_Qty
        else:
            self.dict_CartContent[str_ProductName]={'Price':dec_Price,'Qty':int_Qty}


            
    def show_cart(self):
        print(self.dict_CartContent)

    def change_qty(self,productName,qty):
        self.dict_CartContent[productName]['Qty']=qty
        
    
    def Search_product(self,ProductName):
        for each in self.dict_CartContent:
            if each==ProductName:
                return self.dict_CartContent[each]
            else:
                return False
    




MyCart=ShoppingCart('Johnny')
MyCart.add_item('a',1.2)
MyCart.add_item('ipad Pro',1000,20)
MyCart.add_item('apple Mac',3000)
MyCart.add_item('ipad Pro',1000,-2)
MyCart.show_cart()
