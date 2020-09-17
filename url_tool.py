# 用于按照规则生成URL序列，主要修改object字段
def generate_urls(base_url: str, start: int = 1, stop: int = 0, step: int = 1):
    path, str_params = base_url.split('?')  # 拆分出Params
    params = {param.split('=')[0]: param.split('=')[1] for param in str_params.split('&')}  # 将str_params转换成字典
    params['object'] = '.'.join(params['object'].split('.')[:-1]) + '.{}'   # 修改params的Object字段
    str_url = '?'.join((path, '&'.join(['='.join((i, params[i])) for i in params])))    # 组合出修改后的URL
    return (str_url.format(str(i)) for i in range(start, stop + 1, step))   # 生成URL序列并返回
