class Inventory(object):

    def __init__( self,aName,aSize ):
        self.Slots = {}
        self.Name = aName
        self.Size = aSize
        for x in range(1,self.Size+1):
            self.Slots['Slot'+str(x)] = [x,None,None]
    #Add new Item to the Inventory

    def addItem( self,aNewItem,aAmmount = 1 ):
        added = False   #If the Item was successfully added yet
        ammountLeft = aAmmount   
        #If the new Item can be stacked
        if aNewItem.isStackable: 
                #Iterate through all the Slots in the Inventory
                for slot, value in sorted( self.Slots.items(), key=lambda x : x[1][0] ): 
                    #Keep repeating until either all the items were added, or there is no space left in Inventory
                    while ( ammountLeft > 0 ) and ( Inventory.nextEmpty(self) is not None ):   #While there is still items to be added and there's still space left  
                        if ( value[1] is aNewItem ) and ( value[2] + ammountLeft <= aNewItem.maxStack ):  
                            value[2] += aAmmount
                            added = True
                            ammountLeft = 0
                            break
                        elif  ( value[1] is aNewItem ) and ( value[2] < aNewItem.maxStack ):
                            while ( value[2] < aNewItem.maxStack ) and ( ammountLeft > 0 ):
                                value[2] += 1
                                ammountLeft -= 1
                            break
                        elif ( value[1] is None ):
                            if aAmmount is 1:
                                self.Slots[slot][1] = aNewItem
                                self.Slots[slot][2] = 1
                                ammountLeft = 0
                                break
                            else:
                                self.Slots[slot][1] = aNewItem
                                self.Slots[slot][2] = 1
                                ammountLeft -= 1
                                while (  self.Slots.get(slot)[2]  < aNewItem.maxStack ) and ( ammountLeft > 0 ):
                                    self.Slots.get(slot)[2] += 1
                                    ammountLeft -= 1
                                break
                        else:
                            break   
        #If the Item can't be stacked
        if ( not added ) and ( not aNewItem.isStackable ):
            for slot, value in sorted(self.Slots.items(), key=lambda x : x[1][0]):  #Iterate through all the Slots in the Inventory
                if value[1] == None:    #If the Slot is empty
                    ammountLeft = aAmmount
                    while ( Inventory.nextEmpty(self) != None ) and ( ammountLeft > 0 ):   #While the next Slot is empty and there is still items to be added
                        self.Slots[Inventory.nextEmpty(self)][2] = 1
                        self.Slots[Inventory.nextEmpty(self)][1] = aNewItem  #Adds the item in the empty Slot
                        ammountLeft -= 1
                    break
        if ( not added ) and ( ammountLeft > 0 ):   #If nothing else, the Inventory is full
            print ('Full Inventory!')

    def removeItem( self , aItem, aAmmount = 1 ):
        deleted = False
        ammountLeft = aAmmount
        for slot, value in sorted(self.Slots.items(), key=lambda x : x[1][0]):
            if value[1] is aItem:
                while ( ammountLeft > 0 )
                        if ( value[1] is aItem ) and ( (value[2] - ammountLeft) is 0 ):
                            del self.Slots[slot]
                            deleted = True
                            ammountLeft = 0
                            break
                        elif ( value[1] is aItem  ):

                            break

    def printInventory( self ):
        for slot, value in sorted( self.Slots.items(), key=lambda x : x[1][0] ): #Dont't how the fuck it works, it just fucking works, ok?
            if value[1] != None:
                print ( slot, value[1].Name, value[2] )
            else:
                print ( slot, 'Empty' )
        pass

    def nextEmpty( self ):
        for slot, value in sorted( self.Slots.items(), key=lambda x : x[1][0] ):
            if value[1] == None:
                return slot
                break
        return None

class Item(object):

    Items = {}
    
    def __init__( self, aType,aName,aStackable = False,aMaxStack = 1 ):
        self.Type = aType
        self.Name = aName
        self.isStackable = aStackable
        self.maxStack = aMaxStack
        self.__class__.Items.update( {aName:self} )
