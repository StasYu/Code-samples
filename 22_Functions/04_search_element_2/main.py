site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

user_key = input('enter necessary key: ')

def find_key(key,site):
    if key in site.keys():
        return site[key]
    if isinstance(site.keys(), dict):
        find_key(key, site.keys())
    else:
        print('key is not found')


print(find_key(user_key, site))
