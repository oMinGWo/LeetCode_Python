import xlrd

data = xlrd.open_workbook('/Users/henrylee/Desktop/fuck.xlsx')

table = data.sheet_by_name('fuck')

nrows = table.nrows

content = ''

for i in range(1, nrows):
    name = table.cell(i, 1).value
    ns = name.split('-')
    name = ns[0]
    version = ns[1].split('.apk')[0]
    t = table.cell(i, 2).value[0:2]
    print i, name, version, t

    line = '%s & %s & %s & %s' % (str(i), name, version, t)
    if i % 2 == 1:
        content = content + '\hline\n'
        content = content + line
    else:
        content = content + ' & ' + line + '\\\\' + '\n'


print content
