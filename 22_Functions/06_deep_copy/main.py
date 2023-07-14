# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iphone',
#             'div': 'Купить',
#             'p': 'продать'
#         }
#     }
# }

def struct(count):
    new_count = count - 1
    name = input('\nВведите название продукта для нового сайта: ')
    print(f"\nСайт для {name}:")
    print("site = {")
    print("    'html': {")
    print("        'head': {")
    print("           'title': 'Куплю/продам телефон недорого")
    print("        },")
    print("        'body': {")
    print(f"            'h2': f'У нас самая низкая цена на {name}',")
    print("            'div': 'Купить',")
    print("           'p': 'продать'")
    print("       }")
    print("   }")
    print("}")
    if new_count == 0:
        return None
    struct(new_count)


site_qtt = int(input('Сколько сайтов: '))
struct(site_qtt)

