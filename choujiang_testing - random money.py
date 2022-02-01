# -*- coding = utf-8 -*-
# @Time : 2022/1/13 21:36
# @Author : 汤包
# @File : choujiang.py
# @Software : PyCharm
import random
import xlwt
import time
import pandas as pd
import os
import openpyxl
import xlrd
import shutil

#初始化数值
userName = "Testing "
userName_ask = "是"
ready = "是"
sum = 1 #游玩总次数
ran_dom = 0
ran_dom_2 = 0
ran_dom_choose = 0
money = 0
money_2 = 0
ini_money = 0
lound = 0
superDouble = 0
superMinus = 0
superAdd = 0
#设置如果跳过本轮特殊券的第三方储存变量
superDouble_fake = 0
superMinus_fake = 0
superAdd_fake = 0
result = []
i1 = 0
qustion_00 = 0
qustion_0 = "是"
qustion_1 = "是"
qustion_2 = "否"
qustion_3 = "是"
qustion_4 = []
qustion_5 = "是"
outPutWord = []
chosen = ["加倍","10","5","20","谢谢","降档","加档","加档2","50"]
chosen2 = ["加倍","10","5","20","谢谢","降档","加档","加档2","50"]
choose = 0
datalist = []
countdown_1 = 3 #每轮抽奖等待时间设置
countdown_2 = 0.04 #导出日志等待时间设置
countdown_3 = 1 #生成日志时间设置
countdown_4 = 5 #退出系统时间设置
timeflush = 0.25  # 设置屏幕刷新的间隔时间

#定义一些方法
def del_file(path_data): #删除result文件夹下的日志文件来减少内存的方法
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)
def gameRule():
    print("")
    print("                       欢迎来到本游戏                        ")
    print("")
    print("                     制作人：小笼汤包1827                        ")
    print("")
    print("       版权所有 禁止任何人在未经作者的允许下私自传播或进行商业活动   ")
    print("")
    time.sleep(1)
    print("=============================================================")
    print("                      下面介绍游戏规则                       ")
    print("=============================================================")
    print("")
    time.sleep(1)
    print("         1.初始需设置金额，可以手动设置也可以设置上限随机抽取    ")
    print("")
    time.sleep(0.25)
    print("                         抽取范围：20元 ~ 设置的上限    ")
    print("")
    time.sleep(0.5)
    print("         2.每轮游戏抽奖基础花费10元                        ")
    print("")
    time.sleep(0.5)
    print("         3.每轮抽取都有奖品，会在下面介绍                    ")
    print("")
    time.sleep(0.5)
    print("         4.每轮都会有概率开放作弊功能，即再花25元查看本轮奖品  ")
    print("")
    time.sleep(0.5)
    print("         5.钱包小于等于0时，游戏结束                        ")
    print("")
    time.sleep(1)
    print("=============================================================")
    print("                      下面介绍每轮奖品                        ")
    print("=============================================================")
    print("")
    time.sleep(1)
    print(" [1] 超级加倍券：下一轮若抽到含有数字奖品时加倍获得，与下一轮自动使用 " )
    print("")
    print("           （如抽到特效券不会双倍，券不会加倍获取，券未使用允许保留)" )
    time.sleep(0.5)
    print("")
    print(" [2] 超级加档券：下一轮抽奖花费的金额翻倍，即花 20 元抽一次奖       ")
    print("")
    time.sleep(0.5)
    print(" [3] 超级降档券：下一轮抽奖花费的金额减半，即花  5 元抽一次奖       ")
    print("")
    time.sleep(0.5)
    print(" [4] 5元：钱包 + 5 元                                       ")
    print("")
    time.sleep(0.5)
    print(" [5] 10元：钱包 + 10 元                                     ")
    print("")
    time.sleep(0.5)
    print(" [6] 20元：钱包 + 20 元                                     ")
    print("")
    time.sleep(0.5)
    print(" [7] 50元：钱包 + 50 元                                     ")
    print("")
    time.sleep(0.5)
    print(" [8] 谢谢惠顾：啥玩意都没有                                    ")
    print("")
    time.sleep(0.5)
    print("  注：① 如抽到 [超级加档券]和[超级减档券]，下一轮花费的金额为（20-5）")
    print("")
    print("       即 下一轮需要花 15 元抽一次奖                            ")
    print("")
    time.sleep(0.5)
    print("  注：② 每轮只可使用一次 [超级加档券] 、 [超级减档券]              ")
    print("")
    time.sleep(1.5)
    print("=============================================================")
    print("                       初始化本游戏                           ")
    print("=============================================================")
    print("")
    print("")
    time.sleep(1)

def item(ran_dom,money,superDouble,superMinus,superAdd,result):
    if ran_dom == "加倍" :
        result.append("超级加倍券")
        superDouble = superDouble + 1
    elif ran_dom == "10":
        result.append("10元")
        money = money +10
    elif ran_dom == "5":
        result.append("5元")
        money = money + 5
    elif ran_dom == "20":
        result.append("20元")
        money = money + 20
    elif ran_dom == "谢谢":
        result.append("谢谢惠顾")
    elif ran_dom == "降档":
        result.append("超级降档券")
        superMinus = superMinus + 1
    elif ran_dom == "加档2":
        superAdd = superAdd + 1
        result.append("超级加档券")
    elif ran_dom == "加档":
        superAdd = superAdd + 1
        result.append("超级加档券")
    elif ran_dom == "50":
        money = money + 50
        result.append("50元")
    return ran_dom,money,superDouble,superMinus,superAdd,result

def superDoubleRule(ran_dom,money,superDouble):
    superDouble = superDouble - 1
    if ran_dom == "10" :
        money = money + 10
    elif ran_dom == "5":
        money = money + 5
    elif ran_dom == "20":
        money = money + 20
    elif ran_dom == "50":
        money = money + 50
    return ran_dom,money,superDouble

#主体

gameRule()
print("===========  下 面 请 设 置    基 础 设 置   ===========")
print("")
time.sleep(1)
qustion_0 = input("需要让系统抽取初始金额吗，填入“是”或“否”，如填入“否”则弹出设置选项，敲完请回车 \n")
print("")
if(qustion_0 == "是"):
    qustion_00 = int(input("   请设置上限，敲完请回车 \n"))
    print("")
    money = round(random.uniform(20,qustion_00),2)
    ini_money = money
    time.sleep(1)
    print("   系统为您抽取到初始金额为 %d 元"%money)
    print("")
else:
    money = int(input(" 请设置初始金额,只能为整数，不允许小数，为增强可玩性，请设置大于20的整数,敲完请回车 \n"))
    ini_money = money
print("")
time.sleep(1)
userName_ask = input(" 需要为自己起一个名字吗？（填入“是”或“否”，默认为Testing，敲完请回车）\n")
print("")
if(userName_ask == "是") :
    userName = input("  请输入您的昵称，只允许中文、英文大小写均可、数字拼凑而成不允许其他字符，敲完请回车 \n")
    print("")
# if(money>10):
#     money = money - 10
while(qustion_3 == "是"):
    if(sum != 1):
        print("")
        qustion_5 = int(input(" 请问是否还需要设置金额吗？（填入1~3数字）敲完请回车 \n 1.不设置，默认为前一次设置的 %d 元 \n 2.设置，让系统抽取数字 \n 3.设置，自己设置 \n " % ini_money))
        print("")
        if (qustion_5 == 3):
            money = int(input("请设置第 %d 局金额，只能为整数，不允许小数，为增强可玩性，请设置大于20的整数 \n" % sum))
            print("")
            ini_money = money
        elif qustion_5 == 2:
            qustion_00 = int(input("   请设置上限，敲完请回车 \n"))
            print("")
            money = round(random.uniform(20, qustion_00), 2)
            ini_money = money
            time.sleep(1)
            print("   系统为您抽取到初始金额为 %d 元" % money)
            print("")
        else:
            money = ini_money
    time.sleep(1)
    ready = input(" 准备好了吗？（填入“是”或“否”,敲完请回车）\n")
    print("")
    time.sleep(1)
    if(ready == "否"):
        break
    if(ready == "是") :
        days = 365
        for i in range(days):
            print("\rGame Loading... ：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
            time.sleep(0.01)
        print("")
        print("")
        time.sleep(4)
        print("===============================================================================================")
        print("=     这  是  您  第  %d  次  游  玩  本  游  戏         现 在    游 戏 开 始                  =" % sum)
        print("===============================================================================================")
        print("")
        print("")
        print("")
        time.sleep(3)
        while(money>0 and qustion_1 == "是"):
            time.sleep(1)
            if(ran_dom == 10):  #输入上一轮跳过，则需重新初始化变量
                outPutWord.append("")
                result.append("第%d轮跳过"%i1)
                superAdd_fake = 0
                superMinus_fake = 0
                superDouble_fake = 0
            #扣钱区域
            if(superAdd >0 and  qustion_2 == "是"):
                superAdd = superAdd - 1
                superMinus = superMinus - 1
                superAdd_fake = 1
                superMinus_fake = 1
                money = money - 15
                money_2 = 15
            elif superAdd >0 and qustion_2 == '否':
                superAdd = superAdd - 1
                superAdd_fake = 1
                money = money - 20
                money_2 = 20
            elif superAdd >0:
                superAdd = superAdd - 1
                superAdd_fake = 1
                money = money - 20
                money_2 = 20
            elif superAdd <= 0 and qustion_2 == "是":
                superMinus = superMinus - 1
                superMinus_fake = 1
                money = money - 5
                money_2 = 5
            else :
                money = money - 10
                money_2 = 10
            if(money<0):
                print("您身上已经没钱了，赶紧走人吧")
                break
            i1 = i1 + 1
            data = []
            random.shuffle(chosen)
            random.shuffle(chosen2)
            # 开 启 作 弊 ↓
            # print(chosen)
            print("===================================================================")
            # print("")
            print("                             第 %d 轮"%i1)
            # print("")
            print("===================================================================")
            print("")
            ran_dom_choose = random.random()  #生成0~1的随机数，如果大于0.5，就开放作弊功能，小于则不开放
            if(ran_dom_choose > 0.5 and money >= 25):
                choose = int(input("请输入 1 ~ 11 的数字，每一位数字对应本轮的一份奖品 \n输入 10 为跳过本轮\n输入 11 为作弊功能，即再花 25 元查看本轮奖品  \n敲完请回车 \n"))
                if(choose == 11):
                    print("")
                    money = money - 25
                    print(chosen2)
                    print("")
                    ran_dom_2 = int(input("请输入 1 ~ 9 的数字，每一位数字对应本轮的一份奖品，敲完请回车 \n"))
                    ran_dom = chosen2[ran_dom_2-1]
                if(choose == 10):
                    print("")
                    print("* —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——  *")
                    money = money + money_2
                    time.sleep(1.5)
                    # 恢复特殊券
                    if (superMinus_fake == 1):
                        superMinus = superMinus + 1
                    if (superAdd_fake == 1):
                        superAdd = superAdd + 1
                    if (superDouble_fake == 1):
                        superDouble = superDouble + 1
                    print("\n您已跳过本轮，您身上还有 %d 元钱\n \n您还有 %d 张超级加档券，还有 %d 张超级降档券，还有 %d 张超级加倍券 " % (money, superAdd, superMinus, superDouble))
                    print("")
                    print("")
                    print("")
                    ran_dom = 10
                    data.append(i1)
                    data.append(money)
                    data.append("跳过本轮")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    datalist.append(data)
                    continue
                elif choose != 10 and choose != 11 :
                    ran_dom = chosen[choose-1]
            elif ran_dom_choose > 0.5 and money < 35:
                choose = int(input("请输入 1 ~ 10 的数字，每一位数字对应本轮的一份奖品\n输入 10 为跳过本轮 \n本轮开放作弊功能，但您没有足够的现金支付，敲完请回车 \n"))
                if (choose == 10):
                    print("")
                    print("* —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——  *")
                    money = money + money_2
                    time.sleep(1.5)
                    # 恢复特殊券
                    if (superMinus_fake == 1):
                        superMinus = superMinus + 1
                    if (superAdd_fake == 1):
                        superAdd = superAdd + 1
                    if (superDouble_fake == 1):
                        superDouble = superDouble + 1
                    print("\n您已跳过本轮，您身上还有 %d 元钱\n \n您还有 %d 张超级加档券，还有 %d 张超级降档券，还有 %d 张超级加倍券 " % (money, superAdd, superMinus, superDouble))
                    print("")
                    print("")
                    print("")
                    ran_dom = 10
                    data.append(i1)
                    data.append(money)
                    data.append("跳过本轮")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    datalist.append(data)
                    continue
                else:
                    ran_dom = chosen[choose - 1]
            else:
                choose = int(input("请输入 1 ~ 10 的数字，每一位数字对应本轮的一份奖品\n输入 10 为跳过本轮\n本轮暂不开放使用作弊功能，敲完请回车 \n"))
                if (choose == 10):
                    print("")
                    print("* —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——  *")
                    money = money + money_2
                    time.sleep(1.5)
                    # 恢复特殊券
                    if (superMinus_fake == 1):
                        superMinus = superMinus + 1
                    if (superAdd_fake == 1):
                        superAdd = superAdd + 1
                    if (superDouble_fake == 1):
                        superDouble = superDouble + 1
                    print("\n您已跳过本轮，您身上还有 %d 元钱\n \n您还有 %d 张超级加档券，还有 %d 张超级降档券，还有 %d 张超级加倍券 " % (money, superAdd, superMinus, superDouble))
                    print("")
                    print("")
                    print("")
                    ran_dom = 10
                    data.append(i1)
                    data.append(money)
                    data.append("跳过本轮")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    data.append("-")
                    datalist.append(data)
                    continue
                else:
                    ran_dom = chosen[choose - 1]
            ran_dom,money,superDouble,superMinus,superAdd,result = item(ran_dom,money,superDouble,superMinus,superAdd,result)
            if (superDouble < 0 ):
                print(" X 系统出错，请稍后重启 X")
                break
            elif superAdd < 0 :
                print(" X 系统出错，请稍后重启 X")
                break
            elif superMinus < 0 :
                print(" X 系统出错，请稍后重启 X")
                break

            if (superDouble > 0  and ran_dom == "5"):
                ran_dom, money, superDouble = superDoubleRule(ran_dom, money, superDouble)
                outPutWord.append("您本局已使用超级加倍券一张，您现在还有 %d 张超级加倍券"%(superDouble))
            elif superDouble > 0 and ran_dom == "10" :
                ran_dom, money, superDouble = superDoubleRule(ran_dom, money, superDouble)
                outPutWord.append("您本局已使用超级加倍券一张，您现在还有 %d 张超级加倍券" % (superDouble))
            elif superDouble > 0 and ran_dom == "20" :
                ran_dom, money, superDouble = superDoubleRule(ran_dom, money, superDouble)
                outPutWord.append("您本局已使用超级加倍券一张，您现在还有 %d 张超级加倍券" % (superDouble))
            elif superDouble > 0 and ran_dom == "50" :
                ran_dom, money, superDouble = superDoubleRule(ran_dom, money, superDouble)
                outPutWord.append("您本局已使用超级加倍券一张，您现在还有 %d 张超级加倍券" % (superDouble))
            elif superDouble == 0 :
                outPutWord.append("您还没有超级加倍券")
            else:
                superDouble = superDouble + 0
                outPutWord.append("本轮未使用超级加倍券，您现在还有 %d 张超级加倍券"%(superDouble))
            print(" * —— —— —— —— —— —— —— —— —— —— —— *")
            #倒计时
            for i in range(0, int(countdown_1 / timeflush)):
                list = ["\\", "|", "/", "—"]
                index = i % 4
                print("\r          程 序 正 在 抽 卡 {}".format(list[index]), end="")
                time.sleep(timeflush)
            print("")
            print(" * —— —— —— —— —— —— —— —— —— —— —— *")
            print("")
            outPutWord.append("第%d轮，您抽中的是 " % (i1) + result[i1 - 1] + " ，您身上还有 %d 元钱、超级加档券有 %d 张，超级降档券有 %d 张" % (money, superAdd, superMinus))
            data.append(i1)
            data.append(money)
            data.append(result[i1 - 1])
            data.append(superDouble)
            data.append(superAdd)
            data.append(superMinus)
            datalist.append(data)
            for i2 in range (len(outPutWord)-1,len(outPutWord)-3,-1):
                print(outPutWord[i2])
                print("")

            print("* —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——  *")
            print("")
            time.sleep(1.5)
            if(money < 0):
                print("游戏结束,请下次继续努力")
                break
            if(money <= 5 and superMinus == 0):
                time.sleep(1)
                print("")
                print("")
                print("=======================================================================")
                print("=              游 戏 结 束 , 您 的 钱 包 还 剩 下 %d 元              =" % (money))
                print("=======================================================================")
                break
            qustion_1 = input("请问还要进行下一轮游戏吗？ (填入'是'或'否') ，敲完请回车\n")
            if (superMinus > 0 and qustion_1 == "是"):
                print("")
                qustion_2 = input("请问下一轮要使用超级减档券吗？ (填入'是'或'否') ，敲完请回车\n")
                print("")
                print("")
                print("")
            else :
                qustion_2 = "否"
            if(qustion_1 == "是"):
                print("")
                print("")
                print("")
            if(qustion_1 == "否"):
                time.sleep(1)
                print("")
                print("")
                print("=======================================================================")
                print("=              游 戏 结 束 , 您 的 钱 包 还 剩 下 %d 元              ="%(money))
                print("=======================================================================")
                break
        print("")
        print("")
        #print("剩下的钱为%d元"%(money))
        # print(datalist)
        qustion_3 = 2
        for i in range(0, int(countdown_3 / timeflush)):
            list = ["\\", "|", "/", "—"]
            index = i % 4
            print("\r正在生成日志 {}".format(list[index]), end="")
            time.sleep(timeflush)
        print("")
        print("")
        qustion_4.append(input("日志已生成，是否需要导出呢？（填“是”或“否”），敲完请回车\n"))
        print("")
        # excel 导出模块
        if(qustion_4[sum-1] == "是"):
            time.sleep(0.5)
            print("===================== 正 在 导 出 ===========================")
            print("")
            book = xlwt.Workbook(encoding="utf-8")  #style_compression=0)   创建workbook对象
            # 创建样式对象
            style = xlwt.XFStyle()
            #对齐方式
            align = xlwt.Alignment()
            align.horz = 2  # 设置水平位置，0是左对齐，1是居中，2是右对齐
            # 样式加载对齐方式
            style.alignment = align
            sheet = book.add_sheet("第%d次抽奖日志_log"%sum,cell_overwrite_ok=True)  # 创建工作表
            col = ("轮数","钱包","奖品","超级加倍","超级加档","超级减档")  #“列”信息
            for i in range(0,6):
                sheet.write(0,i,col[i],style=style)  #写入列名
            for i in range(0,i1):
                print("                       第 %d 条                      "%(i+1))
                time.sleep(0.3)
                print("")
                data_excel = datalist[i]
                for j in range(0,6):
                    sheet.write(i+1,j,data_excel[j],style=style)
            book.save(r".\\result\%s_第%d次抽奖日志_log.xls"%(userName,sum))
            print("===================== 导 出 成 功 ===========================")
            print("")
        sum = sum + 1
        qustion_3 = input("请问还需要再来一局吗？（填“是”或“否”），敲完请回车 \n")
        print("")
        if(qustion_3 == "是"):  #初始化各变量
            ran_dom = 0
            ran_dom_2 = 0
            ran_dom_choose = 0
            money = 100
            lound = 0
            superDouble = 0
            superMinus = 0
            superAdd = 0
            result = []
            i1 = 0
            qustion_00 = 0
            qustion_0 = "是"
            qustion_1 = "是"
            qustion_2 = "否"
            qustion_3 = "是"
            outPutWord = []
            chosen = ["加倍","10","5","20","谢谢","降档","加档","加档2","50"]
            chosen2 = ["加倍", "10", "5", "20", "谢谢", "降档", "加档", "加档2","50"]
            choose = 0
            datalist = []
if("是" in qustion_4):
    time.sleep(1.5)
    print("")
    print("          * * * 检 测 到 您 有 日 志 等 待 合 并 * * *   ")
    print("")
    print("")
    time.sleep(0.5)
    print(" * * * * * * * *   自 动 开 始 合 并 日 志 数 据   * * * * * * * *   ")
    result_excel = pd.ExcelWriter('%s_抽奖结果_log.xlsx'%userName)  # 结果保存路径
    origin_file_list = os.listdir(r'./result')  # 获取表格路径
    for i in origin_file_list:
        file_path = r'./result/%s' % i  # 拼接文件路径
        content = pd.read_excel(file_path)  # 读取文件内容
        sheet_name = i[:len(i) - 4]  # 获取文件名
        content.to_excel(result_excel, sheet_name, index=False)  # 写入同一个表的不同sheet
    result_excel.save()
    print("")
    days = 365
    for i in range(days):
        print("\r数据合并进度：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
        time.sleep(0.01)
    print("")
    print("")
    print("                * * * 数 据 合 并 完 成 * * *   ")
    print("")
    print("")
else :
    print("     * * *  您 并 未 输 出 任 何 日 志  ，  无 需 合 并 * * * ")
if("是" in qustion_4):
    time.sleep(1)
    print("")
    print("  * * * 检 测 到 您 result 文 件 夹 下 有 缓 存 日 志 文 件  * * *   ")
    print("")
    time.sleep(1)
    qustion_5 = input("需要删除result文件夹下生成的所有日志文件来减少储存吗？填“是”或“否”，敲完请回车 \n")
    if(qustion_5 == "是"):
        print("")
        days = 365
        for i in range(days):
            print("\r删除缓存进度：{}%".format(round((i + 1) * 100 / days)), end="", flush=True)
            time.sleep(0.01)
        print("")
        path_data = r".\result"
        del_file(path_data)
time.sleep(0.5)
print("")
print("==================================================================")
print("=    游  戏  结  束           感  谢  您  的  游  玩             =")
print("==================================================================")
for b in range(0, int(countdown_4 / timeflush)):
    list = ["\\", "|", "/", "—"]
    index = b % 4
    print("\r程序正在退出 {}".format(list[index]), end="")
    time.sleep(timeflush)