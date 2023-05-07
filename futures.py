import pymysql.cursors, datetime, urllib.request, requests, json, time
from os import system, name
from connection import conn
from random import *
import traceback
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from binance.cm_futures import CMFutures
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError
import datetime 


requests.urllib3.disable_warnings()



time.sleep(0.001)

def clear():
    
        # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    # print out some text

#Getting data from bot Table
row_count = conn.cursor()
rowbot = row_count.execute("SELECT * FROM bot WHERE open = '0' ORDER BY id DESC")
#rowbot_fetch = row_count.fetchone()




#program_starts = time.time()

time.sleep(0.1001)

while rowbot >= 0:


    #Getting Api Key from the database
    api_key = "Your API Key"

    #Getting Api Secret from the database
    api_secret = "Your API Secrete Key"



    # get server time

    client = UMFutures(key=api_key, secret= api_secret)

        


    try:     
            
        #Getting Total without open='0' filter
        totalrow = conn.cursor()
        total_row = totalrow.execute("SELECT * FROM bot")   
                    

        def bot():

            clear()



            program_starts = time.time()

            #time.sleep(0.001)


            #Getting Api Key from the database
            keyrow_cursor = conn.cursor()
            keyrow_cursor.execute("SELECT * FROM users WHERE id = '1' ")
            keyvalue = keyrow_cursor.fetchone()

            api_key = keyvalue ['API_Key']
            api_secret = keyvalue ['Secret_Key']


            # Starting  BOT Functionality from Here
            client = UMFutures(key=api_key, secret= api_secret)
            #client.time()


            #usdt_balance = client.get_asset_balance(asset='USDT')



            # All Bot Parameters and settings

            Sell_Indicator = "Sold"
            DCA_Sell_Indicator = "DCA_Sold"
            Buy_Indicator = "First-Buy"
            Sell_Up_Indicator = "First-Sell"
            Stop_loss_indicator = "Stoploss"
            Buy_up_indicator = "Bought"
            trailing_indicator = "Trailing"
            DCA_trailing_indicator = "DCA_Trailing"
            Trend_Indicator = "Down-Trend"
            Maximum_Price_Initial = 10000000  #When price id falling it will trigger new down trend
            maximum_price = 10000000
            current_date = time.time()
            now_date = datetime.datetime.fromtimestamp(current_date).strftime('%Y-%m-%d %H:%M:%S') #Getting current date and time



            #Getting Date from Bot Table in the Database

            #Getting data from bot Table
            row_count = conn.cursor()
            rowbot = row_count.execute("SELECT * FROM bot WHERE open = '0' ORDER BY id DESC")



            #Getting data from setting Table
            rowsettings_count = conn.cursor()
            rowsettings = rowsettings_count.execute("SELECT * FROM settings WHERE id = '1' ORDER BY id DESC LIMIT 1")

            #Getting data from history Table
            rowhistory_count = conn.cursor()
            rowhistory = rowhistory_count.execute("SELECT * FROM history")

            #Fetch Settings
            bot_table1 = rowsettings_count.fetchone()



            bot_cursor = conn.cursor()
            bot_cursor.execute("SELECT * FROM bot WHERE open = 0 ORDER BY id DESC")
            fetch_rows = list(bot_cursor.fetchall())
            bot_table = fetch_rows
            conn.commit()

            
            
            time.sleep(0.0001)


            for row in fetch_rows:

                

                try:

                    time.sleep(1.0001)

                    current_date = time.time()
                    now_date = datetime.datetime.fromtimestamp(current_date).strftime('%Y-%m-%d %H:%M:%S') #Getting current date and time
                    #usdt_price = USDT()

                    #Fetching data from data from tables in the database

                    bot_table = row_count.fetchone()
                    #bot_table1 = rowsettings_count.fetchone()
                    bot_table2 = rowhistory_count.fetchone()




                    #Database Field Variables

                    bot_id = bot_table['id']
                    bot_open = bot_table['open']
                    initial_move = bot_table['initial_move']
                    lastuuid = bot_table['lastuuid']
                    currency_pair = bot_table['currency_pair']
                    currency_pair_amount = float(bot_table['currency_pair_amount'])
                    initial_buy = float(bot_table['initial_buy'])
                    initial_sell = float(bot_table['initial_sell'])
                    status_bot = bot_table['trade_status']
                    counts = int(bot_table['counts'])
                    maximum_price_db = float(bot_table['maximum_price'])
                    trend_count = bot_table['trend_count']
                    trailing_start_db = float(bot_table['trailing_start'])
                    reset_price_db = float (bot_table['reset_price'])
                    profit_db = float(bot_table['profit'])
                    profit_percentage_db = float(bot_table['profit_percentage'])
                    Daily_amount = float(bot_table['Daily_amount'])
                    percentage_secure = float(bot_table['percentage_secure'])
                    the_maximum_price_db = bot_table['maximum_price']
                    executed_time = bot_table['executed_time']
                    wait_minute_db = float(bot_table['wait_minute'])
                    DCA = bot_table['DCA']
                    DCA_trailing_price = float(bot_table['DCA_trailing_price'])
                    DCA_trailing_start = float(bot_table['DCA_trailing_start'])
                    DCA_trailing_stop = float(bot_table['DCA_trailing_stop'])
                    DCA_UUID = bot_table['DCA_UUID']
                    DCA_qty_percent = float(bot_table['DCA_qty_percent'])
                    First_Price = float(bot_table['First_Price'])
                    Unique_ID = bot_table['Unique_ID']
                    Current_Position = bot_table['Current_Position']
                    Sell_uptrend_percent = float(bot_table['Sell_uptrend_percent'])
                    Total_Task_Profit = float(bot_table['Total_Task_Profit'])
                    Take_Profit = float(bot_table['Take_Profit'])
                    Upsell_Price = float(bot_table['Upsell_Price'])
                    Panic_Sell = bot_table['Panic_Sell']




                    now_date_trade = datetime.datetime.now()


                    def the_coin():

                        time.sleep(0.10)
                        #int((currency_pair[-4:])) #Getting base pair such as USDT, BTC etc :-3 is the last 3 leters 

                        if currency_pair[-4:] == ("USDT") or currency_pair[-4:] == ("BUSD") or currency_pair[-4:] == ("USDC"):
                        
                            return (currency_pair[:-4]) #This will return any letter after the last four letters
                            pass
                        elif currency_pair[-3:] == ("BTC") or currency_pair[-3:] == ("ETH") or currency_pair[-3:] == ("XRP"):
                            
                            return (currency_pair[:-3]) #This will return any letter after the last 3 letters
                            pass            

                    
                    the_coin = the_coin()



                # Calculating quantity increase using DCA

                    #@njit
                    def new_dca_qty():
                        if DCA_qty_percent == 0:
                            return(currency_pair_amount)
                        else:
                            dca_qty = ((currency_pair_amount * DCA_qty_percent)/100) + currency_pair_amount
                            dca_qty = round(dca_qty, 4) #convert the lot steps according to Binance Rule
                            return(dca_qty)
                        time.sleep(0.10)


                    #Calculation using Binance

                    #the_fee = float(client.get_trade_fee(symbol= currency_pair)[0]['makerCommission'])



                    Binance_fee = 1 + 0.001   #this is 0.10% or 1.001 Binance 
                    #Binance_fee = 1.001  
                    
                    
                    
                    """""
                    def Lot_Steps():
                        
                        time.sleep(0.001)

                        Step = (client.get_symbol_info(currency_pair))
                        Convt_Step = ((len(str(float((Step['filters'][2]['stepSize']))))) - 2 ) #if the step return 0.001 the 2 represent the "0." to get the actual step

                        if Convt_Step == 1:
                            return (0)
                        else:
                            return (int(Convt_Step))
                    """    


                    # Counting current open rows
                    row_counting = conn.cursor()
                    counting_row  = row_counting.execute("SELECT * FROM bot WHERE DCA_UUID = %s ORDER BY id DESC", (DCA_UUID,) )


                    #Display Date and Tasks Number
                    
                    
                    #Getting data from bot Table to search for maximum price to set Reset Price
                    row_reset = conn.cursor()
                    rowreset = row_reset.execute("SELECT * FROM bot WHERE currency_pair = %s AND maximum_price = %s", (currency_pair, maximum_price,))
                    reset_fetch = row_reset.fetchone()

                    reset_price = float(reset_fetch['reset_price'])

                    #Getting data from Orders Table for order history
                    roworder_count = conn.cursor()
                    roworder = roworder_count.execute("SELECT * FROM orders WHERE lastuuid = %s AND currency = %s", (lastuuid, currency_pair,))

                    orderstrade = roworder_count.fetchone()


                    #Price Interval Calculation and settings

                    profit_percentage = float(bot_table['trade_interval']) #Percentage of the Price to determine interval entered on task page
                    Buy_interval = (initial_sell * float(profit_percentage)/100)
                    Sell_interval = (initial_buy * float(profit_percentage)/100)
                    btc_hourly_change = float(bot_table['btc_hourly_change'])
                    trailing_start = float(bot_table['trailing_start_set'])
                    trailing_stop = float(bot_table['trailing_stop'])
                    trailing_step = float(bot_table['trailing_step'])
                    trailing_trigger_sell = float(bot_table['trailing_trigger_sell'])
                    DownTrend = float(bot_table['DownTrend'])
                    profit_set = float(bot_table1['profit'])  # updating profit in the settings table
                    bear_change = float(bot_table['bear_change'])

                    the_position = client.get_position_risk(symbol= currency_pair, recvWindow=6000)[0]
                    
                    total_position_Amt = float(the_position['positionAmt'])
                    entry_price = float(the_position['entryPrice'])
                    current_prices_risk = float(the_position['markPrice'])
                    unrealize_profit = float(the_position['unRealizedProfit'])
                    liquidation_Price = float(the_position['liquidationPrice'])
                    the_leverage = the_position['leverage']
                    isolated_Wallet = the_position['isolatedWallet'] #Available to spend
                    isAuto_AddMargin = the_position['isAutoAddMargin']
                    



                    lastmarketprice = float(client.ticker_price(currency_pair)['price'])

                    #Bid Price and Quantiy
                    bidmarketprice = float(client.ticker_price(currency_pair)['price'])

                    #Ask Market Price
                    askmarketprice = float(client.ticker_price(currency_pair)['price'])



                    Sell_Price_trigger =  (((initial_buy * trailing_trigger_sell) / 100) + initial_buy)
                    btctospend = ((currency_pair_amount * askmarketprice) * Binance_fee)
                    btctospend = float(btctospend)

                    btctospend_sell = ((currency_pair_amount * bidmarketprice) * Binance_fee)
                    btctospend_sell = float(btctospend_sell)


                    btctospend_DCA = ((new_dca_qty() * askmarketprice) * Binance_fee)
                    btctospend_DCA = float(btctospend_DCA)

                    sellworth = (currency_pair_amount * bidmarketprice) 
                    #sellworth = ((currency_pair_amount * bidmarketprice) / Binance_fee)

                    lastbuyworth = (initial_buy * currency_pair_amount)
                    #lastbuyworth = ((initial_buy * currency_pair_amount) * Binance_fee)

                    # Calculating profit if initial move was Sell or "Trend"
                    firstsellworth = ((initial_sell * currency_pair_amount) * Binance_fee)
                    buying_back_worth = ((currency_pair_amount * askmarketprice) * Binance_fee)

                    profit = sellworth - lastbuyworth
                    profit_sell = sellworth - lastbuyworth

                    Profit_initial_sell = (buying_back_worth - firstsellworth)  # To Calculate sell profit for initial sell order 


                    #Percentage Function to avoid zero division error
                    #@njit
                    def Percentage_calc():
                        
                        time.sleep(0.10)

                        if lastbuyworth == 0:
                            return (0.0)
                        else:
                            return ((profit/lastbuyworth) * 100)

                    #@njit
                    def Percentage_buy_update():
                        time.sleep(0.10)

                        if lastbuyworth == 0:
                            return (0.0)
                        else:
                            return ((profit/(initial_buy * currency_pair_amount)) * 100)
                    #@njit
                    def Percentage_sell_update():
                        time.sleep(0.10)

                        if firstsellworth == 0:
                            return (0.0)
                        else:
                            return ((Profit_initial_sell/(initial_sell * currency_pair_amount)) * 100)            




                    def profit_coverter():

                        base_coin = "BTCBUSD" #((client.get_symbol_info(currency_pair))['quoteAsset'])

                        if base_coin == "BTC":
                            baze_BTC = float(client.get_order_book(symbol = "BTCUSDT")['bids'][0][0])
                            return (baze_BTC)
                        elif base_coin == "ETH":
                            baze_ETH = float(client.get_order_book(symbol = "ETHUSDT")['bids'][0][0])
                            return (baze_ETH)
                        elif base_coin == "USDT" or "BUSD" or "USDC":
                            return (1)
                        


                    #Profit Calculation for Buy

                    profit = round(profit, 6) 
                    ProfitPercent = round(Percentage_calc(), 8)
                    ProfitPercent_buy_update = round (Percentage_buy_update(), 2)


                    #For initial Sell order
                    ProfitPercent_sell_update = round (Percentage_sell_update(), 4)
                    Profit_initial_sell = round(Profit_initial_sell, 6)


                    #Getting base currency from an open task and use it to call for balance 
                    #@njit
                    def the_base_coin():

                        time.sleep(0.10)
                        
                        #int((currency_pair[-4:])) #Getting base pair such as USDT, BTC etc :-3 is the last 3 leters 

                        if currency_pair[-4:] == ("USDT") or currency_pair[-4:] == ("BUSD") or currency_pair[-4:] == ("USDC"):
                        
                            return (currency_pair[-4:]) #This will return the last four letters
                            pass
                        elif currency_pair[-3:] == ("BTC") or currency_pair[-3:] == ("ETH") or currency_pair[-3:] == ("XRP"):
                            
                            return (currency_pair[-3:]) #This will return any letter after the last 3 letters
                            pass        
                    

                    # Get the count of the main

                    bot_counts = conn.cursor()
                    bot_counts.execute("SELECT * FROM bot WHERE maximum_price = %s AND DCA_UUID = %s", (Maximum_Price_Initial, DCA_UUID, ))
                    bot_count = bot_counts.fetchone()
                    total_count = int(bot_count["counts"])

                    

                    base_coin = the_base_coin()

                    #the_base_balance = client.get_asset_balance(asset = base_coin)
                    #base_coin_balance = (float(the_base_balance['free'])) # Getting the exact base coin balance to check before trading

                    #XXXXXXXXXXXXXXTrading Parameters ends here_XXXXXXXXXXXX-_-_-_-

                    # ::: Placing the first buy order from the database if Scalping is selected as initial move

                    

                    if lastuuid == None and initial_move == "scalping": #and (ROC_signal == "Bullish" and VROC_signal == "Bullish"):


                        qty_converter =  round((currency_pair_amount/lastmarketprice), 3)
                        #lastorder = client.create_order(symbol = currency_pair, quantity = currency_pair_amount, side = "BUY", type = "MARKET")
                        lastorder = client.new_order(symbol= currency_pair, side="BUY", type="MARKET", quantity= qty_converter,)
                        print(lastorder)

                        neworderdata_id = lastorder['orderId']
                        getorder = client.query_order(symbol = currency_pair, orderId= neworderdata_id, recvWindow=10000)

                        bought_price = float(getorder['avgPrice'])
                        symbol = getorder['symbol']
                        quantity = getorder['origQty']
                        filled_quantity = getorder['executedQty']
                        #total_cost = lastorder['cummulativeQuoteQty']
                        order_status = getorder['status']
                        order_type = getorder['side']

                        
                        total_cost = float(getorder['cumQuote'])

                        firtsbuy_id = bot_id
                        if neworderdata_id != None:
                            firstbuy_data = conn.cursor()

                            firstbuy_data.execute("UPDATE bot SET lastuuid = %s, initial_buy = %s, counts = %s, trade_status = %s, maximum_price = %s, executed_time = %s, DCA_UUID = %s, First_Price =%s, Upsell_Price =%s, Unique_ID =%s, Current_Position =%s, currency_pair_amount =%s WHERE id = %s", (neworderdata_id, bought_price, counts + 1, Buy_Indicator, Maximum_Price_Initial, now_date_trade, neworderdata_id, bought_price, bought_price, neworderdata_id, order_type, quantity, firtsbuy_id,) )

                            New_history = "INSERT INTO history(lastuuid,currency_pair,currency_pair_amount,initial_buy,initial_sell,initial_move,profit,profit_percentage,DCA_UUID, status, startdate, end_date, DCA_total_cost, First_Price, Unique_ID, Current_Position) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
                            New_history_value = (neworderdata_id, currency_pair, quantity, bought_price, "0", "scalping", profit, ProfitPercent_buy_update , neworderdata_id, "Trading...", now_date, "0000:00:0000", total_cost, bought_price, neworderdata_id, order_type)

                            New_order = "INSERT INTO orders(lastuuid,currency,quantity,executed_price,type,total_cost,status,filled_quantity,startdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            New_order_value = (neworderdata_id, symbol, quantity, bought_price, order_type, total_cost, order_status, filled_quantity, now_date)

                            firstbuy_data.execute(New_history, New_history_value)
                            firstbuy_data.execute(New_order, New_order_value)

                            conn.commit()

                            time.sleep(0.10)

                        else:
                            print("Checking for next buy opportunity")
                            time.sleep(0.10)


                            continue

                    
                    


                    # ::: Placing the first SELL order from the database if "SPOT_SELL" is selected as initial move



                    if lastuuid != None:

                        time.sleep(0.10)


                        #Getting data from history table

                        lastorderdata_id = orderstrade['lastuuid']
                        lastorderdata_order = orderstrade['type']
                        lastorderdata_status = orderstrade['status']
                        lastorderdata_currency = orderstrade['currency']
                        lastorderdata_price = float(orderstrade['executed_price'])
                        lastorderdata_quantity = float(orderstrade['quantity'])

                        #Getting latest information on orderstatus by collecting current data from exchange

                        history = client.query_order(symbol = currency_pair, orderId = lastuuid)

                        lastorderdata_id_update = history['orderId']
                        lastorderdata_order_update = history['side']
                        lastorderdata_status_update = history['status']
                        lastorderdata_currency_update = history['symbol']
                        lastorderdata_price_update = float(history['avgPrice'])
                        lastorderdata_quantity_update = float(history['origQty'])
                        lastorderdata_cost_update = float(history['cumQuote'])
                        lastorderdata_filled_update = history['executedQty']

                        #Update the order status in the database

                        update_order_status = conn.cursor()
                        update_order_status.execute("UPDATE orders SET type = %s, status = %s, filled_quantity = %s WHERE lastuuid = %s ", (lastorderdata_order_update, lastorderdata_status_update, lastorderdata_filled_update, lastorderdata_id_update,))
                        conn.commit()

                        time.sleep(0.10)



                    if lastuuid != None:

                        time.sleep(0.10)

                        #Getting data from history table
                        roworder_count = conn.cursor()
                        roworder = roworder_count.execute("SELECT * FROM orders WHERE lastuuid = %s AND currency = %s", (lastuuid, currency_pair,))

                        orderstrade = roworder_count.fetchone()

                        lastorderdata_id = orderstrade['lastuuid']
                        lastorderdata_order = orderstrade['type']
                        lastorderdata_status = orderstrade['status']
                        lastorderdata_currency = orderstrade['currency']
                        lastorderdata_price = float(orderstrade['executed_price'])
                        lastorderdata_quantity = float(orderstrade['quantity'])




                        # Calculating waiting period before another buy order is executed

                        def buy_wait_time():

                            # This function is used to delay next buy order with specified "wait_minute" to properly check if signal stay bullish

                            from datetime import timedelta

                            wait_minute = wait_minute_db
                            trade_time = executed_time



                            #now_date_trade = datetime.datetime.now()
                            trade_time = datetime.datetime.strptime(trade_time, '%Y-%m-%d %H:%M:%S.%f')

                            minute_hr = wait_minute * 60
                            new_trade_time = trade_time + timedelta(minutes = minute_hr)


                            if now_date_trade > new_trade_time:
                                return("YES")
                            elif now_date_trade < new_trade_time:
                                return ('NO')
                            elif lastorderdata_order == "SELL":
                                return("YES")



                        #Checking if total history quantity has been updated----------


                        total_cost_data = conn.cursor()
                        totalcostdata = total_cost_data.execute("SELECT * FROM orders WHERE lastuuid = %s", (lastuuid,))
                        total_cost_fetch = total_cost_data.fetchone()

                        the_total_cost =  float(total_cost_fetch['total_cost'])

                        total_cost_history = conn.cursor()
                        totalcosthistory = total_cost_history.execute("SELECT * FROM history WHERE lastuuid = %s", (lastuuid,))
                        total_cost_history_fetch = total_cost_history.fetchone()

                        the_total_history_cost =  float(total_cost_history_fetch['DCA_total_cost'])



                        #DCA_price_total = round(float(DCA_price_total), 10)
                        DCA_price_total = round(entry_price, 10)

                        #@njit
                        def DCA_percentage():
                            
                            time.sleep(0.10)


                            try:
                                percent_total = bidmarketprice - DCA_price_total
                                

                                if percent_total == 0 or percent_total == None:
                                    return(0)
                                else:
                                    DCApercent_total = (percent_total/DCA_price_total)* 100
                                    #DCApercent_total = ((percent_total * Binance_fee)/DCA_price_total)* 100

                                    return(DCApercent_total)
                            except Exception as ex:
                                return(0)
                                print(ex)
                                #print(traceback.format_exc())
                                pass




                        DCA_percent_total = round(float(DCA_percentage()), 2)




                        # TRAILING START Here ::::::::::::

                        # DCA TRAILING START Here ::::::::::::

                        if initial_move == "scalping" and DCA == "YES" and lastorderdata_order == "BUY" and ((((DCA_price_total * DCA_trailing_start)/100) + DCA_price_total) <= bidmarketprice) and (initial_buy != 0) and (status_bot != DCA_trailing_indicator and status_bot != trailing_indicator) and (lastorderdata_status == "FILLED"):
                        
                            try:
                                trailing_id = DCA_UUID
                                price_diff_percentage = ((bidmarketprice - DCA_price_total) / DCA_price_total)*100
                                trailing_percentage_diff = price_diff_percentage - (DCA_trailing_start - DCA_trailing_stop)


                                #$trailing_buyprice = (($rowbot->initial_buy) + (($rowbot->initial_buy * $trailing_stop)/100));

                                trailing_buyprice = ((DCA_price_total) + ((DCA_price_total * trailing_percentage_diff)/100))
                                trailing_buyprice =  round(trailing_buyprice, 8)

                                #//$trailing_startprice = ((($rowbot->initial_buy * $trailing_start)/100) + $rowbot->initial_buy);

                                trailing_startprice = (((DCA_price_total * price_diff_percentage)/100) + DCA_price_total)
                                trailing_startprice = round(trailing_startprice, 8)

                                update_trailing_start = conn.cursor()

                                update_trailing_start.execute("UPDATE bot SET DCA_trailing_price = %s, trade_status = %s, trailing_start = %s WHERE DCA_UUID = %s", (trailing_buyprice, DCA_trailing_indicator, trailing_startprice, trailing_id,))

                                conn.commit()
                            except Exception as ex:
                                print(ex)
                                #print(traceback.format_exc())
                                pass




                        #/// TRAILING STEP ::::::::::::

                        #/// DCA TRAILING STEP ::::::::::::

                        #if initial_move == "scalping" and lastorderdata_order == "BUY" and DCA == "YES" and (bidmarketprice >= ((((DCA_trailing_start - DCA_trailing_stop) * DCA_trailing_price)/100) + DCA_trailing_price) ) and (initial_buy != 0) and ((status_bot == DCA_trailing_indicator) or (status_bot == trailing_indicator)):
                        if initial_move == "scalping" and lastorderdata_order == "BUY" and DCA == "YES" and ((((trailing_start_db * trailing_step)/100) + trailing_start_db) <= bidmarketprice) and (initial_buy != 0) and ((status_bot == DCA_trailing_indicator) or (status_bot == trailing_indicator)):

                            try:
                                step_id = DCA_UUID
                                trailing_stepprice = trailing_start_db - (((DCA_trailing_start - DCA_trailing_stop) * trailing_start_db)/100)
                                
                                #trailing_stepprice = bidmarketprice - (((DCA_trailing_start - DCA_trailing_stop) * bidmarketprice)/100)

                                #trailing_stepprice = ((DCA_trailing_price) + ((DCA_trailing_price * trailing_step)/100))

                                trailing_stepprice = round(trailing_stepprice, 8)

                                trailing_step_startprice = ((trailing_start_db) + ((trailing_start_db * trailing_step)/100))
                                trailing_step_startprice = round(trailing_step_startprice, 8)

                                update_trailing_step = conn.cursor()
                                update_trailing_step.execute ("UPDATE bot SET DCA_trailing_price = %s, trade_status = %s , trailing_start = %s WHERE DCA_UUID = %s", (trailing_stepprice, trailing_indicator, trailing_step_startprice, step_id,))

                                conn.commit()
                            except Exception as ex:
                                return(0)
                                print(ex)
                                #print(traceback.format_exc())
                                pass



                        #DELETE ALL OLD TASKS IF PRICE IS UP ::::::::::::

                        #DCA DELETE ALL OLD TASKS IF PRICE IS UP ::::::::::::

                        if lastmarketprice > DCA_price_total and DCA == "YES" and maximum_price_db != Maximum_Price_Initial and status_bot == DCA_Sell_Indicator:

                            delete_data = conn.cursor()
                            delete_id = bot_id
                            delete_data.execute("DELETE FROM bot WHERE id = %s", (delete_id,))
                            conn.commit()


                        #Update First Task  trend_count back to zero ::::::::::::

                        if lastmarketprice > reset_price and DCA == "YES"and maximum_price_db == Maximum_Price_Initial and reset_price_db == reset_price and lastorderdata_order != "BUY":

                            updateorder_data = conn.cursor()
                            updateorder_id = bot_id

                            updateorder_data.execute("UPDATE bot SET trend_count = '0' WHERE id = %s", (updateorder_id,))
                            conn.commit()


                        #DCA Update First Task  trend_count back to zero ::::::::::::

                        if lastmarketprice > DCA_price_total and DCA == "YES" and maximum_price_db == Maximum_Price_Initial and reset_price_db == reset_price and lastorderdata_order != "BUY":

                            updateorder_data = conn.cursor()
                            updateorder_id = bot_id

                            updateorder_data.execute("UPDATE bot SET trend_count = '0' WHERE id = %s", (updateorder_id,))
                            conn.commit()





                        #Update Profit and Percentage  ::::::::::::

                        if lastorderdata_order == "BUY":

                            converted_profit = round((profit * profit_coverter()), 6)

                            percentage_data = conn.cursor()
                            percentage_id = bot_id

                            percentage_data.execute("UPDATE bot SET profit = %s, profit_percentage = %s, currency_pair_amount =%s WHERE id = %s", (converted_profit, ProfitPercent_buy_update, total_position_Amt, percentage_id,))
                            percentage_data.execute("UPDATE history SET profit = %s, profit_percentage = %s WHERE Unique_ID = %s", (converted_profit, ProfitPercent_buy_update, Unique_ID,))
                            percentage_data.execute("UPDATE history SET DCA_percent = %s WHERE Unique_ID = %s", (DCA_percent_total, Unique_ID,))
                            conn.commit()



                        
                        def other_conditions():
                            
                            #The condition to keep buying on trailing and or to stop buying if liquidated price to current price is less than 20% or percentage indicated below

                            factor_price = current_prices_risk - ((current_prices_risk * percentage_secure)/100)
                            if lastorderdata_order == "BUY" and (liquidation_Price < factor_price):
                                return ("YES")
                            elif lastorderdata_order == "SELL":
                                return ("YES")   
                            elif status_bot == DCA_trailing_indicator or status_bot == trailing_indicator:
                                return("YES")


                        # DCA Check and Place Sell Order when price
                        DCA_Sell_Price_trigger =  (((DCA_trailing_price * trailing_trigger_sell) / 100) + DCA_trailing_price)
                        #DCA_Sell_Price_trigger =  (((DCA_trailing_price * trailing_trigger_sell) / 100) + DCA_trailing_price)

                        if lastorderdata_order == "BUY" and initial_move == "scalping" and DCA == "YES" and (((status_bot == DCA_trailing_indicator or status_bot == trailing_indicator) and DCA_Sell_Price_trigger >= bidmarketprice) or (((((DCA_price_total * trailing_stop)/100) + DCA_price_total) <= bidmarketprice) and ((status_bot != DCA_trailing_indicator or status_bot != trailing_indicator) and Panic_Sell == "YES" ))):

                            #Checking if Coin Balance is enough to sell


                            
                            lastorder = client.new_order(symbol= currency_pair, side="SELL", type="MARKET", quantity= total_position_Amt,)
                            print(lastorder)

                            neworderdata_id = lastorder['orderId']
                            getorder = client.query_order(symbol = currency_pair, orderId= neworderdata_id, recvWindow=10000)

                            sold_price = float(getorder['avgPrice'])
                            symbol = getorder['symbol']
                            quantity = getorder['origQty']
                            filled_quantity = getorder['executedQty']
                            #total_cost = lastorder['cummulativeQuoteQty']
                            order_status = getorder['status']
                            order_type = getorder['side']

                            
                            total_cost = float(getorder['cumQuote'])
                            

                            #sellworth_sell = ((float(quantity) * float(sold_price)) / Binance_fee)
                            lastbuyworth_sell = (DCA_price_total * float(quantity)) 
                            profit_sell = round((total_cost - lastbuyworth_sell), 6)
                            ProfitPercent_sell = ((profit_sell/lastbuyworth_sell) * 100)
                            converted_profit = round((profit_sell * profit_coverter()), 6)
                            ProfitPercent_sell = round(ProfitPercent_sell, 2)

                            sell_id = DCA_UUID
                            history_id = bot_table2['id']

                            if neworderdata_id != None:

                                sell_data = conn.cursor()

                                sell_data.execute("UPDATE settings SET profit = %s WHERE id = %s", (profit_set + profit_sell,'1', ))
                                sell_data.execute("UPDATE bot SET Total_Task_Profit = %s WHERE Unique_ID = %s", (Total_Task_Profit + profit_sell, Unique_ID, ))

                                
                                sell_data.execute("UPDATE bot SET counts = %s WHERE maximum_price = %s AND Unique_ID = %s", (total_count + 1, Maximum_Price_Initial, Unique_ID, ))


                                sell_data.execute("UPDATE bot SET lastuuid = %s, initial_sell = %s, trend_count = %s, trade_status = %s, profit = %s, profit_percentage = %s, executed_time = %s, First_Price =%s, Upsell_Price =%s, Unique_ID =%s, Current_Position =%s WHERE DCA_UUID = %s", (neworderdata_id, sold_price, '0', DCA_Sell_Indicator, converted_profit, ProfitPercent_sell, now_date_trade, First_Price, Upsell_Price, Unique_ID, order_type, DCA_UUID, ))
                                sell_data.execute("UPDATE history SET lastuuid = %s, initial_sell = %s, status = %s, end_date = %s, DCA_percent = %s, First_Price =%s, Unique_ID =%s, Current_Position =%s WHERE Unique_ID = %s", (neworderdata_id, sold_price, 'ORDER Completed', now_date, ProfitPercent_sell, First_Price, Unique_ID, order_type, Unique_ID, ))

                                sell_order = "INSERT INTO orders(lastuuid,currency,quantity,executed_price,type,total_cost,status,filled_quantity,startdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                sell_order_value = (neworderdata_id, symbol, quantity, sold_price, order_type, total_cost, order_status, filled_quantity, now_date)
                                sell_data.execute(sell_order, sell_order_value)

                                conn.commit()

                                #time.sleep(0.02)






                        if (buy_wait_time() == "YES" and initial_move == "scalping" and other_conditions() == "YES") or (lastorderdata_order == "SELL" and other_conditions() == "YES"):
                            print("Buy Price has reached, checking if there is enough balance")

                            

                            qty_converter =  round((Daily_amount/lastmarketprice), 3)
                            #lastorder = client.create_order(symbol = currency_pair, quantity = currency_pair_amount, side = "BUY", type = "MARKET")
                            lastorder = client.new_order(symbol= currency_pair, side="BUY", type="MARKET", quantity= qty_converter,)
                            print(lastorder)

                            neworderdata_id = lastorder['orderId']
                            getorder = client.query_order(symbol = currency_pair, orderId= neworderdata_id, recvWindow=10000)

                            bought_price = float(getorder['avgPrice'])
                            symbol = getorder['symbol']
                            quantity = getorder['origQty']
                            filled_quantity = getorder['executedQty']
                            #total_cost = lastorder['cummulativeQuoteQty']
                            order_status = getorder['status']
                            order_type = getorder['side']

                            
                            total_cost = float(getorder['cumQuote'])


                            def task_status():
                                if status_bot == DCA_trailing_indicator:
                                    return(DCA_trailing_indicator)
                                elif status_bot == trailing_indicator:
                                    return(trailing_indicator)
                                else:
                                    return (Buy_up_indicator)


                            buyorder_id = bot_id

                            if neworderdata_id != None:
                                buyorder_data = conn.cursor()

                                buyorder_data.execute("UPDATE bot SET lastuuid = %s, initial_buy = %s, counts = %s, trade_status = %s, executed_time = %s, DCA_UUID = %s, First_Price =%s, Unique_ID =%s, Current_Position =%s, Upsell_Price =%s, currency_pair_amount =%s WHERE id = %s", (neworderdata_id, bought_price, counts + 1, task_status(), now_date_trade, neworderdata_id, First_Price, Unique_ID, order_type, Upsell_Price, quantity, buyorder_id, ) )

                                buy_history = "INSERT INTO history(lastuuid,currency_pair,currency_pair_amount,initial_buy,initial_sell,initial_move,profit,profit_percentage,status, startdate, end_date, DCA_UUID, DCA_total_cost, First_Price, Unique_ID, Current_Position ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                buy_history_value = (neworderdata_id, currency_pair, quantity, bought_price, "0", "scalping", profit, ProfitPercent_buy_update, "Trading...", now_date, "0000:00:0000", Unique_ID, total_cost, First_Price, Unique_ID, order_type)

                                buy_order = "INSERT INTO orders(lastuuid,currency,quantity,executed_price,type,total_cost,status,filled_quantity,startdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                buy_order_value = (neworderdata_id, symbol, quantity, bought_price, order_type, total_cost, order_status, filled_quantity, now_date)

                                buyorder_data.execute(buy_history, buy_history_value)
                                buyorder_data.execute(buy_order, buy_order_value)

                                conn.commit()

                                #time.sleep(0.02)




                except Exception as ex:

                    #print(ex)
                    print(traceback.format_exc())
                    pass

                time.sleep(0.0001)
                loop_time = time.time()

                print ( " {0} seconds".format(loop_time - program_starts), " ::: ",  now_date, "--", "Task#:", bot_id, '\n', currency_pair, currency_pair_amount, "Last Buy Price:", initial_buy, "and Last Sell Price:", initial_sell)
                #print(currency_pair, currency_pair_amount, "Last Buy Price:", initial_buy, "and Last Sell Price:", initial_sell)

                #print(str(Socket_data))

                time.sleep(0.1001)



        time.sleep(0.100)
        
        bot()


    
    except Exception as ex:

        print(ex)
        #print(traceback.format_exc())
        pass
    
    



    time.sleep(5.10)
