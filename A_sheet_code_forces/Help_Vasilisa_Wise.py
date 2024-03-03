

if __name__=='__main__':


    d = {"r1": 0, "r2": 0, "c1": 0, "c2": 0, "d1": 0, "d2": 0}

    for i in range(3):
        a, b = map(int, input().split())
        if i == 0:
            d["r1"], d["r2"] = a, b
        elif i == 1:
            d["c1"], d["c2"] = a, b
        else:
            d["d1"], d["d2"] = a, b

    x=(d["c1"]-d["d2"]+d["r1"])//2
    y=d['r1']-x
    w=d["d1"]-x
    z=d["r2"]-w

    if (x<=0 or y<=0 or z<=0 or w<=0) or (x>=10 or y>=10 or w>=10 or z>=10) or (x==y or z==w or y==w or x==z or x==w or y==z):

        print("-1")

    elif x+y!=d["r1"] or x+w!=d["d1"] or x+z!=d["c1"] or y+w!=d["c2"] or y+z!=d["d2"]:

        print("-1")

    else:

        print(x,y)
        print(z,w)