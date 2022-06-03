climate = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

climate_new = []
temp = ''

for piece in climate:
    if piece.isdigit():
        temp += piece
    elif piece[0] == '+':
        temp += piece.zfill(3)
    elif temp:
        climate_new.append('"')
        climate_new.append(temp.zfill(2))
        climate_new.append('"')
        temp = ''
        climate_new.append(piece)
    else:
        climate_new.append(piece)
print(climate_new)

end = ' '
for gap in climate_new:
    if gap == '"':
        if end == '':
            end = ' '
        else:
            end = ''
    elif gap.isnumeric():
        end = ''
    print(gap, end=end)
