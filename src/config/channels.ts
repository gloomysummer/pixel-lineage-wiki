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
    title: "Codes & Free Spins Ledger",
    shortTitle: "Codes",
    url: "/codes/",
    color: "#34d399",
    guides: [
      {
        id: "active-codes",
        title: "Active Codes Ledger",
        url: "/codes/",
      },
      {
        id: "codes-not-working",
        title: "Troubleshooting Guide",
        url: "/codes/not-working/",
      },
      {
        id: "how-to-redeem",
        title: "Goblin Merchant Redeem",
        url: "/codes/redeem/",
      },
    ],
  },
  {
    id: "tier-list",
    title: "Meta Rankings & Tier Lists",
    shortTitle: "Tier List",
    url: "/tier-list/",
    color: "#f43f5e",
    guides: [
      {
        id: "class-tier-list",
        title: "Class & Super Meta Tier",
        url: "/tier-list/class-tier-list/",
      },
      {
        id: "race-tier-list",
        title: "Races & Passives Ranking",
        url: "/tier-list/race-tier-list/",
      },
      {
        id: "talent-tier-list",
        title: "Talents & Traits Ranking",
        url: "/tier-list/talent-tier-list/",
      },
    ],
  },
  {
    id: "classes",
    title: "Classes & Evolution Paths",
    shortTitle: "Classes",
    url: "/classes/",
    color: "#a855f7",
    guides: [
      {
        id: "super-classes",
        title: "18 Super Classes Guide",
        url: "/classes/super-classes/",
      },
      {
        id: "warrior-class",
        title: "Warrior & Evolutions",
        url: "/classes/warrior/",
      },
      {
        id: "mage-class",
        title: "Mage & Evolutions",
        url: "/classes/mage/",
      },
    ],
  },
  {
    id: "races",
    title: "Races, Talents & Respecs",
    shortTitle: "Races",
    url: "/races/",
    color: "#c9a227",
    guides: [
      {
        id: "race-tier-list",
        title: "Best Races & Spin Meta",
        url: "/tier-list/race-tier-list/",
      },
      {
        id: "talent-tier-list",
        title: "Talent Drop Rates & Rerolls",
        url: "/tier-list/talent-tier-list/",
      },
      {
        id: "codes-redeem",
        title: "Free Race & Talent Spins",
        url: "/codes/redeem/",
      },
    ],
  },
  {
    id: "gear",
    title: "Armor Sets & Arsenal Gear",
    shortTitle: "Gear",
    url: "/gear/",
    color: "#38bdf8",
    guides: [
      {
        id: "gear-hub",
        title: "Armor Sets & Weapon Stats",
        url: "/gear/",
      },
      {
        id: "super-classes-gear",
        title: "Weapon Scaling by Class",
        url: "/classes/super-classes/",
      },
      {
        id: "warrior-gear",
        title: "Greatsword & Shield Builds",
        url: "/classes/warrior/",
      },
    ],
  },
  {
    id: "guilds",
    title: "Castle, Oaths & Guild Raids",
    shortTitle: "Guilds",
    url: "/guilds/",
    color: "#ec4899",
    guides: [
      {
        id: "guilds-hub",
        title: "Castle Repair & Guild Oaths",
        url: "/guilds/",
      },
      {
        id: "adventures-raids",
        title: "Guild Raids & Bosses",
        url: "/adventures/",
      },
      {
        id: "codes-guild",
        title: "Community Group Perks",
        url: "/codes/redeem/",
      },
    ],
  },
  {
    id: "adventures",
    title: "Adventures, Dungeons & Torment",
    shortTitle: "Adventures",
    url: "/adventures/",
    color: "#f59e0b",
    guides: [
      {
        id: "adventures-hub",
        title: "Torment & Act Progression",
        url: "/adventures/",
      },
      {
        id: "super-trainer-shrine",
        title: "Trainer's Shrine Act 2",
        url: "/classes/super-classes/",
      },
      {
        id: "class-progression",
        title: "Dungeon Survival by Class",
        url: "/tier-list/class-tier-list/",
      },
    ],
  },
  {
    id: "updates",
    title: "Weekly Updates & Patch Notes",
    shortTitle: "Updates",
    url: "/updates/",
    color: "#6366f1",
    guides: [
      {
        id: "updates-hub",
        title: "Weekly Patch Notes Ledger",
        url: "/updates/",
      },
      {
        id: "codes-updates",
        title: "Latest Update Codes",
        url: "/codes/",
      },
      {
        id: "super-updates",
        title: "Halloween & Evolution Event",
        url: "/classes/super-classes/",
      },
    ],
  },
];

export const TOTAL_GUIDES_COUNT = CHANNELS.reduce((acc, ch) => acc + ch.guides.length, 0);

export function getChannelByGuideId(guideId: string): Channel {
  return CHANNELS.find((ch) => ch.guides.some((g) => g.id === guideId)) || CHANNELS[0];
}
