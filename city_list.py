
def main():
    f = open("cities.txt","r")
    m_list = list_makr(f)
    print(m_list)
    return

def list_makr(file):
    new_list = []
    for x in range(4):
        line = file.readline()
        city_line = line[:-1]
        new_list.append(city_line)
    return new_list

main()
