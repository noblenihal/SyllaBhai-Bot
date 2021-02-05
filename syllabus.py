import slate3k as slate
from slate3k.classes import PDF 



def select_doc(usr_msg):
    doc = None
    if (usr_msg  == "/CSE"):
        fp =  open('(1)CSE_only_theory.pdf', 'rb') 
        doc = slate.PDF(fp)
    if (usr_msg  == "/IT"):
        fp =  open('(1)IT_only_theory.pdf', 'rb') 
        doc = slate.PDF(fp)
    if (usr_msg  == "/ECE"):
        fp =  open('(1)ECE_only_theory.pdf', 'rb') 
        doc = slate.PDF(fp)
    if (usr_msg  == "/EEE"):
        fp =  open('(1)EEE_only_theory.pdf', 'rb') 
        doc = slate.PDF(fp)

    return doc

        


def getSubjects(doc):

    pg=doc.__len__()
    subjects  = {}

    for num in range(0,pg):
        try:
            data  = doc[num].split()

            i = None
            j = None

            for index, text in enumerate(data):
                
                if (text ==":" and data[index-1]=="Paper"):

                    i= index
                    break
                
                elif (text == "Paper:"):
                    i=index
                    break
            
            for index, text in enumerate(data):
                
                if (text == "L"):
                    j= index
                    if (j<i):
                        continue
                    else:
                        break
                elif (text == "3" or text == "2" or text =="1"):
                    j= index
                    break

            subjects[num] =(" ".join(data[i+1:j]))

        except TypeError:
            pass

    return subjects


def getSub_name(Abbr:str,msg, subject:dict):

    list_of_abbr =[]
    print(msg)
    if (msg == "/ECE"):
        list_of_abbr  = ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","AE1","STLD","EIM","DS","SAS","AM4","AE2","NAS","COMSY","EFT","COA","CSP","DIGCOM","MAM","CNSY","DSD","IM","MICROENGI","ITC","DSP","VLSI","DCN","AWP","EMBEDDED","OOCOM","WC","ADSP","ITM","ADVVLSI","BIOINS","PLCSCADA","POWERELEC","RFDC","DMS","RER","RAN","PM","EFE","GRID","PC","SEIHE","ECETOPICS","BIOINS","HVPE2","SATCOM","ADHOC","CE","DIP","ASIC","MC","INT","GPS","ASPROC","ROBOTICS","CGMT","NGN"]
    if (msg == "/IT"):
        list_of_abbr  = ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","FCS","STLD","CnS","DS","CG","AM4","COA","TOC","DMS","OOPs","CNSYS","ADA","SE","JAVA","IM","ComSk","CSP","CD","OS","DCN","WT","AI","MnM","ACN","CRYPT","WC","Embed","OOC","CLOUD","DD","SWT","ST","DSP","DOTNET","ENTJAVA","SNA","GRID","ADVDA","PGM","SEIHE","CRYPLAB","MC","ADHOC","HVPE2","BIGDATA","SOCIALNA","SOFTC","BIOI","WEBAPP","VLSI","ITC","HCI","DIP","NGN","GPS","SATCOM","ECOMM","DISSYS","ITSELECT"]
    if (msg == "/CSE"):
        list_of_abbr  = ["AM1","AP1","MP","ET","AM5","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","FCS","STLD","CNS","DS","CG","AM4","COA","TOC","DMS","OOPS","CNSYS","ADA","SE","JAVA","IM","DIGCOM","CSP","CD","OS","COMPNET","WT","AI","MNM","INFOSEC","STQA","WIRELESSCOM","CT","IPR","EMBED","DMBI","ACA","NLP","DSP","SAM","ADVDBMS","PC","ACN","CSYS","SEIHE","MC","ML","HVPE2","DIP","MICROELEC","ADHOC","SC","VLSI","DISSYS","OOSE","COMPVIS","SPM","HCI","ITC","WIBD","SOA","MULTISYS","POPL","TELENET","CSETOPICS"]
    if (msg == "/EEE"):
        list_of_abbr  = ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","AE1","MES","CNS","DS","ELMACH1","ELMACH2","AE2","PS1","EEMI","EMFT","CONS","PROSKILLS","PE","SNT","STLDEEE","CONSYS","INDMANAGE","PS2","UEEE","DSP","VLSI","MAM","PSP","ELDRIVES","ACS","TRANS","RER","PDS","TDAS","PNSSYS","MECHATRONICS","HVE","TOPICEEE","OOC","DMS","BI","DSD","PLCC","EMD","SEIHE","HVPE2","NFS","PSOC","APEPS","DIP","REAPS","ELMACH3","EEC","PSAS","ESD","ES","DCN","OOP","PPI","ISI","DC","EPQ"]
    
    print(list_of_abbr)

    pg_list = []
    for key in subject.keys():
        pg_list.append(key)
    
    print(pg_list)
    new_dic={}
    for i in range(0,len(pg_list)):
        pg = pg_list[i]
        a = list_of_abbr[i]
        new_dic[pg]=a

    return new_dic
  
    # for keys,val in new_dic.items():
    #     if (Abbr == val):
    #         return keys
    # for key,val in abr_sub :
    #     if (key == Abbr):
    #         return val

    

def getUnits(Abbr):
        
        
        msg, doc = select_doc(getDoc(Abbr))
        
        subject = getSubjects(doc)
        print(len(subject))

        num = getSub_name(Abbr,msg, subject)
        
        return num
        units = {}
        data  = doc[num].split()
        
        i = 0
        j= len(data)

        for u_num in range(1,5):
            
           
            for index, text in enumerate(data[i:j]):
                if ("UNIT" in text or "Unit" in text ):
                    i+= index
                    
                    break
            for index, text in enumerate(data[i+1:]):
                if ("UNIT" in text or "Unit" in text or "Text" in text ):
                    j= index+i
                    
                    break
                else:
                    j=index
            
            units[u_num] = (" ".join(data[i:j]))
            
            i=j
            
            j=len(data)
            

        return units 
        

def getDoc(abbr):

    doc_value =  {
        "/ECE": ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","AE1","STLD","EIM","DS","SAS","AM4","AE2","NAS","COMSY","EFT","COA","CSP","DIGCOM","MAM","CNSY","DSD","IM","MICROENGI","ITC","DSP","VLSI","DCN","AWP","EMBEDDED","OOCOM","WC","ADSP","ITM","ADVVLSI","BIOINS","PLCSCADA","POWERELEC","RFDC","DMS","RER","RAN","PM","EFE","GRID","PC","SEIHE","ECETOPICS","BIOINS","HVPE2","SATCOM","ADHOC","CE","DIP","ASIC","MC","INT","GPS","ASPROC","ROBOTICS","CGMT","NGN"],
        "/IT" : ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","FCS","STLD","CnS","DS","CG","AM4","COA","TOC","DMS","OOPs","CNSYS","ADA","SE","JAVA","IM","ComSk","CSP","CD","OS","DCN","WT","AI","MnM","ACN","CRYPT","WC","Embed","OOC","CLOUD","DD","SWT","ST","DSP","DOTNET","ENTJAVA","SNA","GRID","ADVDA","PGM","SEIHE","CRYPLAB","MC","ADHOC","HVPE2","BIGDATA","SOCIALNA","SOFTC","BIOI","WEBAPP","VLSI","ITC","HCI","DIP","NGN","GPS","SATCOM","ECOMM","DISSYS","ITSELECT"],
        "/CSE" : ["AM1","AP1","MP","ET","AM5","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","FCS","STLD","CNS","DS","CG","AM4","COA","TOC","DMS","OOPS","CNSYS","ADA","SE","JAVA","IM","DIGCOM","CSP","CD","OS","COMPNET","WT","AI","MNM","INFOSEC","STQA","WIRELESSCOM","CT","IPR","EMBED","DMBI","ACA","NLP","DSP","SAM","ADVDBMS","PC","ACN","CSYS","SEIHE","MC","ML","HVPE2","DIP","MICROELEC","ADHOC","SC","VLSI","DISSYS","OOSE","COMPVIS","SPM","HCI","ITC","WIBD","SOA","MULTISYS","POPL","TELENET","CSETOPICS"],
        "/EEE" : ["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS","EVS","AM3","AE1","MES","CNS","DS","ELMACH1","ELMACH2","AE2","PS1","EEMI","EMFT","CONS","PROSKILLS","PE","SNT","STLDEEE","CONSYS","INDMANAGE","PS2","UEEE","DSP","VLSI","MAM","PSP","ELDRIVES","ACS","TRANS","RER","PDS","TDAS","PNSSYS","MECHATRONICS","HVE","TOPICEEE","OOC","DMS","BI","DSD","PLCC","EMD","SEIHE","HVPE2","NFS","PSOC","APEPS","DIP","REAPS","ELMACH3","EEC","PSAS","ESD","ES","DCN","OOP","PPI","ISI","DC","EPQ"]

    }
    
    for key, val in doc_value.items():
        for itm in val:
            if (itm==abbr):
                return key



################ THIS WAS GENERATED USING THE PREVIOUS SCRIPT ###################

def units(u:str, m:str, doc:PDF):

    usr_msg = u[1:]
    # msg =Abbr[1:]
    # msg = getDoc(m)
    # doc = select_doc(msg)
    pg_dict={}
    if (m=="/EEE"):
        
        pg_dict = {0: 'AM1', 1: 'AP1', 2: 'MP', 3: 'ET', 4: 'HVPE', 5: 'FOC', 6: 'AC', 7: 'AM2', 8: 'AP2', 9: 'ED', 10: 'ITP', 11: 'EM', 12: 'COMMSKILLS', 13: 'EVS', 15: 'AM3', 16: 'AE1', 17: 'MES', 18: 'CNS', 19: 'DS', 20: 'ELMACH1', 21: 'ELMACH2', 22: 'AE2', 23: 'PS1', 24: 'EEMI', 25: 'EMFT', 26: 'CONS', 27: 'PROSKILLS', 29: 'PE', 30: 'SNT', 31: 'STLDEEE', 32: 'CONSYS', 33: 'INDMANAGE', 34: 'PS2', 35: 'UEEE', 36: 'DSP', 37: 'VLSI', 38: 'MAM', 39: 'PSP', 40: 'ELDRIVES', 41: 'ACS', 42: 'TRANS', 43: 'RER', 44: 'PDS', 45: 'TDAS', 46: 'PNSSYS', 47: 'MECHATRONICS', 49: 'HVE', 50: 'TOPICEEE', 51: 'OOC', 52: 'DMS', 53: 'BI', 54: 'DSD', 55: 'PLCC', 
                    56: 'EMD', 57: 'SEIHE', 58: 'HVPE2', 61: 'NFS', 62: 'PSOC', 63: 'APEPS', 64: 'DIP', 65: 'REAPS', 66: 'ELMACH3', 67: 'EEC', 68: 'PSAS', 69: 'ESD', 70: 'ES', 71: 'DCN', 72: 'OOP', 73: 'PPI', 74: 'ISI', 75: 'DC', 76: 'EPQ'}
    elif (m=="/ECE"):
        pg_dict = {0: 'AM1', 2: 'AP1', 3: 'MP', 4: 'ET', 5: 'HVPE', 6: 'FOC', 7: 'AC', 8: 'AM2', 9: 'AP2', 10: 'ED', 11: 'ITP', 12: 'EM', 13: 'COMMSKILLS', 14: 'EVS', 16: 'AM3', 17: 'AE1', 18: 'STLD', 19: 'EIM', 20: 'DS', 21: 'SAS', 23: 'AM4', 24: 'AE2', 25: 'NAS', 26: 'COMSY', 27: 'EFT', 28: 'COA', 29: 'CSP', 31: 'DIGCOM', 32: 'MAM', 33: 'CNSY', 34: 'DSD', 35: 'IM', 36: 'MICROENGI', 37: 'ITC', 38: 'DSP', 39: 'VLSI', 40: 'DCN', 41: 'AWP', 42: 'EMBEDDED', 43: 'OOCOM', 44: 'WC', 45: 'ADSP', 46: 'ITM', 47: 'ADVVLSI', 48: 'BIOINS', 49: 'PLCSCADA', 50: 'POWERELEC', 51: 'RFDC', 52: 'DMS', 53: 'RER', 54: 'RAN', 55: 'PM', 56: 'EFE', 57: 'GRID', 58: 'PC', 59: 'SEIHE', 60: 'ECETOPICS', 61: 'BIOINS', 62: 'HVPE2', 65: 'SATCOM', 66: 'ADHOC', 68: 'CE', 70: 'DIP', 71: 'ASIC', 72: 'MC', 74: 'INT', 75: 'GPS', 76: 
                    'ASPROC', 77: 'ROBOTICS', 78: 'CGMT', 79: 'NGN'}
    elif (m=="/CSE"):
        pg_dict = {0: 'AM1', 1: 'AP1', 2: 'MP', 3: 'ET', 4: 'AM5', 5: 'FOC', 6: 'AC', 7: 'AM2', 8: 'AP2', 9: 'ED', 10: 'ITP', 11: 'EM', 12: 'COMMSKILLS', 13: 'EVS', 15: 'AM3', 
                    16: 'FCS', 17: 'STLD', 18: 'CNS', 19: 'DS', 20: 'CG', 21: 'AM4', 22: 'COA', 23: 'TOC', 24: 'DMS', 25: 'OOPS', 26: 'CNSYS', 27: 'ADA', 28: 'SE', 29: 'JAVA', 30: 'IM', 31: 'DIGCOM', 32: 'CSP', 34: 'CD', 35: 'OS', 36: 'COMPNET', 37: 'WT', 38: 'AI', 39: 'MNM', 40: 'INFOSEC', 41: 'STQA', 42: 'WIRELESSCOM', 43: 'CT', 44: 'IPR', 45: 'EMBED', 46: 'DMBI', 47: 'ACA', 48: 'NLP', 49: 'DSP', 50: 'SAM', 52: 'ADVDBMS', 53: 'PC', 54: 'ACN', 55: 'CSYS', 56: 'SEIHE', 57: 'MC', 59: 'ML', 
                    60: 'HVPE2', 62: 'DIP', 63: 'MICROELEC', 64: 'ADHOC', 66: 'SC', 67: 'VLSI', 68: 'DISSYS', 69: 'OOSE', 70: 'COMPVIS', 71: 'SPM', 72: 'HCI', 73: 'ITC', 74: 'WIBD', 75: 'SOA', 76: 'MULTISYS', 77: 'POPL', 78: 'TELENET', 79: 'CSETOPICS'}
    elif (m=="/IT"):
        pg_dict = {0: 'AM1', 1: 'AP1', 2: 'MP', 3: 'ET', 4: 'HVPE', 5: 'FOC', 6: 'AC', 7: 'AM2', 8: 'AP2', 9: 'ED', 10: 'ITP', 11: 'EM', 12: 'COMMSKILLS', 13: 'EVS', 15: 'AM3', 16: 'FCS', 17: 'STLD', 18: 'CnS', 19: 'DS', 20: 'CG', 21: 'AM4', 22: 'COA', 23: 'TOC', 24: 'DMS', 25: 'OOPs', 26: 'CNSYS', 27: 'ADA', 28: 'SE', 29: 'JAVA', 30: 'IM', 31: 'ComSk', 32: 'CSP', 34: 'CD', 35: 'OS', 36: 'DCN', 37: 'WT', 38: 'AI', 39: 'MnM', 40: 'ACN', 41: 'CRYPT', 42: 'WC', 43: 'Embed', 44: 'OOC', 45: 'CLOUD', 46: 'DD', 47: 'SWT', 48: 'ST', 49: 'DSP', 50: 'DOTNET', 52: 'ENTJAVA', 53: 'SNA', 54: 'GRID', 55: 'ADVDA', 56: 'PGM', 57: 'SEIHE', 58: 'CRYPLAB', 59: 
                    'MC', 61: 'ADHOC', 63: 'HVPE2', 65: 'BIGDATA', 66: 'SOCIALNA', 67: 'SOFTC', 68: 'BIOI', 69: 'WEBAPP', 71: 'VLSI', 72: 'ITC', 73: 'HCI', 74: 'DIP', 75: 'NGN', 
                    76: 'GPS', 77: 'SATCOM', 78: 'ECOMM', 80: 'DISSYS', 81: 'ITSELECT'}
    
    num = 1
    for key,val in pg_dict.items():
        if (val == usr_msg):
            num = key
            
    units = {}

    data  = doc[num].split()
        
    i = 0
    j= len(data)

    for u_num in range(1,5):
                      
        for index, text in enumerate(data[i:j]):
            if ("UNIT" in text or "Unit" in text ):
                i+= index
                break
        for index, text in enumerate(data[i+1:]):

            if ("UNIT" in text or "Unit" in text or "Text" in text ):
                j= index+i
                break
            elif (index == len(data)-1):
                j=index
                       
        units[u_num] = (" ".join(data[i:j]))
            
        i=j
            
        j=len(data)
    return units 



# print(getUnits("CSETOPICS"))





# def decodeAbbr(msg):

    


# def getSyllabus():

#     syllabus = {}
#     subjs = getSubjects()

#     for i in range(0,6):
#         sub = subjs[i]
#         syllabus[sub] = getUnits(sub)

#     return syllabus



