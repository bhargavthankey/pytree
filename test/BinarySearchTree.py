from pytree.binary_search_tree import BinarySearchTree
    
    
mytree = BinarySearchTree()
mytree[3] = "red"
mytree[1] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

print(mytree[7])
#print(mytree.delete_node(4))

mytree.print_in_order()
mytree.print_pre_order()
mytree.print_post_order()

newtree = BinarySearchTree()

newtree.insert_node(1)
newtree.insert_node(5)
newtree.insert_node(2)
newtree.insert_node(4)
newtree.insert_node(3)
newtree.insert_node(8)
newtree.insert_node(6)
newtree.insert_node(9)
newtree.insert_node(0)
newtree.insert_node(7)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()
print(newtree.length())

newtree.delete_node(7)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(4)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(5)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(9)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(6)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(8)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()

newtree.delete_node(1)
newtree.print_in_order()
newtree.print_pre_order()
newtree.print_post_order()
