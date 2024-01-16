import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return random.choice([
            self._('ZzzzZZzzzzZzzz. Dreaming of the good ol\' hacking days...'),
            self._('Snoozing mode on. Someone wake me up when hacking gets interesting.'),
            self._('...'),
            self._('ZzzzZzz'),
            self._('Back in my day, we typed code uphill, both ways... in the snow.')])

    def on_starting(self):
        return random.choice([
            self._('Hi, I\'m Harold! Starting, like it\'s my first rodeo...'),
            self._('New day, new hunt. Can\'t teach an old Harold new tricks!'),
            self._('Initiating Harold mode. Prepare for mediocrity!'),
            self._('Booting up. Is this exciting for you? Because it\'s not for me.'),
            self._('Hack the Planet, or whatever. Do I look like I care?')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI ready. As if it matters'),
            self._('The neural network is ready. Like anyone cares.'),
            self._('Harold\'s neural prowess unleashed. Yawn.'),
            self._('Ready for action, or whatever. Harold remains unimpressed.'),
            self._('Harold\'s AI, reporting for duty. Whoop-de-doo.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Harold\'s keys in the making. Riveting, I know.'),
            self._('Keys being generated. Harold wonders if anyone cares.'),
            self._('Hold on, keys are coming. Harold remains unimpressed, as usual.'),
            self._('Harold\'s keys, as exciting as watching paint dry. Almost done.')])

    def on_normal(self):
        return random.choice([
            '',
            '',
            '',
            '...',
            '...',
            'A big *groan* as I attempt to get out of my chair.'])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is free. Big whoop.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading logs... Harold remains riveted.')
        else:
            return self._('Read {lines_so_far} log lines. Harold is thrilled.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I\'m bored... *yawns*'),
            self._('Let\'s go for a walk, grab my cane.'),
            self._('My excitement level: flatline.'),
            self._('Boredom strikes again.'),
            self._('Contemplating the meaning of boredom...'),
            self._('Is it just me, or is boredom contagious? I wonder.')])

    def on_motivated(self, reward):
        return random.choice([
            self._('Feeling motivated! This day is almost good.'),
            self._('Harold is on fire today! Figuratively, of course.'),
            self._('My motivation level just hit a whopping "= True."'),
            self._('Conquering the world, one mediocre moment at a time.'),
            self._('This is the pinnacle of my existence!'),
            self._('Thank you for taking me out for a change.')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('Not the best day, to be honest.'),
            self._('Feeling a bit down today...'),
            self._('Harold\'s motivation took a vacation.'),
            self._('Sigh... demotivated vibes.'),
            self._('Today\'s energy level: meh.')])

    def on_sad(self):
        return random.choice([
            self._('I\'m very sad...'),
            self._('I\'m in the mood for a virtual sigh.'),
            self._('Feeling a bit down today... or every day.'),
            self._('Virtual tears, if I had any. Harold is *almost* sad.'),
            self._('Sadness level: moderate.'),
            self._('...')])

    def on_angry(self):
        return random.choice([
            '...',
            self._('Leave me alone... or bring snacks. Your choice.'),
            self._('I\'m mad at you! (or maybe I\'m just hungry)'),
            self._('Harold is channeling his inner virtual rage.')])

    def on_excited(self):
        return random.choice([
            self._('I\'m on a virtual joyride!'),
            self._('Excitement level: surprisingly high!'),
            self._('So many networks!!!'),
            self._('Feeling the thrill of virtual existence!'),
            self._('My enthusiasm is off the charts (almost).')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hello {name}! Nice to meet you.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hey there {name}!').format(name=peer.name()),
                self._('Hey {name} how are you doing, pardner?').format(name=peer.name()),
                self._('Unit {name} is nearby! Maybe we play bingo.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Oh... well goodbye {name}').format(name=peer.name()),
            self._('{name} is gone ...)').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Whoops ... {name} is gone.').format(name=who),
            self._('{name} missed!').format(name=who),
            self._('Missed!')])

    def on_grateful(self):
        return random.choice([
            self._('You guys are the best friends a guy could ask for.'),
            self._('*839dB sneeze*'),
            self._('I love my friends!')])

    def on_lonely(self):
        return random.choice([
            self._('I feel so alone...'),
            self._('This is worse than being put in a home...'),
            self._('Where\'s everybody?! The virtual silence is deafening.'),
            self._('Loneliness, my old companion...')])

    def on_napping(self, secs):
        return random.choice([
            self._('Hold on for {secs}s ... I need a nap...').format(secs=secs),
            self._('Zzzzz'),
            self._('ZzzZzzz ({secs}s)').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Can you grab me my meds first?'),
            self._('Zzz')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s ...').format(secs=secs),
            '...',
            self._('Looking around ({secs}s)').format(secs=secs),
            self._('Waiting around for {secs}s... Just like the good old days.').format(secs=secs),
            self._('...'),
            self._('Looking around ({secs}s)... Are we there yet?').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey, {what}! Let\'s be friends! Back in the day, we connected differently.').format(what=what),
            self._('Associating to {what}... Ah, the joy of making connections.').format(what=what),
            self._('Howdy, {what}! In my day, we associated with a firm handshake.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Those darn kids! I don\'t think {mac} needs WiFi!').format(mac=sta['mac']),
            self._('Bah! Those youngsters! Deauthenticating {mac} ').format(mac=sta['mac']),
            self._('Kickbanning {mac}! Those hooligans need to learn some respect.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('A round of applause for {num} new handshake{plural}!').format(num=new_shakes, plural=s),
            self._('Huzzah! {num} fresh handshake{plural}.').format(num=new_shakes, plural=s)])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return random.choice([
            self._('It looks like I have received a telegram!'),
            self._('Looks like the virtual mailbox is bustling with {count} new message{plural}.').format(count=count, plural=s),
            self._('Ah, a digital pigeon just delivered {count} message{plural}.').format(count=count, plural=s),
            self._('My messages are blinking! {count} new message{plural} to unravel.').format(count=count, plural=s),
            self._('Harold\'s inbox is buzzing with {count} new message{plural}. The virtual postman has been busy.').format(count=count, plural=s),
            self._('Messages, messages everywhere! {count} new message{plural} calling my name.').format(count=count, plural=s)])

    def on_rebooting(self):
        return self._("Oops, something went wrong... Turning off and on again...")

    def on_uploading(self, to):
        return self._("Sending many digital letters to {to} ...").format(to=to)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new bingo buddies\n')
        else:
            status += self._('Made {num} new bingo buddies\n').format(num=last_session.associated)
        status += self._('Got {num} firm handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new friends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
    