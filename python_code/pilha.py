def push(info,value):
    info.append(value)

def pop(info):
    if len(info) > 0:
        info.pop()


info = []
push(info,"victor")
push(info,"rocha")
push(info,"gomes")
pop(info)


print info