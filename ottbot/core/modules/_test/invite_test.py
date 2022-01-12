import tanjun

from ottbot.core.utils.funcs import build_loaders
from ottbot.core.bot import OttBot

component, load_component, unload_component = build_loaders()


@component.with_slash_command
@tanjun.as_slash_command("testinvite", "Invite Test")
async def cmd_testinvite(ctx: tanjun.abc.SlashContext, bot: OttBot = tanjun.injected(type=OttBot)) -> None:
    if ctx.guild_id is None:
        return

    invites = await bot.rest.fetch_guild_invites(ctx.guild_id)
    for invite in invites:
        print(invite.inviter, invite.uses)
    await ctx.respond("...")