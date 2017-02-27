from django.db import models
import json
from os.path import isfile, join

class UserSelection(models.Model):
    #defaults
    default_userid=32
    default_cloc=[{'c0': 'Off'}, {'c1': 'RiskOn'}, {'c2': 'RiskOff'}, {'c3': 'LowestEquity'}, {'c4': 'HighestEquity'},
                {'c5': 'AntiHighestEquity'}, {'c6': 'Anti50/50'}, {'c7': 'Seasonality'}, {'c8': 'Anti-Seasonality'},
                {'c9': 'Previous'}, {'c10': 'None'}, {'c11': 'Anti-Previous'}, {'c12': 'None'}, {'c13': 'None'},
                {'c14': 'None'}, ]
    json_cloc = json.dumps(default_cloc)
    default_selection={'v4futures': ['Off', 'False'], 'v4micro': ['Off', 'False'], 'v4mini': ['Off', 'False']}
    default_board={"1":["0.5LastSIG","RiskOn"],"2":["AntiPrevACT","0.5LastSIG","RiskOn"],"3":["prevACT","0.5LastSIG","RiskOn"],"4":["0.5LastSIG","RiskOff"],"5":["AntiPrevACT","0.5LastSIG","RiskOff"],"6":["prevACT","0.5LastSIG","RiskOff"],"7":["1LastSIG","RiskOn"],"8":["AntiPrevACT","1LastSIG","RiskOn"],"9":["prevACT","1LastSIG","RiskOn"],"10":["1LastSIG","RiskOff"],"11":["AntiPrevACT","1LastSIG","RiskOff"],"12":["prevACT","1LastSIG","RiskOff"],"13":["Anti1LastSIG","RiskOn"],"14":["AntiPrevACT","Anti1LastSIG","RiskOn"],"15":["prevACT","Anti1LastSIG","RiskOn"],"16":["Anti1LastSIG","RiskOff"],"17":["AntiPrevACT","Anti1LastSIG","RiskOff"],"18":["prevACT","Anti1LastSIG","RiskOff"],"19":["Anti0.75LastSIG","RiskOn"],"20":["AntiPrevACT","Anti0.75LastSIG","RiskOn"],"21":["prevACT","Anti0.75LastSIG","RiskOn"],"22":["Anti0.75LastSIG","RiskOff"],"23":["AntiPrevACT","Anti0.75LastSIG","RiskOff"],"24":["prevACT","Anti0.75LastSIG","RiskOff"],"25":["LastSEA","RiskOn"],"26":["AntiPrevACT","LastSEA","RiskOn"],"27":["prevACT","LastSEA","RiskOn"],"28":["LastSEA","RiskOff"],"29":["AntiPrevACT","LastSEA","RiskOff"],"30":["prevACT","LastSEA","RiskOff"],"31":["AntiSEA","RiskOn"],"32":["AntiPrevACT","AntiSEA","RiskOn"],"33":["prevACT","AntiSEA","RiskOn"],"34":["AntiSEA","RiskOff"],"35":["AntiPrevACT","AntiSEA","RiskOff"],"36":["prevACT","AntiSEA","RiskOff"],"Off":["None"],"RiskOn":["RiskOn"],"RiskOff":["RiskOff"],"LowestEquity":["0.5LastSIG"],"HighestEquity":["1LastSIG"],"AntiHighestEquity":["Anti1LastSIG"],"Anti50/50":["Anti0.75LastSIG"],"Seasonality":["LastSEA"],"Anti-Seasonality":["AntiSEA"],"Previous":["prevACT"],"Anti-Previous":["AntiPrevACT"],}
    default_list_boxstyles = [{'c0':{'text':'Off','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'225823','fill-R':'34','fill-G':'88','fill-B':'35','filename':''}},{'c1':{'text':'RiskOn','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'BE0032','fill-R':'190','fill-G':'0','fill-B':'50','filename':''}},{'c2':{'text':'RiskOff','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'222222','fill-R':'34','fill-G':'34','fill-B':'34','filename':''}},{'c3':{'text':'LowestEquity','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F38400','fill-R':'243','fill-G':'132','fill-B':'0','filename':''}},{'c4':{'text':'HighestEquity','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'FFFF00','fill-R':'255','fill-G':'255','fill-B':'0','filename':''}},{'c5':{'text':'AntiHighestEquity','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'A1CAF1','fill-R':'161','fill-G':'202','fill-B':'241','filename':''}},{'c6':{'text':'Anti50/50','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'C2B280','fill-R':'194','fill-G':'178','fill-B':'128','filename':''}},{'c7':{'text':'Seasonality','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'E68FAC','fill-R':'230','fill-G':'143','fill-B':'172','filename':''}},{'c8':{'text':'Anti-Seasonality','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F99379','fill-R':'249','fill-G':'147','fill-B':'121','filename':''}},{'c9':{'text':'Previous','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'654522','fill-R':'101','fill-G':'69','fill-B':'34','filename':''}},{'c10':{'text':'None','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F2F3F4','fill-R':'242','fill-G':'243','fill-B':'244','filename':''}},{'c11':{'text':'Anti-Previous','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'008856','fill-R':'0','fill-G':'136','fill-B':'86','filename':''}},{'c12':{'text':'None','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F2F3F4','fill-R':'242','fill-G':'243','fill-B':'244','filename':''}},{'c13':{'text':'None','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F2F3F4','fill-R':'242','fill-G':'243','fill-B':'244','filename':''}},{'c14':{'text':'None','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'F2F3F4','fill-R':'242','fill-G':'243','fill-B':'244','filename':''}},{'b_clear_all':{'text':'Clear All Bets','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_create_new':{'text':'Create New Board','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_confirm_orders':{'text':'Save Orders','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'33CC00','fill-R':'51','fill-G':'204','fill-B':'0','filename':''}},{'b_order_ok':{'text':'Enter Orders','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'29ABE2','fill-R':'41','fill-G':'171','fill-B':'226','filename':''}},{'b_order_cancel':{'text':'Cancel','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_order_active':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'33CC00','fill-R':'51','fill-G':'204','fill-B':'0','filename':''}},{'b_order_inactive':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_save_ok':{'text':'Place Immediate Orders Now','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'29ABE2','fill-R':'41','fill-G':'171','fill-B':'226','filename':''}},{'b_save_cancel':{'text':'OK/Change Immediate Orders','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'d_order_dialog':{'text':'<b>MOC:</b> Market-On-Close Order. New signals are generated at the close of the market will be placed as Market Orders before the close.<br><b>Immediate:</b> Immediate uses signals generated as of the last Market Close.  If the market is closed, order will be placed as Market-On-Open orders. Otherwise, it will be placed as Market Orders. At the next trigger time, new signals will be placed as MOC orders.','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'d_save_dialog':{'text':'<center><b>Orders successfully saved.</b><br></center> MOC orders will be placed at the trigger times. If you have entered any immediate orders you may place them now or you may cancel and save different orders.  After the page is refreshed you can check order status to see if the orders were placed.','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'text_table':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'16','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_table_title':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_datetimenow':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_triggertimes':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_performance':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_performance_account':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_immediate_orders':{'text':'Immediate Order Info','text-color':'000000','text-font':'Arial Black','text-style':'bold','text-size':'8','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'chip_v4micro':{'text':'50K','text-color':'000000','text-font':'','text-style':'','text-size':'','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':'chip_maroon.png'}},{'chip_v4mini':{'text':'100K','text-color':'000000','text-font':'','text-style':'','text-size':'','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':'chip_purple.png'}},{'chip_v4futures':{'text':'250K','text-color':'000000','text-font':'','text-style':'','text-size':'','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':'chip_orange.png'}},{"1": {"fill-R": "229", "fill-B": "134", "text-size": "24", "fill-Hex": "E59A86", "fill-G": "154", "text-color": "000000", "text": "1", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"2": {"fill-R": "168", "fill-B": "95", "text-size": "24", "fill-Hex": "A87F5F", "fill-G": "127", "text-color": "000000", "text": "2", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"3": {"fill-R": "194", "fill-B": "82", "text-size": "24", "fill-Hex": "C26F52", "fill-G": "111", "text-color": "000000", "text": "3", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"4": {"fill-R": "190", "fill-B": "130", "text-size": "24", "fill-Hex": "BEA382", "fill-G": "163", "text-color": "000000", "text": "4", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"5": {"fill-R": "129", "fill-B": "91", "text-size": "24", "fill-Hex": "81885B", "fill-G": "136", "text-color": "000000", "text": "5", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"6": {"fill-R": "155", "fill-B": "78", "text-size": "24", "fill-Hex": "9B774E", "fill-G": "119", "text-color": "000000", "text": "6", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"7": {"fill-R": "232", "fill-B": "134", "text-size": "24", "fill-Hex": "E8B986", "fill-G": "185", "text-color": "000000", "text": "7", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"8": {"fill-R": "171", "fill-B": "95", "text-size": "24", "fill-Hex": "AB9E5F", "fill-G": "158", "text-color": "000000", "text": "8", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"9": {"fill-R": "197", "fill-B": "82", "text-size": "24", "fill-Hex": "C58D52", "fill-G": "141", "text-color": "000000", "text": "9", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"10": {"fill-R": "193", "fill-B": "130", "text-size": "24", "fill-Hex": "C1C182", "fill-G": "193", "text-color": "000000", "text": "10", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"11": {"fill-R": "132", "fill-B": "91", "text-size": "24", "fill-Hex": "84A75B", "fill-G": "167", "text-color": "000000", "text": "11", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"12": {"fill-R": "158", "fill-B": "78", "text-size": "24", "fill-Hex": "9E964E", "fill-G": "150", "text-color": "000000", "text": "12", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"13": {"fill-R": "208", "fill-B": "194", "text-size": "24", "fill-Hex": "D0ACC2", "fill-G": "172", "text-color": "000000", "text": "13", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"14": {"fill-R": "148", "fill-B": "155", "text-size": "24", "fill-Hex": "94919B", "fill-G": "145", "text-color": "000000", "text": "14", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"15": {"fill-R": "173", "fill-B": "142", "text-size": "24", "fill-Hex": "AD808E", "fill-G": "128", "text-color": "000000", "text": "15", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"16": {"fill-R": "169", "fill-B": "190", "text-size": "24", "fill-Hex": "A9B4BE", "fill-G": "180", "text-color": "000000", "text": "16", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"17": {"fill-R": "109", "fill-B": "151", "text-size": "24", "fill-Hex": "6D9997", "fill-G": "153", "text-color": "000000", "text": "17", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"18": {"fill-R": "134", "fill-B": "138", "text-size": "24", "fill-Hex": "86898A", "fill-G": "137", "text-color": "000000", "text": "18", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"19": {"fill-R": "217", "fill-B": "166", "text-size": "24", "fill-Hex": "D9A6A6", "fill-G": "166", "text-color": "000000", "text": "19", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"20": {"fill-R": "156", "fill-B": "127", "text-size": "24", "fill-Hex": "9C8B7F", "fill-G": "139", "text-color": "000000", "text": "20", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"21": {"fill-R": "181", "fill-B": "114", "text-size": "24", "fill-Hex": "B57A72", "fill-G": "122", "text-color": "000000", "text": "21", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"22": {"fill-R": "178", "fill-B": "162", "text-size": "24", "fill-Hex": "B2AEA2", "fill-G": "174", "text-color": "000000", "text": "22", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"23": {"fill-R": "117", "fill-B": "123", "text-size": "24", "fill-Hex": "75937B", "fill-G": "147", "text-color": "000000", "text": "23", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"24": {"fill-R": "142", "fill-B": "110", "text-size": "24", "fill-Hex": "8E836E", "fill-G": "131", "text-color": "000000", "text": "24", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"25": {"fill-R": "226", "fill-B": "177", "text-size": "24", "fill-Hex": "E29DB1", "fill-G": "157", "text-color": "000000", "text": "25", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"26": {"fill-R": "165", "fill-B": "138", "text-size": "24", "fill-Hex": "A5828A", "fill-G": "130", "text-color": "000000", "text": "26", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"27": {"fill-R": "190", "fill-B": "125", "text-size": "24", "fill-Hex": "BE717D", "fill-G": "113", "text-color": "000000", "text": "27", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"28": {"fill-R": "187", "fill-B": "173", "text-size": "24", "fill-Hex": "BBA5AD", "fill-G": "165", "text-color": "000000", "text": "28", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"29": {"fill-R": "126", "fill-B": "134", "text-size": "24", "fill-Hex": "7E8B86", "fill-G": "139", "text-color": "000000", "text": "29", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"30": {"fill-R": "151", "fill-B": "121", "text-size": "24", "fill-Hex": "977A79", "fill-G": "122", "text-color": "000000", "text": "30", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"31": {"fill-R": "230", "fill-B": "164", "text-size": "24", "fill-Hex": "E69EA4", "fill-G": "158", "text-color": "000000", "text": "31", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"32": {"fill-R": "170", "fill-B": "125", "text-size": "24", "fill-Hex": "AA837D", "fill-G": "131", "text-color": "000000", "text": "32", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"33": {"fill-R": "195", "fill-B": "112", "text-size": "24", "fill-Hex": "C37270", "fill-G": "114", "text-color": "000000", "text": "33", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"34": {"fill-R": "191", "fill-B": "160", "text-size": "24", "fill-Hex": "BFA6A0", "fill-G": "166", "text-color": "000000", "text": "34", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"35": {"fill-R": "131", "fill-B": "121", "text-size": "24", "fill-Hex": "838C79", "fill-G": "140", "text-color": "000000", "text": "35", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}}, {"36": {"fill-R": "156", "fill-B": "108", "text-size": "24", "fill-Hex": "9C7B6C", "fill-G": "123", "text-color": "000000", "text": "36", "text-style": "bold", "text-font": "Book Antigua", "filename": ""}},]
    default_list_customboard=[{'background':{'text':'','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'F2F3F4','fill-R':'242','fill-G':'243','fill-B':'244','filename':''}},{'c0':{'text':'Off','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'cNone':{'text':'','text-color':'FFFFFF','text-font':'Book Antigua','text-style':'bold','text-size':'24','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_auto_select':{'text':'Auto-Select','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_reset_colors':{'text':'Reset','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_save_colors':{'text':'Save Colors','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'33CC00','fill-R':'51','fill-G':'204','fill-B':'0','filename':''}},{'b_reset_board':{'text':'Reset','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'FFFFFF','fill-R':'255','fill-G':'255','fill-B':'255','filename':''}},{'b_save_board':{'text':'Save Colors','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'33CC00','fill-R':'51','fill-G':'204','fill-B':'0','filename':''}},{'text_components':{'text':'','text-color':'000000','text-font':'Book Antigua','text-style':'normal','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_choose_colors':{'text':'<b>Step 1</b> <br>Click on the component box to choose the colors for the components you want to use. Once you are done click the save button. If you do not want to choose custom colors, click Auto-Select and save.','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'text_place_components':{'text':'<b>Step 2</b> <br>Drag and drop components to blank boxes below. You may leave boxes blank.','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'d_save_color_error':{'text':'Please color "Off" component and at least one other component.','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'d_save_board_error':{'text':'Please place at least one component in one of the blank boxes.','text-color':'000000','text-font':'Book Antigua','text-style':'bold','text-size':'18','fill-Hex':'','fill-R':'','fill-G':'','fill-B':'','filename':''}},{'list_loadingscreens':[{'newboard':'Please wait 10-15 minutes for the charts to be recreated.'},{'immediate':'Please wait up to five minutes for immediate orders to be processed.'},{'else':'Please wait up for the board to load.'},]},{'list_autoselect':[{'fill-colorname':'red','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'BE0032','fill-R':'190','fill-G':'0','fill-B':'50'},{'fill-colorname':'black','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'222222','fill-R':'34','fill-G':'34','fill-B':'34'},{'fill-colorname':'lime','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'4FF773','fill-R':'79','fill-G':'247','fill-B':'115'},{'fill-colorname':'yellow','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'FFFF00','fill-R':'255','fill-G':'255','fill-B':'0'},{'fill-colorname':'lightblue','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'A1CAF1','fill-R':'161','fill-G':'202','fill-B':'241'},{'fill-colorname':'buff','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'C2B280','fill-R':'194','fill-G':'178','fill-B':'128'},{'fill-colorname':'purplishpink','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'E68FAC','fill-R':'230','fill-G':'143','fill-B':'172'},{'fill-colorname':'yellowishpink','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'F99379','fill-R':'249','fill-G':'147','fill-B':'121'},{'fill-colorname':'orange','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'F38400','fill-R':'243','fill-G':'132','fill-B':'0'},{'fill-colorname':'grey','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'848482','fill-R':'132','fill-G':'132','fill-B':'130'},{'fill-colorname':'green','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'008856','fill-R':'0','fill-G':'136','fill-B':'86'},{'fill-colorname':'blue','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'0067A5','fill-R':'0','fill-G':'103','fill-B':'165'},{'fill-colorname':'violet','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'604E97','fill-R':'96','fill-G':'78','fill-B':'151'},{'fill-colorname':'purplishred','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'B3446C','fill-R':'179','fill-G':'68','fill-B':'108'},{'fill-colorname':'yellowishbrown','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'654522','fill-R':'101','fill-G':'69','fill-B':'34'},{'fill-colorname':'reddishorange','text-color':'','text-font':'','text-style':'','text-size':'','fill-Hex':'EA2819','fill-R':'235','fill-G':'40','fill-B':'25'},]},]
    default_custom_signals={'AD': {'desc': '<a href="/static/images/v4_AD_BRANK.png" target="_blank">Australian Dollar-CME</a>',  'group': 'currency',  'signals': 1.0}, 'BO': {'desc': '<a href="/static/images/v4_BO_BRANK.png" target="_blank">Soybean Oil-CBT </a>',  'group': 'grain',  'signals': 1.0}, 'BP': {'desc': '<a href="/static/images/v4_BP_BRANK.png" target="_blank">British Pound-CME</a>',  'group': 'currency',  'signals': 1.0}, 'C': {'desc': '<a href="/static/images/v4_C_BRANK.png" target="_blank">Corn-CBT </a>',  'group': 'grain',  'signals': 1.0}, 'CD': {'desc': '<a href="/static/images/v4_CD_BRANK.png" target="_blank">Canadian Dollar-CME</a>',  'group': 'currency',  'signals': 1.0}, 'CL': {'desc': '<a href="/static/images/v4_CL_BRANK.png" target="_blank">Crude Oil-Light-NYMEX</a>',  'group': 'energy',  'signals': 1.0}, 'C': {'desc': '<a href="/static/images/v4_CU_BRANK.png" target="_blank">Euro-CME</a>',  'group': 'currency',  'signals': 1.0}, 'EMD': {'desc': '<a href="/static/images/v4_EMD_BRANK.png" target="_blank">Index-S&P Midcap 400 E-mini-CME</a>',  'group': 'index',  'signals': 1.0}, 'ES': {'desc': '<a href="/static/images/v4_ES_BRANK.png" target="_blank">S&P 500 Index-E-mini-CME</a>',  'group': 'index',  'signals': 1.0}, 'FC': {'desc': '<a href="/static/images/v4_FC_BRANK.png" target="_blank">Cattle-Feeder-CME</a>',  'group': 'meat',  'signals': -1.0}, 'FV': {'desc': '<a href="/static/images/v4_FV_BRANK.png" target="_blank">T-Note-U.S. 5 Yr-CBT</a>',  'group': 'rates',  'signals': 1.0}, 'GC': {'desc': '<a href="/static/images/v4_GC_BRANK.png" target="_blank">Gold-COMEX</a>',  'group': 'metal',  'signals': 1.0}, 'HG': {'desc': '<a href="/static/images/v4_HG_BRANK.png" target="_blank">CopperHG-COMEX</a>',  'group': 'metal',  'signals': 1.0}, 'HO': {'desc': '<a href="/static/images/v4_HO_BRANK.png" target="_blank">Heating Oil #2-NYMEX</a>',  'group': 'energy',  'signals': 1.0}, 'JY': {'desc': '<a href="/static/images/v4_JY_BRANK.png" target="_blank">Japanese Yen-CME</a>',  'group': 'currency',  'signals': 1.0}, 'LC': {'desc': '<a href="/static/images/v4_LC_BRANK.png" target="_blank">Cattle-Live-CME</a>',  'group': 'meat',  'signals': -1.0}, 'LH': {'desc': '<a href="/static/images/v4_LH_BRANK.png" target="_blank">Hogs-Lean-CME</a>',  'group': 'meat',  'signals': -1.0}, 'MP': {'desc': '<a href="/static/images/v4_MP_BRANK.png" target="_blank">Mexican Peso-CME</a>',  'group': 'currency',  'signals': 1.0}, 'NE': {'desc': '<a href="/static/images/v4_NE_BRANK.png" target="_blank">New Zealand Dollar-CME</a>',  'group': 'currency',  'signals': 1.0}, 'NG': {'desc': '<a href="/static/images/v4_NG_BRANK.png" target="_blank">Natural Gas-Henry Hub-NYMEX</a>',  'group': 'energy',  'signals': 1.0}, 'NIY': {'desc': '<a href="/static/images/v4_NIY_BRANK.png" target="_blank">Nikkei 225 Index-Yen-CME</a>',  'group': 'index',  'signals': -1.0}, 'NQ': {'desc': '<a href="/static/images/v4_NQ_BRANK.png" target="_blank">Nasdaq 100 Index-E-mini</a>',  'group': 'index',  'signals': 1.0}, 'PA': {'desc': '<a href="/static/images/v4_PA_BRANK.png" target="_blank">Palladium-NYMEX</a>',  'group': 'metal',  'signals': 1.0}, 'PL': {'desc': '<a href="/static/images/v4_PL_BRANK.png" target="_blank">Platinum-NYMEX</a>',  'group': 'metal',  'signals': 1.0}, 'RB': {'desc': '<a href="/static/images/v4_RB_BRANK.png" target="_blank">Gasoline-Reformulated Blendstock-NYMEX</a>',  'group': 'energy',  'signals': 1.0}, 'S': {'desc': '<a href="/static/images/v4_S_BRANK.png" target="_blank">Soybeans -CBT</a>',  'group': 'grain',  'signals': -1.0}, 'SF': {'desc': '<a href="/static/images/v4_SF_BRANK.png" target="_blank">Swiss Franc-CME-</a>',  'group': 'currency',  'signals': 1.0}, 'SI': {'desc': '<a href="/static/images/v4_SI_BRANK.png" target="_blank">Silver-COMEX</a>',  'group': 'metal',  'signals': 1.0}, 'SM': {'desc': '<a href="/static/images/v4_SM_BRANK.png" target="_blank">Soybean Meal-CBT </a>',  'group': 'grain',  'signals': -1.0}, 'T': {'desc': '<a href="/static/images/v4_TU_BRANK.png" target="_blank">T-Note-U.S.  2 Yr -CBT</a>',  'group': 'rates',  'signals': 1.0}, 'TY': {'desc': '<a href="/static/images/v4_TY_BRANK.png" target="_blank">T-Note-U.S. 10 Yr w/Prj A-CBT</a>',  'group': 'rates',  'signals': 1.0}, 'US': {'desc': '<a href="/static/images/v4_US_BRANK.png" target="_blank">T-Bond-U.S.-CBT</a>',  'group': 'rates',  'signals': 1.0}, 'W': {'desc': '<a href="/static/images/v4_W_BRANK.png" target="_blank">Wheat-CBT </a>',  'group': 'grain',  'signals': 1.0}, 'YM': {'desc': '<a href="/static/images/v4_YM_BRANK.png" target="_blank">DJIA Mini $5 Index-CBT</a>',  'group': 'index',  'signals': 1.0}}

    filename='performance_data.json'
    if isfile(filename):
        with open(filename, 'r') as f:
            json_performance = json.load(f)
    else:
        list_performance=[]
        with open(filename, 'w') as f:
            json.dump(list_performance, f)
        print 'Saved', filename

    filename='boxstyles_data.json'
    if isfile(filename):
        with open(filename, 'r') as f:
            json_boxstyles = json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(default_list_boxstyles, f)
        print 'Saved', filename
        
    filename='customboard_data.json'
    if isfile(filename):
        with open(filename, 'r') as f:
            json_customstyles = json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(default_list_customboard, f)
        print 'Saved', filename

    filename='custom_signals_data.json'
    if isfile(filename):
        with open(filename, 'r') as f:
            json_customsignals = json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(default_custom_signals, f)
        print 'Saved', filename

    userID = models.IntegerField()
    selection = models.TextField()
    v4futures = models.TextField()
    v4mini = models.TextField()
    v4micro = models.TextField()
    componentloc = models.TextField(default=json_cloc)
    #boxstyles = models.TextField(default=json_boxstyles)
    #performance = models.TextField(default=json_performance)
    mcdate = models.TextField()
    timestamp = models.IntegerField()

    def dic(self):
        #fields = ['selection', 'v4futures', 'v4mini', 'v4micro', 'componentloc','boxstyles','performance', 'mcdate', 'timestamp']
        fields = ['selection', 'v4futures', 'v4mini', 'v4micro', 'componentloc', 'mcdate',
                  'timestamp']
        result = {}
        for field in fields :
            result[field] = self.__dict__[field]
        #result['performance'] = self.json_performance
        #result['boxstyles'] = self.json_boxstyles
        #result['customstyles'] = self.json_customstyles
        return result

    def __str__(self):
        return self.selection

'''
class MetaData(models.Model):
    components = models.TextField()
    triggers = models.TextField()
    mcdate = models.TextField()
    timestamp = models.IntegerField()

    def dic(self):
        fields = ['components', 'triggers', 'mcdate', 'timestamp']
        result = {}
        for field in fields :
            result[field] = self.__dict__[field]
        return result

    def __str__(self):
        return self.mcdate


class AccountData(models.Model):
    value1 = models.TextField()
    value2 = models.TextField()
    mcdate = models.TextField()
    timestamp = models.IntegerField()

    def dic(self):
        fields = ['value1', 'value2', 'mcdate', 'timestamp']
        result = {}
        for field in fields :
            result[field] = self.__dict__[field]
        return result

    def __str__(self):
        return self.mcdate
'''