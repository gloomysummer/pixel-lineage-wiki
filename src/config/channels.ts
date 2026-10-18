// ============================================================
// [Config 层] channels.ts — Pixel Lineage 8 大核心频道与知识树架构定义
// 遵循 game-wiki-builder V3 分类与 Roblox 真实系统规范
// ============================================================

export interface ChannelGuide {
  id: string;
  title: string;
  url: string;
}

export interface Channel {
  id: string;
  title: string;
  shortTitle: string;
  url: string;
  color: string;
  guides: ChannelGuide[];
}

export const CHANNELS: Channel[] = [
  {
    id: "codes",
    title: "Codes & Rewards",
    shortTitle: "Codes",
    url: "/codes/",
    color: "#34d399",
    guides: [
      { id: "active-codes", title: "Active Promo Codes", url: "/codes/" },
      { id: "codes-not-working", title: "Code Troubleshooting", url: "/codes/not-working/" },
      { id: "how-to-redeem", title: "Goblin Merchant Redeem", url: "/codes/redeem/" },
    ],
  },
  {
    id: "tier-list",
    title: "Meta Tier Lists",
    shortTitle: "Tier List",
    url: "/tier-list/",
    color: "#f43f5e",
    guides: [
      { id: "tier-hub", title: "Meta Rankings Hub", url: "/tier-list/" },
      { id: "class-tier-list", title: "Class & Super Meta Tier", url: "/tier-list/class-tier-list/" },
      { id: "race-tier-list", title: "Races & Passives Ranking", url: "/tier-list/race-tier-list/" },
      { id: "talent-tier-list", title: "Talents & Traits Ranking", url: "/tier-list/talent-tier-list/" },
    ],
  },
  {
    id: "classes",
    title: "Classes & Evolutions",
    shortTitle: "Classes",
    url: "/classes/",
    color: "#a855f7",
    guides: [
      { id: "classes-hub", title: "Class Archetypes Hub", url: "/classes/" },
      { id: "super-classes", title: "18 Super Classes Guide", url: "/classes/super-classes/" },
      { id: "warrior-class", title: "Warrior Class Guide", url: "/classes/warrior/" },
      { id: "thief-class", title: "Thief Class Guide", url: "/classes/thief/" },
      { id: "mage-class", title: "Mage Class Guide", url: "/classes/mage/" },
      { id: "fist-class", title: "Fist Class Guide", url: "/classes/fist/" },
      { id: "bard-class", title: "Bard Class Guide", url: "/classes/bard/" },
      { id: "archer-class", title: "Archer Class Guide", url: "/classes/archer/" },
      { id: "class-stats", title: "Lv 1-30 Growth Matrix", url: "/classes/stats/" },
    ],
  },
  {
    id: "races",
    title: "Races & Talents",
    shortTitle: "Races",
    url: "/races/",
    color: "#c9a227",
    guides: [
      { id: "races-hub", title: "Bloodlines & Races Hub", url: "/races/" },
      { id: "best-races", title: "Best Races & Spin Meta", url: "/races/best-races/" },
      { id: "orc-race", title: "Orc Lineage Guide", url: "/races/orc/" },
      { id: "elf-race", title: "Elf Lineage Guide", url: "/races/elf/" },
      { id: "nightborn-race", title: "Nightborn Lineage Guide", url: "/races/nightborn/" },
      { id: "dullahan-race", title: "Dullahan Lineage Guide", url: "/races/dullahan/" },
      { id: "seraph-race", title: "Seraph Lineage Guide", url: "/races/seraph/" },
      { id: "celestine-race", title: "Celestine Lineage Guide", url: "/races/celestine/" },
      { id: "traits-guide", title: "Passive Traits & Talents", url: "/traits/" },
      { id: "calculator", title: "Stat & Build Calculator", url: "/calculator/" },
    ],
  },
  {
    id: "gear",
    title: "Arsenal & Gear",
    shortTitle: "Gear",
    url: "/gear/",
    color: "#38bdf8",
    guides: [
      { id: "gear-hub", title: "Equipment & Gear Hub", url: "/gear/" },
      { id: "weapons", title: "Weapons & Scaling Ranks", url: "/gear/weapons/" },
      { id: "armor-sets", title: "Armor Sets & Defense Buffs", url: "/gear/armor-sets/" },
      { id: "legendary-powers", title: "Legendary Powers & Affixes", url: "/gear/legendary-powers/" },
    ],
  },
  {
    id: "guilds",
    title: "Castle & Guilds",
    shortTitle: "Guilds",
    url: "/guilds/",
    color: "#ec4899",
    guides: [
      { id: "guilds-hub", title: "Town Guilds & Castle Hub", url: "/guilds/" },
      { id: "castle-repair", title: "Castle Repair Milestones", url: "/guilds/castle-repair/" },
      { id: "guild-raids", title: "Guild Raids & Boss Encounters", url: "/guilds/guild-raids/" },
      { id: "oaths", title: "Guild Oaths & Pledges", url: "/guilds/oaths/" },
      { id: "arena", title: "PvP Arena Tournament", url: "/guilds/arena/" },
    ],
  },
  {
    id: "adventures",
    title: "Dungeons & Torment",
    shortTitle: "Adventures",
    url: "/adventures/",
    color: "#f59e0b",
    guides: [
      { id: "adventures-hub", title: "Adventures & Dungeons Hub", url: "/adventures/" },
      { id: "torment", title: "Torment & Permadeath Rules", url: "/adventures/torment/" },
      { id: "lineage-ranks", title: "Lineage Ranks Progression", url: "/adventures/lineage-ranks/" },
      { id: "difficulty", title: "Adventure Difficulties", url: "/adventures/difficulty/" },
      { id: "combat-energy", title: "Combat Energy System", url: "/combat/energy/" },
    ],
  },
  {
    id: "updates",
    title: "Updates & Patches",
    shortTitle: "Updates",
    url: "/updates/",
    color: "#6366f1",
    guides: [
      { id: "updates-hub", title: "Weekly Patch Notes Ledger", url: "/updates/" },
      { id: "patch-notes", title: "Latest Hotfixes & Balances", url: "/updates/patch-notes/" },
    ],
  },
];

export const TOTAL_GUIDES_COUNT = CHANNELS.reduce((acc, ch) => acc + ch.guides.length, 0);

export function getChannelByGuideUrl(currentUrl: string): Channel {
  const norm = currentUrl.endsWith('/') ? currentUrl : `${currentUrl}/`;
  // First try exact match on guide URL
  for (const ch of CHANNELS) {
    if (ch.guides.some((g) => g.url === norm)) return ch;
  }
  // Next try channel prefix match
  for (const ch of CHANNELS) {
    if (norm.startsWith(ch.url)) return ch;
  }
  // Fallbacks for traits/calculator/combat
  if (norm.startsWith('/traits/') || norm.startsWith('/calculator/')) {
    return CHANNELS.find((c) => c.id === 'races') || CHANNELS[0];
  }
  if (norm.startsWith('/combat/')) {
    return CHANNELS.find((c) => c.id === 'adventures') || CHANNELS[0];
  }
  return CHANNELS[0];
}
