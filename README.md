- addon provides 2 functions which can be used as onclick actions (it can be any file or directory)
- and provides several contexmenu items (see below)


Onclick Actions ( for skinners )

	1. override onclick actions 
		
		use 'RunScript(script.playlist.helper,action=select)'
		
		• by default = add the selected mediatype to playlist as next item and play it immediatly
		
		• if a skin provides settings like 'skin.hassetting(<media type>_select_queue)' is true - it just queues the selected item as next item to be played in playlist
		
			e.g. 
				skin.hassetting(album_select_queue) - add as next title, playback after current title ends
				!skin.hassetting(song_select_queue) - add as next title and play it immediatly
		
	2. - for skins, which use a dynamic container filled with currently playing playlist (playlistmusic:// ; playlistvideo://)
		you can play the selected media item from that list, without 'clear/destroy' the current playlist
		
		<onclick>RunScript(script.playlist.helper,action=playlist_playoffset)</onclick>
		

					- example for a playlist container
	
					<control type="panel" id="12345">
						<include>playlist_container_atts</include>
						...
							< the other skinning stuff >
						...
						<content>$VAR[playlistmusic]</content>
					</control>
					
					<include name="playlist_container_atts">
						<onfocus>SetProperty(playlist_itemcontrol,enable,home)</onfocus>
						<onunfocus>ClearProperty(playlist_itemcontrol,home)</onunfocus>
						<onclick>RunScript(script.playlist.helper,action=playlist_playoffset)</onclick>
					</include>
					<variable name="playlistmusic">
						<value condition="string.isempty(window(home).property(playlist))">playlistmusic://</value>
						<value>-</value>
					</variable>
	
	
Context Menu Items and Functions
- queue item to last playlistposition	- if not media window
- queue item to next playlistposition 	- if not media window
	
	NOTE
			- using touch device ; GOT ISSUES GETTING INFOLABELS (dbid,dbtype) - FAILS IN CUSTOM WINDOW, BUT NOT IF RUN IT IN Media WINDOW, which is strange
			- use via keyboard/remote all is fine
			
- for skins, which use a dynamic container filled with currently playing playlist (playlistmusic:// ; playlistvideo://)																					
	- switch playlistitems (move up/down)
	- delete playlistitem
	
	INFO for Skinners
			
			- switch playlist position (+/- 1) the only way for indicate if a container is used for playlist content is via set property in the skin
				so the contextitem for switch playlist items : is just visible if 'string.isequal(window(home).property(playlist_itemcontrol),enable)'
					simple add 
					
					<control type="panel" id="12345">
						<onfocus>SetProperty(playlist_itemcontrol,enable,home)</onfocus>
						<onunfocus>ClearProperty(playlist_itemcontrol,home)</onunfocus>
						.. 
					</control>
					
					for the container goup 
						
			- playlist container refresh - when add items to list
				the custom container for playlist wont refresh properly till window reload, therefore using a variable to "switch" between visible state
				
				the script set a window property  ''setproperty(playlist,update,home)'' at start and clears it at end of a playlist script when use (queue,delete,switch) functions
					
					<variable name="playlistmusic">
						<value condition="string.isempty(window(home).property(playlist))">playlistmusic://</value>
						<value>-</value>
					</variable>
			
			
				
				
- activate playlist window - if playlist filled
- activate playercontrols dialog

- save currently active playlist - if playlist filled					TODO: change , check possibility in docs  

- play next song 	 				- if playlist has next item			TODO: add setting for disable
- play previous song 				- if playlist has previous item		TODO: add setting for disable
- play all songs by artist 												TODO: add setting for disable
		if either media window and on '. all albums' listitem entry,
		or if not media window for artist or album items (clears playlist, and start plaing folder)



KNOWN ISSUES:
																			- there is an 'issue' when 'switch_minus' items
				- 	when use : 'SetFocus(container_id,position,absolute)' or 'SetFocus(container_id,position)' , or 'Control.Move(container_id,-1)'
					to focus the previous highlighted playlistitem again, 
					forcing focus position failing if a container control is designed to less items than a playlist is filled with 
					e.g. gui show 8 items
						 playlist if filled with 10 items
						 switch 0(first) to 8(last), result in wrong focus position
						 
TO DO:
- playlist save code - look at docs
- get better diff of current playlist by getting an identifyer - look at docs/jsonrpc get.playlistidentifyer?
  ( currently just checks if a video is playing, no matter which playlist id is active (its absolutely possible to have video files within a active music playlist, even if rare case))

						 