from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("πΌπ'ππΌππΌπππΌππΌππππ")


@register(outgoing=True, pattern='^F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("πΌπππΌππππππππΌπ....")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ππΌ'πΌππΌππππππΌππΌπ")


@register(outgoing=True, pattern='^.F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("πΌπΏπΌ ππππΌπππΌπ πΌππΌπππ ππΌππΌπ")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππππππ πππΎππ ππΌ πππ πππππΌπ ππΌπππππ**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πΎπππππ πΌππΌπ πΌππππππ**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**π½πΌπΎππ π½ππ πΏπΌπ!!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**π½πππππππΌπ πΎππΌππ**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππΌππΏπ πππ**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππΌ ππ πππ ππππΌ πππ ππΌπππΌπ πΏππ, π½ππππ**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππΌπ π½ππ ππ πΌππ, ππππ!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππππ ππ π½ππππ? πππΌ π½ππππ. . . .!!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππΌπ πππππΌπ ππΌππΌ ππππππΌπ, πππππ ππ!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππΌππ ππΌπππ π½πΌππππΌπ ππΌππΌ ππππππΌπ ππππΏπππ ππ πππΌ πππ ππΌππ ππππ, ππππΏπππ ππ ππππππ ππΌπ ππ ππππ π½π**")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππΏπ π½ππ½πΌπππ πΌπ πππ ππΎ, ππΌ ππππΌ π½πππ**")


@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππ  πͺπ¨ππ π¨π€π¨π€ππ£ π£πππ¬ππ§-π£πππ¬ππ§ πππ π ππ‘π€ π’ππ£π©ππ‘ π‘πͺ πππ π’π¨π π₯ππ©πͺπ£πππ£...**")


@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πΎππππ π½πΌπΏππ ππΌππ ππππππΎπ**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππΌπππΌπ ππΌππ π½ππ ππππ, πΌππΌπ ππ πππππππ, πΎππππππ**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππ?πΈ πΈπ²πΏπ²π» πΉπ π―π²π΄πΆππ ππΌπΉπΌπΉ, π‘πΌπ΅ πΊπ?πΈ πΉπ π±πΆπ΄π?π»π΄π―π?π»π΄ π±π¬ πΌπΏπ»π΄ π°ππΊπ? π±πΆπ―π?ππ?πΏ πΆπ»π±πΌπΊπΆπ² π­ π―ππ»π΄πΈππ π±πΌπ?π»π΄ π―π²π΄πΌπΌπΌ**")

CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Untuk mengontoli mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\nM\
\nUsage: Tersedak meledek.\
\n\nY\
\nUsage: Buat yang males adu bacot.\
\n\nC\
\nUsage: Buat menghujat.\
\n\nS\
\nUsage: Haha sokap."
})

CMD_HELP.update({
    "salam2":
    "V\
\nUsage: Hujat Orang caper.\
\n\nJ\
\nUsage: Hujat Jamet.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Ngatain Grup wkwk.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Coba dewek ah.\
\n\nF\
\nUsage: Istighfar.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
})
