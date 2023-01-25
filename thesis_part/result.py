document = open('thesis_part\pr.txt', 'r')
string_dict = document.read()
document.close()
main_dict = eval(string_dict)
for k,v in main_dict.items():
    print(k)
    print(v)