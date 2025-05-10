def addBinary(a, b):
    out = []
    i = 0
    round = False
    while i < (min(len(a),len(b))):

        if (round):
            selection1 = "1"
            #Determines if list a, corresponds to i%2, or list b, corresponds to b%2
            selection2 = b[i]

        else:
            if(int(a[i]) & int(b[i]) == 1):
                round = True
                out.append("0")
            elif (int(a[i]) | int(b[i]) == 1):
                out.append("1") 
            else:
                out.append("0")

    #for i in range(max(len(a),len(b))- min(len(a),len(b))):
        pass 
    output_str : str = ""
    for i in range(len(out)):
        #output_str += out[len(out)-i-1]
        output_str+=out[i]

    return output_str
    
print(addBinary("1","1"))
