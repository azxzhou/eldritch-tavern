define you = Character(_("You"))
define pld = Character(_("Paladin"))
define war = Character(_("Barbarian"))
define whm = Character(_("Cleric"))
define smn = Character(_("Mage"))
define nin = Character(_("Rogue"))
define pat = Character(_("Patron"))
define eld = Character(_("???"))

label start:
    "(Thursday evening, 596 PD. Later known as Vanquishing Day.)"
    
    pat "Hey, tavernkeep!" 
    
    "A shout from across the room jolts you back to attention." 
    
    pat "Another round of beers for us!"
    
    "You glance across your absurdly crowded tavern floor towards the source of the shout - an older-looking paladin who looks like he hasn't shaved in a week."
    
    "Given what he and everyone else are celebrating tonight, he probably hasn't. "
    
    "A wave of your hand satisfies him enough to turn right back to his rowdy teammates, and you duck back into the kitchen to see how swamped your enchanted dishwasher is. "
    
    menu:
        "Check the dishwasher ":
            jump _dishwasher

label _dishwasher:
    "So far it seems to still be chugging along."
    
    "The dirty dishes bin isn't stacked halfway to the ceiling like it was two hours ago, and there are more than enough clean beer mugs for you to quickly grab an armful and head back outside to the beer tap. "
    
    "You catch a few snatches of conversation from the adventurers sitting near the bar counter as you busy yourself pouring all the drinks. "
    
    pat "Man, I never thought that Dark Lord of all things would bring pretty much all of us adventurers together."
    pat "Oh, I'm sure half of our lot will be back to pulling each other's hair out in less than a week."
    pat "But you're right, it's nice for so many of us to celebrate together for once."
    pat "Ain't that right! Cheers to our short-lived harmony, then!"
     
    "You carefully balance the now-full beer mugs in your arms and slip out from behind the counter, making your way through the throng of customers towards the paladin's table. "
    
    menu:
        "Sorry for the wait. Here's your drinks.":
            jump _serve

label _serve:
    pld "Finally, the beer angel is here!"
    
    "The scruffy paladin roars in delight as he sees you approach." 
    
    pld " You should sit and celebrate with us for a while! This occasion is special, lemme tell ya."
    
    "One of his buddies - a tough-looking tiefling barbarian with an eyepatch and a giant axe propped against the wall behind her - notices your hesitant expression and grins at you, gesturing at a figure in sorcerer's robes slumped over at the far end of the table." 
    
    war "Penelope passed out right after we asked you for drinks." 
  
    war "She'll be fine - Eleonora cast Lesser Restoration on her, she's just dead asleep - but we'd hate for a drink to go to waste, you know?"
    
    menu:
        "\Sure, I don't see why not.":
            jump _accept_invite
        "\Thanks for the offer, but...":
            jump _decline_invite

label _accept_invite:
    "The barbarian cheers loudly at your response."
    war "The more the merrier! You deserve a break after all everyone in here has put you through at one point or another."
    
    "As everyone shuffles around to make a spot for you on the benches, a elven cleric sitting at the far end of the table raises a very obviously judgy eyebrow." 
    
    whm "Yeah, and next week you'll be back in here causing more property damage for our poor tavernkeep here. Like clockwork."
    
    war "Hey, I'm not too bad, am I? At least I pay for it afterward!"
    
    menu:
        "And without me having to ask, unlike most of your peers.":
            jump _payment

label _decline_invite:
    pld "Oh, come on. If you don't want to drink, at least sit for a few minutes."
    
    pld "I haven't seen you so much as lean against the counter the whole time I've been here, and it's well past sunset already!"
    
    you "Thanks for the concern, but I'l be fine. I worked food service back in the capital, and that was way worse than this."
    
    nin "So did I."
    
    "The dimuinitive rabbit-eared rogue pipes up from the middle of the group, idly flipping their fork in the air."
    
    nin "I would rather take on a herd of wilding beasts alone than deal with that again."
    
    "Both of you exchange a look of understanding."
    
    menu:
        "Well, I must really be getting back to it.":
            jump _get_up

label _payment:
    "The barbarian roars with laughter, downing half her mug of beer in one gulp."
    
    war "Remember what happened to ol' Artarias? He actually got arrested by the Guild after they had to step into the matter."
    
    war "You ever see that happen before?"
    
    nin "Arguably, that was partially the owner's fault." 
    
    "The dimuinitive rabbit-eared rogue pipes up from the middle of the group, idly flipping their fork in the air."
    
    nin "Great food, but didn't have the chops to be a tavernkeep here. Lots of valleyvoid folk don't realize owning a tavern here is more of a leadership position than anything."
    
    you "You're right. So don't get the impression that this chat entitles any of you to special treatment, yeah?" 
    
    "It's your turn to arch an eyebrow at the group."
    
    you "Speaking of which, I think I hear another group hollering for food back there."
    
    menu:
        "Take your leave of the group ":
            jump _get_up

label _get_up:
    whm "Ah, wait. We haven't told you the story of what happened at the Dark Lord's keep."
    
    whm "Have you heard the full recounting at all yet?"
    
    you "Just bits and pieces here and there."
    
    whm "I imagine you must be dying of curiosity, then?" 
    
    "The cleric doesn't wait for your response."
    
    whm "After Tobias' group of spies tracked the Dark Lord to their hideout - very cleverly glamoured spire right in the middle of the Greystone Plains, by the way - they put out the call to every single adventurer in the valley."
    
    whm "Gave a time and place, said to be there to fight the Dark Lord or not at all."
    
    pld "And wouldn't you know it, damn near every single one of us showed up!" 
    
    pld "Even the Guild didn't have that good of a turnout when building this damn place!"
    
    menu:
        "What happened next?":
            jump _continue

label _continue:
    war "Well, we definitely don't know the ins and outs of it all. There had to be several hundred of us in there, and the Dark Lord was surrounded by at least ten adventurer crews our size or bigger."
    
    war "It was definitely a fierce battle, that's for sure."
    
    nin "Something felt off about the whole thing, though." 
    
    "You strain to hear their next words above the general din of the room." 
    
    nin "They didn't fight like any other ego-bloated person I've taken down. It seemed more like they were fighting to... protect someone."
    
    whm "Protect their stranglehold over the land, more like. They've been sucking the life out of the earth the whole time if the mana levels in the Greystone Plains are any indication."
    
    nin "But then why were their last words an apology?"
    
    pld "I thought they were 'I'm happy'."
    
    war "And I didn't hear anything at all! I guess we'll never be sure."
    
    menu:
        "Thanks for telling me the story. I really should be getting back to work.":
            jump _leave

label _leave:
    "The group waves as you head back to the bar counter, and the fanciful story quickly slips from your mind as you are once again swamped with food and drink orders. "
    
    "Several hours later, you feel your thoughts beginning to fray at the seams. A good chunk of your customers have already filtered out, but there are still three or four tables who seem intent on permanently moving into your tavern. "
    
    "You're not sure what would be best - standing on a chair and yelling at them to leave, or start aggresively closing up shop around them. You can never tell what will work on adventurers. "
    
    menu:
        "Yell":
            jump yell
        "Close":
            jump close

label yell:
    "No one notices you laying a spare plank down on your bar counter and clambering onto the surface, but everyone starts paying attention after you start shouting. "
    
    you "THE TAVERN IS NOW CLOSED. GET OUT OF HERE, I'M FUCKING TIRED."
    
    "Surprisingly, this proves to be very effective. The few people who haven't settled their tabs with you quickly do so, and within five minutes everyone is out of the place. "
    
    jump _continue_closing_up_shop

label close:
    "Most of the groups get the message once you start putting the chairs and benches on top of the tables, but it takes you treating the last group as permanent fixtures in your tavern and spraying cleaner on them to get them to leave. "
    
    jump _continue_closing_up_shop

label _continue_closing_up_shop:
    "After putting all the leftovers in the icebox, setting the cleaner runeba loose on the tavern floor, and loading up the magicked dishwasher with all the dirty dishes, you're ready to finally head upstairs and collapse into bed. "
    
    "Something odd tugs at the back of your mind as you begin to climb the stairs." 
    
    "You... forgot something at the bar? Yes, you definitely did."
    
    "Best to go back for it now. "
    
    jump go_back_to_the_bar_counter

label go_back_to_the_bar_counter:
    "You scour the bar thoroughly, even peeking behind the barrels of beer under the counter, but can't seem to find what you left behind."
    
    "What was it you were looking for, anyway? "
    
    you "Whatever. That's a problem for tomorrow."
    
    "You stand back up only to be met with a strange shadowy figure that quickly consumes your vision. "
    
    menu:
        "L̴̫̬̥͌͘o̷̗͈͗o̶̩̅͝k̵̜̚ ̴͈͆́͘ͅå̶͔w̷̹̝͂͑ǎ̴̤ÿ̸͉̩́̋":
            jump _stare
        "S̷̳̍t̸͍̚ą̴͝r̸̢͊ḛ̷̓":
            jump _stare

label _stare:
    eld "Where are you?" 
    
    "You hear a sad, pitiful voice crying inside your head."
    
    eld "Where did you go?"
    
    "You try to tear your gaze away from the shadowy figure."
    
    "You can't see properly. Shadowy tendrils start to creep into your vision. "
    
    "You have to stop staring."
    
    menu:
        "S̶̲̕t̶̠́â̶͚r̴̭͆e̸̦̕ ̴̕͜s̶̳̃t̵͙́ȃ̶̱r̶̦̕e̸͓̓ ̷͆ͅṡ̷̬t̷̨̉a̸̛ͅr̷̳̈́e̴͈̔ ̵͉́s̵͇̈́t̷̛͎a̸̲̋r̶͇̈́e̵̤͊ ̷̣̍ŝ̴̻t̴͕͛ȁ̸̯ŕ̴̫e̷̡̕ ̷̏ͅs̵̳̿t̸̥͐ä̵̫r̸͕̽e̵̖̿ ̴͖̀s̴̜̉t̶̯̔ ":
            jump _keep_staring

label _keep_staring:
    "You have to stop."
    
    "You can't stop."
    
    "You have to stop."
    
    "You can't stop."
    
    "Where did they go? Why aren't they here?"
    
    "You're scared. You're scared. You're -"
    
    "A loud crash from somewhere in the distance jolts you back to reality. The pressure on your skull suddenly lifts. "
    
    "You blink in the sudden brightness of the tavern, jerking your head towards the source of the sound to see the rabbit-eared rogue from earlier staring at you in surprise. "
    
    nin "Sorry, I forgot something in here. I didn't see you, but the door was unlocked."
    
    nin "Um..." 
    
    "They trail off awkwardly."
    
    nin "I'll go. Good night."
    
    "They scurry out the door, and you walk over to lock it, still a bit shaken."
    
    "You must be more tired than you thought. Maybe you shouldn't open for business tomorrow. "
    
    menu:
        "Go to bed ":
            jump _next_morning

label _next_morning:
    "You don't sleep well that night."
    
    "The shadowy figure drifts in and out of your dreams, crying out for someone."
    
    "You wake to your escaper alarm beeping angrily at you from across the room. "
    
    you "Yes, yes, I'm up."
    
    "You sigh, forcing yourself out of bed and switching the alarm off. The escaper beeps grumpily and floats back over to your nightstand."
    
    "Even if you don't plan to be open for business, you still have errands to run."
    
    "So with some effort, you drag yourself through your morning routine, heading back downstairs."
    
    "You noticed you were running low on evoker spice last night (the evoker stew you put on the menu last week has proven to be surprisingly popular)."
    
    "You also need to figure out what to do with the massive amount of chicken mushrooms that grew in your storeroom after a stray spell missed its intended target during a tavern brawl last week."
    
    "Speaking of which, the Guild is bound to have released a new list of approved foodstuffs already, since it's already well past noon - "
    
    you "?!"
    
    "You come to a sudden stop as you realize that the rabbit-eared rogue from yesterday is casually standing in the middle of your tavern. Didn't you lock the door last night?"
    
    "Before you can react, the rogue surges forward and grabs your shoulders. "
    
    nin "You saw it too, didn't you? Last night, after everyone left."
    
    nin "The shadowy figure. The voice in your head. Calling out for someone."

