# -*- coding: utf-8 -*-
import xbmc

def main():
    method = sys.argv[1]
    
    xbmc.executebuiltin('setproperty(playlist_updating,true,home)')
   
    playlistid = 1 if xbmc.getCondVisibility('player.hasvideo') else 0
    playlist = xbmc.PlayList(playlistid)
    container_id = xbmc.getInfoLabel('system.currentcontrolid')
    position1 = int(xbmc.getInfoLabel('container(%s).currentitem' % container_id)) - 1
    size = int(playlist.size()) - 1
    
    if method == 'minus':
        if position1 == 0:
            position2 = size
        else:
            position2 = int(xbmc.getInfoLabel('container(%s).currentitem' % container_id)) -2
    
    elif method == 'plus':
        if position1 == size:
            position2 = 0
        else:
            position2 = xbmc.getInfoLabel('container(%s).currentitem' % container_id)
    
    if method == 'minus' or method == 'plus':
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Playlist.Swap", "params": { "playlistid": %s, "position1": %s, "position2": %s }, "id": 1}' % (playlistid,position1,position2))
        xbmc.executebuiltin('setfocus(%s,%s)' % (container_id,position2))
    
    if method == 'delete':
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Playlist.Remove", "params": { "playlistid": %s, "position": %s}}' % (playlistid,position1))
    
    xbmc.executebuiltin('clearproperty(playlist_updating,home)')

if __name__ == '__main__':
   main()