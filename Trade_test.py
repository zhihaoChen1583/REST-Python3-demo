from HuobiServices import *

# 查询最新价格
symbol = "ltcbtc"
return_info = get_depth(symbol, type = "step0" )
return_info['ts'] = timestamp_to_datetime(return_info['ts'])
return_info['tick']['ts'] = timestamp_to_datetime(return_info['tick']['ts'])

print(return_info['tick']['ts'])
print("max bids", return_info['tick']['bids'][0])
print("min asks", return_info['tick']['asks'][0])

# 创建并执行订单
order = send_order(amount=10, source='api', symbol='ltcbtc', _type='buy-limit', price=0.0112)
print(order)