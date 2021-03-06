
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import sys
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('RandCMDs')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class RandCMDs(callbacks.Plugin):
    """RandCMDs"""
    threaded = False
    def cookie(self, irc, msg, args, something):
        """cookie"""
        nick = msg.nick
        if something and len(something)>0:
            nick = ' '.join(something[0:])
        irc.reply("gives " + nick + " a cookie", action=True)
    cookie = wrap(cookie, [optional(many('something'))])
    def test(self, irc, msg, args, something):
        """ test """
        self.moo = "moo"
        irc.reply(self.moo)
    test = wrap(test, ['owner', many('something')])
    def test2(self,irc, msg, args, something):
        """ test2 """
        irc.reply(self.moo)
    test2 = wrap(test2, ['owner', many('something')])
    def source(self, irc, msg, args):
        """ source """
        irc.reply("Limnoria: https://github.com/progval/Limnoria with JZTech101's Limnoria-Plugins: https://github.com/jztech101/Limnoria-Plugins and various other plugins")
    def version(self, irc, msg, args):
        """ version """
        irc.reply("Limnoria with JZTech101's Limnoria-Plugins and various other plugins on Python " + sys.version.replace("\n",""))
Class = RandCMDs


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
