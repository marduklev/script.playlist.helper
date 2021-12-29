# -*- coding: utf-8 -*-
import xbmc

def main():
    method = sys.argv[1]
    if method == 'action=select':
        defaultselect_mediaitem()
    else:
        playoffset()

def playoffset():
    xbmc.executebuiltin('setproperty(playlist_updating,true,home)')
    playlistid = 1 if xbmc.getCondVisibility('player.hasvideo') else 0
    playlist = xbmc.PlayList(playlistid)   
    container_id = xbmc.getInfoLabel('system.currentcontrolid')
    current = playlist.getposition()
    selected = int(xbmc.getInfoLabel('container(%s).currentitem' % container_id)) - 1
    index = int(selected) - int(current)
    xbmc.executebuiltin('playlist.playoffset(%s)' % (index))
    xbmc.executebuiltin('clearproperty(playlist_updating,home)')

def defaultselect_mediaitem():
    playlistid = 1 if xbmc.getCondVisibility('player.hasvideo') else 0
    playlist = xbmc.PlayList(0)
    
    xbmc.executebuiltin('setproperty(playlist_updating,true,home)')
    
    dbid = xbmc.getInfoLabel('listItem.dbid') if xbmc.getCondVisibility('!string.isempty(listitem.dbid) + !string.isequal(listitem.dbtype,year)') else 0
    dbtype = xbmc.getInfoLabel('listItem.dbtype') if xbmc.getCondVisibility('!string.isempty(listitem.dbtype)') else None
    
    item_artist = xbmc.getInfoLabel('listitem.artist')
    item_title = xbmc.getInfoLabel('listitem.title') if dbtype == 'song' else xbmc.getInfoLabel('listItem.album')
    item_label = xbmc.getInfoLabel('listItem.label')
    item_thumb = xbmc.getInfoLabel('listItem.icon')

    if xbmc.getCondVisibility('!player.hasaudio'):
        playlist.clear()

    index = playlist.getposition() + 1

    if int(dbid) > 0:
        if xbmc.getCondVisibility('!player.hasaudio'):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Player.Open", "params": {"item": {"%sid": %s} }}' % (dbtype,dbid))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Playlist.Insert", "params": { "item": {"%sid": %s}, "playlistid": %s, "position": %s}}' % (dbtype,dbid,playlistid,index))
            if xbmc.getCondVisibility('!skin.hassetting(%s_select_queue)' % dbtype):
                xbmc.executebuiltin('playlist.playoffset(1)')

    if int(dbid) == 0:
        item = 'file' if xbmc.getCondVisibility('!string.isempty(listitem.filenameandpath)') else 'directory'
        url = xbmc.getInfoLabel('listitem.filenameandpath') if xbmc.getCondVisibility('!string.isempty(listitem.filenameandpath) + [!string.isequal(listitem.dbtype,year) + !string.isequal(listitem.dbtype,genre)]') else xbmc.getInfoLabel('listitem.folderpath')
        
        if xbmc.getCondVisibility('!player.hasaudio'):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Player.Open", "params": {"item": { "%s": "%s"}}}' % (item,url))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0",  "id": 1, "method": "Playlist.Insert", "params": { "item": { "%s": "%s"}, "playlistid": %s, "position": %s}}' % (item,url,playlistid,index))

    if xbmc.getCondVisibility('skin.hassetting(%s_select_queue)' % dbtype):
        if dbtype == 'song' or dbtype == 'album':
            xbmc.executebuiltin('notification(%s %s by %s,  Added to Playlist at position %s,,%s)' % (dbtype,item_title,item_artist,index,item_thumb))
        elif dbtype == 'artist':
            xbmc.executebuiltin('notification($LOCALIZE[625] %s,  Added to Playlist at position %s,,%s)' % (item_artist,index,item_thumb))
        else:
            xbmc.executebuiltin('notification($LOCALIZE[625] %s: %s,  Added to Playlist at position %s,,%s)' % (dbtype,item_label,index,item_thumb)) 

    xbmc.executebuiltin('clearproperty(playlist_updating,home)')

if __name__ == '__main__':
    main()