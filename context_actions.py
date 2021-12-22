# -*- coding: utf-8 -*-
import xbmc

def main():
    method = sys.argv[1]
    
    if method == 'playmedia_dir':
        if xbmc.getCondVisibility('!string.isequal(listitem.dbtype,artist)'):
            url = xbmc.getInfoLabel('listitem.folderpath')
            xbmc.executebuiltin('playmedia(%s,isdir,1)' % url)
        
        elif xbmc.getCondVisibility('string.isequal(listitem.dbtype,artist)'):
            artistid = xbmc.getInfoLabel('listitem.dbid')
            xbmc.executebuiltin('playmedia(musicdb://artists/%s/-1/-2/?albumartistonly=false&amp;artistid=%s,isdir,1)' % (artistid,artistid))
    
    if method == 'play_prev':
        xbmc.Player().playprevious()
    
    if method == 'play_next':
        xbmc.Player().playnext()
    
    if method == 'open_playlist':
        xbmc.executebuiltin('action(playlist)')
    
    if method == 'save_playlist':
        xbmc.executebuiltin('Action(playlist)')
        xbmc.executebuiltin('SendClick(21)')
    
    if method == 'open_playercontrol':
        xbmc.executebuiltin('activatewindow(playercontrols)')

if __name__ == '__main__':
    main()