"""Internet Relay Chat Protocol replies"""


from .message import Message


def _M(*args, **kwargs):
    kwargs["add_nick"] = True
    return Message(*args, **kwargs)


def ERROR(host, reason=None):
    return Message("ERROR", ":Closing link: {0} ({1}".format(host, reason or ""))


def JOIN(name, prefix=None):
    return Message("JOIN", name, prefix=prefix)


def KICK(channel, nick, reason=None, prefix=None):
    return Message("KICK", channel, nick, reason, prefix=prefix)


def MODE(target, modes, params=None, prefix=None):
    if params is None:
        return Message("MODE", target, modes, prefix=prefix)
    return Message("MODE", target, modes, " ".join(params), prefix=prefix)


def PART(channel, nick, reason=None, prefix=None):
    return Message("PART", channel, nick, reason, prefix=prefix)


def PING(server):
    return Message("PING", ":{0}".format(server))


def PONG(server, text):
    return Message("PONG", server, ":{0}".format(text))


def TOPIC(channel, topic, prefix=None):
    return Message("TOPIC", channel, topic, prefix=prefix)


def RPL_WELCOME(network):
    return _M("001", "Welcome to the {0} IRC Network".format(network))


def RPL_YOURHOST(host, version):
    return _M("002", "Your host is {0} running {1}".format(host, version))


def RPL_CREATED(date):
    return _M("003", "This server was created {0}".format(date))


def RPL_MYINFO(server, version, umodes, chmodes):
    return _M("004", server, version, umodes, chmodes)


def RPL_ISUPPORT(features):
    return _M("005", *(features + ("are supported by this server",)))


def RPL_UMODEIS(modes):
    return _M("221", modes)


def RPL_LUSERCLIENT(nusers, nservices, nservers):
    return _M(
        "251",
        "There are {0} users and {1} services on {2} servers".format(
            nusers, nservices, nservers
        )
    )


def RPL_LUSEROP(noperators):
    return _M("252", "{0}".format(noperators), "operator(s) online")


def RPL_LUSERUNKOWN(nunknown):
    return _M("253", "{0}".format(nunknown), "unknown connection(s)")


def RPL_LUSERCHANNELS(nchannels):
    return _M("254", "{0}".format(nchannels), "channels formed")


def RPL_LUSERME(nclients, nservers):
    return _M("255", "I have {0} clients and {1} servers".format(nclients, nservers))


def RPL_AWAY(nick, message):
    return _M("301", nick, ":{0}".format(message))


def RPL_UNAWAY():
    return _M("305", "You are no longer marked as being away")


def RPL_NOWAWAY():
    return _M("306", "You have been marked as being away")


def RPL_WHOISUSER(nick, user, host, realname):
    return _M("311", nick, user, host, "*", ":{0}".format(realname))


def RPL_WHOISSERVER(nick, server, server_info):
    return _M("312", nick, server, server_info)


def RPL_WHOISOPERATOR(nick):
    return _M("313", nick, "is an IRC operator")


def RPL_ENDOFWHO(mask):
    return _M("315", mask, "End of WHO list")


def RPL_WHOISIDLE(nick, idle, signon):
    return _M(
        "317", nick,
        "{0}".format(idle), "{0}".format(signon),
        "seconds idle, signon time"
    )


def RPL_ENDOFWHOIS(nick):
    return _M("318", nick, "End of WHOIS list")


def RPL_WHOISCHANNELS(nick, channels):
    return _M("319", nick, ":{0}".format(" ".join(channels)))


def RPL_LISTSTART(header=None):
    return _M("321", header or "Channels :Users Name")


def RPL_LIST(channel, nvisible, topic):
    return _M("322", channel, "{0}".format(nvisible), topic)


def RPL_LISTEND():
    return _M("323", "End of LIST")


def RPL_CHANNELMODEIS(channel, mode, params=None):
    if params is None:
        return _M("324", channel, mode)
    return _M("324", channel, mode, params)


def RPL_NOTOPIC(channel):
    return _M("331", channel, "No topic is set")


def RPL_TOPIC(channel, topic):
    return _M("332", channel, topic)


def RPL_TOPICWHO(channel, setter, timestamp):
    return _M("333", channel, setter, "{0}".format(timestamp))


def RPL_INVITING(channel, nick):
    return _M("341", "{0} {1}".format(channel, nick))


def RPL_SUMMONING(user):
    return _M("342", "{0} :Summoning user to IRC".format(user))


def RPL_INVITELIST(channel, invitemask):
    return _M("346", "{0} {1}".format(channel, invitemask))


def RPL_ENDOFINVITELIST(channel):
    return _M("347", "{0} :End of channel invite list".format(channel))


def RPL_VERSION(name, version, hostname, url):
    return _M("351", name, version, hostname, url)


def RPL_WHOREPLY(channel, user, host, server, nick, status, hops, name):
    return _M(
        "352", channel, user, host, server, nick, status, ":{0} {1}".format(hops, name)
    )


def RPL_NAMEREPLY(channel, names):
    return _M("353", "=", channel, " ".join(names))


def RPL_ENDOFNAMES(channel):
    return _M("366", channel, "End of NAMES list")


def RPL_MOTD(text):
    return _M("372", "- {0}".format(text))


def RPL_MOTDSTART(server):
    return _M("375", "- {0} Message of the day -".format(server))


def RPL_ENDOFMOTD():
    return _M("376", "End of MOTD command")


def RPL_YOUREOPER():
    return _M("381", "You are now an IRC operator")


def ERR_NOSUCHNICK(nick):
    return _M("401", nick, "No such nick")


def ERR_NOSUCHCHANNEL(channel):
    return _M("403", channel, "No such channel")


def ERR_CANNOTSENDTOCHAN(channel):
    return _M("404", channel, "Cannot send to channel")


def ERR_TOOMANYCHANNELS(channel):
    return _M("405", channel, "You have joined too many channels")


def ERR_UNKNOWNCOMMAND(command):
    return _M("421", command, "Unknown command")


def ERR_NOMOTD():
    return _M("422", "MOTD file is missing")


def ERR_NONICKNAMEGIVEN():
    return _M("431", "No nickname given")


def ERR_ERRONEUSNICKNAME(nick):
    return _M("432", nick, "Erroneous nickname")


def ERR_NICKNAMEINUSE(nick):
    return _M("433", nick, "Nickname is already in use")


def ERR_USERNOTINCHANNEL(nick, channel):
    return _M("441", nick, channel, "They aren't on that channel")


def ERR_NOTREGISTERED():
    return _M("451", "You have not registered")


def ERR_NEEDMOREPARAMS(command):
    return _M("461", command, "Need more parameters")


def ERR_PASSWDMISMATCH():
    return _M("464", "Password incorrect")


def ERR_UNKNOWNMODE(mode, channel=None):
    if channel is None:
        return _M("472", mode, "is unknown mode char to me")
    return _M("472", mode, "is unknown mode char to me for channel {1}".format(channel))


def ERR_CHANOPRIVSNEEDED(channel):
    return _M("482", channel, "You're not channel operator")


def ERR_NOPRIVILEGES():
    return _M("481", "Permission Denied- You're not an IRC operator")


def ERR_NOOPERHOST():
    return _M("491", "No O-lines for your host")


def ERR_USERSDONTMATCH():
    return _M("502", "Cannot change mode for other users")
