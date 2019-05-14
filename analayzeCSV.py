import pandas as pd
import csv
data = pd.read_csv('predictions_CHO.csv')



Hasta1R = data[data['Filename'].str.startswith('hasta1 ')].mean()
Hasta1L = data[data['Filename'].str.startswith('hasta1l ')].mean()
Hasta2R = data[data['Filename'].str.startswith('hasta2 ')].mean()
Hasta2L = data[data['Filename'].str.startswith('hasta2l ')].mean()
Hasta3R = data[data['Filename'].str.startswith('hasta3 ')].mean()
Hasta3L = data[data['Filename'].str.startswith('hasta3l ')].mean()
Hasta4R = data[data['Filename'].str.startswith('hasta4 ')].mean()
Hasta4L = data[data['Filename'].str.startswith('hasta4l ')].mean()
Hasta5R = data[data['Filename'].str.startswith('hasta5 ')].mean()
Hasta5L = data[data['Filename'].str.startswith('hasta5l ')].mean()
Hasta6R = data[data['Filename'].str.startswith('hasta6 ')].mean()
Hasta6L = data[data['Filename'].str.startswith('hasta6l ')].mean()
Hasta7R = data[data['Filename'].str.startswith('hasta7 ')].mean()
Hasta7L = data[data['Filename'].str.startswith('hasta7l ')].mean()
Hasta8R = data[data['Filename'].str.startswith('hasta8 ')].mean()
Hasta8L = data[data['Filename'].str.startswith('hasta8l ')].mean()
Hasta9R = data[data['Filename'].str.startswith('hasta9 ')].mean()
Hasta9L = data[data['Filename'].str.startswith('hasta9l ')].mean()
Hasta10R = data[data['Filename'].str.startswith('hasta10 ')].mean()
Hasta10L = data[data['Filename'].str.startswith('hasta10l ')].mean()
Hasta11R = data[data['Filename'].str.startswith('hasta11 ')].mean()
Hasta11L = data[data['Filename'].str.startswith('hasta11l ')].mean()
Hasta12R = data[data['Filename'].str.startswith('hasta12 ')].mean()
Hasta12L = data[data['Filename'].str.startswith('hasta12l ')].mean()
Hasta13R = data[data['Filename'].str.startswith('hasta13 ')].mean()
Hasta13L = data[data['Filename'].str.startswith('hasta13l ')].mean()
Hasta14R = data[data['Filename'].str.startswith('hasta14 ')].mean()
Hasta14L = data[data['Filename'].str.startswith('hasta14l ')].mean()
Hasta15R = data[data['Filename'].str.startswith('hasta15 ')].mean()
Hasta15L = data[data['Filename'].str.startswith('hasta15l ')].mean()
Hasta16R = data[data['Filename'].str.startswith('hasta16 ')].mean()
Hasta16L = data[data['Filename'].str.startswith('hasta16l ')].mean()
Hasta17R = data[data['Filename'].str.startswith('hasta17 ')].mean()
Hasta17L = data[data['Filename'].str.startswith('hasta17l ')].mean()
Hasta18R = data[data['Filename'].str.startswith('hasta18 ')].mean()
Hasta18L = data[data['Filename'].str.startswith('hasta18l ')].mean()
Hasta19R = data[data['Filename'].str.startswith('hasta19 ')].mean()
Hasta19L = data[data['Filename'].str.startswith('hasta19l ')].mean()


print ('Hasta1R', Hasta1R,
'Hasta1L',Hasta1L,
'Hasta2R',Hasta2R,
'Hasta2L',Hasta2R,
'Hasta3R',Hasta3R,
'Hasta3L',Hasta3L,
'Hasta4R',Hasta4R,
'Hasta4L',Hasta4L,
'Hasta5R',Hasta5R,
'Hasta5L2',Hasta5L,
'Hasta6R',Hasta6R,
'Hasta6L',Hasta6L,
'Hasta7R',Hasta7R,
'Hasta7L',Hasta7L,
'Hasta8R',Hasta8R,
'Hasta8L',Hasta8L,
'Hasta9R',Hasta9R,
'Hasta9L',Hasta9L,
'Hasta10R',Hasta10R,
'Hasta10L',Hasta10L,
'Hasta11R',Hasta11R,
'Hasta11L',Hasta11L,
'Hasta12R',Hasta12R,
'Hasta12L',Hasta12L,
'Hasta13R',Hasta13R,
'Hasta13L',Hasta13L,
'Hasta14R',Hasta14R,
'Hasta14L',Hasta14L,
'Hasta15R',Hasta15R,
'Hasta15L',Hasta15L,
'Hasta16R',Hasta16R,
'Hasta16L',Hasta16L,
'Hasta17R',Hasta17R,
'asta17L',Hasta17L,
'Hasta18R',Hasta18R,
'Hasta18L',Hasta18L,
'Hasta19R',Hasta19R,
'Hasta19L',Hasta19L)
