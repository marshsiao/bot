class translate:
    def rank(lst1):
        list_return = []
        for i in range(0,len(lst1)):
            s = ''
            if lst1[i].text == 'Unranked':
                s = lst1[i].text.replace('Unranked','未參與積分')
            elif lst1[i].text == 'Bronze':
                s = lst1[i].text.replace('Bronze','青銅')
            elif lst1[i].text == 'Silver':
                s = lst1[i].text.replace('Silver','白銀')
            elif lst1[i].text == 'Gold':
                s = lst1[i].text.replace('Gold','黃金')
            elif lst1[i].text == 'Platinum':
                s = lst1[i].text.replace('Platinum','白金')
            elif lst1[i].text == 'Diamond':
                s = lst1[i].text.replace('Diamond','鑽石')
            elif lst1[i].text == 'Master':
                s = lst1[i].text.replace('Master','大師')
            elif lst1[i].text == 'Grandmaster':
                s = lst1[i].text.replace('Grandmaster','宗師')
            elif lst1[i].text == 'Challenger':
                s = lst1[i].text.replace('Challenger','菁英')
            list_return.append(s)
        return list_return
    
    def tier(url):
        s = ''
        if 'tier-op' in url:
            s = 'OP'
        elif 'tier-1' in url:
            s = '1'
        elif 'tier-2' in url:
            s = '2'
        elif 'tier-3' in url:
            s = '3'
        elif 'tier-4' in url:
            s = '4'
        elif 'tier-5' in url:
            s = '5'
        return s
    
    def lane(arg):
        s = ''
        if '上路' in arg:
            s = 'top'
        elif 'top' in arg:
            s = 'top'
        elif '打野' in arg:
            s = 'jungle'
        elif 'jg' in arg:
            s = 'jungle'
        elif '中路' in arg:
            s = 'mid'
        elif 'mid' in arg:
            s = 'mid'
        elif 'ap' in arg:
            s = 'mid'
        elif '下路' in arg:
            s = 'adc'
        elif 'ad' in arg:
            s = 'adc'
        elif '輔助' in arg:
            s = 'support'
        elif 'sup' in arg:
            s = 'support'
        return s
            

    def hero(arg):
        s = ''
        if arg == '亞歷斯塔':
            s = arg.replace('亞歷斯塔','alistar')
        if arg == '牛頭':
            s = ('alistar')
        if arg == '塔隆':
            s = arg.replace('塔隆','talon')
        if arg == '亞菲利歐':
            s = arg.replace('亞菲利歐','aphelios')
        if arg == '月男':
            s = ('aphelios')
        if arg == '伊澤瑞爾':
            s = arg.replace('伊澤瑞爾','ezreal')
        if arg == '伊澤':
            s = ('ezreal')
        if arg == '伊瑞莉雅':
            s = arg.replace('伊瑞莉雅','irelia')
        if arg == '伊瑞':
            s = ('irelia')
        if arg == '刀妹':
            s = ('irelia')
        if arg == '伊羅旖':
            s = arg.replace('伊羅旖','illaoi')
        if arg == '伊芙琳':
            s = arg.replace('伊芙琳','evelynn')
        if arg == '伊莉絲':
            s = arg.replace('伊莉絲','elise')
        if arg == '蜘蛛':
            s = ('elise')
        if arg == '克雷德':
            s = arg.replace('克雷德','kled')
        if arg == '克烈':
            s = ('kled')
        if arg == '克黎思妲':
            s = arg.replace('克黎思妲','kalista')
        if arg == '滑板鞋':
            s = ('kalista')
        if arg == '凱爾':
            s = arg.replace('凱爾','kayle')
        if arg == '凱特琳':
            s = arg.replace('凱特琳','caitlyn')
        if arg == '女警':
            s = ('caitlyn')
        if arg == '凱能':
            s = arg.replace('凱能','kennen')
        if arg == '凱莎':
            s = arg.replace('凱莎','kaisa')
        if arg == '剎雅':
            s = arg.replace('剎雅','xayah')
        if arg == '剛普朗克':
            s = arg.replace('剛普朗克','gangplank')
        if arg == '船長':
            s = ('gangplank')
        if arg == '加里歐':
            s = arg.replace('加里歐','galio')
        if arg == '努努和威朗普':
            s = arg.replace('努努和威朗普','nunu')
        if arg == '努努':
            s = ('nunu')
        if arg == '劫':
            s = arg.replace('劫','zed')
        if arg == '勒布朗':
            s = arg.replace('勒布朗','leblanc')
        if arg == '卡力斯':
            s = arg.replace('卡力斯','khazix')
        if arg == '螳螂':
            s = ('khazix')
        if arg == '卡爾瑟斯':
            s = arg.replace('卡爾瑟斯','karthus')
        if arg == '死哥':
            s = ('karthus')
        if arg == '卡特蓮娜':
            s = arg.replace('卡特蓮娜','katarina')
        if arg == '卡特':
            s = ('katarina')
        if arg == '卡瑪':
            s = arg.replace('卡瑪','karma')
        if arg == '卡莎碧雅':
            s = arg.replace('卡莎碧雅','cassiopeia')
        if arg == '蛇女':
            s = ('cassiopeia')
        if arg == '卡薩丁':
            s = arg.replace('卡薩丁','kassadin')
        if arg == '卡蜜兒':
            s = arg.replace('卡蜜兒','camille')
        if arg == '厄薩斯':
            s = arg.replace('厄薩斯','aatrox')
        if arg == '劍魔':
            s = ('aatrox')
        if arg == '古拉格斯':
            s = arg.replace('古拉格斯','gragas')
        if arg == '酒桶':
            s = ('gragas')
        if arg == '史加納':
            s = arg.replace('史加納','skarner')
        if arg == '史瓦妮':
            s = arg.replace('史瓦妮','sejuani')
        if arg == '豬女':
            s = ('sejuani')
        if arg == '吉茵珂絲':
            s = arg.replace('吉茵珂絲','jinx')
        if arg == '吉茵':
            s = ('jinx')
        if arg == '吶兒':
            s = arg.replace('吶兒','gnar')
        if arg == '嘉文四世':
            s = arg.replace('嘉文四世','jarvaniv')
        if arg == '嘉文':
            s = ('jarvaniv')
        if arg == '圖奇':
            s = arg.replace('圖奇','twitch')
        if arg == '老鼠':
            s = ('twitch')
        if arg == '埃可尚':
            s = arg.replace('埃可尚','akshan')
        if arg == '埃爾文':
            s = arg.replace('埃爾文','ivern')
        if arg == '塔莉雅':
            s = arg.replace('塔莉雅','taliyah')
        if arg == '巖雀':
            s = ('taliyah')
        if arg == '岩雀':
            s = ('taliyah')
        if arg == '塔里克':
            s = arg.replace('塔里克','taric')
        if arg == '夜曲':
            s = arg.replace('夜曲','nocturne')
        if arg == '奈德麗':
            s = arg.replace('奈德麗','nidalee')
        if arg == '豹女':
            s = ('nidalee')
        if arg == '奧莉安娜':
            s = arg.replace('奧莉安娜','orianna')
        if arg == '球女':
            s = ('orianna')
        if arg == '好運姐':
            s = arg.replace('好運姐','missfortune')
        if arg == '女槍':
            s = ('missfortune')
        if arg == '妮可':
            s = arg.replace('妮可','neeko')
        if arg == '姍娜':
            s = arg.replace('姍娜','senna')
        if arg == '威寇茲':
            s = arg.replace('威寇茲','velkoz')
        if arg == '姬亞娜':
            s = arg.replace('姬亞娜','qiyana')
        if arg == '娜米':
            s = arg.replace('娜米','nami')
        if arg == '婕莉':
            s = arg.replace('婕莉','zeri')
        if arg == '安妮':
            s = arg.replace('安妮','annie')
        if arg == '寇格魔':
            s = arg.replace('寇格魔','kogmaw')
        if arg == '狗':
            s = ('kogmaw')
        if arg == '大嘴':
            s = ('kogmaw')
        if arg == '崔絲塔娜':
            s = arg.replace('崔絲塔娜','tristana')
        if arg == '砲娘':
            s = ('tristana')
        if arg == '炮娘':
            s = ('tristana')
        if arg == '小砲':
            s = ('tristana')
        if arg == '小炮':
            s = ('tristana')
        if arg == '巴德':
            s = arg.replace('巴德','bard')
        if arg == '布蘭德':
            s = arg.replace('布蘭德','brand')
        if arg == '火人':
            s = ('brand')
        if arg == '布郎姆':
            s = arg.replace('布郎姆','braum')
        if arg == '布隆':
            s = ('braum')
        if arg == '布里茨':
            s = arg.replace('布里茨','blitzcrank')
        if arg == '機器人':
            s = ('blitzcrank')
        if arg == '希格斯':
            s = arg.replace('希格斯','ziggs')
        if arg == '炸彈人':
            s = ('ziggs')
        if arg == '希瓦娜':
            s = arg.replace('希瓦娜','shyvana')
        if arg == '龍女':
            s = ('shyvana')
        if arg == '希維爾':
            s = arg.replace('希維爾','sivir')
        if arg == '輪子媽':
            s = ('sivir')
        if arg == '庫奇':
            s = arg.replace('庫奇','corki')
        if arg == '飛機':
            s = ('corki')
        if arg == '弗力貝爾':
            s = arg.replace('弗力貝爾','volibear')
        if arg == '熊':
            s = ('volibear')
        if arg == '弗拉迪米爾':
            s = arg.replace('弗拉迪米爾','vladimir')
        if arg == '血鬼':
            s = ('vladimir')
        if arg == '悟空':
            s = arg.replace('悟空','monkeyking')
        if arg == '猴子':
            s = ('monkeyking')
        if arg == '悠咪':
            s = arg.replace('悠咪','yuumi')
        if arg == '貓咪':
            s = ('yuumi')
        if arg == '慨影':
            s = arg.replace('慨影','kayn')
        if arg == '慎':
            s = arg.replace('慎','shen')
        if arg == '腎':
            s = ('shen')
        if arg == '拉克絲':
            s = arg.replace('拉克絲','lux')
        if arg == '拉姆斯':
            s = arg.replace('拉姆斯','rammus')
        if arg == '龍龜':
            s = ('rammus')
        if arg == '提摩':
            s = arg.replace('提摩','teemo')
        if arg == '提毛':
            s = ('teemo')
        if arg == '斯溫':
            s = arg.replace('斯溫','swain')
        if arg == '易大師':
            s = arg.replace('易大師','masteryi')
        if arg == '劍聖':
            s = ('masteryi')
        if arg == '星朵拉':
            s = arg.replace('星朵拉','syndra')
        if arg == '札克':
            s = arg.replace('札克','zac')
        if arg == '李星':
            s = arg.replace('李星','leesin')
        if arg == '瞎子':
            s = ('leesin')
        if arg == '盲僧':
            s = ('leesin')
        if arg == '杰西':
            s = arg.replace('杰西','jayce')
        if arg == '傑斯':
            s = ('jayce')
        if arg == '枷蘿':
            s = arg.replace('枷蘿','zyra')
        if arg == '柔依':
            s = arg.replace('柔依','zoe')
        if arg == '極靈':
            s = arg.replace('極靈','zilean')
        if arg == '時鐘':
            s = ('zilean')
        if arg == '歐拉夫':
            s = arg.replace('歐拉夫','olaf')
        if arg == '汎':
            s = arg.replace('汎','vayne')
        if arg == '薇恩':
            s = ('vayne')
        if arg == '沃維克':
            s = arg.replace('沃維克','warwick')
        if arg == '狼人':
            s = ('warwick')
        if arg == '法洛士':
            s = arg.replace('法洛士','varus')
        if arg == '波比':
            s = arg.replace('波比','poppy')
        if arg == '泰達米爾':
            s = arg.replace('泰達米爾','tryndamere')
        if arg == '蠻王':
            s = ('tryndamere')
        if arg == '派克':
            s = arg.replace('派克','pyke')
        if arg == '淣菈':
            s = arg.replace('淣菈','nilah')
        if arg == '漢默丁格':
            s = arg.replace('漢默丁格','heimerdinger')
        if arg == '潘森':
            s = arg.replace('潘森','pantheon')
        if arg == '烏爾加特':
            s = arg.replace('烏爾加特','urgot')
        if arg == '垃圾車':
            s = ('urgot')
        if arg == '烏迪爾':
            s = arg.replace('烏迪爾','udyr')
        if arg == '煞蜜拉':
            s = arg.replace('煞蜜拉','samira')
        if arg == '燼':
            s = arg.replace('燼','jhin')
        if arg == '特朗德':
            s = arg.replace('特朗德','trundle')
        if arg == '犽凝':
            s = arg.replace('犽凝','yone')
        if arg == '牙齦':
            s = ('yone')
        if arg == '犽宿':
            s = arg.replace('犽宿','yasuo')
        if arg == '牙膏':
            s = ('yasuo')
        if arg == '珍娜':
            s = arg.replace('珍娜','janna')
        if arg == '瑟菈紛':
            s = arg.replace('瑟菈紛','seraphine')
        if arg == '瑟雷西':
            s = arg.replace('瑟雷西','thresh')
        if arg == '錘石':
            s = ('thresh')
        if arg == '睿娜妲':
            s = arg.replace('睿娜妲','renata')
        if arg == '科加斯':
            s = arg.replace('科加斯','chogath')
        if arg == '大蟲子':
            s = ('chogath')
        if arg == '約瑞科':
            s = arg.replace('約瑞科','yorick')
        if arg == '納帝魯斯':
            s = arg.replace('納帝魯斯','nautilus')
        if arg == '納帝滷味':
            s = ('nautilus')
        if arg == '滷味':
            s = ('nautilus')
        if arg == '納瑟斯':
            s = arg.replace('納瑟斯','nasus')
        if arg == '狗頭':
            s = ('nasus')
        if arg == '索娜':
            s = arg.replace('索娜','sona')
        if arg == '索拉卡':
            s = arg.replace('索拉卡','soraka')
        if arg == '維克特':
            s = arg.replace('維克特','viktor')
        if arg == '電銲工':
            s = ('viktor')
        if arg == '電焊工':
            s = ('viktor')
        if arg == '維爾戈':
            s = arg.replace('維爾戈','viego')
        if arg == '維迦':
            s = arg.replace('維迦','veigar')
        if arg == '小法師':
            s = ('veigar')
        if arg == '小法':
            s = ('veigar')
        if arg == '翱銳龍獸':
            s = arg.replace('翱銳龍獸','aurelionsol')
        if arg == '龍獸':
            s = ('aurelionsol')
        if arg == '艾克':
            s = arg.replace('艾克','ekko')
        if arg == '艾妮維亞':
            s = arg.replace('艾妮維亞','anivia')
        if arg == '冰鳥':
            s = ('anivia')
        if arg == '艾希':
            s = arg.replace('艾希','ashe')
        if arg == '茂凱':
            s = arg.replace('茂凱','maokai')
        if arg == '莉莉亞':
            s = arg.replace('莉莉亞','lillia')
        if arg == '小鹿':
            s = ('lillia')
        if arg == '菲歐拉':
            s = arg.replace('菲歐拉','fiora')
        if arg == '菲艾':
            s = arg.replace('菲艾','vi')
        if arg == '葛雷夫':
            s = arg.replace('葛雷夫','graves')
        if arg == '葛炮':
            s = ('graves')
        if arg == '葛砲':
            s = ('graves')
        if arg == '男槍':
            s = ('graves')
        if arg == '葵恩':
            s = arg.replace('葵恩','quinn')
        if arg == '鳥人':
            s = ('quinn')
        if arg == '蒙多醫生':
            s = arg.replace('蒙多醫生','drmundo')
        if arg == '蒙多':
            s = ('drmundo')
        if arg == '蓋倫':
            s = arg.replace('蓋倫','garen')
        if arg == '薇可絲':
            s = arg.replace('薇可絲','vex')
        if arg == '熬夜波比':
            s = ('vex')
        if arg == '薩科':
            s = arg.replace('薩科','shaco')
        if arg == '小丑':
            s = ('shaco')
        if arg == '藍寶':
            s = arg.replace('藍寶','rumble')
        if arg == '貝爾薇斯':
            s = arg.replace('貝爾薇斯','belveth')
        if arg == '貪啃奇':
            s = arg.replace('貪啃奇','tahmkench')
        if arg == '蟾蜍':
            s = ('tahmkench')
        if arg == '塔姆':
            s = ('tahmkench')
        if arg == '費德提克':
            s = arg.replace('費德提克','fiddlesticks')
        if arg == '草人':
            s = ('fiddlesticks')
        if arg == '稻草人':
            s = ('fiddlesticks')
        if arg == '賈克斯':
            s = arg.replace('賈克斯','jax')
        if arg == '賽勒斯':
            s = arg.replace('賽勒斯','sylas')
        if arg == '賽垃圾':
            s = ('sylas')
        if arg == '賽拉斯':
            s = ('sylas')
        if arg == '賽恩':
            s = arg.replace('賽恩','sion')
        if arg == '賽特':
            s = arg.replace('賽特','sett')
        if arg == '赫克林':
            s = arg.replace('赫克林','hecarim')
        if arg == '人馬':
            s = ('hecarim')
        if arg == '趙信':
            s = arg.replace('趙信','xinzhao')
        if arg == '路西恩':
            s = arg.replace('路西恩','lucian')
        if arg == '辛吉德':
            s = arg.replace('辛吉德','singed')
        if arg == '慢跑伯':
            s = ('singed')
        if arg == '逆命':
            s = arg.replace('逆命','twistedfate')
        if arg == '卡牌':
            s = ('twistedfate')
        if arg == '達瑞文':
            s = arg.replace('達瑞文','draven')
        if arg == '瑞文':
            s = ('draven')
        if arg == '達瑞斯':
            s = arg.replace('達瑞斯','darius')
        if arg == '瑞斯':
            s = ('darius')
        if arg == '瑞斯叔叔':
            s = ('darius')
        if arg == '鄂爾':
            s = arg.replace('鄂爾','ornn')
        if arg == '山羊':
            s = ('ornn')
        if arg == '奧恩':
            s = ('ornn')
        if arg == '銳兒':
            s = arg.replace('銳兒','rell')
        if arg == '銳空':
            s = arg.replace('銳空','rakan')
        if arg == '鏡爪':
            s = arg.replace('鏡爪','kindred')
        if arg == '關':
            s = arg.replace('關','gwen')
        if arg == '剪刀妹':
            s = ('gwen')
        if arg == '格溫':
            s = ('gwen')
        if arg == '阿卡莉':
            s = arg.replace('阿卡莉','akali')
        if arg == '阿姆姆':
            s = arg.replace('阿姆姆','amumu')
        if arg == '嬰兒':
            s = ('amumu')
        if arg == '阿璃':
            s = arg.replace('阿璃','ahri')
        if arg == '阿祈爾':
            s = arg.replace('阿祈爾','azir')
        if arg == '雷尼克頓':
            s = arg.replace('雷尼克頓','renekton')
        if arg == '鱷魚':
            s = ('renekton')
        if arg == '雷歐娜':
            s = arg.replace('雷歐娜','leona')
        if arg == '日女':
            s = ('leona')
        if arg == '雷玟':
            s = arg.replace('雷玟','riven')
        if arg == '雷珂煞':
            s = arg.replace('雷珂煞','reksai')
        if arg == '挖土機':
            s = ('reksai')
        if arg == '挖掘機':
            s = ('reksai')
        if arg == '雷茲':
            s = arg.replace('雷茲','ryze')
        if arg == '光頭':
            s = ('ryze')
        if arg == '雷葛爾':
            s = arg.replace('雷葛爾','rengar')
        if arg == '獅子':
            s = ('rengar')
        if arg == '獅子狗':
            s = ('rengar')
        if arg == '露璐':
            s = arg.replace('露璐','lulu')
        if arg == '飛斯':
            s = arg.replace('飛斯','fizz')
        if arg == '魚人':
            s = ('fizz')
        if arg == '小魚人':
            s = ('fizz')
        if arg == '馬爾札哈':
            s = arg.replace('馬爾札哈','malzahar')
        if arg == '魔甘娜':
            s = arg.replace('魔甘娜','morgana')
        if arg == '魔鬥凱薩':
            s = arg.replace('魔鬥凱薩','mordekaiser')
        if arg == '麗珊卓':
            s = arg.replace('麗珊卓','lissandra')
        if arg == '冰女':
            s = ('lissandra')
        if arg == '墨菲特':
            s = arg.replace('墨菲特','malphite')
        if arg == '石頭人':
            s = ('malphite')
        if arg == '石頭':
            s = ('malphite')
        if arg == '黛安娜':
            s = arg.replace('黛安娜','diana')
        if arg == '月女':
            s = ('diana')
        if arg == '齊勒斯':
            s = arg.replace('齊勒斯','xerath')
        return s
     
