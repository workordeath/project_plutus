def getIdentification():
    id_data_file = open("id_data.txt", 'r')
    id_cache = ""
    id_list = []
    
    for line in id_data_file:
        id_cache += (line.partition(':')[0])
        id_cache += " "
        id_cache += (line.partition(':')[2])
        id_list.append(id_cache)
        id_cache = ""
        ## Get's the substring after the ':' keyword. [2].
    
    
    print(id_list)
    id_data_file.close()
