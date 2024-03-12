def bp(ds):
    q = 0
    for i in range(len(ds)):
        ds.append(i**2)
    print("5 số đầu của list:", ds[:5])
    print("5 số cuối của list:", ds[-5:])