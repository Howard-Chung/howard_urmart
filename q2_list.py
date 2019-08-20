def add_val_to_list(val = '', list = []):
    # if not list: list = []

    print("mem location of id = " + str(id(val)))
    print("mem location of ll = " + str(id(list)))
    print(id(list))
    list.append(val)
    return list


list1 = add_val_to_list('b')
print(list1)
print(id(list1))
list2 = add_val_to_list('c')
print(list2)
list3 = add_val_to_list('a')
print(list3)


# def add_val_to_list1(val, ll = ''):
#     print("AAAv")
#     print(id(val))
#     print(id(ll))
#     # if not list: list = []
#     # print("CCC")
#     # print(list)
#     ll += val
#     return ll
#
# print("CCCvvv")
# print(id(add_val_to_list1))
#
# list1 = add_val_to_list1('a')
# print(list1)
# list2 = add_val_to_list1('a', 'b')
# print(list2)
# list3 = add_val_to_list1('b')
# print(list3)
#
#
#
# def foo1(a):
#     # function block
#     a += 1
#     print('id of a:', id(a))  # id of y and a are same
#     return a
#
#
# # main or caller block
# x = 10
# y = foo1(x)
#
# # value of x is unchanged
# print('x:', x)
#
# # value of y is the return value of the function foo1
# # after adding 1 to argument 'a' which is actual variable 'x'
# print('y:', y)
#
# print('id of x:', id(x))  # id of x
# print('id of y:', id(y))  # id of y, different from x
#
#
#
# # print("CCC1")
# #
# # def foo2(func_list):
# #     # function block
# #     func_list.append(30)  # append an element
# #
# #
# # def foo3(func_list):
# #     # function block
# #     del func_list[1]  # delete 2nd element
# #
# #
# # def foo4(func_list):
# #     # function block
# #     func_list[0] = 100  # change value of 1st element
#
#
# # # main or caller block
# # list1 = [10, 20]
# # list2 = list1  # list1 and list2 point to same list object
# #
# # print('original list:', list1)
# # print('list1 id:', id(list1))
# #
# # print('value of list2:', list2)
# # print('list2 id:', id(list2))
# #
# # foo2(list1)
# # print('\nafter foo2():', list1)
# # print('list1 id:', id(list1))
# #
# # print('value of list2:', list2)
# # print('list2 id:', id(list2))
# #
# # foo3(list1)
# # print('\nafter foo3():', list1)
# # print('list1 id:', id(list1))
# #
# # print('value of list2:', list2)
# # print('list2 id:', id(list2))
# #
# # foo4(list1)
# # print('\nafter foo4():', list1)
# # print('list1 id:', id(list1))
# #
# # print('value of list2:', list2)
# # print('list2 id:', id(list2))