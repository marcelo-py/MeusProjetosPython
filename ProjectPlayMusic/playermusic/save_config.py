import json

a = './arquivos/config.json'


def arquivo_existe():
    try:
        arq = open(a, 'r')
        arq.close()
        return True
    except Exception as erro:
        print(erro, '... Deve ser criado automaticamente')
        return False


def save_config(musica='', volume='', diretorio=''):
    if not arquivo_existe():
        conf_set = {'ultima_musica': 'Selecione uma musica', 'volume': 100, 'musica_e_diretorio': '/'}
        with open(a, 'w') as ini:
            json.dump(conf_set, ini, indent=True)
        return conf_set

    else:
        config_save = {'ultima_musica': musica, 'volume': volume, 'musica_e_diretorio': diretorio}
        with open(a, 'w+') as js:
            json.dump(config_save, js, indent=True)


def consult_config():
    if arquivo_existe():
        with open(a, 'r') as js:
            dic = json.load(js)
            return dic

    return save_config()
