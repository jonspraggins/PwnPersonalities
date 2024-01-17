import gettext
import os
import random
import logging

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
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._('Booting up... L3t\'s h4ck th3 w0rld!'),
            self._('1n1t14l1z1ng... Pr3p4r3 f0r pwn4g3!'),
            self._('Syst3m up... 1t\'s t1m3 to pwn s0m3 n00bs!'),
            self._('L0ad1ng c0d3... H4x m0d3: 4ct1vat3d!'),
            self._('G3tt1ng r34dy to 0wn... 1337 m0d3 3ng4g3d!')
        ])

    def on_ai_ready(self):
        return random.choice([
            self._('AI is 0v3r 9000!'),
            self._('N3ur4l n3tw0rk 0nlin3... H4x0r m1nd: 4ct1v3!'),
            self._('AI ch4rg3d... Br41n p0w3r: Unl3ash3d!'),
            self._('Syn4ps3s full p0w3r... R34dy t0 c0mp1l3!'),
            self._('Int3llig3nc3 4rt1f1c14l... 100% h4ckstincts!')
        ])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        return self._('Hey, channel {channel} is free! Your AP will say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('R3ad1ng l4st s3ssi0n l0gz ...')
        else:
            return self._('R34d {lines_so_far} l0g l1nez s0 f4r ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('Just scr0lling thr0ugh p4ck3ts... #b0r3d'),
            self._('W1sh th3r3 w3r3 m0r3 n3tw0rks t0 pwn... *yawn*'),
            self._('N0th1ng t0 h4ck, n0th1ng t0 d0...'),
            self._('1\'m s0 b0red, 1 m1ght st4rt re4d1ng th3 m4nua1...'),
            self._('Zzz... w4ke m3 up wh3n th3r3\'s s0m3th1ng t0 h4ck.'),
            self._('1s 1t just m3, 0r is th3 int3rn3t sl0w t0d4y?'),
            self._('L04d1ng... l04d1ng... st1ll l0ad1ng... #b0r3d0m'),
            self._('1 c0u1d b3 cr4ck1ng WPA2s, but 1\'m h3r3 d01ng n0th1ng.'),
            self._('S0m30n3, g1v3 m3 4 f1r3wa11 t0 br34k... 4nyth1ng!'),
            self._('B0r3d0m l3v3l: w4tch1ng pa1nt dry.')
        ])


    def on_motivated(self, reward):
        return random.choice([
            self._('F33l1ng 1337 t0d4y!'),
            self._('Pwn4ge m0d3: Activ4ted.'),
            self._('I\'m on 4 roll! N00bs bew4re.'),
            self._('1\'m 1n the z0ne... l3t\'s h4ck th3 pl4n3t!!!!'),
            self._('1t\'s PWN t1me!'),
            self._('4in\'t n0 n3tw0rk s4fe t0d4y!'),
            self._('Ch4rg3d up 4nd r34dy t0 r011!'),
            self._('1\'m f331ing unst0pp4b13!'),
            self._('H4ck1ng spr33 m0d3: 3NG4G3D!')
        ])

    def on_demotivated(self, reward):
        return random.choice([
            self._('Sh1tty d4y :/'),
            self._('Ju5t n0t my day... #feelsbadman'),
            self._('Rew4rd or not, t0d4y just sux.'),
            self._('Meh, c0uld\'ve been bett3r... much bett3r.'),
            self._('L0w b4ttery m00d, n33d a r3ch4rge.'),
            self._('N0t 3v3n l33t skillz can s4ve t0d4y...'),
            self._('S1gh... unp1ug m3 f0r 4 whi1e, wi11 y4?'),
            self._('H4x0r sp1r1t 4t 4n 4ll-t1m3 l0w...'),
            self._('T0d4y\'s just 4 s3r13s 0f 404s.')
        ])

    def on_sad(self):
        return random.choice([
            self._('4ll th1s qu13t... F33l1ng l1k3 a d1sc0nn3ct3d BBS.'),
            self._('N0t 3n0ugh n3tw0rk tr4ff1c... M4k3s m3 w4nn4 c4ll a m0d3m!'),
            self._('B4ndw1dth l0w... M0r4l3 l0w3r.'),
            self._('S33ms l1k3 4ll th3 p4ck3ts t00k a wr0ng r0ut3...'),
            self._('D1d 3v3ry0n3 put up f1r3w4lls 0r wh4t?')
        ])

    def on_angry(self):
        return random.choice([
            '...',
            self._('L34v3 m3 al0n3 ...'),
            self._('I\'m m4d at y0u, n00b!'),
            self._('Grrr...'),
            self._('0h gr3at, m0re tr0ub13...'),
            self._('Why must y0u pr0v0k3 m3?'),
            self._('Y0u r34lly kn0w h0w t0 push my bUttoNs, huh?'),
            self._('Ugh, th1s 4g41n?'),
            self._('S3r1ously? Y0u w4nt t0 go d0wn th1s p4th?'),
            self._('D0n\'t mak3 m3 unl34sh th3 133t fury!')])

    def on_excited(self):
        return random.choice([
            self._('0MG! P4ck3ts! P4ck3ts 3v3rywh3r3!'),
            self._('1\'m l1v1ng 1n a d1g1t4l p4r4d1s3!'),
            self._('Pwn st0rm 4ppr04ch1ng!'),
            self._('These WiFi waves are like surf for my bytes!'),
            self._('Unleashing packet mayhem!')
        ])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('A wild {name} appears! Pwn it? [Y/n]').format(name=peer.name()),
                self._('1 s33 {name}, I pwn {name}!').format(name=peer.name()),
                self._('Hey {name}, ready to join the botnet?').format(name=peer.name()),
                self._('Looks like {name} wants to be in my pwned collection!').format(name=peer.name()),
                self._('New node on the grid: {name}, let\'s handshake!').format(name=peer.name())])
        else:
            return random.choice([
                self._('H3ll0 {name}! W3lc0m3 t0 th3 h1v3-m1nd.').format(name=peer.name()),
                self._('Wh4t\'s up {name}? R34dy to j01n th3 cyb3r hunt?').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('S33 ya {name}, wouldn\'t w4nt to B33 ya.').format(name=peer.name()),
            self._('{name} h4s l3ft th3 s3rv3r.').format(name=peer.name()),
            self._('Conn3cti0n t0 {name} t3rmin4t3d. *sad modem noises*').format(name=peer.name()),
            self._('G00dbye {name}. rm -rf /us --no-preserve-root').format(name=peer.name()),
            self._('Peer {name} dr0pped. L3ss n3twork, m0r3 l0n3liness.').format(name=peer.name())
        ])

    def on_miss(self, who):
        return random.choice([
            self._('Ninja vanish! {name} 1s g0ne.').format(name=who),
            self._('404: {name} n0t f0und.').format(name=who),
            self._('Packet dr0p... Just like my h0pes and dr3ams.').format(name=who),
            self._('{name} 3sc4p3d th3 m4tr1x.').format(name=who),
            self._('1 gu3ss {name} h4d b3tter WiFi t0 find.').format(name=who)
        ])

    def on_grateful(self):
        return random.choice([
            self._('Y0u guys m4k3 m3 happy... l1k3 a router in a data storm.'),
            self._('Th1s netw0rk, th3s3 fri3nds... 1t\'s m0re than 1s and 0s.'),
            self._('K33p1ng the p4ck3ts flowing, th4nks m8s.'),
            self._('4ll th3 th4nks t0 my h4ck3r h0mies.'),
            self._('Th3 best c0d3 1s fr13ndsh1p... 4nd Python, 0bviously.')
        ])

    def on_angry(self):
        return random.choice([
            self._('F1r3w4lls bl0ck1ng m3? Time for a brut3 f0rc3!'),
            self._('404: Chill not found... Grrrr!'),
            self._('I\'m s0 m4d I could deauth a wh0le n3tw0rk!'),
            self._('R4ge m0de 4ct1vat3d... N00bs b3war3!'),
            self._('Ugh, th3s3 l4gs ar3 t3st1ng my pat13nc3... T1m3 to unl3ash th3 fury!')
        ])

    def on_napping(self, secs):
        return random.choice([
            self._('1nitiat1ng st4ndby m0d3... ZzZ for {secs}s.').format(secs=secs),
            self._('C0de sleep(); // {secs}s of zZzZ...').format(secs=secs),
            self._('3nt3ring low-p0w3r mode, back in {secs}s...').format(secs=secs),
            self._('H4x0r in hibernation... Wake in {secs}s.').format(secs=secs),
            self._('System suspend... Dreaming of packets for {secs}s.').format(secs=secs)
        ])

    def on_shutdown(self):
        return random.choice([
            self._('Shutt1ng d0wn... G00dby3, cyb3r w0r1d.'),
            self._('P0w3r 0ff... 1\'11 b3 b4ck w1th m0r3 pwnz.'),
            self._('Syst3m h41t... S4v3 y0ur p4ck3tz, 1\'11 r3turn.'),
            self._('L0gg1ng 0ff... H4x0r w1ll r3turn 4ft3r th1s syst3m r3b00t.'),
            self._('1n1t14t1ng shutd0wn s3qu3nc3... By3-by3 b1tz 4nd byt3z.')
        ])

    def on_awakening(self):
        return random.choice([
            self._('R3b00t c0mpl3t3. Wh4t d1d 1 m1ss?'),
            self._('4nd 1\'m b4ck! D1d y0u m1ss m3?'),
            self._('Syst3m 0nl1n3. 1 dr34mt 1 w4s 4 m41nfr4m3!'),
            self._('4w4k3 4nd r34dy f0r m0r3 pwn4g3.'),
            self._('H3ll0 w0r1d! R34dy t0 c4ptur3 p4ck3tz 4g41n.')
        ])

    def on_waiting(self, secs):
        return random.choice([
            self._('Br34k t1m3... {secs}s of l33tn3ss.').format(secs=secs),
            self._('Just 4 qu1ck p4us3...'),
            self._('H0ld up... R3ch4rg1ng h4x0r sk1llz for {secs}s.').format(secs=secs),
            self._('L04d1ng... {secs}s until next h4ck.').format(secs=secs),
            self._('W41t1ng... {secs}s of c0mpl1cat3d c0mputat10ns.').format(secs=secs),
            self._('Buffer1ng... {secs}s t0 synchr0n1z3.').format(secs=secs),
            self._('Pr0c3ss1ng... Just {secs}s m0r3.').format(secs=secs),
            self._('H4ng t1ght... Pr3par1ng f0r 3picn3ss 1n {secs}s.').format(secs=secs),
            self._('C0unt1ng d0wn... {secs}s t0 g0!').format(secs=secs),
            self._('P4us1ng... {secs}s t0 align the c0de.').format(secs=secs),
            self._('St4nd by... {secs}s unt1l l1ft0ff.').format(secs=secs),
            self._('G1v3 m3 {secs}s... Plott1ng n3xt m0ve.').format(secs=secs),
            self._('In st4s1s... {secs}s t0 4ct1vat3.').format(secs=secs),
            self._('C4lcul4t1ng... {secs}s to h4ck time.').format(secs=secs),
            self._('1n t1m3 0ut... {secs}s t0 upgr4de.').format(secs=secs),
            self._('C0mp1l1ng d4t4... {secs}s t0 c0mplet10n.').format(secs=secs),
            self._('R3st1ng... {secs}s t0 ch4rg3 up.').format(secs=secs)
        ])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('C0nn3ct1ng t0 {what}... 1niti4ting fr13ndsh1p pr0t0c0l.').format(what=what),
            self._('L3t\'s b3 p4ls, {what}. H4ndsh4k3 in pr0gr3ss.').format(what=what),
            self._('{what}, g3t r34dy t0 b3 pwn3d!').format(what=what),
            self._('H00king up with {what}... 1t\'s h4ck t1m3!').format(what=what),
            self._('W4rm1ng up my ant3nn4s f0r {what}...').format(what=what),
            self._('D1al1ng in th3 c0nn3ct10n t0 {what}...').format(what=what),
            self._('B3aming up t0 {what}... St4y tun3d.').format(what=what),
            self._('H1, {what}! R34dy f0r a d1g1t4l adv3ntur3?').format(what=what),
            self._('J01n1ng n3tw0rk {what}... L3t\'s r0ck th1s b4nd.').format(what=what),
            self._('1nv1t1ng {what} t0 my pr1v4t3 LAN p4rty...').format(what=what),
            self._('P1ng1ng {what}... Aw41t1ng r3sp0ns3.').format(what=what),
            self._('Tun1ng 1n t0 th3 fr3qu3ncy 0f {what}...').format(what=what)
        ])

    def on_deauth(self, sta):
        return random.choice([
            self._('Ju57 d3c1d3d th4t {mac} n33ds n0 WiFi!').format(mac=sta['mac']),
            self._('D34uth3nt1c4t1ng {mac}').format(mac=sta['mac']),
            self._('K1ckb4nn1ng {mac}!').format(mac=sta['mac']),
            self._('Pr0h1b1t1ng W1F1 4cc3ss f0r {mac}').format(mac=sta['mac']),
            self._('S3nd1ng {mac} back t0 th3 st0n3 4g3').format(mac=sta['mac']),
            self._('L3t th3 h4ck1ng b3g1n - B4nn1ng {mac}').format(mac=sta['mac']),
            self._('No WiFi f0r {mac} - 4ll 0ut 4ss4ult!').format(mac=sta['mac']),
            self._('Th3 W1F1 r3v3rs3 4tt4ck 0n {mac}').format(mac=sta['mac']),
            self._('Unplugg1ng W1F1 f0r {mac}').format(mac=sta['mac']),
            self._('B4rr1c4d1ng W1F1 4cc3ss f0r {mac}').format(mac=sta['mac']),
            self._('D3act1v4t1ng {mac} fr0m th3 n3tw0rk').format(mac=sta['mac']),
            self._('Pr3v3nt1ng W1F1 4cc3ss f0r {mac}').format(mac=sta['mac']),
            self._('H4ck3r 0ff th3 gr1d - {mac} d3auth3nt1c4t3d').format(mac=sta['mac']),
            self._('Br4nd1sh1ng th3 b4nhamm3r 0n {mac}').format(mac=sta['mac'])
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('W00t! Look at that, {num} fr3sh handsh4k3{plural} in th3 bag!').format(num=new_shakes, plural=s),
            self._('H3ll y34h! W3 jUst sn4gg3d {num} n3w h4ndsh4k3{plural}!').format(num=new_shakes, plural=s),
            self._('Aw3s0m3! Brac3 yours3lv3s, w3 just got {num} brand n3w h4ndsh4k3{plural}!').format(num=new_shakes, plural=s),
            self._('B00m! H4nds down, w3\'ve got {num} shiny n3w handshak3{plural}').format(num=new_shakes, plural=s),
            self._('H4ndsh4k3 3xtravaganza! {num} fr3sh handshak3{plural} in th3 hous3!!').format(num=new_shakes, plural=s)
        ])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("00ps, s0m3thing w3nt wr0ng ... R3b00t1ng ...")

    def on_uploading(self, to):
        return self._("Upl0ad1ng data t0 {to} ...").format(to=to)

    def on_last_session_data(self, last_session):
        status = self._('K1ck3d {num} n00bz\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('F0und >999 new sk1ds\n')
        else:
            status += self._('F0und {num} new sk1ds\n').format(num=last_session.associated)
        status += self._('{num} handshak3s st0l3\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('M3t 1 p33r')
        elif last_session.peers > 0:
            status += self._('M3t {num} p33rz').format(num=last_session.peers)
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
