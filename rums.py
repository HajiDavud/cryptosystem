"""RUM REQEMLERI"""

def nums(x):
    case={
        "X":10,
        "L":50,
        "M":1000,
        "D":500,
        "C":100,
        "V":5,
        "I":1,
    }


    return case.get(x)
def netice(y): #netice ingilis dinlinde nedi ona bax! = result

    case={
        0:"",
        1:"I",
        4:"IV",
        5:"V",
        9:"IX",
        10:"X",
        40:"XL",
        50:"L",
        90:"XC",
        100:"C",
        400:"CD",
        500:"D",
        900:"CM",
        1000:"M",
    }
    ll = case.keys()
    ld = list(ll)
    aa = 13
    ccc = y
    ddd = []
    ok = 1
    aze =1
    for i in range(len(case)):
        while y>=0 and aa>=0:
            if ld[aa]<=y:
                if(aa!=13):
                    if ld[aa+1] <= y:
                        aze+=1
                        y -= ld[aa+1]
                        ddd += [case.get(ld[aa+1])]
                        aa+=1
                else:
                    y -= ld[aa]
                    ddd += [case.get(ld[aa])]
                    ok+=1

            aa -=1
        return ddd



    return case.get(y)
def tapici(ll):
    cc = []
    dd = 0
    for i in range(len(ll)):
        if ll[i] == "None":
            cc += []
        else:
            cc += [ll[i]]
    for i in range(len(cc)):
        dd +=int(cc[i])

    return dd

def yoxlayici(other):
    a= [
        ['1','5'],
        ['1','10'],
        ['10','50'],
        ['10','100'],
        ['100','500'],
        ['100','1000'],
    ]

    b = ["4","9","40","90","400","900"]
    c = len(other)-1

    while (c>0):
        for i in range(len(a)):
            if other[c-1]==a[i][0] and other[c]==a[i][1]:
                other[c-1]=b[i]
                del other[c]
        c-=1
    return other
num = input()
caca = []
other =[]
numlis=list(num)
for i in range(len(numlis)):
    other.append(str(nums(numlis[i])))
caca += yoxlayici(other)
ll =[]
ll +=[str(tapici(other))]
ff = ll[0]
bb = []
bb += netice(int(ff))
sss=''
if len(bb)>1:
    for i in range(len(bb)):
        sss += bb[i]
    print(sss,end =None)
else:
    print(bb[0],end=None)
