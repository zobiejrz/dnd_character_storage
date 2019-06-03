using System;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Generic;

using Discord;
using Discord.Commands;

namespace dnd_character_storage.Core.Command
{
    
    public class HelloWorld : ModuleBase<SocketCommandContext>
    {
        [Command("say"), Summary("HelloWorld")]
        public async Task hello([Remainder] string text)
        {
            await Context.Message.DeleteAsync();
            await Context.Channel.SendMessageAsync (text);
        }
        [Command("ask")]
        public async Task ask([Remainder] string text)
        {
            if (text.ToLower() == "what is the primary goal") await ReplyAsync ( $"{Context.User.Mention} to win the game." );
        }

    }
}