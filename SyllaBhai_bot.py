import syllabus as sy
from telegram import *
from telegram.ext import * 
import slate3k as slate
from config import TOKEN

fp_ece =  open('(1)ECE_only_theory.pdf', 'rb') 
doc_ece= slate.PDF(fp_ece)

fp_it =  open('(1)IT_only_theory.pdf', 'rb') 
doc_it = slate.PDF(fp_it)

fp_cse =  open('(1)CSE_only_theory.pdf', 'rb') 
doc_cse = slate.PDF(fp_cse)

fp_eee =  open('(1)EEE_only_theory.pdf', 'rb') 
doc_eee = slate.PDF(fp_eee)


bot = Bot(TOKEN)  

print(bot.get_me())
updater  = Updater(TOKEN, use_context=True)

dispatcher  = updater.dispatcher 

def start_function(update:Update,context:CallbackContext):

    s = "Namaskar 🙏 , Welcome to my bot 🤖 "  

    bot.send_message(
        chat_id = update.effective_chat.id,
        text = s
    )

    kbd_layout = [['/CSE', '/IT'], ['/ECE', '/EEE'],['/NOTES'],['/CONTACT_OWNER']]

    # converting layout to markup
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
    kbd = ReplyKeyboardMarkup(kbd_layout)

    # sending the reply so as to activate the keyboard
    update.message.reply_text(text="Select your Branch ", reply_markup=kbd)


    


start_value5 = CommandHandler("start" , start_function)

dispatcher.add_handler(start_value5)


def CON(update:Update,context:CallbackContext):

    bot.send_message(chat_id = update.effective_chat.id, text='''
~ Nihal Gupta ~

Username : @noble_nihal

Instagram : https://www.instagram.com/noble_nihal/
    ''')



cont = CommandHandler("CONTACT_OWNER" , CON)

dispatcher.add_handler(cont)

def NOTE(update:Update,context:CallbackContext ):
    
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = '''There you go, STUDY HARD !!

https://drive.google.com/drive/u/3/folders/1ICRW3UzUpcNnfhT7W9jn0WwyAS0WWbI-

More Notes for ECE and EEE will be added soon :) 

          
        '''    )
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = '''
Notes Provided by Prakriti MSIT  🙏        
        '''    )


NOTES = CommandHandler("NOTES", NOTE, pass_args=True)

dispatcher.add_handler(NOTES)


def EE(update:Update,context:CallbackContext):

    sem  = ["SEM1", "SEM2", "SEM3", "SEM4","SEM5","SEM6","SEM7","SEM8"]
    
    msg = update.effective_message.text
    # creating list of input buttons
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardbutton.html
    keyboard = [[
        InlineKeyboardButton(sem[0], callback_data=msg + " " + sem[0]), InlineKeyboardButton(sem[1], callback_data=msg + " " + sem[1])
    ], [
        InlineKeyboardButton(sem[2], callback_data=msg + " " + sem[2]), InlineKeyboardButton(sem[3], callback_data=msg + " " + sem[3])
    ], [
        InlineKeyboardButton(sem[4], callback_data=msg + " " + sem[4]), InlineKeyboardButton(sem[5], callback_data=msg + " " + sem[5])
    ],[
        InlineKeyboardButton(sem[6], callback_data=msg + " " + sem[6]), InlineKeyboardButton(sem[7], callback_data=msg + " " + sem[7])
    ]]

    # creating a reply markup of inline keyboard options
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardmarkup.html
    reply_markup = InlineKeyboardMarkup(keyboard)

    # sending the message to the current chat id
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    pass
    





eee = CommandHandler(["EEE","CSE","IT","ECE"], EE)

dispatcher.add_handler(eee)

def ALL(update:Update,context:CallbackContext):

    
    user_msg = update.effective_message.text
    m = sy.getDoc(user_msg[1:])
    doc = None
    if(m=="/ECE"):
        doc = doc_ece
    elif(m=="/CSE"):
        doc = doc_cse
    elif(m=="/IT"):
        doc = doc_it
    elif(m=="/EEE"):
        doc = doc_eee
    _sy= sy.units(user_msg,m,doc)
    s=""
    for key, value in _sy.items():
        s+= str(key) + " - " + value + "\n\n"
    
   
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = str(s)
    )



all_subjects = CommandHandler(["AM1","AP1","MP","ET","HVPE","FOC","AC","AM2","AP2","ED","ITP","EM","COMMSKILLS",
"EVS","AM3","AE1","MES","CNS","DS","ELMACH1","ELMACH2","AE2","PS1","EEMI","EMFT","CONS","PROSKILLS","PE","SNT",
"STLDEEE","CONSYS","INDMANAGE","PS2","UEEE","DSP","VLSI","MAM","PSP","ELDRIVES","ACS","TRANS","RER","PDS","TDAS",
"PNSSYS","MECHATRONICS","HVE","TOPICEEE","OOC","DMS","BI","DSD","PLCC","EMD","SEIHE","HVPE2","NFS","PSOC","APEPS",
"DIP","REAPS","ELMACH3","EEC","PSAS","ESD","ES","DCN","OOP","PPI","ISI","DC","EPQ","FCS","STLD","CG","AM4","COA","TOC",
"OOPS","CNSYS","ADA","SE","JAVA","IM","COMSK","CSP","CD","OS","WT","AI","MNM","ACN","CRYPT","WC","EMBED","CLOUD",
"DD","SWT","ST","DOTNET","ENTJAVA","SNA","GRID","ADVDA","PGM","CRYPLAB","MC","ADHOC","BIGDATA","SOCIALNA","SOFTC",
"BIOI","WEBAPP","ITC","HCI","NGN","GPS","SATCOM","ECOMM","DISSYS","ITSELECT","AM5","DIGCOM","COMPNET","INFOSEC","STQA",
"WIRELESSCOM","CT","IPR","DMBI","ACA","NLP","SAM","ADVDBMS","PC","CSYS","ML","MICROELEC","SC","OOSE","COMPVIS","SPM",
"WIBD","SOA","MULTISYS","POPL","TELENET","CSETOPICS","EIM","SAS","NAS","COMSY","EFT","CNSY","MICROENGI","AWP","EMBEDDED",
"OOCOM","ADSP","ITM","ADVVLSI","BIOINS","PLCSCADA","POWERELEC","RFDC","RAN","PM","EFE","ECETOPICS","CE","ASIC","INT",
"ASPROC","ROBOTICS","CGMT"],ALL)
dispatcher.add_handler(all_subjects)





def button(update:Update, context:CallbackContext):
    """
    callback method handling button press
    """
    
    # getting the callback query
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
    query: CallbackQuery = update.callback_query
    dat = query.data.split()
    
    if (dat[0]=="/EEE"):
        if(dat[1]=="SEM1"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM1    
/AP1
/MP
/ET
/HVPE
/FOC
/AC             
            '''
 
            )
        if(dat[1]=="SEM2"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM2
/AP2
/ED
/ITP
/EM
/COMMSKILLS
/EVS           
            '''

            )
        if(dat[1]=="SEM3"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM3
/AE1
/MES
/CNS
/DS
/ELMACH1          
            '''

            )
        if(dat[1]=="SEM4"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/ELMACH2
/AE2
/PS1
/EEMI
/EMFT
/CONS          
            '''

            )
        if(dat[1]=="SEM5"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/PROSKILLS
/PE
/SNT
/STLDEEE
/CONSYS
/INDMANAGE         
            '''

            )
        if(dat[1]=="SEM6"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/PS2
/UEEE
/DSP
/VLSI
/MAM
/PSP         
            '''

            )
        if(dat[1]=="SEM7"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/ELDRIVES
/ACS
/TRANS
/RER
/PDS
/TDAS
/PNSSYS
/MECHATRONICS
/HVE
/TOPICEEE
/OOC
/DMS
/BI
/DSD
/PLCC
/EMD
/SEIHE          
            '''

            )
        if(dat[1]=="SEM8"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/HVPE2
/NFS
/PSOC
/APEPS
/DIP
/REAPS
/ELMACH3
/EEC
/PSAS
/ESD
/ES 
/DCN
/OOP
/PPI
/ISI
/DC
/EPQ           
            '''

            )
# -----------------------------ECE-----------------------------
    if (dat[0]=="/ECE"):
        if(dat[1]=="SEM1"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM1
/AP1
/MP
/ET
/HVPE
/FOC
/AC             
            '''

            )
        if(dat[1]=="SEM2"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM2
/AP2
/ED
/ITP
/EM
/COMMSKILLS
/EVS           
            '''

            )
        if(dat[1]=="SEM3"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM3
/AE1
/STLD
/EIM
/DS
/SAS        
            '''

            )
        if(dat[1]=="SEM4"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM4
/AE2
/NAS
/COMSY
/EFT
/COA        
            '''

            )
        if(dat[1]=="SEM5"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/CSP
/DIGCOM
/MAM
/CNSY
/DSD
/IM      
            '''

            )
        if(dat[1]=="SEM6"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/MICROENGI
/ITC
/DSP
/VLSI
/DCN
/AWP       
            '''

            )
        if(dat[1]=="SEM7"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/EMBEDDED
/OOCOM
/WC
/ADSP
/ITM
/ADVVLSI
/BIOINS
/PLCSCADA
/POWERELEC
/RFDC
/DMS
/RER
/RAN
/PM
/EFE
/GRID
/PC
/SEIHE
/ECETOPICS        
            '''

            )
        if(dat[1]=="SEM8"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/HVPE2
/SATCOM
/ADHOC
/CE
/DIP
/ASIC
/MC
/INT
/GPS
/ASPROC
/ROBOTICS
/CGMT
/NGN        
            '''
            )



 # -------------------------------------IT------------------------------------------


    if (dat[0]=="/IT"):
        if(dat[1]=="SEM1"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM1
/AP1
/MP
/ET
/HVPE
/FOC
/AC             
            '''

            )
        if(dat[1]=="SEM2"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM2
/AP2
/ED
/ITP
/EM
/COMMSKILLS
/EVS           
            '''

            )
        if(dat[1]=="SEM3"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM3
/FCS
/STLD
/CNS
/DS
/CG          
            '''

            )
        if(dat[1]=="SEM4"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM4
/COA
/TOC
/DMS
/OOPS
/CNSYS         
            '''

            )
        if(dat[1]=="SEM5"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/ADA
/SE
/JAVA
/IM
/COMSK (*Comm system)
/CSP        
            '''

            )
        if(dat[1]=="SEM6"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/CD
/OS
/DCN
/WT
/AI
/MNM     
            '''

            )
        if(dat[1]=="SEM7"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/ACN
/CRYPT
/WC
/EMBED
/OOC
/CLOUD
/DD
/SWT
/ST
/DSP
/DOTNET
/ENTJAVA
/SNA
/GRID
/ADVDA
/PGM
/SEIHE         
            '''

            )
        if(dat[1]=="SEM8"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/MC
/ADHOC
/HVPE2
/BIGDATA
/SOCIALNA
/SOFTC
/BIOI
/WEBAPP
/VLSI
/ITC
/HCI
/DIP
/NGN
/GPS
/SATCOM
/ECOMM
/DISSYS
/ITSELECT          
            '''

            )
            
# ---------------------------------CSE------------------------
    if (dat[0]=="/CSE"):
        if(dat[1]=="SEM1"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM1
/AP1
/MP
/ET
/HVPE
/FOC
/AC             
            '''

            )
        if(dat[1]=="SEM2"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM2
/AP2
/ED
/ITP
/EM
/COMMSKILLS
/EVS           
            '''

            )
        if(dat[1]=="SEM3"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM3
/FCS
/STLD
/CNS
/DS
/CG         
            '''

            )
        if(dat[1]=="SEM4"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/AM4
/COA
/TOC
/DMS
/OOPS
/CNSYS        
            '''

            )
        if(dat[1]=="SEM5"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/ADA
/SE
/JAVA
/IM
/DIGCOM
/CSP        
            '''

            )
        if(dat[1]=="SEM6"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/CD
/OS
/COMPNET
/WT
/AI
/MNM         
            '''

            )
        if(dat[1]=="SEM7"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/INFOSEC
/STQA
/WIRELESSCOM
/CT
/IPR
/EMBED
/DMBI
/ACA
/NLP
/DSP
/SAM
/ADVDBMS
/PC
/ACN
/CSYS
/SEIHE          
            '''

            )
        if(dat[1]=="SEM8"):
            bot.send_message( chat_id = update.effective_chat.id,
            text = '''
👉 Your Subjects are :

/MC
/ML
/HVPE2
/DIP
/MICROELEC
/ADHOC
/SC
/VLSI
/DISSYS
/OOSE
/COMPVIS
/SPM
/HCI
/ITC
/WIBD
/SOA
/MULTISYS
/POPL
/TELENET
/CSETOPICS           
            '''

            )


            
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.answer
    query.answer()

    # editing message sent by the bot
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.edit_message_text
    query.edit_message_text(text= dat[0] + " " + dat[1])







dispatcher.add_handler(CallbackQueryHandler(button))
# def test_function5(update:Update,context:CallbackContext):
    
    
#     _sy= sy.getUnits(5)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value5 = CommandHandler("CG" , test_function5, pass_args=True)

# dispatcher.add_handler(start_value5)

# def test_function0(update:Update,context:CallbackContext ):
    
    
#     _sy= sy.getUnits(0)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value0 = CommandHandler("AM3" , test_function0, pass_args=True)

# dispatcher.add_handler(start_value0)

# def test_function1(update:Update,context:CallbackContext ):
    
    
#     _sy= sy.getUnits(1)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value1 = CommandHandler("FCS" , test_function1, pass_args=True)

# dispatcher.add_handler(start_value1)

# def test_function2(update:Update,context:CallbackContext ):
    
    
#     _sy= sy.getUnits(2)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value2 = CommandHandler("STLD" , test_function2, pass_args=True)

# dispatcher.add_handler(start_value2)

# def test_function3(update:Update,context:CallbackContext ):
    
    
#     _sy= sy.getUnits(3)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value3 = CommandHandler("CS" , test_function3, pass_args=True)

# dispatcher.add_handler(start_value3)

# def test_function4(update:Update,context:CallbackContext ):
    
    
#     _sy= sy.getUnits(4)
#     s=""
#     for key, value in _sy.items():
#         s+= str(key) + " - " + value + "\n\n"

#     bot.send_message(
#         chat_id = update.effective_chat.id,
#         text = str(s)
#     )


# start_value4 = CommandHandler("DS", test_function4, pass_args=True)

# dispatcher.add_handler(start_value4)





updater.start_polling()