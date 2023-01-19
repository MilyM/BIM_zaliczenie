import ifcopenshell as ifc


data = ifc.open('231110AC-11-Smiley-West-04-07-2007.ifc')

walls = data.by_type('IfcWall')
walls_number = len(walls)

print(f'Liczba ścian {walls_number}')

external_walls = []

# pset = ifc_u.element.get_psets(walls[0])
# print(pset['Pset_WallCommon']['IsExternal'])


for each in walls:
    pset = ifc.util.element.get_psets(each)
    if pset.get('Pset_WallCommon'):
        if bool(pset['Pset_WallCommon']['IsExternal']):
            external_walls.append(each)


external_walls_number = len(external_walls)
print(f'Liczba ścian zewnętrznych {external_walls_number}')