from tkinter import filedialog
import pickle #remove this line when implementing
StripThis=pickle.load(open("c:\\Users\\david\\Downloads\\pickle.pkl",'rb')) #set StripThis as your contract string
ContractLanguage='.sol' #I guess pass the language through here? Takes input ".vy", ".rs", or ".sol"

def StripSolContract(StripThis):
    file=StripThis
    LineList=[]
    for line in file.splitlines():
        TestLine=line.replace(" ","")
        if '//' in line:
            AppendThis=line.split('//',1)[0]
            MaybeAppendThis=AppendThis.replace(" ","")
            if MaybeAppendThis != "":
                LineList.append(AppendThis)
            pass
        elif TestLine is not "":
            AppendThis=line
            LineList.append(AppendThis)   
    return LineList

def StripVyContract(StripThis):
    file=StripThis
    LineList=[]
    SkipThisLine=False
    for line in file.splitlines():
        if SkipThisLine is False:
            if '#' in line:
                if line == "#":
                    continue
                AppendThis=line.split('#')[0]
                MaybeAppendThis=AppendThis.replace(" ","")
                if len(MaybeAppendThis)<=1:
                    continue
                elif MaybeAppendThis.split()[0]=="#":
                    continue
                elif MaybeAppendThis is not "":
                    LineList.append(AppendThis)
                    continue

            elif "'''" in line:
                LeftLine=line.split("'''",1)[0]
                MaybeLeftLine=LeftLine.replace(" ","")
                SkipThisLine=True
                if MaybeLeftLine!="" and MaybeLeftLine != "'''":
                    LineList.append(LeftLine)
                continue
            
            elif '"""' in line:
                LeftLine=line.split('"""',1)[0]
                MaybeLeftLine=LeftLine.replace(" ","")
                SkipThisLine=True
                if MaybeLeftLine!="" and MaybeLeftLine != '"""' and LeftLine !="":
                    LineList.append(LeftLine)
                continue
            else: 
                if line.replace(' ','') is not "":
                    AppendThis=line
                    LineList.append(AppendThis)
                    continue
        elif SkipThisLine is True:
            if "'''" in line:
                SkipThisLine=False
                if line == "'''":
                    continue
                SplittedLine=line.split("'''")
                RightLine=SplittedLine[len(SplittedLine)-1]
                if RightLine != "'''" and RightLine != "":
                    LineList.append(RightLine)
                continue

            elif '"""' in line:
                SkipThisLine=False
                if line == '"""':
                    continue
                SplittedLine=line.split('"""')
                RightLine=SplittedLine[len(SplittedLine)-1]
                if RightLine != '"""' and RightLine != "":
                    LineList.append(RightLine)
                continue
    return LineList

def WriteContract(LineList):
    StrippedContract=""
    for x in LineList:
        if StrippedContract == "":
            StrippedContract=x
            continue
        else:
            StrippedContract=StrippedContract+"\n"+x
            continue
    print(StrippedContract)
    return StrippedContract


if ('.sol' or '.rs') == ContractLanguage:
    WriteContract(StripSolContract(StripMeDaddy))
elif '.vy' == ContractLanguage:
    WriteContract(StripVyContract(StripMeDaddy))
