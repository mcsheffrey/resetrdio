from rdio import Rdio
from rdio_consumer_credentials import *
from urllib2 import HTTPError

# create an instance of the Rdio object with our consumer credentials
rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))

try:
  # authenticate against the Rdio service
  url = rdio.begin_authentication('oob')
  print 'Go to: ' + url
  verifier = raw_input('Then enter the code: ').strip()
  rdio.complete_authentication(verifier)

  # find out what playlists you created
  ownedPlaylists = rdio.call('getPlaylists')['result']['owned']
  collabPlaylists = rdio.call('getPlaylists')['result']['collab']
  subscribedPlaylists = rdio.call('getPlaylists')['result']['subscribed']

  # list them
  for playlist in ownedPlaylists:
    print '%(shortUrl)s\t%(name)s' % playlist
    print playlist['key']

  for playlist in collabPlaylists:
    print '%(shortUrl)s\t%(name)s' % playlist
    rdio.call('setPlaylistCollaborating', {'playlist': playlist['key'], 'collaborating': 'false'})

  for playlist in subscribedPlaylists:
    print '%(shortUrl)s\t%(name)s' % playlist
    rdio.call('removeFromCollection', {'keys': playlist['key']})


except HTTPError, e:
  # if we have a protocol error, print it
  print e.read()
