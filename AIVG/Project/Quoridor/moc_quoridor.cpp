/****************************************************************************
** Meta object code from reading C++ file 'quoridor.h'
**
** Created by: The Qt Meta Object Compiler version 68 (Qt 6.3.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../Quoridor/quoridor.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/QList>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'quoridor.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 68
#error "This file was generated using the moc from 6.3.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Quoridor_t {
    const uint offsetsAndSize[240];
    char stringdata0[2706];
};
#define QT_MOC_LITERAL(ofs, len) \
    uint(offsetof(qt_meta_stringdata_Quoridor_t, stringdata0) + ofs), len 
static const qt_meta_stringdata_Quoridor_t qt_meta_stringdata_Quoridor = {
    {
QT_MOC_LITERAL(0, 8), // "Quoridor"
QT_MOC_LITERAL(9, 7), // "ai_wall"
QT_MOC_LITERAL(17, 0), // ""
QT_MOC_LITERAL(18, 9), // "next_move"
QT_MOC_LITERAL(28, 9), // "best_move"
QT_MOC_LITERAL(38, 10), // "game_state"
QT_MOC_LITERAL(49, 1), // "s"
QT_MOC_LITERAL(51, 9), // "best_wall"
QT_MOC_LITERAL(61, 7), // "minimax"
QT_MOC_LITERAL(69, 1), // "n"
QT_MOC_LITERAL(71, 16), // "QTreeWidgetItem*"
QT_MOC_LITERAL(88, 17), // "check_wall_number"
QT_MOC_LITERAL(106, 13), // "shortest_path"
QT_MOC_LITERAL(120, 5), // "place"
QT_MOC_LITERAL(126, 10), // "find_nodes"
QT_MOC_LITERAL(137, 12), // "QList<place>"
QT_MOC_LITERAL(150, 9), // "find_near"
QT_MOC_LITERAL(160, 16), // "check_placeble_1"
QT_MOC_LITERAL(177, 16), // "check_placeble_2"
QT_MOC_LITERAL(194, 10), // "paintEvent"
QT_MOC_LITERAL(205, 12), // "QPaintEvent*"
QT_MOC_LITERAL(218, 15), // "mousePressEvent"
QT_MOC_LITERAL(234, 12), // "QMouseEvent*"
QT_MOC_LITERAL(247, 5), // "event"
QT_MOC_LITERAL(253, 24), // "on_newGameButton_clicked"
QT_MOC_LITERAL(278, 14), // "start_new_game"
QT_MOC_LITERAL(293, 14), // "undo_last_move"
QT_MOC_LITERAL(308, 10), // "find_moves"
QT_MOC_LITERAL(319, 13), // "reset_buttons"
QT_MOC_LITERAL(333, 12), // "game_manager"
QT_MOC_LITERAL(346, 9), // "game_over"
QT_MOC_LITERAL(356, 11), // "set_players"
QT_MOC_LITERAL(368, 12), // "remove_piece"
QT_MOC_LITERAL(381, 26), // "on_pushButton_0000_clicked"
QT_MOC_LITERAL(408, 26), // "on_pushButton_0002_clicked"
QT_MOC_LITERAL(435, 26), // "on_pushButton_0004_clicked"
QT_MOC_LITERAL(462, 26), // "on_pushButton_0006_clicked"
QT_MOC_LITERAL(489, 26), // "on_pushButton_0008_clicked"
QT_MOC_LITERAL(516, 26), // "on_pushButton_0010_clicked"
QT_MOC_LITERAL(543, 26), // "on_pushButton_0012_clicked"
QT_MOC_LITERAL(570, 26), // "on_pushButton_0014_clicked"
QT_MOC_LITERAL(597, 26), // "on_pushButton_0016_clicked"
QT_MOC_LITERAL(624, 26), // "on_pushButton_0200_clicked"
QT_MOC_LITERAL(651, 26), // "on_pushButton_0202_clicked"
QT_MOC_LITERAL(678, 26), // "on_pushButton_0204_clicked"
QT_MOC_LITERAL(705, 26), // "on_pushButton_0206_clicked"
QT_MOC_LITERAL(732, 26), // "on_pushButton_0208_clicked"
QT_MOC_LITERAL(759, 26), // "on_pushButton_0210_clicked"
QT_MOC_LITERAL(786, 26), // "on_pushButton_0212_clicked"
QT_MOC_LITERAL(813, 26), // "on_pushButton_0214_clicked"
QT_MOC_LITERAL(840, 26), // "on_pushButton_0216_clicked"
QT_MOC_LITERAL(867, 26), // "on_pushButton_0400_clicked"
QT_MOC_LITERAL(894, 26), // "on_pushButton_0402_clicked"
QT_MOC_LITERAL(921, 26), // "on_pushButton_0404_clicked"
QT_MOC_LITERAL(948, 26), // "on_pushButton_0406_clicked"
QT_MOC_LITERAL(975, 26), // "on_pushButton_0408_clicked"
QT_MOC_LITERAL(1002, 26), // "on_pushButton_0410_clicked"
QT_MOC_LITERAL(1029, 26), // "on_pushButton_0412_clicked"
QT_MOC_LITERAL(1056, 26), // "on_pushButton_0414_clicked"
QT_MOC_LITERAL(1083, 26), // "on_pushButton_0416_clicked"
QT_MOC_LITERAL(1110, 26), // "on_pushButton_0600_clicked"
QT_MOC_LITERAL(1137, 26), // "on_pushButton_0602_clicked"
QT_MOC_LITERAL(1164, 26), // "on_pushButton_0604_clicked"
QT_MOC_LITERAL(1191, 26), // "on_pushButton_0606_clicked"
QT_MOC_LITERAL(1218, 26), // "on_pushButton_0608_clicked"
QT_MOC_LITERAL(1245, 26), // "on_pushButton_0610_clicked"
QT_MOC_LITERAL(1272, 26), // "on_pushButton_0612_clicked"
QT_MOC_LITERAL(1299, 26), // "on_pushButton_0614_clicked"
QT_MOC_LITERAL(1326, 26), // "on_pushButton_0616_clicked"
QT_MOC_LITERAL(1353, 26), // "on_pushButton_0800_clicked"
QT_MOC_LITERAL(1380, 26), // "on_pushButton_0802_clicked"
QT_MOC_LITERAL(1407, 26), // "on_pushButton_0804_clicked"
QT_MOC_LITERAL(1434, 26), // "on_pushButton_0806_clicked"
QT_MOC_LITERAL(1461, 26), // "on_pushButton_0808_clicked"
QT_MOC_LITERAL(1488, 26), // "on_pushButton_0810_clicked"
QT_MOC_LITERAL(1515, 26), // "on_pushButton_0812_clicked"
QT_MOC_LITERAL(1542, 26), // "on_pushButton_0814_clicked"
QT_MOC_LITERAL(1569, 26), // "on_pushButton_0816_clicked"
QT_MOC_LITERAL(1596, 26), // "on_pushButton_1000_clicked"
QT_MOC_LITERAL(1623, 26), // "on_pushButton_1002_clicked"
QT_MOC_LITERAL(1650, 26), // "on_pushButton_1004_clicked"
QT_MOC_LITERAL(1677, 26), // "on_pushButton_1006_clicked"
QT_MOC_LITERAL(1704, 26), // "on_pushButton_1008_clicked"
QT_MOC_LITERAL(1731, 26), // "on_pushButton_1010_clicked"
QT_MOC_LITERAL(1758, 26), // "on_pushButton_1012_clicked"
QT_MOC_LITERAL(1785, 26), // "on_pushButton_1014_clicked"
QT_MOC_LITERAL(1812, 26), // "on_pushButton_1016_clicked"
QT_MOC_LITERAL(1839, 26), // "on_pushButton_1200_clicked"
QT_MOC_LITERAL(1866, 26), // "on_pushButton_1202_clicked"
QT_MOC_LITERAL(1893, 26), // "on_pushButton_1204_clicked"
QT_MOC_LITERAL(1920, 26), // "on_pushButton_1206_clicked"
QT_MOC_LITERAL(1947, 26), // "on_pushButton_1208_clicked"
QT_MOC_LITERAL(1974, 26), // "on_pushButton_1210_clicked"
QT_MOC_LITERAL(2001, 26), // "on_pushButton_1212_clicked"
QT_MOC_LITERAL(2028, 26), // "on_pushButton_1214_clicked"
QT_MOC_LITERAL(2055, 26), // "on_pushButton_1216_clicked"
QT_MOC_LITERAL(2082, 26), // "on_pushButton_1400_clicked"
QT_MOC_LITERAL(2109, 26), // "on_pushButton_1402_clicked"
QT_MOC_LITERAL(2136, 26), // "on_pushButton_1404_clicked"
QT_MOC_LITERAL(2163, 26), // "on_pushButton_1406_clicked"
QT_MOC_LITERAL(2190, 26), // "on_pushButton_1408_clicked"
QT_MOC_LITERAL(2217, 26), // "on_pushButton_1410_clicked"
QT_MOC_LITERAL(2244, 26), // "on_pushButton_1412_clicked"
QT_MOC_LITERAL(2271, 26), // "on_pushButton_1414_clicked"
QT_MOC_LITERAL(2298, 26), // "on_pushButton_1416_clicked"
QT_MOC_LITERAL(2325, 26), // "on_pushButton_1600_clicked"
QT_MOC_LITERAL(2352, 26), // "on_pushButton_1602_clicked"
QT_MOC_LITERAL(2379, 26), // "on_pushButton_1604_clicked"
QT_MOC_LITERAL(2406, 26), // "on_pushButton_1606_clicked"
QT_MOC_LITERAL(2433, 26), // "on_pushButton_1608_clicked"
QT_MOC_LITERAL(2460, 26), // "on_pushButton_1610_clicked"
QT_MOC_LITERAL(2487, 26), // "on_pushButton_1612_clicked"
QT_MOC_LITERAL(2514, 26), // "on_pushButton_1614_clicked"
QT_MOC_LITERAL(2541, 26), // "on_pushButton_1616_clicked"
QT_MOC_LITERAL(2568, 21), // "on_undoButton_clicked"
QT_MOC_LITERAL(2590, 22), // "on_radioButton_clicked"
QT_MOC_LITERAL(2613, 24), // "on_radioButton_2_clicked"
QT_MOC_LITERAL(2638, 25), // "on_details_Button_clicked"
QT_MOC_LITERAL(2664, 19), // "on_checkBox_clicked"
QT_MOC_LITERAL(2684, 21) // "on_checkBox_2_clicked"

    },
    "Quoridor\0ai_wall\0\0next_move\0best_move\0"
    "game_state\0s\0best_wall\0minimax\0n\0"
    "QTreeWidgetItem*\0check_wall_number\0"
    "shortest_path\0place\0find_nodes\0"
    "QList<place>\0find_near\0check_placeble_1\0"
    "check_placeble_2\0paintEvent\0QPaintEvent*\0"
    "mousePressEvent\0QMouseEvent*\0event\0"
    "on_newGameButton_clicked\0start_new_game\0"
    "undo_last_move\0find_moves\0reset_buttons\0"
    "game_manager\0game_over\0set_players\0"
    "remove_piece\0on_pushButton_0000_clicked\0"
    "on_pushButton_0002_clicked\0"
    "on_pushButton_0004_clicked\0"
    "on_pushButton_0006_clicked\0"
    "on_pushButton_0008_clicked\0"
    "on_pushButton_0010_clicked\0"
    "on_pushButton_0012_clicked\0"
    "on_pushButton_0014_clicked\0"
    "on_pushButton_0016_clicked\0"
    "on_pushButton_0200_clicked\0"
    "on_pushButton_0202_clicked\0"
    "on_pushButton_0204_clicked\0"
    "on_pushButton_0206_clicked\0"
    "on_pushButton_0208_clicked\0"
    "on_pushButton_0210_clicked\0"
    "on_pushButton_0212_clicked\0"
    "on_pushButton_0214_clicked\0"
    "on_pushButton_0216_clicked\0"
    "on_pushButton_0400_clicked\0"
    "on_pushButton_0402_clicked\0"
    "on_pushButton_0404_clicked\0"
    "on_pushButton_0406_clicked\0"
    "on_pushButton_0408_clicked\0"
    "on_pushButton_0410_clicked\0"
    "on_pushButton_0412_clicked\0"
    "on_pushButton_0414_clicked\0"
    "on_pushButton_0416_clicked\0"
    "on_pushButton_0600_clicked\0"
    "on_pushButton_0602_clicked\0"
    "on_pushButton_0604_clicked\0"
    "on_pushButton_0606_clicked\0"
    "on_pushButton_0608_clicked\0"
    "on_pushButton_0610_clicked\0"
    "on_pushButton_0612_clicked\0"
    "on_pushButton_0614_clicked\0"
    "on_pushButton_0616_clicked\0"
    "on_pushButton_0800_clicked\0"
    "on_pushButton_0802_clicked\0"
    "on_pushButton_0804_clicked\0"
    "on_pushButton_0806_clicked\0"
    "on_pushButton_0808_clicked\0"
    "on_pushButton_0810_clicked\0"
    "on_pushButton_0812_clicked\0"
    "on_pushButton_0814_clicked\0"
    "on_pushButton_0816_clicked\0"
    "on_pushButton_1000_clicked\0"
    "on_pushButton_1002_clicked\0"
    "on_pushButton_1004_clicked\0"
    "on_pushButton_1006_clicked\0"
    "on_pushButton_1008_clicked\0"
    "on_pushButton_1010_clicked\0"
    "on_pushButton_1012_clicked\0"
    "on_pushButton_1014_clicked\0"
    "on_pushButton_1016_clicked\0"
    "on_pushButton_1200_clicked\0"
    "on_pushButton_1202_clicked\0"
    "on_pushButton_1204_clicked\0"
    "on_pushButton_1206_clicked\0"
    "on_pushButton_1208_clicked\0"
    "on_pushButton_1210_clicked\0"
    "on_pushButton_1212_clicked\0"
    "on_pushButton_1214_clicked\0"
    "on_pushButton_1216_clicked\0"
    "on_pushButton_1400_clicked\0"
    "on_pushButton_1402_clicked\0"
    "on_pushButton_1404_clicked\0"
    "on_pushButton_1406_clicked\0"
    "on_pushButton_1408_clicked\0"
    "on_pushButton_1410_clicked\0"
    "on_pushButton_1412_clicked\0"
    "on_pushButton_1414_clicked\0"
    "on_pushButton_1416_clicked\0"
    "on_pushButton_1600_clicked\0"
    "on_pushButton_1602_clicked\0"
    "on_pushButton_1604_clicked\0"
    "on_pushButton_1606_clicked\0"
    "on_pushButton_1608_clicked\0"
    "on_pushButton_1610_clicked\0"
    "on_pushButton_1612_clicked\0"
    "on_pushButton_1614_clicked\0"
    "on_pushButton_1616_clicked\0"
    "on_undoButton_clicked\0on_radioButton_clicked\0"
    "on_radioButton_2_clicked\0"
    "on_details_Button_clicked\0on_checkBox_clicked\0"
    "on_checkBox_2_clicked"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Quoridor[] = {

 // content:
      10,       // revision
       0,       // classname
       0,    0, // classinfo
     109,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags, initial metatype offsets
       1,    1,  668,    2, 0x08,    1 /* Private */,
       3,    0,  671,    2, 0x08,    3 /* Private */,
       4,    1,  672,    2, 0x08,    4 /* Private */,
       7,    1,  675,    2, 0x08,    6 /* Private */,
       8,    3,  678,    2, 0x08,    8 /* Private */,
      11,    0,  685,    2, 0x08,   12 /* Private */,
      12,    3,  686,    2, 0x08,   13 /* Private */,
      14,    4,  693,    2, 0x08,   17 /* Private */,
      16,    2,  702,    2, 0x08,   22 /* Private */,
      17,    2,  707,    2, 0x08,   25 /* Private */,
      18,    2,  712,    2, 0x08,   28 /* Private */,
      19,    1,  717,    2, 0x08,   31 /* Private */,
      21,    1,  720,    2, 0x08,   33 /* Private */,
      24,    0,  723,    2, 0x08,   35 /* Private */,
      25,    0,  724,    2, 0x08,   36 /* Private */,
      26,    0,  725,    2, 0x08,   37 /* Private */,
      27,    0,  726,    2, 0x08,   38 /* Private */,
      28,    0,  727,    2, 0x08,   39 /* Private */,
      29,    0,  728,    2, 0x08,   40 /* Private */,
      30,    0,  729,    2, 0x08,   41 /* Private */,
      31,    3,  730,    2, 0x08,   42 /* Private */,
      32,    2,  737,    2, 0x08,   46 /* Private */,
      33,    0,  742,    2, 0x08,   49 /* Private */,
      34,    0,  743,    2, 0x08,   50 /* Private */,
      35,    0,  744,    2, 0x08,   51 /* Private */,
      36,    0,  745,    2, 0x08,   52 /* Private */,
      37,    0,  746,    2, 0x08,   53 /* Private */,
      38,    0,  747,    2, 0x08,   54 /* Private */,
      39,    0,  748,    2, 0x08,   55 /* Private */,
      40,    0,  749,    2, 0x08,   56 /* Private */,
      41,    0,  750,    2, 0x08,   57 /* Private */,
      42,    0,  751,    2, 0x08,   58 /* Private */,
      43,    0,  752,    2, 0x08,   59 /* Private */,
      44,    0,  753,    2, 0x08,   60 /* Private */,
      45,    0,  754,    2, 0x08,   61 /* Private */,
      46,    0,  755,    2, 0x08,   62 /* Private */,
      47,    0,  756,    2, 0x08,   63 /* Private */,
      48,    0,  757,    2, 0x08,   64 /* Private */,
      49,    0,  758,    2, 0x08,   65 /* Private */,
      50,    0,  759,    2, 0x08,   66 /* Private */,
      51,    0,  760,    2, 0x08,   67 /* Private */,
      52,    0,  761,    2, 0x08,   68 /* Private */,
      53,    0,  762,    2, 0x08,   69 /* Private */,
      54,    0,  763,    2, 0x08,   70 /* Private */,
      55,    0,  764,    2, 0x08,   71 /* Private */,
      56,    0,  765,    2, 0x08,   72 /* Private */,
      57,    0,  766,    2, 0x08,   73 /* Private */,
      58,    0,  767,    2, 0x08,   74 /* Private */,
      59,    0,  768,    2, 0x08,   75 /* Private */,
      60,    0,  769,    2, 0x08,   76 /* Private */,
      61,    0,  770,    2, 0x08,   77 /* Private */,
      62,    0,  771,    2, 0x08,   78 /* Private */,
      63,    0,  772,    2, 0x08,   79 /* Private */,
      64,    0,  773,    2, 0x08,   80 /* Private */,
      65,    0,  774,    2, 0x08,   81 /* Private */,
      66,    0,  775,    2, 0x08,   82 /* Private */,
      67,    0,  776,    2, 0x08,   83 /* Private */,
      68,    0,  777,    2, 0x08,   84 /* Private */,
      69,    0,  778,    2, 0x08,   85 /* Private */,
      70,    0,  779,    2, 0x08,   86 /* Private */,
      71,    0,  780,    2, 0x08,   87 /* Private */,
      72,    0,  781,    2, 0x08,   88 /* Private */,
      73,    0,  782,    2, 0x08,   89 /* Private */,
      74,    0,  783,    2, 0x08,   90 /* Private */,
      75,    0,  784,    2, 0x08,   91 /* Private */,
      76,    0,  785,    2, 0x08,   92 /* Private */,
      77,    0,  786,    2, 0x08,   93 /* Private */,
      78,    0,  787,    2, 0x08,   94 /* Private */,
      79,    0,  788,    2, 0x08,   95 /* Private */,
      80,    0,  789,    2, 0x08,   96 /* Private */,
      81,    0,  790,    2, 0x08,   97 /* Private */,
      82,    0,  791,    2, 0x08,   98 /* Private */,
      83,    0,  792,    2, 0x08,   99 /* Private */,
      84,    0,  793,    2, 0x08,  100 /* Private */,
      85,    0,  794,    2, 0x08,  101 /* Private */,
      86,    0,  795,    2, 0x08,  102 /* Private */,
      87,    0,  796,    2, 0x08,  103 /* Private */,
      88,    0,  797,    2, 0x08,  104 /* Private */,
      89,    0,  798,    2, 0x08,  105 /* Private */,
      90,    0,  799,    2, 0x08,  106 /* Private */,
      91,    0,  800,    2, 0x08,  107 /* Private */,
      92,    0,  801,    2, 0x08,  108 /* Private */,
      93,    0,  802,    2, 0x08,  109 /* Private */,
      94,    0,  803,    2, 0x08,  110 /* Private */,
      95,    0,  804,    2, 0x08,  111 /* Private */,
      96,    0,  805,    2, 0x08,  112 /* Private */,
      97,    0,  806,    2, 0x08,  113 /* Private */,
      98,    0,  807,    2, 0x08,  114 /* Private */,
      99,    0,  808,    2, 0x08,  115 /* Private */,
     100,    0,  809,    2, 0x08,  116 /* Private */,
     101,    0,  810,    2, 0x08,  117 /* Private */,
     102,    0,  811,    2, 0x08,  118 /* Private */,
     103,    0,  812,    2, 0x08,  119 /* Private */,
     104,    0,  813,    2, 0x08,  120 /* Private */,
     105,    0,  814,    2, 0x08,  121 /* Private */,
     106,    0,  815,    2, 0x08,  122 /* Private */,
     107,    0,  816,    2, 0x08,  123 /* Private */,
     108,    0,  817,    2, 0x08,  124 /* Private */,
     109,    0,  818,    2, 0x08,  125 /* Private */,
     110,    0,  819,    2, 0x08,  126 /* Private */,
     111,    0,  820,    2, 0x08,  127 /* Private */,
     112,    0,  821,    2, 0x08,  128 /* Private */,
     113,    0,  822,    2, 0x08,  129 /* Private */,
     114,    0,  823,    2, 0x08,  130 /* Private */,
     115,    0,  824,    2, 0x08,  131 /* Private */,
     116,    0,  825,    2, 0x08,  132 /* Private */,
     117,    0,  826,    2, 0x08,  133 /* Private */,
     118,    0,  827,    2, 0x08,  134 /* Private */,
     119,    0,  828,    2, 0x08,  135 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void,
    0x80000000 | 5, 0x80000000 | 5,    6,
    0x80000000 | 5, 0x80000000 | 5,    6,
    QMetaType::Void, 0x80000000 | 5, QMetaType::Int, 0x80000000 | 10,    6,    9,    2,
    QMetaType::Bool,
    QMetaType::Void, 0x80000000 | 13, 0x80000000 | 13, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 15, 0x80000000 | 13, QMetaType::Int, QMetaType::Int,    2,    2,    2,    2,
    0x80000000 | 15, 0x80000000 | 13, 0x80000000 | 13,    2,    2,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    2,    2,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 20,    2,
    QMetaType::Void, 0x80000000 | 22,   23,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int, QMetaType::Int, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    2,    2,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void Quoridor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<Quoridor *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->ai_wall((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 1: _t->next_move(); break;
        case 2: { game_state _r = _t->best_move((*reinterpret_cast< std::add_pointer_t<game_state>>(_a[1])));
            if (_a[0]) *reinterpret_cast< game_state*>(_a[0]) = std::move(_r); }  break;
        case 3: { game_state _r = _t->best_wall((*reinterpret_cast< std::add_pointer_t<game_state>>(_a[1])));
            if (_a[0]) *reinterpret_cast< game_state*>(_a[0]) = std::move(_r); }  break;
        case 4: _t->minimax((*reinterpret_cast< std::add_pointer_t<game_state>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast< std::add_pointer_t<QTreeWidgetItem*>>(_a[3]))); break;
        case 5: { bool _r = _t->check_wall_number();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 6: _t->shortest_path((*reinterpret_cast< std::add_pointer_t<place>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<place>>(_a[2])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[3]))); break;
        case 7: _t->find_nodes((*reinterpret_cast< std::add_pointer_t<QList<place>>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<place>>(_a[2])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[3])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[4]))); break;
        case 8: { QList<place> _r = _t->find_near((*reinterpret_cast< std::add_pointer_t<place>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<place>>(_a[2])));
            if (_a[0]) *reinterpret_cast< QList<place>*>(_a[0]) = std::move(_r); }  break;
        case 9: _t->check_placeble_1((*reinterpret_cast< std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[2]))); break;
        case 10: _t->check_placeble_2((*reinterpret_cast< std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[2]))); break;
        case 11: _t->paintEvent((*reinterpret_cast< std::add_pointer_t<QPaintEvent*>>(_a[1]))); break;
        case 12: _t->mousePressEvent((*reinterpret_cast< std::add_pointer_t<QMouseEvent*>>(_a[1]))); break;
        case 13: _t->on_newGameButton_clicked(); break;
        case 14: _t->start_new_game(); break;
        case 15: _t->undo_last_move(); break;
        case 16: _t->find_moves(); break;
        case 17: _t->reset_buttons(); break;
        case 18: _t->game_manager(); break;
        case 19: _t->game_over(); break;
        case 20: _t->set_players((*reinterpret_cast< std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[3]))); break;
        case 21: _t->remove_piece((*reinterpret_cast< std::add_pointer_t<int>>(_a[1])),(*reinterpret_cast< std::add_pointer_t<int>>(_a[2]))); break;
        case 22: _t->on_pushButton_0000_clicked(); break;
        case 23: _t->on_pushButton_0002_clicked(); break;
        case 24: _t->on_pushButton_0004_clicked(); break;
        case 25: _t->on_pushButton_0006_clicked(); break;
        case 26: _t->on_pushButton_0008_clicked(); break;
        case 27: _t->on_pushButton_0010_clicked(); break;
        case 28: _t->on_pushButton_0012_clicked(); break;
        case 29: _t->on_pushButton_0014_clicked(); break;
        case 30: _t->on_pushButton_0016_clicked(); break;
        case 31: _t->on_pushButton_0200_clicked(); break;
        case 32: _t->on_pushButton_0202_clicked(); break;
        case 33: _t->on_pushButton_0204_clicked(); break;
        case 34: _t->on_pushButton_0206_clicked(); break;
        case 35: _t->on_pushButton_0208_clicked(); break;
        case 36: _t->on_pushButton_0210_clicked(); break;
        case 37: _t->on_pushButton_0212_clicked(); break;
        case 38: _t->on_pushButton_0214_clicked(); break;
        case 39: _t->on_pushButton_0216_clicked(); break;
        case 40: _t->on_pushButton_0400_clicked(); break;
        case 41: _t->on_pushButton_0402_clicked(); break;
        case 42: _t->on_pushButton_0404_clicked(); break;
        case 43: _t->on_pushButton_0406_clicked(); break;
        case 44: _t->on_pushButton_0408_clicked(); break;
        case 45: _t->on_pushButton_0410_clicked(); break;
        case 46: _t->on_pushButton_0412_clicked(); break;
        case 47: _t->on_pushButton_0414_clicked(); break;
        case 48: _t->on_pushButton_0416_clicked(); break;
        case 49: _t->on_pushButton_0600_clicked(); break;
        case 50: _t->on_pushButton_0602_clicked(); break;
        case 51: _t->on_pushButton_0604_clicked(); break;
        case 52: _t->on_pushButton_0606_clicked(); break;
        case 53: _t->on_pushButton_0608_clicked(); break;
        case 54: _t->on_pushButton_0610_clicked(); break;
        case 55: _t->on_pushButton_0612_clicked(); break;
        case 56: _t->on_pushButton_0614_clicked(); break;
        case 57: _t->on_pushButton_0616_clicked(); break;
        case 58: _t->on_pushButton_0800_clicked(); break;
        case 59: _t->on_pushButton_0802_clicked(); break;
        case 60: _t->on_pushButton_0804_clicked(); break;
        case 61: _t->on_pushButton_0806_clicked(); break;
        case 62: _t->on_pushButton_0808_clicked(); break;
        case 63: _t->on_pushButton_0810_clicked(); break;
        case 64: _t->on_pushButton_0812_clicked(); break;
        case 65: _t->on_pushButton_0814_clicked(); break;
        case 66: _t->on_pushButton_0816_clicked(); break;
        case 67: _t->on_pushButton_1000_clicked(); break;
        case 68: _t->on_pushButton_1002_clicked(); break;
        case 69: _t->on_pushButton_1004_clicked(); break;
        case 70: _t->on_pushButton_1006_clicked(); break;
        case 71: _t->on_pushButton_1008_clicked(); break;
        case 72: _t->on_pushButton_1010_clicked(); break;
        case 73: _t->on_pushButton_1012_clicked(); break;
        case 74: _t->on_pushButton_1014_clicked(); break;
        case 75: _t->on_pushButton_1016_clicked(); break;
        case 76: _t->on_pushButton_1200_clicked(); break;
        case 77: _t->on_pushButton_1202_clicked(); break;
        case 78: _t->on_pushButton_1204_clicked(); break;
        case 79: _t->on_pushButton_1206_clicked(); break;
        case 80: _t->on_pushButton_1208_clicked(); break;
        case 81: _t->on_pushButton_1210_clicked(); break;
        case 82: _t->on_pushButton_1212_clicked(); break;
        case 83: _t->on_pushButton_1214_clicked(); break;
        case 84: _t->on_pushButton_1216_clicked(); break;
        case 85: _t->on_pushButton_1400_clicked(); break;
        case 86: _t->on_pushButton_1402_clicked(); break;
        case 87: _t->on_pushButton_1404_clicked(); break;
        case 88: _t->on_pushButton_1406_clicked(); break;
        case 89: _t->on_pushButton_1408_clicked(); break;
        case 90: _t->on_pushButton_1410_clicked(); break;
        case 91: _t->on_pushButton_1412_clicked(); break;
        case 92: _t->on_pushButton_1414_clicked(); break;
        case 93: _t->on_pushButton_1416_clicked(); break;
        case 94: _t->on_pushButton_1600_clicked(); break;
        case 95: _t->on_pushButton_1602_clicked(); break;
        case 96: _t->on_pushButton_1604_clicked(); break;
        case 97: _t->on_pushButton_1606_clicked(); break;
        case 98: _t->on_pushButton_1608_clicked(); break;
        case 99: _t->on_pushButton_1610_clicked(); break;
        case 100: _t->on_pushButton_1612_clicked(); break;
        case 101: _t->on_pushButton_1614_clicked(); break;
        case 102: _t->on_pushButton_1616_clicked(); break;
        case 103: _t->on_undoButton_clicked(); break;
        case 104: _t->on_radioButton_clicked(); break;
        case 105: _t->on_radioButton_2_clicked(); break;
        case 106: _t->on_details_Button_clicked(); break;
        case 107: _t->on_checkBox_clicked(); break;
        case 108: _t->on_checkBox_2_clicked(); break;
        default: ;
        }
    }
}

const QMetaObject Quoridor::staticMetaObject = { {
    QMetaObject::SuperData::link<QMainWindow::staticMetaObject>(),
    qt_meta_stringdata_Quoridor.offsetsAndSize,
    qt_meta_data_Quoridor,
    qt_static_metacall,
    nullptr,
qt_incomplete_metaTypeArray<qt_meta_stringdata_Quoridor_t
, QtPrivate::TypeAndForceComplete<Quoridor, std::true_type>
, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QString, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<game_state, std::false_type>, QtPrivate::TypeAndForceComplete<game_state, std::false_type>, QtPrivate::TypeAndForceComplete<game_state, std::false_type>, QtPrivate::TypeAndForceComplete<game_state, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<game_state, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<QTreeWidgetItem *, std::false_type>, QtPrivate::TypeAndForceComplete<bool, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<place, std::false_type>, QtPrivate::TypeAndForceComplete<place, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QList<place>, std::false_type>, QtPrivate::TypeAndForceComplete<place, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<QList<place>, std::false_type>, QtPrivate::TypeAndForceComplete<place, std::false_type>, QtPrivate::TypeAndForceComplete<place, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QPaintEvent *, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<QMouseEvent *, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<int, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>, QtPrivate::TypeAndForceComplete<void, std::false_type>


>,
    nullptr
} };


const QMetaObject *Quoridor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Quoridor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_Quoridor.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int Quoridor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 109)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 109;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 109)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 109;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
