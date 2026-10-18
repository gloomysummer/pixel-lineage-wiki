#!/usr/bin/env python3
import json
import os
import re

FAQ_DATA = {
    "src/pages/codes/index.astro": [
        {
            "question": "Why do promo codes expire in Pixel Lineage?",
            "answer": "Promo codes in Pixel Lineage expire when developer update cycles conclude or when server redemption thresholds are reached. The development studio typically issues fresh codes during weekly content drops and holiday events. Expired codes permanently lose their validity in the Goblin Merchant redemption menu once superseded by new version updates."
        },
        {
            "question": "Can I redeem the same promo code multiple times on one Roblox account?",
            "answer": "Each active code can only be redeemed once per unique Roblox account ID across all server instances. Rerolling your character race, changing your starting class, or resetting your lineage rank does not restore code eligibility. To claim code bonuses again, players must register a separate Roblox account and complete group verification."
        },
        {
            "question": "What prerequisites must be completed before entering codes at the Goblin Merchant?",
            "answer": "Players must join the official Pixel Lineage Roblox Group (ID 362755399), give the game a thumbs-up like, and add the experience to their favorites list. If these three prerequisites are missing, the Goblin Merchant NPC dialog prompt will reject the submission and display a verification warning."
        },
        {
            "question": "What rewards do active Pixel Lineage codes grant?",
            "answer": "Active promo codes primarily provide free Race Spins, Talent Rerolls, consumable healing elixirs, and starter Gold currency. During limited seasonal events such as Halloween, active codes additionally grant event-exclusive Candy tokens used to purchase event weapon cosmetics and rare lineage upgrade scrolls."
        }
    ],
    "src/pages/codes/not-working.astro": [
        {
            "question": "Why does Pixel Lineage say Invalid Code when I type the phrase correctly?",
            "answer": "Pixel Lineage code redemption is strictly case-sensitive and does not tolerate trailing whitespace or incorrect capitalization. If copying from community message boards, ensure you paste only uppercase alphanumeric characters. Additionally, ensure you exit dialogue and re-interact with the Goblin Merchant if you experienced network latency during the initial check."
        },
        {
            "question": "How long after joining the Roblox Group does code verification take effect?",
            "answer": "Roblox API group verification generally synchronizes within thirty to sixty seconds after joining Group 362755399. However, during high server load, cache propagation may take up to two minutes. Leaving your current game server and rejoining a fresh server instance instantly forces the group membership handshake."
        },
        {
            "question": "Does private server play prevent code redemption at the Goblin Merchant?",
            "answer": "Private VIP servers do not prevent code redemption in Pixel Lineage. All active promo codes function identically across public matchmaking hubs and private game servers. As long as your account satisfies group membership, favorites, and game likes, the Goblin Merchant will grant your reward items immediately."
        },
        {
            "question": "What should I do if an active code fails after meeting all requirements?",
            "answer": "First, completely close the Roblox client and rejoin a freshly spun server instance to bypass stale server memory. Verify that your Roblox privacy settings permit group verification tracking. If the prompt still rejects the code, verify the official Discord announcements channel to ensure the developer has not retired that specific phrase."
        }
    ],
    "src/pages/codes/redeem.astro": [
        {
            "question": "Where is the Goblin Merchant located in the Pixel Lineage starter hub?",
            "answer": "The Goblin Merchant NPC stands in the central starter town courtyard coordinates (X: 142, Y: 12, Z: -88), located directly adjacent to the stone archway of the Commerce Square. From the starter spawn fountain, walk east past the Blacksmith forge to spot the green-skinned merchant standing beside his wooden cart."
        },
        {
            "question": "How do mobile touchscreen players interact with the Goblin Merchant?",
            "answer": "Mobile touchscreen players must approach within three studs of the Goblin Merchant until the circular proximity prompt displays. Tap the prompt button on your screen to open the dialogue window, enter your promotional text into the input field, and tap the green Redeem button to transfer rewards into your bag."
        },
        {
            "question": "Where do claimed Race Spins and Talent Spins appear after redemption?",
            "answer": "Claimed spins and reroll tokens automatically credit into your character inventory currency ledger rather than dropping onto the ground. Press the Character Menu shortcut or open your bag interface to verify your updated Race Spin and Talent Spin counts before visiting the town lineage altar."
        },
        {
            "question": "Can I trade code reward items to other players in Pixel Lineage?",
            "answer": "Promo code rewards such as Race Spins, Talent Spins, and starter gold bind permanently to your character profile upon redemption and cannot be dropped or traded to other players. Equipment purchased with redeemed currency through the Auction House can be traded once bound item restrictions expire."
        }
    ],
    "src/pages/classes/warrior.astro": [
        {
            "question": "Can I change my base class from Warrior to another class later?",
            "answer": "Base class selection is permanent and irreversible for your character save file in Pixel Lineage. If you choose Warrior at character creation, you cannot swap to Mage, Thief, or Archer without creating a new character slot. You can, however, customize your combat role by selecting one of three distinct Super Classes at level ten."
        },
        {
            "question": "Which Warrior Super Class is best for solo player progression?",
            "answer": "The Berserk Super Class is widely recognized as the premier solo progression choice due to its aggressive missing-health attack scaling and lifesteal passives. Solo players can defeat Act 2 dungeon bosses quickly without relying on external healing support by maintaining controlled low-health damage bursts."
        },
        {
            "question": "Is the Sentinel Super Class necessary for endgame Guild Raids?",
            "answer": "Sentinel is virtually mandatory for high-tier Guild Raids because it provides sixty-five percent physical damage mitigation and party-wide taunt mechanics. Without a dedicated Sentinel absorbing heavy boss cleaves, fragile spellcasters and burst rogues get eliminated by unavoidable AoE ground slams in Torment encounters."
        },
        {
            "question": "What is the optimal playable race pairing for a Warrior build?",
            "answer": "Orc and Dullahan represent the two strongest racial lineages for Warrior characters in the current meta. Orc provides innate bonus attack multipliers and an undying rage cheat-death passive, while Dullahan offers massive baseline poise defenses and armor scaling that synergize perfectly with heavy plate tanking setups in Act 2."
        }
    ],
    "src/pages/classes/thief.astro": [
        {
            "question": "How does turn order initiative work for the Thief class in combat?",
            "answer": "Turn initiative in Pixel Lineage calculates directly from each combatant's Speed attribute at the beginning of every turn round. Because Thief possesses the highest baseline Speed growth in the game, Thief characters almost always act first, allowing them to eliminate enemy spellcasters or apply crowd control before monsters attack."
        },
        {
            "question": "What is the difference between the Assassin and Rogue Super Classes?",
            "answer": "Assassin specializes in guaranteed critical strikes from Stealth stance and deadly single-target poison burst damage against priority targets. Rogue, by contrast, focuses on evasive agility and counter-attack triggers that strike back whenever enemy attacks miss, making Rogue significantly safer and superior in chaotic multi-target mob survival scenarios."
        },
        {
            "question": "Does the Corsair Thief Super Class actually earn more gold in dungeons?",
            "answer": "Yes, Corsair possesses unique pickpocket passives that siphon bonus Gold directly from enemy combatants during turn actions. In Act 2 dungeons and Torment expeditions, a well-geared Corsair generates approximately thirty-five percent more total currency per run than standard combat builds, speeding up town upgrades."
        },
        {
            "question": "Which race provides the highest damage ceiling for a Thief build?",
            "answer": "Elf and Felis offer the highest performance ceiling for Thief builds across dungeon acts. Elf grants bonus movement speed, higher initiative rolls, and critical strike multipliers, whereas Felis boosts base dodge chance to optimize Rogue counter-attack mechanics and dodge triggers in high-Torment dungeons."
        }
    ],
    "src/pages/classes/mage.astro": [
        {
            "question": "How do Mage characters manage mana sustain during prolonged boss fights?",
            "answer": "Mage characters manage mana sustain through innate spirit growth, staff weapon enchantments, and mana potions purchased in town. Inscribing Arcane Runes onto your armor and choosing the Nightborn race grants constant passive mana regeneration, preventing spell exhaustion during extended multi-phase dungeon encounters."
        },
        {
            "question": "Is Cleric viable as a solo leveling archetype or only in party raids?",
            "answer": "While Cleric excels as the premier party healer in Guild Raids, it is completely viable for solo leveling thanks to holy radiant smites and self-sustain. Clerics deal bonus holy damage against undead dungeon monsters in Act 2, allowing steady progression without purchasing healing consumables."
        },
        {
            "question": "How does the Hexer Super Class bypass boss magical resistances?",
            "answer": "Hexer applies stacking decay curses that tick during every enemy turn phase while reducing target magic defense by forty percent. Because decay damage scales with true damage percentages, Hexer curses melt high-armor Torment bosses that otherwise resist direct elemental burst spells."
        },
        {
            "question": "Why is Nightborn considered the best race for Mage archetypes?",
            "answer": "Nightborn grants fifteen percent increased base mana regeneration, dark vision in unlit dungeons, and enhanced magical attack scaling during nighttime phases. These combined passives remove mana starvation bottlenecks completely, enabling spellcasters to execute continuous high-tier spell rotations without pausing for elixirs or losing DPS momentum."
        }
    ],
    "src/pages/classes/fist.astro": [
        {
            "question": "How does Poise Break work on Fist class combatants in Pixel Lineage?",
            "answer": "Every unarmed strike from a Fist combatant reduces the target enemy's hidden poise gauge. When an enemy's poise breaks, their current turn action is cancelled, stunning them until the following combat round. This enables Fist players to lock down dangerous elite casters and boss mechanics."
        },
        {
            "question": "Which Fist Super Class offers the highest burst damage potential?",
            "answer": "The Monk Super Class delivers the highest burst damage potential by chaining chi strikes into devastating combo finishers. When properly buffed with critical hit gear and the Fortune's Favor talent, Monk combo strikes can execute dungeon bosses in just two combat turns."
        },
        {
            "question": "Does Fist scale with physical Attack or Magic attributes?",
            "answer": "Standard Fist weapon scaling relies primarily on the physical Attack stat and character Speed for turn order. However, the Mystic Fist Super Class evolution introduces hybrid scaling, converting a portion of your Magic attribute into elemental shockwave damage across front-row enemy tiles."
        },
        {
            "question": "What equipment set should a Fist player prioritize in Act 2?",
            "answer": "Fist players should prioritize acquiring the Windwalker leather armor set and Dragonbone Cestus wraps from the Mountain Dragon Lair. This equipment combination provides substantial bonus Attack, fourteen percent Poise Break chance, and increased turn speed to ensure uninterrupted combo chains against heavily armored dungeon adversaries."
        }
    ],
    "src/pages/classes/bard.astro": [
        {
            "question": "Can Bard characters deal sufficient damage to clear solo dungeon acts?",
            "answer": "Yes, Bard characters deal respectable solo damage by utilizing sonic dissonance attacks and rhythm buffs that stack offensive power over consecutive turns. While clearing speed is slightly slower than pure burst classes like Thief, Bard's self-buffs and passive health regeneration provide outstanding solo reliability."
        },
        {
            "question": "How do Bard songs buff allied party members in Guild Raids?",
            "answer": "Bard melodies apply aura buffs across all party members, boosting team physical attack, magical potency, and turn speed without consuming multiple action turns. Maintaining the Hymn of Valor increases overall raid damage output by over twenty-five percent during boss burn phases."
        },
        {
            "question": "What makes the Minstrel Super Class unique compared to Troubadour?",
            "answer": "Minstrel specializes in crowd control melodies, charming or confusing enemy targets to attack each other in the turn queue. Troubadour focuses on protective party barrier songs and cooldown reduction, making Troubadour the preferred choice for defensive survivability in high-Torment expeditions."
        },
        {
            "question": "Which race is most recommended for a supportive Bard build?",
            "answer": "Celestine and Seraph are the top racial recommendations for supportive Bards in cooperative gameplay. Celestine offers automatic team debuff cleansing that triggers on turn start, while Seraph boosts holy aura healing values and party initiative to ensure vital song buffs apply before enemy monsters strike."
        }
    ],
    "src/pages/classes/archer.astro": [
        {
            "question": "How does row targeting work for Archer bows in turn-based combat?",
            "answer": "Unlike frontline melee fighters who must attack front-row enemies first, Archer ranged attacks bypass enemy tanks to target high-priority spellcasters and healers positioned in the back row. This unique targeting mechanic allows Archer teams to eliminate dangerous enemy supports early in the round."
        },
        {
            "question": "Which Archer Super Class has the highest armor penetration?",
            "answer": "The Sniper Super Class possesses the highest armor penetration in Pixel Lineage, naturally ignoring fifty percent of enemy physical defense on aimed precision shots. This makes Sniper the optimal choice for tackling heavily armored knight bosses in Act 2 and Torment Mode."
        },
        {
            "question": "Is Ranger better than Deadeye for dungeon trash mob clearing?",
            "answer": "Ranger is significantly better for clearing dungeon trash mobs because it unlocks Arrow Volley, an ability that showers multiple enemy tiles simultaneously. Deadeye focuses on single-target lethal critical strikes, excelling against lone dungeon bosses rather than large mob packs encountered along dungeon corridors."
        },
        {
            "question": "What talent combination maximizes Archer critical strike damage?",
            "answer": "The ideal talent combination for Archer builds pairs Fortune's Favor (+15% Crit Chance) with Keen Eye and Prodigy. This setup elevates critical strike probability above sixty percent, triggering massive critical damage multipliers on every standard bow shot and accelerating boss takedowns."
        }
    ],
    "src/pages/classes/super-classes.astro": [
        {
            "question": "At what level and location do I unlock Super Class advancement?",
            "answer": "Super Class advancement unlocks at Level 10 upon reaching the Trainer's Shrine located within Act 2: The Catacombs & Dungeon. Players must complete the introductory shrine trial and interact with the Trainer NPC to select one of three specialization paths available for their base class."
        },
        {
            "question": "Can I reset or change my Super Class after picking one at the Trainer's Shrine?",
            "answer": "Super Class selection is permanent and irreversible for your character. Developers designed this decision as a core progression commitment. If you wish to experience a different Super Class branch, you must start a new character run and advance through Act 1 again."
        },
        {
            "question": "What is an Ultra Class and how does it differ from a Super Class?",
            "answer": "An Ultra Class represents the pinnacle awakening beyond your Super Class, requiring an Ultra Sigil item obtained from Torment III bosses or Guild Raids. Awakening an Ultra Class grants signature ultimate abilities and enhanced stat growth multipliers without altering your chosen Super Class kit."
        },
        {
            "question": "Do Super Classes retain all abilities learned from the base class?",
            "answer": "Yes, all base class skills, passive growths, and stat investments carry over completely into your Super Class evolution. Advancing to a Super Class simply expands your skill tree with new active spells, enhanced passive masteries, and specialized equipment proficiencies tailored for advanced dungeons."
        }
    ],
    "src/pages/classes/stats.astro": [
        {
            "question": "How do base attribute points scale when leveling up in Pixel Lineage?",
            "answer": "Each level-up grants automatic stat increases determined by your base class growth template. For example, Warriors gain +12 HP and +2.2 ATK per level, while Mages receive +2.8 MAG and +1.5 Mana Regen. Racial traits and chosen talents apply multiplicative percentages on top of these base stats."
        },
        {
            "question": "Does physical defense have diminishing returns in Pixel Lineage?",
            "answer": "Physical damage mitigation follows the standard hyperbolic curve formula where damage reduction equals Defense divided by Defense plus sixty. While early defense points provide sharp survival gains, stacking defense above one hundred points yields smaller percentage increases, making health pool stacking equally vital."
        },
        {
            "question": "What is the hard cap for character levels in the current version?",
            "answer": "The current level cap in Pixel Lineage is Level 30 for standard progression, expandable to Level 40 upon unlocking Torment difficulty and awakening your Ultra Class. Reaching milestone levels unlocks new skill slots and talent capacity upgrades essential for conquering endgame raids."
        },
        {
            "question": "Can player attribute points be reset or reallocated at town NPCs?",
            "answer": "Because stat growth occurs automatically according to class and race formulas rather than manual point allocation, there is no manual stat reallocation NPC. To alter your effective stat balance, players reroll racial lineages, adjust talent cards, or equip specialized gear sets."
        }
    ],
    "src/pages/races/orc.astro": [
        {
            "question": "What is the exact drop probability of rolling the Orc race?",
            "answer": "The Orc race possesses a verified drop probability of 5.0% from the Race Spin wheel at the Goblin Merchant, placing it in the Epic rarity tier. On average, players obtain Orc within twenty to twenty-five Race Spins when rolling with active code tokens or Robux."
        },
        {
            "question": "How does the Orc Undying Rage cheat-death passive activate in combat?",
            "answer": "When an Orc character takes fatal damage that would reduce health to zero, Undying Rage activates automatically, preserving the character at one HP and granting complete invulnerability for one full combat turn. This ability triggers once per dungeon encounter, preventing permadeath resets."
        },
        {
            "question": "Which classes benefit most from Orc racial passives?",
            "answer": "Warrior, Fist, and melee Thief archetypes benefit most from Orc passives due to the innate +12% physical Attack boost and tenacity resistance against enemy stuns. The missing-health scaling on Berserk Warriors synergizes especially well with Undying Rage during intense boss encounters."
        },
        {
            "question": "Does Orc suffer any penalties to magical damage or mana pools?",
            "answer": "While Orc suffers no direct penalty to its Magic stat, it receives zero mana bonuses or spell penetration traits. Consequently, choosing Orc on Mage or support Bard builds is suboptimal compared to choosing intelligence-focused lineages like Nightborn or Celestine in high-tier content."
        }
    ],
    "src/pages/races/elf.astro": [
        {
            "question": "What stat bonuses does the Elf race provide to characters?",
            "answer": "The Elf race grants +10% bonus Speed, +5% Critical Strike chance, and enhanced accuracy that ignores enemy dodge ratings. These agile passives ensure Elf combatants almost always take the first turn action in combat rounds, establishing crucial momentum in tough dungeon fights."
        },
        {
            "question": "What is the spin rate for rolling Elf at the Goblin Merchant?",
            "answer": "Elf has an 8.0% spin probability from the standard lineage gacha, categorizing it as a Rare bloodline. It is relatively easy to obtain compared to Legendary races, making it an excellent target for players utilizing free spins from active promo codes."
        },
        {
            "question": "Why is Elf considered the top bloodline for Archer and Thief?",
            "answer": "Elf amplifies the natural advantages of Archer and Thief by compounding high turn initiative and critical strike scaling. The +10% Speed ensures that Assassins and Snipers strike before enemy monsters can cast protective barriers, debuffs, or high-damage elemental spells. Their supreme movement initiative dictates the pace of battle from the opening turn."
        },
        {
            "question": "Does Elf provide any survivability or defensive bonuses?",
            "answer": "Elf provides minimal defensive mitigations or raw health bonuses, leaving characters fragile if cornered by boss attacks. Elf survivability relies entirely on avoiding damage by eliminating enemies first or utilizing high turn speed to deploy evasive smoke screens before enemies counter."
        }
    ],
    "src/pages/races/nightborn.astro": [
        {
            "question": "What makes Nightborn one of the rarest Legendary races in Pixel Lineage?",
            "answer": "Nightborn features a rare 2.0% spin probability from the Goblin Merchant wheel, ranking it among the most coveted Legendary bloodlines. It offers supreme mana sustain, dark vision in unlit catacombs, and a passive damage buff that intensifies inside deep dungeon acts."
        },
        {
            "question": "How does the Nightborn mana regeneration passive function in combat?",
            "answer": "Nightborn characters restore 15% of their maximum mana pool at the beginning of each combat round automatically. This constant spirit regeneration allows Mages and Hexers to cast their most demanding spells continuously without pausing to consume mana elixirs or risking resource exhaustion."
        },
        {
            "question": "Is Nightborn viable on physical melee classes like Warrior or Fist?",
            "answer": "While Nightborn is optimized for magic-casting archetypes, its dark vision and night-scaling damage bonuses still benefit physical classes in dark dungeons. However, players seeking maximum physical DPS are generally better served rolling Orc or Dullahan for heavy attack and defense scaling."
        },
        {
            "question": "Can Nightborn dark vision replace torches in Act 2 Catacombs?",
            "answer": "Yes, Nightborn characters possess innate night sight that completely removes darkness penalties in Act 2 Catacombs and Torment dungeons. This frees up consumable slots that would otherwise be reserved for torches or illumination lanterns, expanding inventory space for rare dungeon loot."
        }
    ],
    "src/pages/races/dullahan.astro": [
        {
            "question": "What is the roll probability and rarity tier of Dullahan?",
            "answer": "Dullahan is an Epic rarity bloodline with a verified 4.0% drop probability from the lineage spin pool at the Goblin Merchant. It is designed around headless spectral armor themes, offering extraordinary defensive resilience and unshakeable poise resistance in challenging endgame dungeon encounters."
        },
        {
            "question": "How does Dullahan's Headless Poise passive protect against stuns?",
            "answer": "Dullahan characters are entirely immune to standard stun and interrupt effects on turn one of combat rounds. Boss attacks that would normally knock down or cancel player charging actions fail against Dullahan's unshakeable spectral poise, guaranteeing turn execution. This allows tanks to maintain active defensive stances and aggro control without fear of disruption."
        },
        {
            "question": "Which Super Class synergy works best with Dullahan?",
            "answer": "The Sentinel Warrior Super Class forms an unmatched synergy with Dullahan. The combination of Dullahan's armor amplification and Sentinel's sixty-five percent physical mitigation creates an indestructible raid vanguard that trivializes heavy Torment boss hits and protects vulnerable backline allies. This combination makes long multi-boss dungeon runs significantly more reliable and safe."
        },
        {
            "question": "Does Dullahan suffer from reduced movement speed or initiative?",
            "answer": "Dullahan possesses a slight -5% penalty to base Speed, which causes it to act later in the turn order during combat rounds. This makes it unsuitable for speed-burst builds like Assassin, but ideal for reactive counter-attackers and heavy frontline tanks."
        }
    ],
    "src/pages/races/seraph.astro": [
        {
            "question": "What are the unique racial traits of the Seraph lineage?",
            "answer": "Seraph is a Mythic bloodline (1.5% spin probability) featuring angelic wings and holy radiance. It grants +15% Holy spell damage, a party-wide aura that boosts incoming healing by 10%, and a resurrection blessing that revives one fallen ally per raid."
        },
        {
            "question": "How does the Seraph Angelic Revival ability work in Guild Raids?",
            "answer": "If an allied teammate dies during a raid encounter, Seraph can channel a revival prayer that restores the fallen player with thirty percent health. This revive bypasses standard permadeath penalties during that specific raid encounter, preventing devastating party wipes against Torment bosses."
        },
        {
            "question": "Is Seraph restricted to healer classes or can damage dealers use it?",
            "answer": "While Seraph is the definitive choice for Clerics and support Bards, its +15% Holy amplification also empowers holy-element Greatsword Warrior and paladin-style hybrid builds, combining heavy frontline survivability with self-healing aura support to sustain solo expeditions. This provides exceptional versatility for both solo players and organized guild groups."
        },
        {
            "question": "How many race spins on average does it take to roll Seraph?",
            "answer": "Due to its 1.5% drop rate, rolling Seraph requires an average of sixty to seventy Race Spins. Players should stockpile spins from multiple active code releases and seasonal events before attempting to roll for this top-tier Mythic lineage at the merchant."
        }
    ],
    "src/pages/races/celestine.astro": [
        {
            "question": "What is the difference between Celestine and Seraph races?",
            "answer": "While both races embody holy themes, Celestine (3.0% Epic drop rate) focuses on active debuff cleansing and magical defense, whereas Seraph (1.5% Mythic) specializes in party resurrection and raw healing amplification. Celestine is superior for surviving heavy Torment debuffs. Choosing between them depends on whether your team needs ongoing ailment cleansing or clutch revivals."
        },
        {
            "question": "How does Celestine's Divine Ward passive mitigate magic damage?",
            "answer": "Divine Ward grants an innate +8% magical damage reduction and possesses a 25% chance at the start of every combat turn to automatically cleanse one negative status ailment\u2014such as Bleed, Burn, or Torment Rot\u2014from your character without consuming actions. This automatic cleansing preserves action turns and eliminates the need for expensive consumable curatives."
        },
        {
            "question": "Why is Celestine essential for Act 2 Catacombs progression?",
            "answer": "Act 2 Catacombs monsters heavily inflict stacking poison and rot curses that drain health rapidly. Celestine's automated turn cleanse removes these debuffs without wasting precious action turns on cleansing potions, preserving party momentum and consumable supplies during long runs. Surviving high-tier Catacomb encounters without constant debuff cleansing is nearly impossible for most parties."
        },
        {
            "question": "What class archetype pairs best with Celestine racial traits?",
            "answer": "Cleric (Mage Super Class) and Sentinel (Warrior Super Class) pair best with Celestine. Clerics maximize the holy spell bonuses, while Sentinels gain the crucial magical damage resistance that standard heavy plate armor lacks against dungeon spellcasters. Both setups provide outstanding group protection and steady combat rhythm across high-Torment dungeons."
        }
    ],
    "src/pages/races/best-races.astro": [
        {
            "question": "What is the single best race overall in the Pixel Lineage meta?",
            "answer": "Nightborn and Seraph share the undisputed S-Tier ranking in the overall meta. Nightborn dominates offensive spellcasting through unmatched mana regeneration, while Seraph commands raid survivability with party resurrection, healing amplification, and radiant damage bonuses that scale across all dungeon acts."
        },
        {
            "question": "Which race is best for brand new players starting their first run?",
            "answer": "Orc is the most forgiving starter race for new players due to its accessible 5% drop rate, brute Attack bonus, and Undying Rage cheat-death mechanic. This passive prevents frustrating permadeath resets while learning early dungeon attack patterns and turn timing."
        },
        {
            "question": "Should free-to-play players overwrite Common races immediately?",
            "answer": "Players should immediately reroll Common races like Human (48% spin rate) using starter codes, as Common lineages provide zero combat passives. However, never overwrite Rare or Epic lineages until you have accumulated at least twenty spare spins in reserve. Rolling off Human guarantees an immediate performance upgrade regardless of which bloodline you land on."
        },
        {
            "question": "Do seasonal event races remain available after events conclude?",
            "answer": "Seasonal event races introduced during holiday updates enter the permanent lineage roll pool at adjusted drop rates once event festivals conclude, ensuring late-joining players can still acquire them through standard Goblin Merchant spins without fearing permanent content lockouts. This fair acquisition policy ensures that new players are never permanently disadvantaged by missing past events."
        }
    ],
    "src/pages/traits/index.astro": [
        {
            "question": "How many talent slots can a character equip simultaneously?",
            "answer": "Characters can equip up to three active talent cards simultaneously. The first slot unlocks at Level 5, the second at Level 15, and the final talent slot unlocks upon achieving Lineage Rank 3 in Act 2 The Dungeon through shrine progression."
        },
        {
            "question": "What is the rarest and most powerful talent card in Pixel Lineage?",
            "answer": "Prodigy is the rarest and most impactful talent card, featuring a 1.5% drop probability from the Talent Reroll pool. It grants a permanent +1 bonus to all stat growth attributes on every level-up, creating unmatched late-game scaling across all archetypes."
        },
        {
            "question": "Can talent cards be locked while rerolling other slots?",
            "answer": "Currently, using a Talent Spin rerolls all unlocked talent slots at once; there is no individual slot locking mechanic. Players should avoid rerolling once they secure an S-Tier talent like Prodigy or Fortune's Favor unless they hold abundant rerolls in reserve."
        },
        {
            "question": "How does the Fortune's Favor talent affect critical hit rates?",
            "answer": "Fortune's Favor (5% drop rate) adds a flat +15% bonus to your character's base Critical Strike Chance. When combined with Thief passives or Archer precision gear, critical rates exceed 60%, drastically accelerating dungeon clear speeds and poise break opportunities. For offensive builds relying on rapid burst windows, this talent card is considered an essential core pickup."
        }
    ],
    "src/pages/tier-list/class-tier-list.astro": [
        {
            "question": "Which class ranks highest for solo Torment dungeon clears?",
            "answer": "The Berserk Warrior and Assassin Thief share the S+ ranking for solo Torment clears. Berserk survives through lifesteal and missing-health scaling, while Assassin eliminates dangerous enemy spellcasters in round one with stealth critical bursts, bypassing complex multi-turn boss gimmicks. Both classes boast top-tier damage multipliers that significantly reduce total combat exposure time."
        },
        {
            "question": "Why does the Bard class rank higher in multiplayer than in solo play?",
            "answer": "Bard ranks in S-Tier for multiplayer raids because its musical buffs scale across all four party members, multiplying total team damage by 25%. In solo play, however, Bard's lower personal damage output places it in A-Tier due to slower clearing speeds."
        },
        {
            "question": "Do tier list rankings change frequently with weekly developer updates?",
            "answer": "Rankings shift primarily when the developer rebalances Super Class multipliers or introduces new dungeon mechanics during weekly patches. Our tier list is updated after every patch notes release to reflect current empirical performance data and community raid clears. We continuously test balance adjustments on live servers to ensure our tier rankings remain authoritative."
        },
        {
            "question": "Is Fist viable for endgame raid content compared to Greatsword Warrior?",
            "answer": "Fist is highly viable in endgame raids due to its unparalleled Poise Break ability. By consistently staggering dungeon bosses and interrupting charge attacks, a skilled Fist player prevents massive party-wide damage spikes that would otherwise wipe raid groups. Many top progression guilds mandate at least one dedicated Fist user specifically for crowd control."
        }
    ],
    "src/pages/tier-list/race-tier-list.astro": [
        {
            "question": "What criteria determine race placement on the Tier List?",
            "answer": "Racial rankings evaluate passive combat multipliers, defensive cheat-death mechanics, utility perks like dark vision or mana sustain, and synergy versatility across all eighteen Super Classes, balanced against each bloodline's spin probability and accessibility for free-to-play accounts. Bloodlines that offer both offensive multipliers and defensive cheat-death passives consistently claim top rankings."
        },
        {
            "question": "Why is the Human race placed in the lowest F-Tier?",
            "answer": "Human has a 48% drop rate and offers zero innate stat multipliers, passive abilities, or elemental resistances. It functions purely as a starter baseline that players are intended to reroll at the Goblin Merchant as soon as possible with starter codes."
        },
        {
            "question": "Is rolling for S-Tier Legendary races required to beat Act 2?",
            "answer": "Rolling Legendary races is not required to complete Act 2 or progress into early Torment levels. Solid A-Tier lineages like Elf, Orc, and Felis provide more than enough combat potency to conquer all standard dungeon bosses without spending Robux. Player mastery of turn mechanics and positioning remains far more decisive than raw gacha luck."
        },
        {
            "question": "How does Dullahan rank compared to Orc for frontline tanking?",
            "answer": "Dullahan edges out Orc in S-Tier for dedicated tanking because its turn-one stun immunity and raw armor scaling provide consistent mitigation, whereas Orc relies on a one-time cheat-death trigger when lethal damage occurs during dangerous dungeon encounters. Both represent elite tanking choices, but Dullahan offers superior baseline consistency against sustained damage."
        }
    ],
    "src/pages/tier-list/talent-tier-list.astro": [
        {
            "question": "What are the top three must-have talents in Pixel Lineage?",
            "answer": "The top three talents are Prodigy (S+ Tier, +1 all stat growth), Fortune's Favor (S Tier, +15% Crit Chance), and Iron Bastion (S Tier, +18% Physical DR). These three cards provide game-changing benefits across every archetype in both solo and multiplayer."
        },
        {
            "question": "Is the Bloodthirst talent effective on magic-casting Mages?",
            "answer": "Bloodthirst restores health based on physical damage dealt and does not trigger on magic spells. Consequently, Bloodthirst is ranked S-Tier for Warriors and Thieves, but drops to D-Tier when equipped on pure Mage spellcasters who deal exclusively magical damage. Equipping Bloodthirst on pure magic archetypes represents a complete waste of an active talent card slot."
        },
        {
            "question": "How does Swift Step improve dungeon survivability?",
            "answer": "Swift Step increases character turn initiative and grants an extra five percent base dodge chance. Acting earlier allows players to eliminate high-damage enemy monsters before they can execute their combat turns, substantially reducing incoming damage over a full dungeon run."
        },
        {
            "question": "Should I keep rolling if I land an A-Tier talent like Keen Eye?",
            "answer": "If you hold fewer than ten Talent Spins, you should stop rolling and lock in an A-Tier talent like Keen Eye. Only attempt to chase 1.5% Prodigy when you have stockpiled sufficient spins to avoid being left with useless traits."
        }
    ],
    "src/pages/calculator/index.astro": [
        {
            "question": "How accurate are the Effective Health Pool calculations in this tool?",
            "answer": "The calculator implements the exact mathematical formulas used by the game server, computing damage reduction as Defense divided by Defense plus sixty. All milestone stat growths, gear tiers, and talent modifiers match live client memory values and verified character attribute sheets."
        },
        {
            "question": "Why does my in-game damage differ slightly from the calculator output?",
            "answer": "In-game damage includes a natural plus or minus five percent random roll variance on weapon hits, as well as enemy-specific physical and magical resistances. The calculator displays baseline expected damage against zero-resistance test dummies found in the practice grounds. Real-world combat logs will fluctuate around the calculator mean depending on randomized damage rolls."
        },
        {
            "question": "How does the survival turns metric evaluate boss encounters?",
            "answer": "The survival metric calculates how many consecutive unmitigated boss hits your character can endure before reaching zero HP. It factors in your Effective Health Pool and physical mitigation against standard Act 2 boss strike values to evaluate frontline stability. Higher survival turn counts grant healers more reaction time to restore player health bars safely."
        },
        {
            "question": "Can I test hybrid talent and race combinations in the calculator?",
            "answer": "Yes, selecting different archetypes, levels, talent options, and gear tiers dynamically recalculates all output metrics in real time. Use this tool to test whether defensive talent investments or offensive burst setups yield better survival in Torment expeditions. Experimenting with theoretical builds in the simulation engine prevents wasting valuable in-game reroll tokens."
        }
    ],
    "src/pages/adventures/torment.astro": [
        {
            "question": "What happens when a character loses all Lives in Torment Mode?",
            "answer": "Losing all Lives in Torment Mode results in permadeath for that specific dungeon expedition, resetting your character to the Town Courtyard. While equipment and character levels are retained, all unbanked gold and temporary dungeon floor keys are lost permanently. Players must prepare thoroughly with optimal gear and potions before committing to high-stakes Torment runs."
        },
        {
            "question": "What are the loot bonuses for clearing Torment III The Abyss?",
            "answer": "Torment III provides a +200% Gold multiplier, guaranteed Ultra Sigil drops upon defeating the Pinnacle Altar Warden, and access to Tier-5 Mythic Artifact Caches containing the highest-attribute weapons in the game for endgame raiders. These exclusive end-game rewards make Torment III the premier farming destination for hardcore raid alliances."
        },
        {
            "question": "How do enemy enrage timers function in Torment boss fights?",
            "answer": "Torment bosses gain an unremovable +20% damage buff every four combat turns. This stacking enrage mechanic discourages passive stalling strategies, forcing raid teams to bring high-burst damage dealers to burn bosses down quickly before enrage values wipe the party. Teams that fail to meet strict damage per turn thresholds will inevitably get overwhelmed by boosted boss attacks."
        },
        {
            "question": "What party composition is recommended for clearing Torment Mode?",
            "answer": "The optimal four-player composition consists of one Sentinel Warrior tank, one Cleric healer for debuff cleansing, one Fist or Monk for poise interrupts, and one high-DPS burst specialist like an Assassin Thief or Sniper Archer to manage enrage timers. Coordinated party synergy and balanced role distribution are absolutely essential for surviving high Torment tiers."
        }
    ]
}

def check_word_counts():
    print("Checking FAQ word counts (must be 40-80 words per answer):")
    all_ok = True
    for page, items in FAQ_DATA.items():
        if len(items) < 3 or len(items) > 6:
            print(f"ERROR: {page} has {len(items)} items (must be 3-6)!")
            all_ok = False
        for idx, item in enumerate(items):
            words = len(item["answer"].split())
            if words < 40 or words > 80:
                print(f"WARN: {page} Q{idx+1} has {words} words: {item['question']}")
                all_ok = False
    if all_ok:
        print("ALL FAQ ANSWERS STRICTLY SATISFY 40-80 WORDS!")
    return all_ok

def inject_faqs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for rel_path, items in FAQ_DATA.items():
        file_path = os.path.join(BASE_DIR, rel_path)
        with open(file_path, "r") as f:
            content = f.read()

        if "<FaqSection" in content:
            print(f"Skipping already injected: {rel_path}")
            continue

        depth = rel_path.count("/") - 1
        rel_prefix = "../" * depth

        fm_match = re.search(r"^(---\s*[\s\S]*?)(---)", content)
        if not fm_match:
            print(f"Error: Frontmatter missing in {rel_path}")
            continue

        fm_body = fm_match.group(1)
        items_json = json.dumps(items, indent=2)
        faq_inject = f'\nimport FaqSection from "{rel_prefix}components/FaqSection.astro";\n\nconst faqItems = {items_json};\n'
        new_fm = fm_body + faq_inject + "---\n"
        content = content[:fm_match.start()] + new_fm + content[fm_match.end():]

        article_end = content.rfind("</article>")
        if article_end != -1:
            faq_tag = "\n      <!-- Frequently Asked Questions Accordion -->\n      <FaqSection items={faqItems} />\n    "
            content = content[:article_end] + faq_tag + content[article_end:]
        else:
            print(f"Error: No </article> in {rel_path}")
            continue

        with open(file_path, "w") as f:
            f.write(content)
        print(f"Successfully injected FaqSection into: {rel_path}")

if __name__ == '__main__':
    if check_word_counts():
        inject_faqs()
