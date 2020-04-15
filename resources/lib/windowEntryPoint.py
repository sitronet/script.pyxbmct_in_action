#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

global Kodi
Kodi = True

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "resources", "lib"))

from resources.lib import pyxbmctExtended

if Kodi:
    import xbmc
    import xbmcgui
    import xbmcaddon
    import pyxbmct


    ADDON = xbmcaddon.Addon()
    ADDONID = ADDON.getAddonInfo('id')
    ADDONNAME = ADDON.getAddonInfo('name')
    ADDONVERSION = ADDON.getAddonInfo('version')
    KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split(".")[0])

    ARTWORK = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'skins', 'Default', 'media'))

    #__language__ = xbmc.Language(os.getcwd()).getLocalizedString
    __settings__ = xbmcaddon.Addon(id=ADDONID)
    __language__ = __settings__.getLocalizedString

    # screen 16:9 so to have grid square fix to 16-9 on 1280 x 720 max of pyxbmct
    SIZE_WIDTH_pyxbmct = 1280
    SIZE_HEIGHT_pyxbmct = 720
    SEIZE = 16 * 4  #32 16 option so here the grid is  64 columns X 36 lines : composed with  2304 tiles
    NEUF =   9 * 4  #18 or 9

    def translation(message_id, default=False):

        try:
            if not __language__(message_id) and default:
                #xbmc.log('language default', xbmc.LOGNOTICE)
                xbmc.log( 'traduction absente : ' + str(message_id) , xbmc.LOGDEBUG)
                return default
            xbmc.log('language traduit', xbmc.LOGDEBUG)
            xbmc.log( __language__(message_id), xbmc.LOGDEBUG)
            return __language__(message_id).encode('utf-8')
        except:
            return __language__(message_id)


# Kodi key action codes.
# More codes available in xbmcgui module
ACTION_PREVIOUS_MENU = 10
"""ESC action"""
ACTION_NAV_BACK = 92
"""Backspace action"""
ACTION_MOVE_LEFT = 1
"""Left arrow key"""
ACTION_MOVE_RIGHT = 2
"""Right arrow key"""
ACTION_MOVE_UP = 3
"""Up arrow key"""
ACTION_MOVE_DOWN = 4
"""Down arrow key"""
ACTION_MOUSE_WHEEL_UP = 104
"""Mouse wheel up"""
ACTION_MOUSE_WHEEL_DOWN = 105
"""Mouse wheel down"""
ACTION_MOUSE_DRAG = 106
"""Mouse drag"""
ACTION_MOUSE_MOVE = 107
"""Mouse move"""
ACTION_MOUSE_LEFT_CLICK = 100
"""Mouse click"""

ACTION_CONTEXT_MENU = 117
'''for my webchip remote'''
ACTION_FORWARD = 16
ACTION_REWIND = 17
ACTION_MUTE = 91
ACTION_NEXT_ITEM = 14
ACTION_PAUSE = 12
ACTION_PLAY = 68
ACTION_PLAYER_FORWARD = 77
ACTION_PLAYER_PLAY = 79
ACTION_PLAYER_PLAYPAUSE = 229
ACTION_PLAYER_REWIND = 78
ACTION_PREV_CONTROL = 182
ACTION_PREV_ITEM = 15
ACTION_PREV_LETTER = 141
ACTION_PREV_PICTURE = 29
ACTION_PREV_SCENE = 139
ACTION_SHOW_FULLSCREEN = 36
ACTION_SHOW_GUI = 18
ACTION_SHOW_INFO = 11
ACTION_SHOW_MPLAYER_OSD = 83
ACTION_SHOW_OSD = 24
ACTION_SHOW_OSD_TIME = 123
ACTION_SHOW_PLAYLIST = 33
ACTION_SMALL_STEP_BACK = 76
ACTION_STEP_BACK = 21
ACTION_STEP_FORWARD = 20
ACTION_STOP = 13
ACTION_SWITCH_PLAYER = 234
ACTION_VOLAMP_DOWN = 94
ACTION_VOLAMP_UP = 93
ACTION_VOLUME_DOWN = 89
ACTION_VOLUME_UP = 88


class MyOriginalSkin(pyxbmct.Skin):
    '''
    original source is :
    @property
    def main_bg_img(self):
        return os.path.join(self.images, 'AddonWindow', 'SKINDEFAULT.jpg')

    @property
    def background_img(self):
        return os.path.join(self.images, 'AddonWindow', 'ContentPanel.png')
    '''
    '''
    @property
    def background_img(self):
        return xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'skins', 'Default', 'media', 'pcp_allegro.png'))

    @property
    def title_background_img(self):
        return xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'skins', 'Default', 'media','pcp_harmony.png'))

    @property
    def main_bg_img(self):
        return xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'), 'resources', 'skins', 'Default', 'media','pcp_vibrato.png'))
    
    
    pyxbmct.addonwindow.skin = MyOriginalSkin()
    '''

# Then create your UI window class with the new background
#class MyCoolWindow(pyxbmct.AddonWindow):

#class FenetreOne(pyxbmct.AddonFullWindow):    # background img (skin) header+ title could be hide ok
#class FenetreOne(pyxbmct.AddonDialogWindow):  # background (skin) header+ title + on the top screen
#class FenetreOne(pyxbmct.BlankDialogWindow):  # transparent without header+title and on top screen
#class FenetreOne(pyxbmct.BlankFullWindow):    # black background without header+title (cannot change background) could be hide
#class FenetreOne(pyxbmctExtended.BackgroundDialogWindow)  # background (skin) without header+title - could be hide
#class FenetreOne(pyxbmctExtended.BackgroundFullWindow)  # background (skin) without header+title - could be hide

#class
class FenetreOne(pyxbmct.AddonFullWindow):
    '''
    AddonFullWindow permit the change of the skin and can be hide to show other window over this one
    This is entry point of the demonstration
    '''

    def __init__(self,*args, **kwargs):
        title = args[0]
        super(FenetreOne, self).__init__(title)
        #super(FenetreOne, self).__init__() # if class changed without title
        xbmc.log('Starting FenetreOne', xbmc.LOGNOTICE)
        self.promptStartScript()
        self.geometrie()
        self.defineControlMenus()
        self.putControlElements()
        self.connectControlElements()
        self.setFocus(self.listMenu_Racine)

    def onAction(self, action):
        """
        Catch button actions.
        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_PAUSE:  # currently it's the space bar on my remote
            xbmc.log('Action Pause', xbmc.LOGNOTICE)
            self.pause_play()

        elif action == ACTION_PLAY or action == ACTION_PLAYER_PLAY:
            xbmc.log('Action Play', xbmc.LOGNOTICE)
            self.pause_play()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            xbmc.log('Action vol up', xbmc.LOGNOTICE)
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            xbmc.log('Action vol down', xbmc.LOGNOTICE)
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)

    def connexionEvent(self):
        # Connect key and mouse events for list navigation feedback.
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE,
             pyxbmct.ACTION_MOVE_LEFT,
             pyxbmct.ACTION_MOVE_RIGHT],
            self.list_Menu_Navigation)

    def quit(self):
        xbmc.log('quit asked - Exit program  0 fonction quit() .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this script ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit program  0 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def promptStartScript(self):
        ''' only a dialog popup to notify the begining of the program'''
        __addon__ = xbmcaddon.Addon()
        __addonname__ = __addon__.getAddonInfo('name')
        __icon__ = __addon__.getAddonInfo('icon')

        ligne_1_Information = translation(32010, default='Running test Addon Script')
        ligne_2_Information = translation((32020), default='Version de Kodi : ') + str(KODI_VERSION)
        ligne_3_Information =  translation(32030, default='Addon : ') + ADDONNAME + ' ; ' + translation(32040, default= 'Version : ') + ADDONVERSION
        time = 3000 #in miliseconds

        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(ADDONNAME,ligne_1_Information, time, __icon__))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(ADDONNAME,ligne_2_Information, time, __icon__))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(ADDONNAME,ligne_3_Information, time, __icon__))

    def geometrie(self):
        '''set the geometry of the screen (main Window of the script, point of entry )
        to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()            # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()                         # 1920

        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10            # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH //10             # 192

        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT
        xbmc.log('Size of FenetreOne : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct
            self.screeny = SIZE_HEIGHT_pyxbmct
        #pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of FenetreOne set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program

        self.image_button_pause = self.image_dir + '/pause.png'   # get from Xsqueeze
        self.image_button_stop = self.image_dir + '/stop.png'     # get from Xsqueeze
        self.image_button_play = self.image_dir + '/play.png'     # get from Xsqueeze
        self.textureback_slider_duration = self.image_dir + '/slider_back.png'  # Get from plugin audio spotify
        self.texture_slider_duration = self.image_dir + '/slider_button_new.png'
        self.image_list_focus = self.image_dir + '/MenuItemFO.png'        # Drawing myself from an original pyXBMCt
        self.textureback_slider_volume = self.image_dir + '/slider_back.png'   # Get from jivelite (Squeezebox controler)
        self.texture_slider_volume = self.image_dir + '/slider_button_new.png'  # Get from jivelite

        self.imagedefond = self.image_dir + '/fond-noir.jpg'    # Get somewhere Online

    def defineControlMenus(self):
        # list for the items of the menu
        self.listeRacinePourMenu = [
                                    'Fenetre 1 : AddonFullWindow' ,
                                    'Fenetre 2 : AddonDialogWindow' ,
                                    'Fenetre 3 : BlankDialogWindow',
                                    'Fenetre 4 : BlankFullWindow',
                                    'Fenetre 5 : BackgroundDialogWindow (extended)',
                                    'Fenetre 6 : BackgroundFullWindow (extended)'
                                    ]
        self.list_racine_label = pyxbmct.Label('Waiting Action...', textColor='0xFF808080')
        self.Information_textbox = pyxbmct.TextBox()
        self.listMenu_Racine = pyxbmct.List(buttonFocusTexture=self.image_list_focus, _itemHeight=40)
        # To get marks on the screen :
        self.label0 = pyxbmct.Label('ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_abcdefghijklmnopqrstuvwxyz')
        self.label1 = pyxbmct.Label('A')
        self.label2 = pyxbmct.Label('B')
        self.label3 = pyxbmct.Label('C')
        self.label4 = pyxbmct.Label('D')
        self.label5 = pyxbmct.Label('E')
        self.label6 = pyxbmct.Label('F')
        self.label7 = pyxbmct.Label('G')
        self.label8 = pyxbmct.Label('H')
        self.label9 = pyxbmct.Label('I')
        self.label10 = pyxbmct.Label('J')
        self.labelT = pyxbmct.Label('T')
        self.labelU = pyxbmct.Label('U')

    def putControlElements(self):
        ''' mainly place the menu list and other controls elements on the screen

        '''
        row_depart = 3
        col_depart = row_depart
        self.espace_row = NEUF - 5  # tiles
        self.espace_col = (SEIZE // 2) - col_depart

        ligneLabel = NEUF - 2
        # label pour indiquer les items sélectionnés dans la hiérarchie des menus, permet aussi de tester la navigation
        self.placeControl(control= self.list_racine_label, 
                          row= ligneLabel, 
                          column= 2, 
                          rowspan= 1, 
                          columnspan= 10
                          )

        self.placeControl(control=self.Information_textbox,
                          row= row_depart ,
                          column= (SEIZE // 2 ) + 3 ,
                          rowspan= (NEUF // 2) - row_depart,
                          columnspan= (SEIZE // 2) - col_depart,
                          pad_x= 4,
                          pad_y= 4
                          )
        self.Information_textbox.setText('Try to press : \n' 
                                         'OK, Select, ContextMenu or Volume+ or Volume- keys \n' 
                                         ' from your remote to watch in action'
                                         )
        self.Information_textbox.setVisible(True)

        self.placeControl(control= self.listMenu_Racine,
                          row= row_depart,
                          column= col_depart,
                          rowspan=self.espace_row,
                          columnspan= self.espace_col )
        
        # Add items to the list
        self.listMenu_Racine.addItems(self.listeRacinePourMenu)
        # Add marks
        self.placeControl(control=self.label0, row=ligneLabel - 4, column=0, rowspan=1, columnspan= SEIZE // 2 )
        self.placeControl(control=self.label1, row=ligneLabel - 2, column=0, rowspan=1, columnspan=2)
        self.placeControl(control=self.label2, row=ligneLabel - 2, column=1, rowspan=1, columnspan=2)
        self.placeControl(control=self.label3, row=ligneLabel - 2, column=2, rowspan=1, columnspan=2)
        self.placeControl(control=self.label4, row=ligneLabel - 2, column=3, rowspan=1, columnspan=2)
        self.placeControl(control=self.label5, row=ligneLabel - 2, column=4, rowspan=1, columnspan=2)
        self.placeControl(control=self.label6, row=ligneLabel - 2, column=5, rowspan=1, columnspan=2)
        self.placeControl(control=self.label7, row=ligneLabel - 2, column=6, rowspan=1, columnspan=2)
        self.placeControl(control=self.label8, row=ligneLabel - 2, column=7, rowspan=1, columnspan=2)
        self.placeControl(control=self.label9, row=ligneLabel - 2, column=8, rowspan=1, columnspan=2)
        self.placeControl(control=self.label10, row=ligneLabel - 2, column=9, rowspan=1, columnspan=2)

        self.placeControl(control=self.labelT, row=ligneLabel - 2, column=SEIZE - 1, rowspan=1, columnspan=2)
        self.placeControl(control=self.labelU, row=ligneLabel - 2, column=SEIZE, rowspan=1, columnspan=2)


    def connectControlElements(self):
        # Connect the list to a function to display which list item is selected.
        # example :
        # self.connect(self.list_Menu, lambda: xbmc.executebuiltin('Notification(Note!,{0} selected.)'.format(
        #    self.list_Menu.getListItem(self.list_Menu.getSelectedPosition()).getLabel())))
        self.connect(self.listMenu_Racine, self.navigationFromMenuRacine)
        # etcoetera...
        #

    def navigationFromMenuRacine(self):

        itemSelectionRacine = self.listMenu_Racine.getListItem(self.listMenu_Racine.getSelectedPosition()).getLabel()
        self.list_racine_label.setLabel(str(itemSelectionRacine))

        if itemSelectionRacine == 'Fenetre 1 : AddonFullWindow':

            self.fenetre1 = Fenetre1('Can write a title -> Window n° 1')
            self.fenetre1.doModal()
            del self.fenetre1

        if itemSelectionRacine == 'Fenetre 2 : AddonDialogWindow':

            self.fenetre2 = Fenetre2('Can write a title -> Window n° 2')
            self.fenetre2.doModal()
            del self.fenetre2

        elif itemSelectionRacine == 'Fenetre 3 : BlankDialogWindow':
            self.fenetre3 = Fenetre3()
            self.fenetre3.doModal()
            del self.fenetre3

        elif itemSelectionRacine ==  'Fenetre 4 : BlankFullWindow':
            self.fenetre4 = Fenetre4()
            self.fenetre4.doModal()
            del self.fenetre4

        elif itemSelectionRacine ==  'Fenetre 5 : BackgroundDialogWindow (extended)':
            self.fenetre5 = Fenetre5()
            self.fenetre5.doModal()
            del self.fenetre5

        elif itemSelectionRacine == 'Fenetre 6 : BackgroundFullWindow (extended)':
            self.fenetre6 = Fenetre6()
            self.fenetre6.doModal()
            del self.fenetre6

    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in main Window ')
        contextMenuFrame.doModal()
        del contextMenuFrame

class Fenetre1(pyxbmct.AddonFullWindow):
    '''
    AddonFullWindow and AddonDialog Window have an header ( title-bar + title + close button)
    AddonFullWindow have a background
    '''
    def __init__(self, *args ):
        title = args[0] # for AddonFullWindow

        super(Fenetre1, self).__init__(title)

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2      # So 1280 / 2 = 640
            self.screeny = SIZE_HEIGHT_pyxbmct // 2     # So 720 / 2 = 360
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 1 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3 , int(SEIZE / 2) , 28 , 28 ) #TODO: to adjust because is not always a square
        self.pochette.setImage(self.cover_jpg)

        # place a fadeLabel on the grid: line(row) 8, column 4
        # which spans 3 rows and 27 columns
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(control=self.labeltitre,
                          row= 8,
                          column= 4,
                          rowspan= 3,
                          columnspan= 27
                          )
        self.labeltitre.addLabel('Fenetre 1 : AddonFullWindow ')

        # print a label to write the size of this window (self)
        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10 , 4 , 1 , 12)
        self.labelSize.setLabel(str(self.screenx) + ' X ' + str(self.screeny) )

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 1 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 1 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)

    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 1')
        contextMenuFrame.doModal()
        del contextMenuFrame


class Fenetre2(pyxbmct.AddonDialogWindow):
    '''
    AddonFullWindow and AddonDialog Window have an header ( title-bar + title + close button)
    AddonDialogWindow have a transparent background
    '''

    def __init__(self, *args ):
        title = args[0] # for AddonFullWindow and AddonDialogWindow
        super(Fenetre2, self).__init__(title)

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2
            self.screeny = SIZE_HEIGHT_pyxbmct // 2
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 2 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'      # pour le démarrage then updated
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3 , int(SEIZE / 2) , 28 , 28 )  # to fix
        self.pochette.setImage(self.cover_jpg)

        # print a fadeLabel
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(self.labeltitre,  8 , 4 , 3 , 27 )
        self.labeltitre.addLabel('Fenetre 2 : AddonDialogWindow ')

        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10, 4, 1, 12)
        self.labelSize.setLabel( str(self.screenx) + ' X ' + str(self.screeny) )

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 2 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 2 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)

    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 2 ')
        contextMenuFrame.doModal()
        del contextMenuFrame


class Fenetre3(pyxbmct.BlankDialogWindow):
    '''BlankFullWindow and BlankDialogWindow have not an header
       BlankDialogWindow have a transparent background so we see just the elements put by
       placeControl()
       BlankFullWindow have a black background that hide the parent window'''

    def __init__(self, *args ):
        #note : there isn't title here
        super(Fenetre3, self).__init__()

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2
            self.screeny = SIZE_HEIGHT_pyxbmct // 2
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 3 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'      # pour le démarrage then updated
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3 , int(SEIZE / 2) , 28 , 28 )  # to fix
        self.pochette.setImage(self.cover_jpg)

        # print a fadeLabel
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(self.labeltitre,  8 , 4 , 3 , 27 )
        self.labeltitre.addLabel('Fenetre 3 : BlankDialogWindow ')

        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10, 4, 1, 12)
        self.labelSize.setLabel( str(self.screenx) + ' X ' + str(self.screeny) )

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 3 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 3 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)


    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 3')
        contextMenuFrame.doModal()
        del contextMenuFrame


class Fenetre4(pyxbmct.BlankFullWindow):
    '''BlankFullWindow and BlankDialogWindow have not an header
       BlankDialogWindow have a transparent background so we see just the element put by
       placeControl()
       BlankFullWindow have a black background that hide the parent window'''

    def __init__(self, *args ):

        super(Fenetre4, self).__init__()

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2
            self.screeny = SIZE_HEIGHT_pyxbmct // 2
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 4 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'      # pour le démarrage then updated
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3 , int(SEIZE / 2) , 28 , 28 )  # to fix
        self.pochette.setImage(self.cover_jpg)

        # print a fadeLabel
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(self.labeltitre,  8 , 4 , 3 , 27 )
        self.labeltitre.addLabel('Fenetre 4 : BlankFullWindow ')

        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10, 4, 1, 12)
        self.labelSize.setLabel( str(self.screenx) + ' X ' + str(self.screeny) )

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 4 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 4 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)


    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 4')
        contextMenuFrame.doModal()
        del contextMenuFrame

class Fenetre5(pyxbmctExtended.BackgroundDialogWindow):
    '''BackgroundFullWindow and BackgroundDialogWindow have not an header
        like BlankFullWindow and BlankDialogWindow
        BackgroundDialogWindow have a transparent background beyond the self.window
        so we see the parent Window but inside itself it have a background fix by skin (main_bg_img)
        unlike BlankDialogWindow (reminder all is transparent)
        BackgroundDialogWindow, it is an extended class of the pyxbmct framework
    '''

    def __init__(self, *args ):

        super(Fenetre5, self).__init__()

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2
            self.screeny = SIZE_HEIGHT_pyxbmct // 2
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 5 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK    # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'      # pour le démarrage then updated
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3 , int(SEIZE / 2) , 28 , 28 )  # to fix
        self.pochette.setImage(self.cover_jpg)

        # print a fadeLabel
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(self.labeltitre,  8 , 4 , 3 , 27 )
        self.labeltitre.addLabel('Fenetre 5 : BackgroundDialogWindow ')

        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10, 4, 1, 12)
        self.labelSize.setLabel( str(self.screenx) + ' X ' + str(self.screeny) )

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 5 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 5 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)


    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 5')
        contextMenuFrame.doModal()
        del contextMenuFrame


class Fenetre6(pyxbmctExtended.BackgroundFullWindow):
    '''BackgroundFullWindow and BackgroundDialogWindow doesn't have an header
        like BlankFullWindow and BlankDialogWindow.
        BackgroundFullWindow have a black background beyond the window
        so we could not see the parent Window and inside itself it have a different background fix by skin  (main_bg_img)
        unlike BlankFullWindow
        This BackgroundFullWindow, it is an extension of the original pyxbmct
    '''

    def __init__(self, *args):

        super(Fenetre6, self).__init__()

        '''set the geometry of the screen (main Window of the script, point of entry )
                to place later elements and controls (list button image etc...)'''
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.GRIDSCREEN_Y = SIZESCREEN_HEIGHT // 10  # 108
        self.GRIDSCREEN_X = SIZESCREEN_WIDTH // 10  # 192
        self.screenx = SIZESCREEN_WIDTH
        self.screeny = SIZESCREEN_HEIGHT

        if self.screenx > SIZE_WIDTH_pyxbmct:
            self.screenx = SIZE_WIDTH_pyxbmct // 2
            self.screeny = SIZE_HEIGHT_pyxbmct // 2
        # pyxbmct :
        self.setGeometry(width_=self.screenx, height_=self.screeny, rows_=NEUF, columns_=SEIZE)
        xbmc.log('Size of Fenetre 6 set to : ' + str(self.screenx) + ' x ' + str(self.screeny), xbmc.LOGNOTICE)

        self.image_dir = ARTWORK  # path to pictures used in the program
        # print a picture
        self.cover_jpg = self.image_dir + '/music.png'  # pour le démarrage then updated
        self.pochette = pyxbmct.Image(self.cover_jpg)
        self.placeControl(self.pochette, 3, int(SEIZE / 2), 28, 28)  # to fix
        self.pochette.setImage(self.cover_jpg)

        # print a fadeLabel
        self.labeltitre = pyxbmct.FadeLabel()
        self.placeControl(self.labeltitre, 8, 4, 3, 27)
        self.labeltitre.addLabel('Fenetre 6 : BackgroundFullWindow ')

        self.labelSize = pyxbmct.Label('')
        self.placeControl(self.labelSize, 10, 4, 1, 12)
        self.labelSize.setLabel( str(self.screenx) + ' X ' + str(self.screeny))

    def quit(self):
        xbmc.log('quit asked - Exit Window .', xbmc.LOGNOTICE)
        line1 = " Do you want to exit this Window 6 ? "
        Acknownledge = xbmcgui.Dialog().yesno('Quit', line1)
        if Acknownledge:
            xbmc.log('quit done - Exit Window 6 fonction quit() .', xbmc.LOGNOTICE)
            self.close()
        else:
            pass

    def onAction(self, action):
        """
        Catch button actions.

        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == ACTION_VOLUME_UP:    # it's the volume key Vol+  on my remote
            self.promptVolume()

        elif action == ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.promptVolume()

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)

    def promptVolume(self):
        volumeFrame =  VolumeFrameChild()
        volumeFrame.doModal()
        del volumeFrame

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Window 6')
        contextMenuFrame.doModal()
        del contextMenuFrame



class ContextMenuFrameChild(pyxbmct.AddonDialogWindow):
    '''This one is  resized  on Top with header : bar-title + title + close button
       the background is 'background_img' of skin
       the title-bar is 'title_background_img' of skin
       Beyond the window, the parent window is visible
    '''

    def __init__(self, *args):
        title = args[0]
        super(ContextMenuFrameChild, self).__init__(title)
        # get image back
        self.image_dir = ARTWORK  # path to pictures used in the program
        self.cover_jpg = self.image_dir + '/music.png'

        Size_W_ChildSelf = 500
        Size_H_ChildSelf = 400
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # 1920
        self.setGeometry(width_=Size_W_ChildSelf, height_=Size_H_ChildSelf,
                         rows_=10, columns_=10,
                         pos_x=int(640 - (Size_W_ChildSelf // 2)),
                         pos_y=int(360 - Size_H_ChildSelf // 2 ))

        self.set_info_controls()

        # Connect a key action (Backspace) to close the window.
        self.connect(ACTION_NAV_BACK, self.close)
        self.connect(ACTION_PREVIOUS_MENU, self.close)

        self.connectEventList([pyxbmct.ACTION_MOVE_LEFT,
                               pyxbmct.ACTION_MOVE_RIGHT,
                               pyxbmct.ACTION_MOUSE_DRAG,
                               pyxbmct.ACTION_MOUSE_LEFT_CLICK],
                              self.context_update)
        xbmc.log('fin init child ContextMenu Frame', xbmc.LOGDEBUG)

    def set_info_controls(self):
        self.label_context = pyxbmct.Label('-------------------Development---------------------',
                                           alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(control=self.label_context, row=0, column=0, rowspan=1, columnspan=10)
        self.button_context = pyxbmct.Button('Bouton', focusTexture=self.cover_jpg, noFocusTexture=self.cover_jpg)
        self.placeControl(control=self.button_context, row=4, column=0, rowspan=4, columnspan=4)

        self.label_context_basdroite = pyxbmct.Label('BD')
        self.placeControl(control=self.label_context_basdroite, row=10, column=0, rowspan=1, columnspan=1)
        self.label_context_basgauche = pyxbmct.Label('BG. 500 x 400 px') # it will print outside the window
        self.placeControl(control=self.label_context_basgauche, row=10, column=9, rowspan=1, columnspan=5)

        self.setFocus(self.button_context)

    def context_update(self):
        xbmc.log('update Context', xbmc.LOGNOTICE)


class VolumeFrameChild(pyxbmct.BlankDialogWindow):
    '''
    This one is transparent background and resized on top
    @author : rondrach , a novice in python programming
    I wrote this example class to use in my addon kodijivelette
    of course you have to code the functions slider_update,
    setVolume and getVolume to interact with the main program
    '''

    def __init__(self):
        super(VolumeFrameChild, self).__init__()
        # get image back
        self.image_dir = ARTWORK  # path to pictures used in the program
        self.textureback_slider_volume = self.image_dir + '/rem_sliderbar_bkgrd.png' #get form jivelite
        self.texture_slider_volume = self.image_dir + '/rem_slider.png'  # get from jivelite

        # take care of pos_x & pos_y
        Size_W_ChildSelf = 400
        Size_H_ChildSelf = 76
        SIZESCREEN_HEIGHT = xbmcgui.getScreenHeight()  # exemple  # 1080
        SIZESCREEN_WIDTH = xbmcgui.getScreenWidth()  # exemple 1920
        xbmc.log('size screen FrameParentVolume : ' + str(SIZESCREEN_WIDTH) + ' x ' + str(SIZESCREEN_HEIGHT), xbmc.LOGNOTICE)
        # reminder :
        # we fit the parent window to 64 columns  x 32 rows with virtual pixel of 1280 x 720
        # the pos_x and pos_y are on the virtual pixel grid pyxbmct (1280 x 720)
        # inside this child frame we define a grid : 2 rows X 10 columns
        self.setGeometry(width_= Size_W_ChildSelf,
                         height_= Size_H_ChildSelf,
                         rows_= 2,
                         columns_= 10,
                         pos_x= int((SIZE_WIDTH_pyxbmct // 2 )- (Size_W_ChildSelf // 2)),
                         pos_y= SIZE_HEIGHT_pyxbmct - Size_H_ChildSelf
                         )

        self.set_info_controls()
        self.volumePercent = self.getVolume()

        # Connect a key action (Backspace) to close the window.
        #self.connect(ACTION_NAV_BACK, self.close)
        #self.connect(ACTION_PREVIOUS_MENU, self.close)

        self.connectEventList([
                        pyxbmct.ACTION_MOVE_LEFT,
                        pyxbmct.ACTION_MOUSE_LEFT_CLICK,
                        pyxbmct.ACTION_MOVE_RIGHT
                        ],
                        self.slider_update)

        self.setFocus(self.slider_volume)

        xbmc.log('fin init child Volume Frame', xbmc.LOGDEBUG)

    def set_info_controls(self):

        self.label_volume = pyxbmct.Label('volume')
        self.placeControl(control=self.label_volume,
                          row= 0,
                          column= 0,
                          rowspan= 1,
                          columnspan= 10)

        self.slider_volume = pyxbmct.Slider(textureback=self.textureback_slider_volume,
                                            texture=self.texture_slider_volume,
                                            texturefocus=self.texture_slider_volume, orientation=xbmcgui.HORIZONTAL)
        self.placeControl(control= self.slider_volume,
                          row= 1,
                          column= 0,
                          rowspan= 1,
                          columnspan= 10
                          )
        volumePercent = float(50)
        self.slider_volume.setPercent(volumePercent)

    def slider_update(self):
        # Update slider value label when the slider nib moves
        volumeSliderPercent = self.slider_volume.getPercent()
        self.label_volume.setLabel('Volume : ' + str(volumeSliderPercent) + ' %')

    def onAction(self, action):
        if action == xbmcgui.ACTION_VOLUME_UP:  # it's the volume key Vol+  on my remote
            self.setVolume('UP')
        elif action == xbmcgui.ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.setVolume('DOWN')

    def getVolume(self):
        # need to know the actual volume in percent from the slider
        return self.slider_volume.getPercent()

    def setVolume(self, UpOrDown):

        volumePercent = self.getVolume()

        if UpOrDown == 'UP':
            volumePercent = volumePercent + 5.
            if volumePercent >= 100:
                volumePercent = 100

        elif UpOrDown == 'DOWN':
            volumePercent = volumePercent - 5.
            if volumePercent < 0:
                volumePercent = 0
        else:
            pass

        self.slider_volume.setPercent(volumePercent)
        self.label_volume.setLabel('Volume : ' + str(volumePercent) + ' %')

    def quit(self):
        xbmc.log('quit asked - Exit Window Volume.', xbmc.LOGNOTICE)
        self.close()

    def onAction(self, action):
        """
        Catch button actions.
        ``action`` is an instance of :class:`xbmcgui.Action` class.
        """
        if action == ACTION_PREVIOUS_MENU:
            xbmc.log('Action Previous_menu' , xbmc.LOGNOTICE)
            self.quit()

        elif action == ACTION_NAV_BACK:
            xbmc.log('Action nav_back' , xbmc.LOGNOTICE)
            self.quit()

        elif action == xbmcgui.ACTION_CONTEXT_MENU:     # it's a strange icon key on my remote
            xbmc.log('Action ContextMenu', xbmc.LOGNOTICE)
            self.flagContextMenu = True
            self.promptContextMenu()

        elif action == xbmcgui.ACTION_VOLUME_UP:  # it's the volume key Vol+  on my remote
            self.setVolume('UP')

        elif action == xbmcgui.ACTION_VOLUME_DOWN:  # it's the volume key Vol-  on my remote
            self.setVolume('DOWN')

        else:
            xbmc.log('else condition onAction ' + repr(action)  , xbmc.LOGNOTICE)
            self._executeConnected(action, self.actions_connected)

    def promptContextMenu(self):
        contextMenuFrame = ContextMenuFrameChild('ContextMenu Key pressed in Volume Window')
        contextMenuFrame.doModal()
        del contextMenuFrame
