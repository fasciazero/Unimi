# pushButtons
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     for i in range (0,9):
#         for y in range (0,9):
#             if i < 5 and y < 5:
#                  d.write('void Quoridor::on_pushButton_0'+ str(i*2) + '0' + str(y*2) +'_clicked()\n{\
#                  \n\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ' && !move_select){\
#                     \n\t\tfind_moves();\
#                     \n\t\tmove_select = true; show_wall = false; wall_enabled = false; update(); return;}\
#                     \n\tif(move_select){\
#                     \n\t\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + '){\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); return;}\
#                     \n\t\tif(BLUE){\
#                     \n\t\t\tplayer_blue.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 1);\
#                     \n\t\t\tmoves.append("m 1");\
#                     \n\t\t\tBLUE = false; RED = true;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}\
#                     \n\n\t\tif(RED){\
#                     \n\t\t\tplayer_red.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 2);\
#                     \n\t\t\tmoves.append("m 2");\
#                     \n\t\t\tBLUE = true; RED = false;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}}}\n\n')
#                 # d.write('void on_pushButton_0'+ str(i*2) + '0' + str(y*2) +'_clicked();\n')
#             if i >= 5 and y < 5:
#                  d.write('void Quoridor::on_pushButton_'+ str(i*2) + '0' + str(y*2) +'_clicked()\n{\
#                     \n\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ' && !move_select){\
#                     \n\t\tfind_moves();\
#                     \n\t\tmove_select = true; show_wall = false; wall_enabled = false; update(); return;}\
#                     \n\tif(move_select){\
#                     \n\t\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + '){\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); return;}\
#                     \n\t\tif(BLUE){\
#                     \n\t\t\tplayer_blue.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 1);\
#                     \n\t\t\tmoves.append("m 1");\
#                     \n\t\t\tBLUE = false; RED = true;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}\
#                     \n\n\t\tif(RED){\
#                     \n\t\t\tplayer_red.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 2);\
#                     \n\t\t\tmoves.append("m 2");\
#                     \n\t\t\tBLUE = true; RED = false;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}}}\n\n')
#                 # d.write('void on_pushButton_'+ str(i*2) + '0' + str(y*2) +'_clicked();\n')
#             if i < 5 and y >= 5:
#                  d.write('void Quoridor::on_pushButton_0'+ str(i*2) + str(y*2) +'_clicked()\n{\
#                     \n\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ' && !move_select){\
#                     \n\t\tfind_moves();\
#                     \n\t\tmove_select = true; show_wall = false; wall_enabled = false; update(); return;}\
#                     \n\tif(move_select){\
#                     \n\t\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + '){\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); return;}\
#                     \n\t\tif(BLUE){\
#                     \n\t\t\tplayer_blue.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 1);\
#                     \n\t\t\tmoves.append("m 1");\
#                     \n\t\t\tBLUE = false; RED = true;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}\
#                     \n\n\t\tif(RED){\
#                     \n\t\t\tplayer_red.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 2);\
#                     \n\t\t\tmoves.append("m 2");\
#                     \n\t\t\tBLUE = true; RED = false;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}}}\n\n')
#                 # d.write('void on_pushButton_0'+ str(i*2) + str(y*2) +'_clicked();\n')
#             if i >= 5 and y >= 5:
#                  d.write('void Quoridor::on_pushButton_'+ str(i*2) + str(y*2) +'_clicked()\n{\
#                     \n\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ' && !move_select){\
#                     \n\t\tfind_moves();\
#                     \n\t\tmove_select = true; show_wall = false; wall_enabled = false; update(); return;}\
#                     \n\tif(move_select){\
#                     \n\t\tif(curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + '){\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); return;}\
#                     \n\t\tif(BLUE){\
#                     \n\t\t\tplayer_blue.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 1);\
#                     \n\t\t\tmoves.append("m 1");\
#                     \n\t\t\tBLUE = false; RED = true;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}\
#                     \n\n\t\tif(RED){\
#                     \n\t\t\tplayer_red.append(place('+ str(i*2) + ', ' + str(y*2) + '));\
#                     \n\t\t\tremove_pawn(curr_position[0], curr_position[1]);\
#                     \n\t\t\tset_players('+ str(i*2) + ', '+ str(y*2) + ', 2);\
#                     \n\t\t\tmoves.append("m 2");\
#                     \n\t\t\tBLUE = true; RED = false;\
#                     \n\t\t\treset_buttons(); show_wall = true; wall_enabled = true; update(); game_manager(); return;}}}\n\n')
#                 # d.write('void on_pushButton_'+ str(i*2) + str(y*2) +'_clicked();\n')

#
## wall_position
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     n=0
#     for y in range(15, 516, 65):
#         m=1
#         for i in range(65, 521, 65):
#             d.write('if((event->pos().x() > '+ str(i) +' && event->pos().x() < '+ str(i+15) +') && (event->pos().y() > '+ str(y) +' && event->pos().y() < '+ str(y+50) +'))\
#                         \n\tif(vertical) {\
#                         \n\t\tif(board_matrix['+ str(n) +']['+ str(m) +'] == 1 || board_matrix['+ str(n) +'+1]['+ str(m) +'] == 1 || board_matrix['+ str(n) +'+2]['+ str(m) +'] == 1) return;\
#                         \n\t\tboard_copy_1['+ str(n) +']['+ str(m) +'] = 1; board_copy_1['+ str(n) +'+1]['+ str(m) +'] = 1; board_copy_1['+ str(n) +'+2]['+ str(m) +'] = 1;\
#                         \n\t\tboard_copy_2['+ str(n) +']['+ str(m) +'] = 1; board_copy_2['+ str(n) +'+1]['+ str(m) +'] = 1; board_copy_2['+ str(n) +'+2]['+ str(m) +'] = 1;\
#                         \n\t\tcheck_placeble_1(player_blue[0], player_blue[1]);\
#                         \n\t\tcheck_placeble_2(player_red[0], player_red[1]);\
#                         \n\t\tif(placeble_1 && placeble_2){\
#                         \n\t\t\tvertical_walls.append(wall('+ str(i) +'+2, '+ str(y) +'+2)); update();\
#                         \n\t\t\tboard_matrix['+ str(n) +']['+ str(m) +'] = 1; board_matrix['+ str(n) +'+1]['+ str(m) +'] = 1; board_matrix['+ str(n) +'+2]['+ str(m) +'] = 1; placeble_1 = false; placeble_2 = false;\
#                         \n\t\t\tif(BLUE){BLUE = false; RED = true; game_manager(); return;}\
#                         \n\t\t\tif(RED){BLUE = true; RED = false; game_manager(); return;}}}\n\n')
#             m+=2
#         n+=2
#
#     n=1
#     for y in range(65, 521, 65):
#         m=0
#         for i in range(15, 516, 65):
#             d.write('if((event->pos().x() > '+ str(i) +' && event->pos().x() < '+ str(i+50) +') && (event->pos().y() > '+ str(y) +' && event->pos().y() < '+ str(y+15) +'))\
#                             \n\tif(horizontal) {\
#                             \n\t\tif(board_matrix['+ str(n) +']['+ str(m) +'] == 1 || board_matrix['+ str(n) +']['+ str(m) +'+1] == 1 || board_matrix['+ str(n) +']['+ str(m) +'+2] == 1) return;\
#                             \n\t\tboard_copy_1['+ str(n) +']['+ str(m) +'] = 1; board_copy_1['+ str(n) +']['+ str(m) +'+1] = 1; board_copy_1['+ str(n) +']['+ str(m) +'+2] = 1;\
#                             \n\t\tboard_copy_2['+ str(n) +']['+ str(m) +'] = 1; board_copy_2['+ str(n) +']['+ str(m) +'+1] = 1; board_copy_2['+ str(n) +']['+ str(m) +'+2] = 1;\
#                             \n\t\tcheck_placeble_1(player_blue[0], player_blue[1]);\
#                             \n\t\tcheck_placeble_2(player_red[0], player_red[1]);\
#                             \n\t\tif(placeble_1 && placeble_2){\
#                             \n\t\t\thorizontal_walls.append(wall('+ str(i) +'+2, '+ str(y) +'+2)); update();\
#                             \n\t\t\tboard_matrix['+ str(n) +']['+ str(m) +'] = 1; board_matrix['+ str(n) +']['+ str(m) +'+1] = 1; board_matrix['+ str(n) +']['+ str(m) +'+2] = 1; placeble_1 = false; placeble_2 = false;\
#                             \n\t\t\tif(BLUE){BLUE = false; RED = true; game_manager(); return;}\
#                             \n\t\t\tif(RED){BLUE = true; RED = false; game_manager(); return;}}}\n\n')
#             m+=2
#         n+=2


# ## wall_highlight
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     n=0
#     for y in range(15, 516, 65):
#         m=1
#         for i in range(65, 521, 65):
#             d.write('if((event->pos().x() > '+ str(i) +' && event->pos().x() < '+ str(i+15) +') && (event->pos().y() > '+ str(y) +' && event->pos().y() < '+ str(y+50) +')){\
#                         \n\tif(board_matrix['+ str(n) +']['+ str(m) +'] == 1 || board_matrix['+ str(n) +'+1]['+ str(m) +'] == 1 || board_matrix['+ str(n) +'+2]['+ str(m) +'] == 1) return;\
#                         \n\t\twall_position[0] = '+ str(i) +'+2; wall_position[1] = '+ str(y) +'+2;\
#                         \n\t\thorizontal = false; vertical = true; update();}\n\n')
#             m+=2
#         n+=2
#
#     n=1
#     for y in range(65, 521, 65):
#         m=0
#         for i in range(15, 516, 65):
#             d.write('if((event->pos().x() > '+ str(i) +' && event->pos().x() < '+ str(i+50) +') && (event->pos().y() > '+ str(y) +' && event->pos().y() < '+ str(y+15) +')){\
#                         \n\tif(board_matrix['+ str(n) +']['+ str(m) +'] == 1 || board_matrix['+ str(n) +']['+ str(m) +'+1] == 1 || board_matrix['+ str(n) +']['+ str(m) +'+2] == 1) return;\
#                         \n\twall_position[0] = '+ str(i) +'+2; wall_position[1] = '+ str(y) +'+2;\
#                         \n\thorizontal = true; vertical = false; update();}\n\n')
#             m+=2
#         n+=2
#

# ## set_players
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     for i in range (0,9):
#         for y in range (0,9):
#             if i < 5 and y < 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + '){\
#                             \n\tif(p == 1){\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setIcon(ButtonIcon1);\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setIconSize(pixma.rect().size()); show_wall = true; update();}\
#                             \n\tif(p == 2){\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setIcon(ButtonIcon2);\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setIconSize(pixmap2.rect().size()); show_wall = true; update();}}\n\n')
#             if i >= 5 and y < 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + '){\
#                             \n\tif(p == 1){\
#                                 \n\t\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setIcon(ButtonIcon1);\
#                                 \n\t\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setIconSize(pixma.rect().size()); show_wall = true; update();}\
#                             \n\tif(p == 2){\
#                                 \n\t\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setIcon(ButtonIcon2);\
#                                 \n\t\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setIconSize(pixmap2.rect().size()); show_wall = true; update();}}\n\n')
#             if i < 5 and y >= 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + '){\
#                             \n\tif(p == 1){\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setIcon(ButtonIcon1);\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setIconSize(pixma.rect().size()); show_wall = true; update();}\
#                             \n\tif(p == 2){\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setIcon(ButtonIcon2);\
#                                 \n\t\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setIconSize(pixmap2.rect().size()); show_wall = true; update();}}\n\n')
#             if i >= 5 and y >= 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + '){\
#                             \n\tif(p == 1){\
#                                 \n\t\tui->pushButton_'+ str(i*2) + str(y*2) +'->setIcon(ButtonIcon1);\
#                                 \n\t\tui->pushButton_'+ str(i*2) + str(y*2) +'->setIconSize(pixma.rect().size()); show_wall = true; update();}\
#                             \n\tif(p == 2){\
#                                 \n\t\tui->pushButton_'+ str(i*2) + str(y*2) +'->setIcon(ButtonIcon2);\
#                                 \n\t\tui->pushButton_'+ str(i*2) + str(y*2) +'->setIconSize(pixmap2.rect().size()); show_wall = true; update();}}\n\n')

#
# ## remove_pawn
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     for i in range (0,9):
#         for y in range (0,9):
#             if i < 5 and y < 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + ') ui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setIcon(QIcon());\n')
#             if i >= 5 and y < 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + ') ui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setIcon(QIcon());\n')
#             if i < 5 and y >= 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + ') ui->pushButton_0'+ str(i*2) + str(y*2) +'->setIcon(QIcon());\n')
#             if i >= 5 and y >= 5:
#                 d.write('if(x == '+ str(i*2) + ' && y == '+ str(y*2) + ') ui->pushButton_'+ str(i*2) + str(y*2) +'->setIcon(QIcon());\n')
#
#
# ## find_moves
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     for i in range (0,9):
#         for y in range (0,9):
#             if i < 5 and y < 5:
#                 d.write('if ((curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ') || (left[0] == '+ str(i*2) +' && left[1] == '+ str(y*2) +') || (up[0] == '+ str(i*2) +' && up[1] == '+ str(y*2) +') || (right[0] == '+ str(i*2) +' && right[1] == '+ str(y*2) +') || (down[0] == '+ str(i*2) +' && down[1] == '+ str(y*2) +') || (jump_left[0] == '+ str(i*2) +' && jump_left[1] == '+ str(y*2) +') || (jump_right[0] == '+ str(i*2) +' && jump_right[1] == '+ str(y*2) +'))\
#                     \n\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setEnabled(true); else ui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setEnabled(false);\n\n')
#             if i >= 5 and y < 5:
#                 d.write('if ((curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ') || (left[0] == '+ str(i*2) +' && left[1] == '+ str(y*2) +') || (up[0] == '+ str(i*2) +' && up[1] == '+ str(y*2) +') || (right[0] == '+ str(i*2) +' && right[1] == '+ str(y*2) +') || (down[0] == '+ str(i*2) +' && down[1] == '+ str(y*2) +') || (jump_left[0] == '+ str(i*2) +' && jump_left[1] == '+ str(y*2) +') || (jump_right[0] == '+ str(i*2) +' && jump_right[1] == '+ str(y*2) +'))\
#                     \n\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setEnabled(true); else ui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setEnabled(false);\n\n')
#             if i < 5 and y >= 5:
#                 d.write('if ((curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ') || (left[0] == '+ str(i*2) +' && left[1] == '+ str(y*2) +') || (up[0] == '+ str(i*2) +' && up[1] == '+ str(y*2) +') || (right[0] == '+ str(i*2) +' && right[1] == '+ str(y*2) +') || (down[0] == '+ str(i*2) +' && down[1] == '+ str(y*2) +') || (jump_left[0] == '+ str(i*2) +' && jump_left[1] == '+ str(y*2) +') || (jump_right[0] == '+ str(i*2) +' && jump_right[1] == '+ str(y*2) +'))\
#                     \n\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setEnabled(true); else ui->pushButton_0'+ str(i*2) + str(y*2) +'->setEnabled(false);\n\n')
#             if i >= 5 and y >= 5:
#                 d.write('if ((curr_position[0] == '+ str(i*2) + ' && curr_position[1] == '+ str(y*2) + ') || (left[0] == '+ str(i*2) +' && left[1] == '+ str(y*2) +') || (up[0] == '+ str(i*2) +' && up[1] == '+ str(y*2) +') || (right[0] == '+ str(i*2) +' && right[1] == '+ str(y*2) +') || (down[0] == '+ str(i*2) +' && down[1] == '+ str(y*2) +') || (jump_left[0] == '+ str(i*2) +' && jump_left[1] == '+ str(y*2) +') || (jump_right[0] == '+ str(i*2) +' && jump_right[1] == '+ str(y*2) +'))\
#                     \n\tui->pushButton_'+ str(i*2) + str(y*2) +'->setEnabled(true); else ui->pushButton_'+ str(i*2) + str(y*2) +'->setEnabled(false);\n\n')

#
# ## reset_buttons
# with open(r'C:\Users\Secernato\Desktop\out.txt', 'w') as d:
#     for i in range (0,9):
#         for y in range (0,9):
#             if i < 5 and y < 5:
#                 d.write('\nui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setEnabled(true);')
#                 # \nelse \
#                 #    \n\tui->pushButton_0'+ str(i*2) + '0' + str(y*2) +'->setEnabled(false);\n\n')
#             if i >= 5 and y < 5:
#                 d.write('\nui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setEnabled(true);')
#                 # \nelse \
#                 #    \n\tui->pushButton_'+ str(i*2) + '0' + str(y*2) +'->setEnabled(false);\n\n')
#             if i < 5 and y >= 5:
#                 d.write('\nui->pushButton_0'+ str(i*2) + str(y*2) +'->setEnabled(true);')
#                 # \nelse \
#                 #    \n\tui->pushButton_0'+ str(i*2) + str(y*2) +'->setEnabled(false);\n\n')
#             if i >= 5 and y >= 5:
#                 d.write('\nui->pushButton_'+ str(i*2) + str(y*2) +'->setEnabled(true);')
#                 # \nelse \
#                 #    \n\tui->pushButton_'+ str(i*2) + str(y*2) +'->setEnabled(false);\n\n')
