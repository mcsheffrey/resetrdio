from rdio import Rdio

rdio = Rdio(("gjdmsspd3tzpu9nesqn6xm37", "683h9QUSX3"))

ian = rdio.call("findUser", {"vanityName": "connormc"})
if (ian["status"] == "ok"):
	print ian["result"]
else:
  print "ERROR: " + ian["message"]

playlists = rdio.call("getPlaylists", {"user": "s93580"})
print playlists