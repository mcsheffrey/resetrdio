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

  # find out what playlists you are subscribed to
  collab_playlists = rdio.call('getPlaylists')['result']['collab']
  subscribed_playlists = rdio.call('getPlaylists')['result']['subscribed']

  # loop through collaborations and unsubscribe
  for playlist in collab_playlists:
    print '%(shortUrl)s\t%(name)s' % playlist
    rdio.call('setPlaylistCollaborating', {'playlist': playlist['key'], 'collaborating': 'false'})

  # loop through playlist subscriptions and ubsubscribe
  for playlist in subscribed_playlists:
    print '%(shortUrl)s\t%(name)s' % playlist
    rdio.call('removeFromCollection', {'keys': playlist['key']})


except HTTPError, e:
  # if we have a protocol error, print it
  print e.read()
