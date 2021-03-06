

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('TimeBomb')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('TimeBomb', True)


TimeBomb = conf.registerPlugin('TimeBomb')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(RandCMDs, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName."""))
conf.registerChannelValue(TimeBomb, "bombsExempt", registry.String('', ("""Exempted Hosts, Separated by ,""")))
conf.registerGlobalValue(TimeBomb, "bombsExempt", registry.String('', ("""Exempted Hosts, Separated by ,""")))
conf.registerChannelValue(TimeBomb, "bombsEnabled", registry.Boolean(False, ("""Bombs""")))
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
conf.registerGlobalValue(TimeBomb, "bombsEnabled", registry.Boolean(False, ("""Bombs"""))) 
conf.registerGlobalValue(TimeBomb, "logChan", registry.String('', ("""The channel this will be logging to"""))) 
conf.registerChannelValue(TimeBomb, "bombDefenseEnabled", registry.Boolean(False, ("""Bombs Defense""")))
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
conf.registerGlobalValue(TimeBomb, "bombDefenseEnabled", registry.Boolean(False, ("""Bombs Defense""")))
