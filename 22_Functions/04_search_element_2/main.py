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

user_key = input('enter necessary key: ').split()
print(user_key)
def find_key(site, key, depth, count=0):
    count += 1
    if depth is not None and count > int(depth):
        return None

    if key in site:
        return site[key]

    for i_site in site.values():
        if isinstance(i_site, dict):
            result = find_key(i_site, key, depth, count)
            if result:
                break
    else:
        result = None

    return result

if len(user_key) == 1:
    res = find_key(site, user_key[0], depth=None)
elif len(user_key) > 1:
    res = find_key(site, user_key[0], depth=user_key[1])
print(res)
