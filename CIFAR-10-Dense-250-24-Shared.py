import tensorflow as tf
import os
from scipy import misc
import csv

initializer=tf.contrib.layers.xavier_initializer()

weights={
    'conv1': tf.get_variable('conv1', [7,7,3,24],tf.float32,initializer),

    'd1conv11': tf.get_variable('d1conv11w',[1,1,24,96],tf.float32,initializer),
    'd133conv1': tf.get_variable('d1conv12w',[3,3,96,24],tf.float32,initializer),
    'd1conv21': tf.get_variable('d1conv21w',[1,1,48,96],tf.float32,initializer),
    'd1conv31': tf.get_variable('d1conv31w',[1,1,72,96],tf.float32,initializer),
    'd1conv41': tf.get_variable('d1conv41w',[1,1,96,96],tf.float32,initializer),
    'd133conv2': tf.get_variable('d1conv42w',[3,3,96,24],tf.float32,initializer),
    'd1conv51': tf.get_variable('d1conv51w',[1,1,120,96],tf.float32,initializer),
    'd1conv61': tf.get_variable('d1conv61w',[1,1,144,96],tf.float32,initializer),

    't1conv': tf.get_variable('t1convw',[1,1,168,84],tf.float32,initializer),

    'd2conv11': tf.get_variable('d2conv11w',[1,1,84,96],tf.float32,initializer),
    'd233conv1': tf.get_variable('d2conv12w',[3,3,96,24],tf.float32,initializer),
    'd2conv21': tf.get_variable('d2conv21w',[1,1,108,96],tf.float32,initializer),
    'd2conv31': tf.get_variable('d2conv31w',[1,1,132,96],tf.float32,initializer),
    'd2conv41': tf.get_variable('d2conv41w',[1,1,156,96],tf.float32,initializer),
    'd2conv51': tf.get_variable('d2conv51w',[1,1,180,96],tf.float32,initializer),
    'd2conv61': tf.get_variable('d2conv61w',[1,1,204,96],tf.float32,initializer),
    'd2conv71': tf.get_variable('d2conv71w',[1,1,228,96],tf.float32,initializer),
    'd233conv2': tf.get_variable('d2conv72w',[3,3,96,24],tf.float32,initializer),
    'd2conv81': tf.get_variable('d2conv81w',[1,1,252,96],tf.float32,initializer),
    'd2conv91': tf.get_variable('d2conv91w',[1,1,276,96],tf.float32,initializer),
    'd2conv101': tf.get_variable('d2conv101w',[1,1,300,96],tf.float32,initializer),
    'd2conv111': tf.get_variable('d2conv111w',[1,1,324,96],tf.float32,initializer),
    'd2conv121': tf.get_variable('d2conv121w',[1,1,348,96],tf.float32,initializer),

    't2conv': tf.get_variable('t2convw',[1,1,372,186],tf.float32,initializer),

    'd3conv11': tf.get_variable('d3conv11w',[1,1,186,96],tf.float32,initializer),
    'd333conv1': tf.get_variable('d3conv12w',[3,3,96,24],tf.float32,initializer),
    'd3conv21': tf.get_variable('d3conv21w',[1,1,210,96],tf.float32,initializer),
    'd3conv31': tf.get_variable('d3conv31w',[1,1,234,96],tf.float32,initializer),
    'd3conv41': tf.get_variable('d3conv41w',[1,1,258,96],tf.float32,initializer),
    'd3conv51': tf.get_variable('d3conv51w',[1,1,282,96],tf.float32,initializer),
    'd3conv61': tf.get_variable('d3conv61w',[1,1,306,96],tf.float32,initializer),
    'd3conv71': tf.get_variable('d3conv71w',[1,1,330,96],tf.float32,initializer),
    'd3conv81': tf.get_variable('d3conv81w',[1,1,354,96],tf.float32,initializer),
    'd3conv91': tf.get_variable('d3conv91w',[1,1,378,96],tf.float32,initializer),
    'd3conv101': tf.get_variable('d3conv101w',[1,1,402,96],tf.float32,initializer),
    'd3conv111': tf.get_variable('d3conv111w',[1,1,426,96],tf.float32,initializer),
    'd3conv121': tf.get_variable('d3conv121w',[1,1,450,96],tf.float32,initializer),
    'd3conv131': tf.get_variable('d3conv131w',[1,1,474,96],tf.float32,initializer),
    'd3conv141': tf.get_variable('d3conv141w',[1,1,498,96],tf.float32,initializer),
    'd3conv151': tf.get_variable('d3conv151w',[1,1,522,96],tf.float32,initializer),
    'd3conv161': tf.get_variable('d3conv161w',[1,1,546,96],tf.float32,initializer),
    'd3conv171': tf.get_variable('d3conv171w',[1,1,570,96],tf.float32,initializer),
    'd3conv181': tf.get_variable('d3conv181w',[1,1,594,96],tf.float32,initializer),
    'd3conv191': tf.get_variable('d3conv191w',[1,1,618,96],tf.float32,initializer),
    'd3conv201': tf.get_variable('d3conv201w',[1,1,642,96],tf.float32,initializer),
    'd3conv211': tf.get_variable('d3conv211w',[1,1,666,96],tf.float32,initializer),
    'd3conv221': tf.get_variable('d3conv221w',[1,1,690,96],tf.float32,initializer),
    'd3conv231': tf.get_variable('d3conv231w',[1,1,714,96],tf.float32,initializer),
    'd3conv241': tf.get_variable('d3conv241w',[1,1,738,96],tf.float32,initializer),
    'd3conv251': tf.get_variable('d3conv251w',[1,1,762,96],tf.float32,initializer),
    'd3conv261': tf.get_variable('d3conv261w',[1,1,786,96],tf.float32,initializer),
    'd3conv271': tf.get_variable('d3conv271w',[1,1,810,96],tf.float32,initializer),
    'd3conv281': tf.get_variable('d3conv281w',[1,1,834,96],tf.float32,initializer),
    'd3conv291': tf.get_variable('d3conv291w',[1,1,858,96],tf.float32,initializer),
    'd3conv301': tf.get_variable('d3conv301w',[1,1,882,96],tf.float32,initializer),
    'd3conv311': tf.get_variable('d3conv311w',[1,1,906,96],tf.float32,initializer),
    'd333conv2': tf.get_variable('d3conv312w',[3,3,96,24],tf.float32,initializer),
    'd3conv321': tf.get_variable('d3conv321w',[1,1,930,96],tf.float32,initializer),
    'd3conv331': tf.get_variable('d3conv331w',[1,1,954,96],tf.float32,initializer),
    'd3conv341': tf.get_variable('d3conv341w',[1,1,978,96],tf.float32,initializer),
    'd3conv351': tf.get_variable('d3conv351w',[1,1,1002,96],tf.float32,initializer),
    'd3conv361': tf.get_variable('d3conv361w',[1,1,1026,96],tf.float32,initializer),
    'd3conv371': tf.get_variable('d3conv371w',[1,1,1050,96],tf.float32,initializer),
    'd3conv381': tf.get_variable('d3conv381w',[1,1,1074,96],tf.float32,initializer),
    'd3conv391': tf.get_variable('d3conv391w',[1,1,1098,96],tf.float32,initializer),
    'd3conv401': tf.get_variable('d3conv401w',[1,1,1122,96],tf.float32,initializer),
    'd3conv411': tf.get_variable('d3conv411w',[1,1,1146,96],tf.float32,initializer),
    'd3conv421': tf.get_variable('d3conv421w',[1,1,1170,96],tf.float32,initializer),
    'd3conv431': tf.get_variable('d3conv431w',[1,1,1194,96],tf.float32,initializer),
    'd3conv441': tf.get_variable('d3conv441w',[1,1,1218,96],tf.float32,initializer),
    'd3conv451': tf.get_variable('d3conv451w',[1,1,1242,96],tf.float32,initializer),
    'd3conv461': tf.get_variable('d3conv461w',[1,1,1266,96],tf.float32,initializer),
    'd3conv471': tf.get_variable('d3conv471w',[1,1,1290,96],tf.float32,initializer),
    'd3conv481': tf.get_variable('d3conv481w',[1,1,1314,96],tf.float32,initializer),
    'd3conv491': tf.get_variable('d3conv491w',[1,1,1338,96],tf.float32,initializer),
    'd3conv501': tf.get_variable('d3conv501w',[1,1,1362,96],tf.float32,initializer),
    'd3conv511': tf.get_variable('d3conv511w',[1,1,1386,96],tf.float32,initializer),
    'd3conv521': tf.get_variable('d3conv521w',[1,1,1410,96],tf.float32,initializer),
    'd3conv531': tf.get_variable('d3conv531w',[1,1,1434,96],tf.float32,initializer),
    'd3conv541': tf.get_variable('d3conv541w',[1,1,1458,96],tf.float32,initializer),
    'd3conv551': tf.get_variable('d3conv551w',[1,1,1482,96],tf.float32,initializer),
    'd3conv561': tf.get_variable('d3conv561w',[1,1,1506,96],tf.float32,initializer),
    'd3conv571': tf.get_variable('d3conv571w',[1,1,1530,96],tf.float32,initializer),
    'd3conv581': tf.get_variable('d3conv581w',[1,1,1554,96],tf.float32,initializer),
    'd3conv591': tf.get_variable('d3conv591w',[1,1,1578,96],tf.float32,initializer),
    'd3conv601': tf.get_variable('d3conv601w',[1,1,1602,96],tf.float32,initializer),

    't3conv': tf.get_variable('t3convw',[1,1,1626,813],tf.float32,initializer),

    'd4conv11': tf.get_variable('d4conv11w',[1,1,813,96],tf.float32,initializer),
    'd433conv1': tf.get_variable('d4conv12w',[3,3,96,24],tf.float32,initializer),
    'd4conv21': tf.get_variable('d4conv21w',[1,1,837,96],tf.float32,initializer),
    'd4conv31': tf.get_variable('d4conv31w',[1,1,861,96],tf.float32,initializer),
    'd4conv41': tf.get_variable('d4conv41w',[1,1,885,96],tf.float32,initializer),
    'd4conv51': tf.get_variable('d4conv51w',[1,1,909,96],tf.float32,initializer),
    'd4conv61': tf.get_variable('d4conv61w',[1,1,933,96],tf.float32,initializer),
    'd4conv71': tf.get_variable('d4conv71w',[1,1,957,96],tf.float32,initializer),
    'd4conv81': tf.get_variable('d4conv81w',[1,1,981,96],tf.float32,initializer),
    'd4conv91': tf.get_variable('d4conv91w',[1,1,1005,96],tf.float32,initializer),
    'd4conv101': tf.get_variable('d4conv101w',[1,1,1029,96],tf.float32,initializer),
    'd4conv111': tf.get_variable('d4conv111w',[1,1,1053,96],tf.float32,initializer),
    'd4conv121': tf.get_variable('d4conv121w',[1,1,1077,96],tf.float32,initializer),
    'd4conv131': tf.get_variable('d4conv131w',[1,1,1101,96],tf.float32,initializer),
    'd4conv141': tf.get_variable('d4conv141w',[1,1,1125,96],tf.float32,initializer),
    'd4conv151': tf.get_variable('d4conv151w',[1,1,1149,96],tf.float32,initializer),
    'd4conv161': tf.get_variable('d4conv161w',[1,1,1173,96],tf.float32,initializer),
    'd4conv171': tf.get_variable('d4conv171w',[1,1,1197,96],tf.float32,initializer),
    'd4conv181': tf.get_variable('d4conv181w',[1,1,1221,96],tf.float32,initializer),
    'd4conv191': tf.get_variable('d4conv191w',[1,1,1245,96],tf.float32,initializer),
    'd4conv201': tf.get_variable('d4conv201w',[1,1,1269,96],tf.float32,initializer),
    'd4conv211': tf.get_variable('d4conv211w',[1,1,1293,96],tf.float32,initializer),
    'd4conv221': tf.get_variable('d4conv221w',[1,1,1317,96],tf.float32,initializer),
    'd433conv2': tf.get_variable('d4conv222w',[3,3,96,24],tf.float32,initializer),
    'd4conv231': tf.get_variable('d4conv231w',[1,1,1341,96],tf.float32,initializer),
    'd4conv241': tf.get_variable('d4conv241w',[1,1,1365,96],tf.float32,initializer),
    'd4conv251': tf.get_variable('d4conv251w',[1,1,1389,96],tf.float32,initializer),
    'd4conv261': tf.get_variable('d4conv261w',[1,1,1413,96],tf.float32,initializer),
    'd4conv271': tf.get_variable('d4conv271w',[1,1,1437,96],tf.float32,initializer),
    'd4conv281': tf.get_variable('d4conv281w',[1,1,1461,96],tf.float32,initializer),
    'd4conv291': tf.get_variable('d4conv291w',[1,1,1485,96],tf.float32,initializer),
    'd4conv301': tf.get_variable('d4conv301w',[1,1,1509,96],tf.float32,initializer),
    'd4conv311': tf.get_variable('d4conv311w',[1,1,1533,96],tf.float32,initializer),
    'd4conv321': tf.get_variable('d4conv321w',[1,1,1557,96],tf.float32,initializer),
    'd4conv331': tf.get_variable('d4conv331w',[1,1,1581,96],tf.float32,initializer),
    'd4conv341': tf.get_variable('d4conv341w',[1,1,1605,96],tf.float32,initializer),
    'd4conv351': tf.get_variable('d4conv351w',[1,1,1629,96],tf.float32,initializer),
    'd4conv361': tf.get_variable('d4conv361w',[1,1,1653,96],tf.float32,initializer),
    'd4conv371': tf.get_variable('d4conv371w',[1,1,1677,96],tf.float32,initializer),
    'd4conv381': tf.get_variable('d4conv381w',[1,1,1701,96],tf.float32,initializer),
    'd4conv391': tf.get_variable('d4conv391w',[1,1,1725,96],tf.float32,initializer),
    'd4conv401': tf.get_variable('d4conv401w',[1,1,1749,96],tf.float32,initializer),
    'd4conv411': tf.get_variable('d4conv411w',[1,1,1773,96],tf.float32,initializer),
    'd4conv421': tf.get_variable('d4conv421w',[1,1,1797,96],tf.float32,initializer),

    'fc': tf.get_variable('fcw',[1821,10],tf.float32,initializer),
}

biases={
    'conv1': tf.get_variable('conv1b',[24],tf.float32,initializer),

    'd1conv11': tf.get_variable('d1conv11b',[96],tf.float32,initializer),
    'd133conv1': tf.get_variable('d1conv12b',[24],tf.float32,initializer),
    'd1conv21': tf.get_variable('d1conv21b',[96],tf.float32,initializer),
    'd1conv31': tf.get_variable('d1conv31b',[96],tf.float32,initializer),
    'd1conv41': tf.get_variable('d1conv41b',[96],tf.float32,initializer),
    'd133conv2': tf.get_variable('d1conv42b',[24],tf.float32,initializer),
    'd1conv51': tf.get_variable('d1conv51b',[96],tf.float32,initializer),
    'd1conv61': tf.get_variable('d1conv61b',[96],tf.float32,initializer),

    't1conv': tf.get_variable('t1convb',[84],tf.float32,initializer),

    'd2conv11': tf.get_variable('d2conv11b',[96],tf.float32,initializer),
    'd233conv1': tf.get_variable('d2conv12b',[24],tf.float32,initializer),
    'd2conv21': tf.get_variable('d2conv21b',[96],tf.float32,initializer),
    'd2conv31': tf.get_variable('d2conv31b',[96],tf.float32,initializer),
    'd2conv41': tf.get_variable('d2conv41b',[96],tf.float32,initializer),
    'd2conv51': tf.get_variable('d2conv51b',[96],tf.float32,initializer),
    'd2conv61': tf.get_variable('d2conv61b',[96],tf.float32,initializer),
    'd2conv71': tf.get_variable('d2conv71b',[96],tf.float32,initializer),
    'd233conv2': tf.get_variable('d2conv72b',[24],tf.float32,initializer),
    'd2conv81': tf.get_variable('d2conv81b',[96],tf.float32,initializer),
    'd2conv91': tf.get_variable('d2conv91b',[96],tf.float32,initializer),
    'd2conv101': tf.get_variable('d2conv101b',[96],tf.float32,initializer),
    'd2conv111': tf.get_variable('d2conv111b',[96],tf.float32,initializer),
    'd2conv121': tf.get_variable('d2conv121b',[96],tf.float32,initializer),

    't2conv': tf.get_variable('t2conv',[186],tf.float32,initializer),

    'd3conv11': tf.get_variable('d3conv11b',[96],tf.float32,initializer),
    'd333conv1': tf.get_variable('d3conv12b',[24],tf.float32,initializer),
    'd3conv21': tf.get_variable('d3conv21b',[96],tf.float32,initializer),
    'd3conv31': tf.get_variable('d3conv31b',[96],tf.float32,initializer),
    'd3conv41': tf.get_variable('d3conv41b',[96],tf.float32,initializer),
    'd3conv51': tf.get_variable('d3conv51b',[96],tf.float32,initializer),
    'd3conv61': tf.get_variable('d3conv61b',[96],tf.float32,initializer),
    'd3conv71': tf.get_variable('d3conv71b',[96],tf.float32,initializer),
    'd3conv81': tf.get_variable('d3conv81b',[96],tf.float32,initializer),
    'd3conv91': tf.get_variable('d3conv91b',[96],tf.float32,initializer),
    'd3conv101': tf.get_variable('d3conv101b',[96],tf.float32,initializer),
    'd3conv111': tf.get_variable('d3conv111b',[96],tf.float32,initializer),
    'd3conv121': tf.get_variable('d3conv121b',[96],tf.float32,initializer),
    'd3conv131': tf.get_variable('d3conv131b',[96],tf.float32,initializer),
    'd3conv141': tf.get_variable('d3conv141b',[96],tf.float32,initializer),
    'd3conv151': tf.get_variable('d3conv151b',[96],tf.float32,initializer),
    'd3conv161': tf.get_variable('d3conv161b',[96],tf.float32,initializer),
    'd3conv171': tf.get_variable('d3conv171b',[96],tf.float32,initializer),
    'd3conv181': tf.get_variable('d3conv181b',[96],tf.float32,initializer),
    'd3conv191': tf.get_variable('d3conv191b',[96],tf.float32,initializer),
    'd3conv201': tf.get_variable('d3conv201b',[96],tf.float32,initializer),
    'd3conv211': tf.get_variable('d3conv211b',[96],tf.float32,initializer),
    'd3conv221': tf.get_variable('d3conv221b',[96],tf.float32,initializer),
    'd3conv231': tf.get_variable('d3conv231b',[96],tf.float32,initializer),
    'd3conv241': tf.get_variable('d3conv241b',[96],tf.float32,initializer),
    'd3conv251': tf.get_variable('d3conv251b',[96],tf.float32,initializer),
    'd3conv261': tf.get_variable('d3conv261b',[96],tf.float32,initializer),
    'd3conv271': tf.get_variable('d3conv271b',[96],tf.float32,initializer),
    'd3conv281': tf.get_variable('d3conv281b',[96],tf.float32,initializer),
    'd3conv291': tf.get_variable('d3conv291b',[96],tf.float32,initializer),
    'd3conv301': tf.get_variable('d3conv301b',[96],tf.float32,initializer),
    'd3conv311': tf.get_variable('d3conv311b',[96],tf.float32,initializer),
    'd333conv2': tf.get_variable('d3conv312b',[24],tf.float32,initializer),
    'd3conv321': tf.get_variable('d3conv321b',[96],tf.float32,initializer),
    'd3conv331': tf.get_variable('d3conv331b',[96],tf.float32,initializer),
    'd3conv341': tf.get_variable('d3conv341b',[96],tf.float32,initializer),
    'd3conv351': tf.get_variable('d3conv351b',[96],tf.float32,initializer),
    'd3conv361': tf.get_variable('d3conv361b',[96],tf.float32,initializer),
    'd3conv371': tf.get_variable('d3conv371b',[96],tf.float32,initializer),
    'd3conv381': tf.get_variable('d3conv381b',[96],tf.float32,initializer),
    'd3conv391': tf.get_variable('d3conv391b',[96],tf.float32,initializer),
    'd3conv401': tf.get_variable('d3conv401b',[96],tf.float32,initializer),
    'd3conv411': tf.get_variable('d3conv411b',[96],tf.float32,initializer),
    'd3conv421': tf.get_variable('d3conv421b',[96],tf.float32,initializer),
    'd3conv431': tf.get_variable('d3conv431b',[96],tf.float32,initializer),
    'd3conv441': tf.get_variable('d3conv441b',[96],tf.float32,initializer),
    'd3conv451': tf.get_variable('d3conv451b',[96],tf.float32,initializer),
    'd3conv461': tf.get_variable('d3conv461b',[96],tf.float32,initializer),
    'd3conv471': tf.get_variable('d3conv471b',[96],tf.float32,initializer),
    'd3conv481': tf.get_variable('d3conv481b',[96],tf.float32,initializer),
    'd3conv491': tf.get_variable('d3conv491b',[96],tf.float32,initializer),
    'd3conv501': tf.get_variable('d3conv501b',[96],tf.float32,initializer),
    'd3conv511': tf.get_variable('d3conv511b',[96],tf.float32,initializer),
    'd3conv521': tf.get_variable('d3conv521b',[96],tf.float32,initializer),
    'd3conv531': tf.get_variable('d3conv531b',[96],tf.float32,initializer),
    'd3conv541': tf.get_variable('d3conv541b',[96],tf.float32,initializer),
    'd3conv551': tf.get_variable('d3conv551b',[96],tf.float32,initializer),
    'd3conv561': tf.get_variable('d3conv561b',[96],tf.float32,initializer),
    'd3conv571': tf.get_variable('d3conv571b',[96],tf.float32,initializer),
    'd3conv581': tf.get_variable('d3conv581b',[96],tf.float32,initializer),
    'd3conv591': tf.get_variable('d3conv591b',[96],tf.float32,initializer),
    'd3conv601': tf.get_variable('d3conv601b',[96],tf.float32,initializer),

    't3conv': tf.get_variable('t3conv',[813],tf.float32,initializer),

    'd4conv11': tf.get_variable('d4conv11b',[96],tf.float32,initializer),
    'd433conv1': tf.get_variable('d4conv12b',[24],tf.float32,initializer),
    'd4conv21': tf.get_variable('d4conv21b',[96],tf.float32,initializer),
    'd4conv31': tf.get_variable('d4conv31b',[96],tf.float32,initializer),
    'd4conv41': tf.get_variable('d4conv41b',[96],tf.float32,initializer),
    'd4conv51': tf.get_variable('d4conv51b',[96],tf.float32,initializer),
    'd4conv61': tf.get_variable('d4conv61b',[96],tf.float32,initializer),
    'd4conv71': tf.get_variable('d4conv71b',[96],tf.float32,initializer),
    'd4conv81': tf.get_variable('d4conv81b',[96],tf.float32,initializer),
    'd4conv91': tf.get_variable('d4conv91b',[96],tf.float32,initializer),
    'd4conv101': tf.get_variable('d4conv101b',[96],tf.float32,initializer),
    'd4conv111': tf.get_variable('d4conv111b',[96],tf.float32,initializer),
    'd4conv121': tf.get_variable('d4conv121b',[96],tf.float32,initializer),
    'd4conv131': tf.get_variable('d4conv131b',[96],tf.float32,initializer),
    'd4conv141': tf.get_variable('d4conv141b',[96],tf.float32,initializer),
    'd4conv151': tf.get_variable('d4conv151b',[96],tf.float32,initializer),
    'd4conv161': tf.get_variable('d4conv161b',[96],tf.float32,initializer),
    'd4conv171': tf.get_variable('d4conv171b',[96],tf.float32,initializer),
    'd4conv181': tf.get_variable('d4conv181b',[96],tf.float32,initializer),
    'd4conv191': tf.get_variable('d4conv191b',[96],tf.float32,initializer),
    'd4conv201': tf.get_variable('d4conv201b',[96],tf.float32,initializer),
    'd4conv211': tf.get_variable('d4conv211b',[96],tf.float32,initializer),
    'd4conv221': tf.get_variable('d4conv221b',[96],tf.float32,initializer),
    'd433conv2': tf.get_variable('d4conv222b',[24],tf.float32,initializer),
    'd4conv231': tf.get_variable('d4conv231b',[96],tf.float32,initializer),
    'd4conv241': tf.get_variable('d4conv241b',[96],tf.float32,initializer),
    'd4conv251': tf.get_variable('d4conv251b',[96],tf.float32,initializer),
    'd4conv261': tf.get_variable('d4conv261b',[96],tf.float32,initializer),
    'd4conv271': tf.get_variable('d4conv271b',[96],tf.float32,initializer),
    'd4conv281': tf.get_variable('d4conv281b',[96],tf.float32,initializer),
    'd4conv291': tf.get_variable('d4conv291b',[96],tf.float32,initializer),
    'd4conv301': tf.get_variable('d4conv301b',[96],tf.float32,initializer),
    'd4conv311': tf.get_variable('d4conv311b',[96],tf.float32,initializer),
    'd4conv321': tf.get_variable('d4conv321b',[96],tf.float32,initializer),
    'd4conv331': tf.get_variable('d4conv331b',[96],tf.float32,initializer),
    'd4conv341': tf.get_variable('d4conv341b',[96],tf.float32,initializer),
    'd4conv351': tf.get_variable('d4conv351b',[96],tf.float32,initializer),
    'd4conv361': tf.get_variable('d4conv361b',[96],tf.float32,initializer),
    'd4conv371': tf.get_variable('d4conv371b',[96],tf.float32,initializer),
    'd4conv381': tf.get_variable('d4conv381b',[96],tf.float32,initializer),
    'd4conv391': tf.get_variable('d4conv391b',[96],tf.float32,initializer),
    'd4conv401': tf.get_variable('d4conv401b',[96],tf.float32,initializer),
    'd4conv411': tf.get_variable('d4conv411b',[96],tf.float32,initializer),
    'd4conv421': tf.get_variable('d4conv421b',[96],tf.float32,initializer),

    'fc': tf.get_variable('fcb',[10],tf.float32,initializer),
}

x=tf.placeholder(tf.float32,[100,32,32,3])
y=tf.placeholder(tf.float32)

def conv(x,weight,bias):
    batchnorm=tf.layers.batch_normalization(x)
    activate=tf.nn.relu(batchnorm,name='relu')
    convolution=tf.add(tf.nn.conv2d(activate,weight,strides=[1,1,1,1],padding='SAME'),bias,name='conv')
    return convolution

def subblock(x,weight11,bias11,weight33,bias33):
    conv11=conv(x,weight11,bias11)
    conv33=conv(conv11,weight33,bias33)
    return tf.concat([x,conv33],axis=3)

def avgpool(x,kernel,stride):
    return tf.nn.avg_pool(x,ksize=[1,kernel,kernel,1],strides=[1,stride,stride,1],padding='SAME')

def maxpool(x,kernel,stride):
    return tf.nn.max_pool(x,ksize=[1,kernel,kernel,1],strides=[1,stride,stride,1],padding='SAME')

def transition(x,weight11,bias11):
    conv11=conv(x,weight11,bias11)
    return avgpool(conv11,2,2)

def classification(x,weightfc,biasfc):
    globalpool=tf.reshape(tf.nn.avg_pool(x,ksize=[1,4,4,1],strides=[1,1,1,1],padding='VALID'),[-1,1821])
    fc=tf.add(tf.matmul(globalpool,weightfc),biasfc)
    return fc

def network(x):
    with tf.name_scope('InputLayer'):
        conv1=conv(x,weights['conv1'],biases['conv1'])
        pool=maxpool(conv1,3,1)

    with tf.name_scope('DenseBock1'):
        d1conv1=subblock(pool,weights['d1conv11'],biases['d1conv11'],weights['d133conv1'],biases['d133conv1'])
        d1conv2=subblock(d1conv1,weights['d1conv21'],biases['d1conv21'],weights['d133conv1'],biases['d133conv1'])
        d1conv3=subblock(d1conv2,weights['d1conv31'],biases['d1conv31'],weights['d133conv1'],biases['d133conv1'])
        d1conv4=subblock(d1conv3,weights['d1conv41'],biases['d1conv41'],weights['d133conv2'],biases['d133conv2'])
        d1conv5=subblock(d1conv4,weights['d1conv51'],biases['d1conv51'],weights['d133conv2'],biases['d133conv2'])
        d1conv6=subblock(d1conv5,weights['d1conv61'],biases['d1conv61'],weights['d133conv2'],biases['d133conv2'])

    with tf.name_scope('Transition1'):
        t1=transition(d1conv6,weights['t1conv'],biases['t1conv'])

    with tf.name_scope('DenseBlock2'):
        d2conv1=subblock(t1,weights['d2conv11'],biases['d2conv11'],weights['d233conv1'],biases['d233conv1'])
        d2conv2=subblock(d2conv1,weights['d2conv21'],biases['d2conv21'],weights['d233conv1'],biases['d233conv1'])
        d2conv3=subblock(d2conv2,weights['d2conv31'],biases['d2conv31'],weights['d233conv1'],biases['d233conv1'])
        d2conv4=subblock(d2conv3,weights['d2conv41'],biases['d2conv41'],weights['d233conv1'],biases['d233conv1'])
        d2conv5=subblock(d2conv4,weights['d2conv51'],biases['d2conv51'],weights['d233conv1'],biases['d233conv1'])
        d2conv6=subblock(d2conv5,weights['d2conv61'],biases['d2conv61'],weights['d233conv1'],biases['d233conv1'])
        d2conv7=subblock(d2conv6,weights['d2conv71'],biases['d2conv71'],weights['d233conv2'],biases['d233conv2'])
        d2conv8=subblock(d2conv7,weights['d2conv81'],biases['d2conv81'],weights['d233conv2'],biases['d233conv2'])
        d2conv9=subblock(d2conv8,weights['d2conv91'],biases['d2conv91'],weights['d233conv2'],biases['d233conv2'])
        d2conv10=subblock(d2conv9,weights['d2conv101'],biases['d2conv101'],weights['d233conv2'],biases['d233conv2'])
        d2conv11=subblock(d2conv10,weights['d2conv111'],biases['d2conv111'],weights['d233conv2'],biases['d233conv2'])
        d2conv12=subblock(d2conv11,weights['d2conv121'],biases['d2conv121'],weights['d233conv2'],biases['d233conv2'])

    with tf.name_scope('Transition2'):
        t2=transition(d2conv12,weights['t2conv'],biases['t2conv'])

    with tf.name_scope('DenseBlock3'):
        d3conv1=subblock(t2,weights['d3conv11'],biases['d3conv11'],weights['d333conv1'],biases['d333conv1'])
        d3conv2=subblock(d3conv1,weights['d3conv21'],biases['d3conv21'],weights['d333conv1'],biases['d333conv1'])
        d3conv3=subblock(d3conv2,weights['d3conv31'],biases['d3conv31'],weights['d333conv1'],biases['d333conv1'])
        d3conv4=subblock(d3conv3,weights['d3conv41'],biases['d3conv41'],weights['d333conv1'],biases['d333conv1'])
        d3conv5=subblock(d3conv4,weights['d3conv51'],biases['d3conv51'],weights['d333conv1'],biases['d333conv1'])
        d3conv6=subblock(d3conv5,weights['d3conv61'],biases['d3conv61'],weights['d333conv1'],biases['d333conv1'])
        d3conv7=subblock(d3conv6,weights['d3conv71'],biases['d3conv71'],weights['d333conv1'],biases['d333conv1'])
        d3conv8=subblock(d3conv7,weights['d3conv81'],biases['d3conv81'],weights['d333conv1'],biases['d333conv1'])
        d3conv9=subblock(d3conv8,weights['d3conv91'],biases['d3conv91'],weights['d333conv1'],biases['d333conv1'])
        d3conv10=subblock(d3conv9,weights['d3conv101'],biases['d3conv101'],weights['d333conv1'],biases['d333conv1'])
        d3conv11=subblock(d3conv10,weights['d3conv111'],biases['d3conv111'],weights['d333conv1'],biases['d333conv1'])
        d3conv12=subblock(d3conv11,weights['d3conv121'],biases['d3conv121'],weights['d333conv1'],biases['d333conv1'])
        d3conv13=subblock(d3conv12,weights['d3conv131'],biases['d3conv131'],weights['d333conv1'],biases['d333conv1'])
        d3conv14=subblock(d3conv13,weights['d3conv141'],biases['d3conv141'],weights['d333conv1'],biases['d333conv1'])
        d3conv15=subblock(d3conv14,weights['d3conv151'],biases['d3conv151'],weights['d333conv1'],biases['d333conv1'])
        d3conv16=subblock(d3conv15,weights['d3conv161'],biases['d3conv161'],weights['d333conv1'],biases['d333conv1'])
        d3conv17=subblock(d3conv16,weights['d3conv171'],biases['d3conv171'],weights['d333conv1'],biases['d333conv1'])
        d3conv18=subblock(d3conv17,weights['d3conv181'],biases['d3conv181'],weights['d333conv1'],biases['d333conv1'])
        d3conv19=subblock(d3conv18,weights['d3conv191'],biases['d3conv191'],weights['d333conv1'],biases['d333conv1'])
        d3conv20=subblock(d3conv19,weights['d3conv201'],biases['d3conv201'],weights['d333conv1'],biases['d333conv1'])
        d3conv21=subblock(d3conv20,weights['d3conv211'],biases['d3conv211'],weights['d333conv1'],biases['d333conv1'])
        d3conv22=subblock(d3conv21,weights['d3conv221'],biases['d3conv221'],weights['d333conv1'],biases['d333conv1'])
        d3conv23=subblock(d3conv22,weights['d3conv231'],biases['d3conv231'],weights['d333conv1'],biases['d333conv1'])
        d3conv24=subblock(d3conv23,weights['d3conv241'],biases['d3conv241'],weights['d333conv1'],biases['d333conv1'])
        d3conv25=subblock(d3conv24,weights['d3conv251'],biases['d3conv251'],weights['d333conv1'],biases['d333conv1'])
        d3conv26=subblock(d3conv25,weights['d3conv261'],biases['d3conv261'],weights['d333conv1'],biases['d333conv1'])
        d3conv27=subblock(d3conv26,weights['d3conv271'],biases['d3conv271'],weights['d333conv1'],biases['d333conv1'])
        d3conv28=subblock(d3conv27,weights['d3conv281'],biases['d3conv281'],weights['d333conv1'],biases['d333conv1'])
        d3conv29=subblock(d3conv28,weights['d3conv291'],biases['d3conv291'],weights['d333conv1'],biases['d333conv1'])
        d3conv30=subblock(d3conv29,weights['d3conv301'],biases['d3conv301'],weights['d333conv1'],biases['d333conv1'])

        d3conv31=subblock(d3conv30,weights['d3conv311'],biases['d3conv311'],weights['d333conv2'],biases['d333conv2'])
        d3conv32=subblock(d3conv31,weights['d3conv321'],biases['d3conv321'],weights['d333conv2'],biases['d333conv2'])
        d3conv33=subblock(d3conv32,weights['d3conv331'],biases['d3conv331'],weights['d333conv2'],biases['d333conv2'])
        d3conv34=subblock(d3conv33,weights['d3conv341'],biases['d3conv341'],weights['d333conv2'],biases['d333conv2'])
        d3conv35=subblock(d3conv34,weights['d3conv351'],biases['d3conv351'],weights['d333conv2'],biases['d333conv2'])
        d3conv36=subblock(d3conv35,weights['d3conv361'],biases['d3conv361'],weights['d333conv2'],biases['d333conv2'])
        d3conv37=subblock(d3conv36,weights['d3conv371'],biases['d3conv371'],weights['d333conv2'],biases['d333conv2'])
        d3conv38=subblock(d3conv37,weights['d3conv381'],biases['d3conv381'],weights['d333conv2'],biases['d333conv2'])
        d3conv39=subblock(d3conv38,weights['d3conv391'],biases['d3conv391'],weights['d333conv2'],biases['d333conv2'])
        d3conv40=subblock(d3conv39,weights['d3conv401'],biases['d3conv401'],weights['d333conv2'],biases['d333conv2'])
        d3conv41=subblock(d3conv40,weights['d3conv411'],biases['d3conv411'],weights['d333conv2'],biases['d333conv2'])
        d3conv42=subblock(d3conv41,weights['d3conv421'],biases['d3conv421'],weights['d333conv2'],biases['d333conv2'])
        d3conv43=subblock(d3conv42,weights['d3conv431'],biases['d3conv431'],weights['d333conv2'],biases['d333conv2'])
        d3conv44=subblock(d3conv43,weights['d3conv441'],biases['d3conv441'],weights['d333conv2'],biases['d333conv2'])
        d3conv45=subblock(d3conv44,weights['d3conv451'],biases['d3conv451'],weights['d333conv2'],biases['d333conv2'])
        d3conv46=subblock(d3conv45,weights['d3conv461'],biases['d3conv461'],weights['d333conv2'],biases['d333conv2'])
        d3conv47=subblock(d3conv46,weights['d3conv471'],biases['d3conv471'],weights['d333conv2'],biases['d333conv2'])
        d3conv48=subblock(d3conv47,weights['d3conv481'],biases['d3conv481'],weights['d333conv2'],biases['d333conv2'])
        d3conv49=subblock(d3conv48,weights['d3conv491'],biases['d3conv491'],weights['d333conv2'],biases['d333conv2'])
        d3conv50=subblock(d3conv49,weights['d3conv501'],biases['d3conv501'],weights['d333conv2'],biases['d333conv2'])
        d3conv51=subblock(d3conv50,weights['d3conv511'],biases['d3conv511'],weights['d333conv2'],biases['d333conv2'])
        d3conv52=subblock(d3conv51,weights['d3conv521'],biases['d3conv521'],weights['d333conv2'],biases['d333conv2'])
        d3conv53=subblock(d3conv52,weights['d3conv531'],biases['d3conv531'],weights['d333conv2'],biases['d333conv2'])
        d3conv54=subblock(d3conv53,weights['d3conv541'],biases['d3conv541'],weights['d333conv2'],biases['d333conv2'])
        d3conv55=subblock(d3conv54,weights['d3conv551'],biases['d3conv551'],weights['d333conv2'],biases['d333conv2'])
        d3conv56=subblock(d3conv55,weights['d3conv561'],biases['d3conv561'],weights['d333conv2'],biases['d333conv2'])
        d3conv57=subblock(d3conv56,weights['d3conv571'],biases['d3conv571'],weights['d333conv2'],biases['d333conv2'])
        d3conv58=subblock(d3conv57,weights['d3conv581'],biases['d3conv581'],weights['d333conv2'],biases['d333conv2'])
        d3conv59=subblock(d3conv58,weights['d3conv591'],biases['d3conv591'],weights['d333conv2'],biases['d333conv2'])
        d3conv60=subblock(d3conv59,weights['d3conv601'],biases['d3conv601'],weights['d333conv2'],biases['d333conv2'])

    with tf.name_scope('Transition3'):
        t3=transition(d3conv60,weights['t3conv'],biases['t3conv'])

    with tf.name_scope('DenseBlock4'):
        d4conv1=subblock(t3,weights['d4conv11'],biases['d4conv11'],weights['d433conv1'],biases['d433conv1'])
        d4conv2=subblock(d4conv1,weights['d4conv21'],biases['d4conv21'],weights['d433conv1'],biases['d433conv1'])
        d4conv3=subblock(d4conv2,weights['d4conv31'],biases['d4conv31'],weights['d433conv1'],biases['d433conv1'])
        d4conv4=subblock(d4conv3,weights['d4conv41'],biases['d4conv41'],weights['d433conv1'],biases['d433conv1'])
        d4conv5=subblock(d4conv4,weights['d4conv51'],biases['d4conv51'],weights['d433conv1'],biases['d433conv1'])
        d4conv6=subblock(d4conv5,weights['d4conv61'],biases['d4conv61'],weights['d433conv1'],biases['d433conv1'])
        d4conv7=subblock(d4conv6,weights['d4conv71'],biases['d4conv71'],weights['d433conv1'],biases['d433conv1'])
        d4conv8=subblock(d4conv7,weights['d4conv81'],biases['d4conv81'],weights['d433conv1'],biases['d433conv1'])
        d4conv9=subblock(d4conv8,weights['d4conv91'],biases['d4conv91'],weights['d433conv1'],biases['d433conv1'])
        d4conv10=subblock(d4conv9,weights['d4conv101'],biases['d4conv101'],weights['d433conv1'],biases['d433conv1'])
        d4conv11=subblock(d4conv10,weights['d4conv111'],biases['d4conv111'],weights['d433conv1'],biases['d433conv1'])
        d4conv12=subblock(d4conv11,weights['d4conv121'],biases['d4conv121'],weights['d433conv1'],biases['d433conv1'])
        d4conv13=subblock(d4conv12,weights['d4conv131'],biases['d4conv131'],weights['d433conv1'],biases['d433conv1'])
        d4conv14=subblock(d4conv13,weights['d4conv141'],biases['d4conv141'],weights['d433conv1'],biases['d433conv1'])
        d4conv15=subblock(d4conv14,weights['d4conv151'],biases['d4conv151'],weights['d433conv1'],biases['d433conv1'])
        d4conv16=subblock(d4conv15,weights['d4conv161'],biases['d4conv161'],weights['d433conv1'],biases['d433conv1'])
        d4conv17=subblock(d4conv16,weights['d4conv171'],biases['d4conv171'],weights['d433conv1'],biases['d433conv1'])
        d4conv18=subblock(d4conv17,weights['d4conv181'],biases['d4conv181'],weights['d433conv1'],biases['d433conv1'])
        d4conv19=subblock(d4conv18,weights['d4conv191'],biases['d4conv191'],weights['d433conv1'],biases['d433conv1'])
        d4conv20=subblock(d4conv19,weights['d4conv201'],biases['d4conv201'],weights['d433conv1'],biases['d433conv1'])
        d4conv21=subblock(d4conv20,weights['d4conv211'],biases['d4conv211'],weights['d433conv1'],biases['d433conv1'])
        d4conv22=subblock(d4conv21,weights['d4conv221'],biases['d4conv221'],weights['d433conv2'],biases['d433conv2'])
        d4conv23=subblock(d4conv22,weights['d4conv231'],biases['d4conv231'],weights['d433conv2'],biases['d433conv2'])
        d4conv24=subblock(d4conv23,weights['d4conv241'],biases['d4conv241'],weights['d433conv2'],biases['d433conv2'])
        d4conv25=subblock(d4conv24,weights['d4conv251'],biases['d4conv251'],weights['d433conv2'],biases['d433conv2'])
        d4conv26=subblock(d4conv25,weights['d4conv261'],biases['d4conv261'],weights['d433conv2'],biases['d433conv2'])
        d4conv27=subblock(d4conv26,weights['d4conv271'],biases['d4conv271'],weights['d433conv2'],biases['d433conv2'])
        d4conv28=subblock(d4conv27,weights['d4conv281'],biases['d4conv281'],weights['d433conv2'],biases['d433conv2'])
        d4conv29=subblock(d4conv28,weights['d4conv291'],biases['d4conv291'],weights['d433conv2'],biases['d433conv2'])
        d4conv30=subblock(d4conv29,weights['d4conv301'],biases['d4conv301'],weights['d433conv2'],biases['d433conv2'])
        d4conv31=subblock(d4conv30,weights['d4conv311'],biases['d4conv311'],weights['d433conv2'],biases['d433conv2'])
        d4conv32=subblock(d4conv31,weights['d4conv321'],biases['d4conv321'],weights['d433conv2'],biases['d433conv2'])
        d4conv33=subblock(d4conv32,weights['d4conv331'],biases['d4conv331'],weights['d433conv2'],biases['d433conv2'])
        d4conv34=subblock(d4conv33,weights['d4conv341'],biases['d4conv341'],weights['d433conv2'],biases['d433conv2'])
        d4conv35=subblock(d4conv34,weights['d4conv351'],biases['d4conv351'],weights['d433conv2'],biases['d433conv2'])
        d4conv36=subblock(d4conv35,weights['d4conv361'],biases['d4conv361'],weights['d433conv2'],biases['d433conv2'])
        d4conv37=subblock(d4conv36,weights['d4conv371'],biases['d4conv371'],weights['d433conv2'],biases['d433conv2'])
        d4conv38=subblock(d4conv37,weights['d4conv381'],biases['d4conv381'],weights['d433conv2'],biases['d433conv2'])
        d4conv39=subblock(d4conv38,weights['d4conv391'],biases['d4conv391'],weights['d433conv2'],biases['d433conv2'])
        d4conv40=subblock(d4conv39,weights['d4conv401'],biases['d4conv401'],weights['d433conv2'],biases['d433conv2'])
        d4conv41=subblock(d4conv40,weights['d4conv411'],biases['d4conv411'],weights['d433conv2'],biases['d433conv2'])
        d4conv42=subblock(d4conv41,weights['d4conv421'],biases['d4conv421'],weights['d433conv2'],biases['d433conv2'])

    with tf.name_scope('ClassificationLayer'):
        out=classification(d4conv42,weights['fc'],biases['fc'])

    return out

predict_y=network(x)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=predict_y))
update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
with tf.control_dependencies(update_ops):
    optimize=tf.train.AdamOptimizer().minimize(loss)

def save(path,sess):
    saver=tf.train.Saver()
    saver.save(sess,path)

def restore(sess):
    saver=tf.train.Saver()
    saver.restore(sess,tf.train.latest_checkpoint('./Dense-250-24-Shared/'))


def train():
    print('Loading train images')
    path='train/'
    files=os.listdir(path)
    images=[]
    for file in files: images.append(misc.imread(path+file))
    print('Images loaded')
    labels=[]
    with open('trainLabels.csv','rt') as csvfile:
        labelcsv=csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in labelcsv:
            row=row[0].rstrip()
            row=row.split(',')
            row=row[-1]
            if row=='airplane': labels.append([1,0,0,0,0,0,0,0,0,0])
            if row=='automobile': labels.append([0,1,0,0,0,0,0,0,0,0])
            if row=='bird': labels.append([0,0,1,0,0,0,0,0,0,0])
            if row=='cat': labels.append([0,0,0,1,0,0,0,0,0,0])
            if row=='deer': labels.append([0,0,0,0,1,0,0,0,0,0])
            if row=='dog': labels.append([0,0,0,0,0,1,0,0,0,0])
            if row=='frog': labels.append([0,0,0,0,0,0,1,0,0,0])
            if row=='horse': labels.append([0,0,0,0,0,0,0,1,0,0])
            if row=='ship': labels.append([0,0,0,0,0,0,0,0,1,0])
            if row=='truck': labels.append([0,0,0,0,0,0,0,0,0,1])
    print('Labels loaded')
    print('Batch size : 10')
    print('Variables saved after every 2 Epochs')
    print('100 Epochs')
    with tf.Session() as sess:
        try: restore(sess)
        except: print("Couldn't restore, Reinitializing"); sess.run(tf.global_variables_initializer())
        for epoch in range(1,101):
            epochloss=0
            for i in range(1,501):
                batchimages,batchlabels=images[100*(i-1):100*(i)],labels[100*(i-1):100*i]
                batchloss,_=sess.run([loss,optimize],feed_dict={x:batchimages, y:batchlabels})
                print('Batch',i,'out of 500 completed in epoch',epoch,'. Batch loss : ', batchloss)
                epochloss+=batchloss
            print('Epoch',epoch,'completed, loss :',epochloss)
            if epoch%2==0: save('Dense-250-24-Shared/var.ckpt',sess)
        print('Network trained')

train()